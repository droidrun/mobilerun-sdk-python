# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import io
import os
import re
import hmac
import json
import math
import time
import base64
import random
import hashlib
import threading
import contextlib
from typing import (
    Any,
    Generic,
    Mapping,
    TypeVar,
    BinaryIO,
    Callable,
    Iterator,
    Sequence,
    Awaitable,
    Generator,
    AsyncIterator,
    cast,
)
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from urllib.parse import urlsplit
from typing_extensions import TypeVar as DefaultTypeVar

import anyio
import httpx
from pydantic import BaseModel

from .._types import NotGiven
from .._compat import PYDANTIC_V1, model_parse, get_model_fields
from .._exceptions import APIStatusError, APITimeoutError, APIConnectionError

_T = TypeVar("_T")
_R = TypeVar("_R")
_OutputT = DefaultTypeVar("_OutputT", default=None)
_ModelT = TypeVar("_ModelT", bound=BaseModel)


def header_boolean(value: str | None) -> bool | None:
    return True if value == "true" else False if value == "false" else None


class BinaryResult:
    def __init__(self, data: bytes, content_type: str | None) -> None:
        self.bytes = data
        self.content_type = content_type

    def base64(self) -> str:
        return base64.b64encode(self.bytes).decode("ascii")

    def data_url(self) -> str:
        return "data:" + (self.content_type or "application/octet-stream") + ";base64," + self.base64()

    def save(self, path: str | os.PathLike[str]) -> str:
        filename = os.fspath(path)
        with open(filename, "wb") as file:
            file.write(self.bytes)
        return filename

    async def asave(self, path: str | os.PathLike[str]) -> str:
        return await anyio.to_thread.run_sync(self.save, path)


class ObjectPage(Generic[_T, _R]):
    def __init__(self, items: list[_T], response: _R) -> None:
        self.items = items
        self.response = response


class PagedObjectPage(ObjectPage[_T, _R]):
    def __init__(
        self,
        items: list[_T],
        response: _R,
        next_number: Callable[[], int | str | None] | None = None,
        load: Callable[[int], PagedObjectPage[_T, _R]]
        | Callable[[int | str | None], PagedObjectPage[_T, _R]]
        | None = None,
    ) -> None:
        super().__init__(items, response)
        self._next = next_number
        self._load = cast(Callable[[int | str | None], PagedObjectPage[_T, _R]] | None, load)

    def has_next_page(self) -> bool:
        return self._next is not None and self._next() is not None

    def get_next_page(self) -> PagedObjectPage[_T, _R]:
        number = self._next() if self._next is not None else None
        if number is None or self._load is None:
            raise RuntimeError("No next object page")
        return self._load(number)

    def __iter__(self) -> Iterator[_T]:
        page = self
        while True:
            yield from page.items
            if not page.has_next_page():
                return
            page = page.get_next_page()


class AsyncObjectPage(ObjectPage[_T, _R]):
    def __init__(
        self,
        items: list[_T],
        response: _R,
        next_number: Callable[[], int | str | None] | None = None,
        load: Callable[[int], Awaitable[AsyncObjectPage[_T, _R]]]
        | Callable[[int | str | None], Awaitable[AsyncObjectPage[_T, _R]]]
        | None = None,
    ) -> None:
        super().__init__(items, response)
        self._next = next_number
        self._load = cast(Callable[[int | str | None], Awaitable[AsyncObjectPage[_T, _R]]] | None, load)

    def has_next_page(self) -> bool:
        return self._next is not None and self._next() is not None

    async def get_next_page(self) -> AsyncObjectPage[_T, _R]:
        number = self._next() if self._next is not None else None
        if number is None or self._load is None:
            raise RuntimeError("No next object page")
        return await self._load(number)

    async def __aiter__(self) -> AsyncIterator[_T]:
        page = self
        while True:
            for item in page.items:
                yield item
            if not page.has_next_page():
                return
            page = await page.get_next_page()


