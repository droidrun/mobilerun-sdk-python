# Inspection and runs may incur compute charges. Run: rye run python examples/compute.py
import sys
import time
import uuid
from typing import TypeVar, Callable

from mobilerun_sdk import Run, MobilerunSDK, WaitFailureError
from mobilerun_sdk.types.compute import RunLogsResponse, RunRetrieveResponse

# Public mobilerun-functions greeting example: no hosts, credentials or scopes.
SOURCE = """from pydantic import BaseModel
from mobilerun_functions import Context, script
class Input(BaseModel):
    name: str = "world"
class Output(BaseModel):
    message: str
@script
def main(input: Input, ctx: Context) -> Output:
    ctx.log.info("greeting")
    return Output(message=f"Hello, {input.name}!")
"""
T = TypeVar("T")


def inspect(load: Callable[[float], T], ready: Callable[[T], bool]) -> T:
    deadline = time.monotonic() + 120
    while time.monotonic() < deadline:
        value = load(min(30, deadline - time.monotonic()))
        if ready(value):
            return value
        time.sleep(min(1, max(0, deadline - time.monotonic())))
    raise TimeoutError("Inspection deadline exceeded")


def inspection_ready(status: str | None) -> bool:
    if status == "rejected":
        raise RuntimeError("Function inspection failed")
    return status == "ready"


def compute(sdk: MobilerunSDK, name: str) -> tuple[RunRetrieveResponse, RunLogsResponse]:
    validation = sdk.compute.functions.validations.create(source=SOURCE)

    reader = sdk.api.with_options(max_retries=0)
    validated = inspect(
        lambda timeout: reader.compute.functions.validations.retrieve(validation.data.id, wait_s=0, timeout=timeout),
        lambda response: response.data.status != "pending",
    ).data
    if validated.status == "failed" or not validated.valid:
        raise RuntimeError("Validation failed")
    fn = sdk.compute.functions.create(name=name, source=SOURCE)
    version: int | None = None
    run: Run | None = None
    failed = False
    try:
        inspect(
            lambda timeout: reader.compute.functions.retrieve(fn.id, timeout=timeout),
            lambda response: inspection_ready(
                response.data.latest_version.status if response.data.latest_version else None
            ),
        )
        fn.source()
        uploaded = fn.versions.create(source=SOURCE)
        if uploaded.data is None:
            raise RuntimeError("Missing uploaded version")
        uploaded_version = uploaded.data.version
        version = uploaded_version
        inspect(
            lambda timeout: reader.compute.functions.versions.retrieve(
                uploaded_version, function_id=fn.id, timeout=timeout
            ),
            lambda response: inspection_ready(response.data.status if response.data else None),
        )
        fn.versions.list()
        sdk.compute.functions.list(search=name)
        run = fn.runs.create(input={"name": "Ada"}, version=version, wait_s=0)
        if type(run) is not Run:
            raise TypeError("Expected a Run handle")
        finished = run.wait(timeout=600)
        run.wait_logs(timeout=60)
        return finished, run.logs()  # A link envelope, not the log bytes.
    except BaseException:
        failed = True
        raise
    finally:
        try:
            if run is not None and run.status not in ("done", "failed"):
                run.cancel()
                try:
                    run.wait(timeout=60)
                except WaitFailureError:
                    pass
            if version is not None:
                fn.versions.delete(version)
            fn.delete()
        except Exception:
            if not failed:
                raise
            print("Compute cleanup failed; inspect function " + fn.id, file=sys.stderr)


if __name__ == "__main__":
    compute(MobilerunSDK(), "sdk-example-" + str(uuid.uuid4()))