class AsyncObjectPager(Generic[_T, _R]):
    def __init__(self, load: Callable[[], Awaitable[AsyncObjectPage[_T, _R]]]) -> None:
        self._load = load
        self._first: AsyncObjectPage[_T, _R] | None = None
        self._lock = anyio.Lock()

    async def _get(self) -> AsyncObjectPage[_T, _R]:
        async with self._lock:
            if self._first is None:
                self._first = await self._load()
            return self._first

    def __await__(self) -> Generator[object, None, AsyncObjectPage[_T, _R]]:
        return self._get().__await__()

    async def __aiter__(self) -> AsyncIterator[_T]:
        async for item in await self:
            yield item


def next_object_page(
    current: int | None, has_next: bool | None, total: int | None, requested: int | str | None
) -> int | None:
    if (
        type(requested) is not int
        or requested < 1
        or type(current) is not int
        or current < 0
        or type(total) is not int
        or total < 0
        or type(has_next) is not bool
    ):
        raise ValueError("Invalid object pagination metadata")
    if not has_next or current >= total:
        return None
    if current < requested:
        raise ValueError("Object pagination made no forward progress")
    return current + 1


def next_object_cursor(next_cursor: object, requested: int | str | None, seen: set[str]) -> str | None:
    if next_cursor is None or next_cursor == "":
        return None
    if not isinstance(next_cursor, str):
        raise ValueError("Invalid object cursor pagination metadata")
    if next_cursor == requested or next_cursor in seen:
        raise ValueError("Object pagination made no forward progress")
    return next_cursor


class ObjectReadyError(Exception):
    """Failed readiness after create disposes the new resource by default when disposal is declared.

    The error retains the handle, readiness cause, disposal status and any cleanup error; callers can opt out per create.
    """

    def __init__(
        self,
        object: object,
        id: str,
        cause: BaseException,
        disposed: bool = False,
        cleanup_error: BaseException | None = None,
    ) -> None:
        super().__init__("Object readiness failed after creation")
        self.object = object
        self.id = id
        self.cause = cause
        self.disposed = disposed
        self.cleanup_error = cleanup_error


class WaitError(Exception):
    pass


@dataclass(frozen=True)
class WaitOutput(Generic[_T, _R]):
    output: _T
    response: _R


class OutputValidationError(WaitError):
    def __init__(self, object_id: str, response: object, parser_error: Exception) -> None:
        super().__init__(f"Output validation failed: {parser_error}")
        self.cause = parser_error
        self.object_id = object_id
        self.response = response
        self.parser_error = parser_error


def is_model_type(value: Any) -> bool:
    return isinstance(value, type) and issubclass(value, BaseModel)


def model_output_schema(value: Any) -> Any:
    if is_model_type(value):
        if PYDANTIC_V1:
            return value.schema()  # pyright: ignore[reportDeprecated]
        return value.model_json_schema()
    return value


def output_parser(value: object) -> Callable[[object], Any] | None:
    if is_model_type(value):
        return lambda data: model_parse(cast(type[BaseModel], value), data)
    return None


MISSING = object()


def read_path(value: object, names: Sequence[str]) -> Any:
    for key in names:
        if isinstance(value, BaseModel):
            name = next(
                (name for name, field in get_model_fields(type(value)).items() if (field.alias or name) == key), key
            )
            fields = value.__fields_set__ if PYDANTIC_V1 else value.model_fields_set  # pyright: ignore[reportDeprecated]
            if name not in fields:
                return MISSING
            value = getattr(value, name, MISSING)
        elif isinstance(value, Mapping):
            value = cast(Mapping[str, object], value).get(key, MISSING)
        else:
            return MISSING
    return value


def condition_met(value: object, until: str) -> bool:
    if until == "present":
        return value is not MISSING and value is not None
    return isinstance(value, (str, list)) and len(cast("str | list[object]", value)) > 0


def parse_output(
    parser: Callable[[object], _T], value: object, response: _R, object_id: str, object_name: str = "object"
) -> WaitOutput[_T, _R]:
    try:
        if value is MISSING:
            raise ValueError(f"Completed {object_name} has no output")
        return WaitOutput(parser(value), response)
    except Exception as error:
        raise OutputValidationError(object_id, response, error) from error


class WaitTimeoutError(WaitError, TimeoutError):
    pass


class WaitCancelledError(WaitError):
    pass


class WaitFailureError(WaitError):
    def __init__(self, response: object) -> None:
        super().__init__("Object entered a failure state")
        self.response = response


def attach_cleanup_error(original: BaseException, cleanup: BaseException) -> None:
    note = getattr(original, "add_note", None)
    if note is not None:
        note(f"Object cleanup failed: {cleanup!r}")
    cleanup.__context__ = None
    if original.__context__ is None:
        original.__context__ = cleanup


def bound_extra(extra: object, bindings: dict[str, object], *, headers: bool = False) -> dict[str, object]:
    if headers:
        bindings = {key: str(value) if value is not None else None for key, value in bindings.items()}
    if extra is None:
        return bindings
    if not isinstance(extra, Mapping):
        raise TypeError("Bound parameters require object request extras")
    values = cast(Mapping[str, object], extra)
    if headers:
        names = {name.lower() for name in bindings}
        values = {key: value for key, value in values.items() if key.lower() not in names}
    return {**values, **bindings}


def check_wait(timeout: float, poll_interval: float) -> None:
    if not math.isfinite(timeout) or timeout <= 0 or not math.isfinite(poll_interval) or poll_interval <= 0:
        raise ValueError("timeout and poll_interval must be positive")


def wait_sync(
    poll: Callable[[float], _T],
    state: Callable[[_T], str],
    success: Sequence[str],
    failure: Sequence[str],
    *,
    pending: Sequence[str] | None = None,
    timeout: float,
    poll_interval: float,
    cancel: threading.Event | None = None,
    retry: Callable[[Exception], bool] | None = None,
    retry_delay: Callable[[Exception, int], float] | None = None,
    poll_request_timeout: float | None = None,
) -> _T:
    """Sync requests cannot be hard-aborted in flight; cancellation/deadlines are checked between requests."""
    check_wait(timeout, poll_interval)
    deadline = time.monotonic() + timeout
    attempts = 0
    last_error: Exception | None = None
    if poll_request_timeout is not None:
        retry = retry_poll
        retry_delay = lambda error, attempt: poll_delay(error, attempt, poll_interval)
    while True:
        if cancel is not None and cancel.is_set():
            raise WaitCancelledError("Wait cancelled")
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise WaitTimeoutError("Wait timed out") from last_error
        try:
            result = poll(min(remaining, poll_request_timeout) if poll_request_timeout is not None else remaining)
        except Exception as error:
            if not wait_retry(error, retry, deadline):
                raise
            last_error = error
            delay = min(
                retry_delay(error, attempts) if retry_delay is not None else 0, max(0, deadline - time.monotonic())
            )
            attempts += 1
            if cancel is None:
                time.sleep(delay)
            else:
                cancel.wait(delay)
            continue
        attempts = 0
        if poll_request_timeout is not None and time.monotonic() >= deadline:
            raise WaitTimeoutError("Wait timed out") from last_error
        if state(result) in success:
            return result
        if state(result) in failure or (pending is not None and state(result) not in pending):
            raise WaitFailureError(result)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise WaitTimeoutError("Wait timed out") from last_error
        delay = min(poll_interval, remaining)
        if cancel is None:
            time.sleep(delay)
        else:
            cancel.wait(delay)


SINGLE_CALL_INTERVAL = 1.0


READINESS_RETRY_STATUSES = [408, 409, 429]
READINESS_IMMEDIATE_STATUSES = [408]
READINESS_SERVER_ERROR_MIN = 500
READINESS_BACKOFF = 0.5
READINESS_MAX_BACKOFF = 8
READINESS_JITTER_MIN = 0.75


def retry_readiness(error: Exception) -> bool:
    if isinstance(error, APITimeoutError):
        return True
    if not isinstance(error, APIStatusError):
        return False
    header = error.response.headers.get("x-should-retry")
    if header == "false":
        return False
    return (
        header == "true"
        or error.status_code in READINESS_RETRY_STATUSES
        or error.status_code >= READINESS_SERVER_ERROR_MIN
    )


def readiness_delay(error: Exception, attempt: int) -> float:
    if isinstance(error, APITimeoutError) or (
        isinstance(error, APIStatusError) and error.status_code in READINESS_IMMEDIATE_STATUSES
    ):
        return 0
    return retry_backoff(error, attempt)


POLL_TRANSPORT_ERRORS = (APITimeoutError, APIConnectionError)


def retry_poll(error: Exception) -> bool:
    return isinstance(error, POLL_TRANSPORT_ERRORS) or (
        isinstance(error, APIStatusError)
        and (error.status_code in READINESS_RETRY_STATUSES or error.status_code >= READINESS_SERVER_ERROR_MIN)
    )


def poll_delay(error: Exception, attempt: int, interval: float) -> float:
    return interval if isinstance(error, POLL_TRANSPORT_ERRORS) else retry_backoff(error, attempt)


def retry_backoff(error: Exception, attempt: int) -> float:
    if isinstance(error, APIStatusError):
        milliseconds = error.response.headers.get("retry-after-ms")
        after = error.response.headers.get("retry-after")
        if milliseconds is not None:
            try:
                delay = float(milliseconds) / 1000
                if math.isfinite(delay) and delay >= 0:
                    return delay
            except ValueError:
                pass
        if after is not None:
            try:
                try:
                    delay = float(after)
                except ValueError:
                    delay = cast(datetime, parsedate_to_datetime(after)).timestamp() - time.time()
                if math.isfinite(delay) and delay >= 0:
                    return delay
            except (ValueError, TypeError, OverflowError):
                pass
    base: float = min(READINESS_BACKOFF * 2 ** min(attempt, 10), READINESS_MAX_BACKOFF)
    return base * random.uniform(READINESS_JITTER_MIN, 1)


def wait_retry(error: Exception, retry: Callable[[Exception], bool] | None, deadline: float) -> bool:
    retryable = retry is not None and retry(error)
    if (isinstance(error, APITimeoutError) or retryable) and time.monotonic() >= deadline:
        raise WaitTimeoutError("Wait timed out") from error
    return retryable


def ready_sync(call: Callable[[float], _T], *, timeout: float, cancel: threading.Event | None = None) -> _T:
    return wait_sync(
        call,
        lambda _: "ready",
        ["ready"],
        [],
        timeout=timeout,
        poll_interval=SINGLE_CALL_INTERVAL,
        cancel=cancel,
        retry=retry_readiness,
        retry_delay=readiness_delay,
    )


async def ready_async(call: Callable[[float], Awaitable[_T]], *, timeout: float) -> _T:
    return await wait_async(
        call,
        lambda _: "ready",
        ["ready"],
        [],
        timeout=timeout,
        poll_interval=SINGLE_CALL_INTERVAL,
        retry=retry_readiness,
        retry_delay=readiness_delay,
    )


async def wait_async(
    poll: Callable[[float], Awaitable[_T]],
    state: Callable[[_T], str],
    success: Sequence[str],
    failure: Sequence[str],
    *,
    pending: Sequence[str] | None = None,
    timeout: float,
    poll_interval: float,
    retry: Callable[[Exception], bool] | None = None,
    retry_delay: Callable[[Exception, int], float] | None = None,
    poll_request_timeout: float | None = None,
) -> _T:
    check_wait(timeout, poll_interval)
    deadline = time.monotonic() + timeout
    attempts = 0
    last_error: Exception | None = None
    if poll_request_timeout is not None:
        retry = retry_poll
        retry_delay = lambda error, attempt: poll_delay(error, attempt, poll_interval)
    try:
        with anyio.fail_after(timeout):
            while True:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise WaitTimeoutError("Wait timed out") from last_error
                try:
                    result = await poll(
                        min(remaining, poll_request_timeout) if poll_request_timeout is not None else remaining
                    )
                except Exception as error:
                    if not wait_retry(error, retry, deadline):
                        raise
                    last_error = error
                    delay = min(
                        retry_delay(error, attempts) if retry_delay is not None else 0,
                        max(0, deadline - time.monotonic()),
                    )
                    attempts += 1
                    await anyio.sleep(delay)
                    continue
                attempts = 0
                if poll_request_timeout is not None and time.monotonic() >= deadline:
                    raise WaitTimeoutError("Wait timed out") from last_error
                if state(result) in success:
                    return result
                if state(result) in failure or (pending is not None and state(result) not in pending):
                    raise WaitFailureError(result)
                await anyio.sleep(min(poll_interval, max(0, deadline - time.monotonic())))
    except TimeoutError as error:
        if isinstance(error, WaitTimeoutError):
            raise
        raise WaitTimeoutError("Wait timed out") from (last_error or error)


def record_field(info: object, root: str, path: str) -> Any:
    value = read_path(info, ".".join(part for part in (root, path) if part).split("."))
    return None if value is MISSING else value


class WebhookVerificationError(ValueError):
    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__("Webhook verification failed: " + reason)


def _signature_header(headers: Any, name: str) -> str:
    if hasattr(headers, "getlist"):
        matches = list(headers.getlist(name))
    elif hasattr(headers, "get_all"):
        matches = list(headers.get_all(name) or [])
    elif hasattr(headers, "items"):
        matches = [value for key, value in headers.items() if key.lower() == name.lower()]
    elif hasattr(headers, "get"):
        value = headers.get(name)
        matches = [] if value is None else [value]
    else:
        raise WebhookVerificationError("malformed")
    if not matches or matches[0] is None:
        raise WebhookVerificationError("missing_header")
    if len(matches) != 1:
        raise WebhookVerificationError("malformed")
    value = matches[0]
    if isinstance(value, (list, tuple)):
        if len(cast(Sequence[Any], value)) != 1:
            raise WebhookVerificationError("malformed")
        value = cast(Sequence[Any], value)[0]
    if not isinstance(value, str):
        raise WebhookVerificationError("malformed")
    return value


def verify_signature(
    body: Any, headers: Any, secret: Any, scheme: Mapping[str, Any], *, tolerance: Any = None, now: Any = None
) -> Any:
    if not isinstance(body, (str, bytes)):
        raise TypeError("Webhook body must be the raw string or bytes, before JSON parsing")
    timestamp = _signature_header(headers, scheme["timestamp_header"])
    signature = _signature_header(headers, scheme["signature_header"])
    tolerance = scheme["tolerance_seconds"] if tolerance is None else tolerance
    now = time.time() if now is None else now
    if (
        re.fullmatch(r"[0-9]+", timestamp) is None
        or len(timestamp.lstrip("0")) > 16
        or not isinstance(now, (int, float))
        or not math.isfinite(now)
        or not isinstance(tolerance, (int, float))
        or not math.isfinite(tolerance)
        or tolerance < 0
        or not isinstance(secret, str)
        or not secret
    ):
        raise WebhookVerificationError("malformed")
    number = int(timestamp.lstrip("0") or "0")
    if number > 9007199254740991:
        raise WebhookVerificationError("malformed")
    prefix = scheme["signature_prefix"]
    if not signature.startswith(prefix):
        raise WebhookVerificationError("malformed")
    digest = signature[len(prefix) :]
    if re.fullmatch(r"[0-9a-fA-F]{64}", digest) is None:
        raise WebhookVerificationError("malformed")
    seconds = number / (1000 if scheme["timestamp_unit"] == "ms" else 1)
    if abs(now - seconds) > tolerance:
        raise WebhookVerificationError("timestamp_out_of_tolerance")
    raw = body.encode("utf-8") if isinstance(body, str) else body
    try:
        key = secret.encode("utf-8")
    except UnicodeError:
        raise WebhookVerificationError("malformed") from None
    expected = hmac.new(key, timestamp.encode("ascii") + b"." + raw, hashlib.sha256).digest()
    if not hmac.compare_digest(expected, bytes.fromhex(digest)):
        raise WebhookVerificationError("invalid_signature")
    try:
        return json.loads(raw)
    except (ValueError, UnicodeError):
        raise WebhookVerificationError("malformed") from None


def definite_confirm_failure(error: BaseException) -> bool:
    return isinstance(error, APIStatusError) and 400 <= error.status_code < 500 and error.status_code != 408


@dataclass
class UploadFile:
    data: str | os.PathLike[str] | bytes | BinaryIO
    filename: str | None = None
    content_type: str | None = None
    size: int | None = None


UploadInput = str | os.PathLike[str] | bytes | BinaryIO | UploadFile


class UploadError(RuntimeError):
    def __init__(self) -> None:
        super().__init__("Presigned upload failed")


@dataclass
class PreparedUpload:
    data: str | os.PathLike[str] | bytes | BinaryIO
    filename: str
    content_type: str
    size: int
    offset: int = 0

    @contextlib.contextmanager
    def open(self) -> Iterator[BinaryIO]:
        if isinstance(self.data, (str, os.PathLike)):
            with open(self.data, "rb") as source:
                yield source
        elif isinstance(self.data, bytes):
            with io.BytesIO(self.data) as source:
                yield source
        else:
            self.data.seek(self.offset)
            try:
                yield self.data
            finally:
                self.data.seek(self.offset)


def upload_content_type(filename: str) -> str:
    extension = filename.rsplit(".", 1)[-1].lower()
    return {
        "apk": "application/vnd.android.package-archive",
        "xapk": "application/zip",
        "apks": "application/zip",
        "ipa": "application/octet-stream",
        "json": "application/json",
        "txt": "text/plain",
        "csv": "text/csv",
        "pdf": "application/pdf",
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "zip": "application/zip",
    }.get(extension, "application/octet-stream")


def prepare_upload(
    value: UploadInput, *, filename: str | None = None, content_type: str | None = None, size: int | None = None
) -> PreparedUpload:
    wrapped = value if isinstance(value, UploadFile) else UploadFile(value)
    data = wrapped.data
    filename = filename if filename is not None else wrapped.filename
    content_type = content_type if content_type is not None else wrapped.content_type
    size = size if size is not None else wrapped.size
    offset = 0
    if isinstance(data, (str, os.PathLike)):
        path = Path(data)
        if not path.is_file():
            raise TypeError("Upload path must name a file")
        filename = filename or path.name
        actual = path.stat().st_size
    elif isinstance(data, bytes):
        actual = len(data)
    elif hasattr(data, "read"):
        if not isinstance(cast(object, data.read(0)), bytes):
            raise TypeError("Upload file must be opened in binary mode")
        filename = filename or (Path(data.name).name if isinstance(getattr(data, "name", None), str) else None)
        try:
            offset = data.tell()
            data.seek(0, os.SEEK_END)
            actual = data.tell() - offset
            data.seek(offset)
        except (AttributeError, OSError, io.UnsupportedOperation):
            data = data.read()
            if not isinstance(cast(object, data), bytes):
                raise TypeError("Upload file must be opened in binary mode") from None
            actual = len(data)
    else:
        raise TypeError("Unsupported upload input")
    if size is not None and (type(size) is not int or size != actual):
        raise TypeError("Upload size must match the measured byte count")
    size = actual
    if not filename:
        raise TypeError("Upload bytes and streams require a filename")
    if not isinstance(cast(object, size), int) or size < 0:
        raise TypeError("Invalid upload size")
    return PreparedUpload(data, filename, content_type or upload_content_type(filename), size, offset)


def upload_urls(response: Any, files: Sequence[PreparedUpload], scheme: Mapping[str, Any]) -> list[str]:
    if scheme.get("url_path"):
        url = read_path(response, scheme["url_path"].split("."))
        if len(files) != 1 or not isinstance(url, str):
            raise ValueError("Invalid presigned upload URL")
        return [url]
    rows = read_path(response, scheme["urls_path"].split("."))
    if (
        not isinstance(rows, list)
        or len(cast(list[Any], rows)) != len(files)
        or len({file.filename for file in files}) != len(files)
    ):
        raise ValueError("Upload URL count or file names do not match")
    rows = cast(list[Any], rows)
    by_name = {
        read_path(row, scheme["name_field"].split(".")): read_path(row, scheme["url_field"].split(".")) for row in rows
    }
    if len(by_name) != len(rows):
        raise ValueError("Duplicate upload URL name")
    urls = [by_name.get(file.filename) for file in files]
    if any(not isinstance(url, str) for url in urls):
        raise ValueError("Missing upload URL for a file")
    return cast(list[str], urls)


def _upload_request(api: Any, url: str, file: PreparedUpload, content: Any, timeout: Any) -> httpx.Request:
    parsed = urlsplit(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc or parsed.username or parsed.password:
        raise TypeError("Invalid presigned URL")
    effective = api.timeout if isinstance(timeout, NotGiven) else timeout
    effective = effective if isinstance(effective, httpx.Timeout) else httpx.Timeout(effective)
    # Construct a fresh request: do not inherit API headers, cookies or auth.
    return httpx.Request(
        "PUT",
        url,
        headers={"Content-Type": file.content_type, "Content-Length": str(file.size)},
        content=content,
        extensions={"timeout": effective.as_dict()},
    )


def _upload_failure(response: httpx.Response) -> APIStatusError:
    # Keep status/retry headers, but never retain a signed URL or storage body.
    request = httpx.Request("PUT", response.request.url.copy_with(query=None))
    safe = httpx.Response(response.status_code, headers=response.headers, request=request, content=b"")
    return APIStatusError("Presigned PUT failed", response=safe, body=None)


def _upload_connection(error: httpx.TransportError, url: str) -> APIConnectionError:
    # Clear the transport exception's signed request even in implicit context chains.
    error.request = httpx.Request("PUT", httpx.URL(url).copy_with(query=None))
    safe = APIConnectionError(request=error.request)
    return safe


def put_upload_sync(api: Any, file: PreparedUpload, url: str, *, timeout: Any) -> None:
    failure: Exception
    for attempt in range(api.max_retries + 1):
        try:
            with file.open() as source:
                request = _upload_request(api, url, file, source, timeout)
                response = api._client.send(request, auth=None, follow_redirects=False)
            response.close()
            if response.is_success:
                return
            failure = _upload_failure(response)
            if response.status_code < 500 or attempt >= api.max_retries:
                raise failure
        except httpx.TransportError as error:
            failure = _upload_connection(error, url)
        if attempt >= api.max_retries:
            raise failure from None
        time.sleep(min(60.0, retry_backoff(failure, attempt)))


async def put_upload_async(api: Any, file: PreparedUpload, url: str, *, timeout: Any) -> None:
    failure: Exception
    for attempt in range(api.max_retries + 1):
        try:
            with file.open() as source:

                async def chunks() -> AsyncIterator[bytes]:
                    while True:
                        chunk = await anyio.to_thread.run_sync(source.read, 65536)
                        if not chunk:
                            return
                        yield chunk

                request = _upload_request(api, url, file, chunks(), timeout)
                response = await api._client.send(request, auth=None, follow_redirects=False)
            await response.aclose()
            if response.is_success:
                return
            failure = _upload_failure(response)
            if response.status_code < 500 or attempt >= api.max_retries:
                raise failure
        except httpx.TransportError as error:
            failure = _upload_connection(error, url)
        if attempt >= api.max_retries:
            raise failure from None
        await anyio.sleep(min(60.0, retry_backoff(failure, attempt)))


def verify_webhook(
    body: str | bytes, headers: Any, secret: str, *, tolerance: float = 300, now: float | None = None
) -> Any:
    """Verify the raw body before parsing it. now is epoch seconds. No API key is needed."""
    return verify_signature(
        body,
        headers,
        secret,
        {
            "algorithm": "hmac-sha256",
            "signature_header": "x-mobilerun-signature",
            "signature_prefix": "sha256=",
            "timestamp_header": "x-mobilerun-timestamp",
            "timestamp_unit": "ms",
            "signed_payload": "{timestamp}.{body}",
            "tolerance_seconds": 300,
        },
        tolerance=tolerance,
        now=now,
    )


class Screenshot(BinaryResult):
    def __init__(self, data: bytes, headers: Mapping[str, str]) -> None:
        super().__init__(data, headers.get("Content-Type"))
        self.id: str | None = headers.get("X-Screenshot-Id")
        self.saved: bool | None = header_boolean(headers.get("X-Screenshot-Saved"))
