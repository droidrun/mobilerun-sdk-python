# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .screenshots import (
    ScreenshotsResource,
    AsyncScreenshotsResource,
    ScreenshotsResourceWithRawResponse,
    AsyncScreenshotsResourceWithRawResponse,
    ScreenshotsResourceWithStreamingResponse,
    AsyncScreenshotsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.workflows import execution_list_params, execution_retrieve_params, execution_get_metrics_params
from ....types.workflows.execution_list_response import ExecutionListResponse
from ....types.workflows.execution_abort_response import ExecutionAbortResponse
from ....types.workflows.execution_retrieve_response import ExecutionRetrieveResponse
from ....types.workflows.execution_get_metrics_response import ExecutionGetMetricsResponse

__all__ = ["ExecutionsResource", "AsyncExecutionsResource"]


class ExecutionsResource(SyncAPIResource):
    @cached_property
    def screenshots(self) -> ScreenshotsResource:
        return ScreenshotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ExecutionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        execution_id: str,
        *,
        include: Literal["input"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionRetrieveResponse:
        """
        Fetch a single flow execution by its ID, including its status, kind, result or
        error, and start/finish timestamps. Add `include=input` to get what each step
        ran with. Returns 404 if no execution matches.

        Args:
          include: Extra data to add to each step of `result.steps` (loop children included).
              `input` adds a field `input` per step: what the step ran with, resolved after
              templating and without values the platform adds (ids, session and idempotency
              keys, script state). For sandbox steps, nested `input` is the effective input
              when available, otherwise the submitted input. The value is the input object, a
              marker `{ "notRecorded": "too_large" | "invalid" | "unavailable" }` (`too_large`
              adds `bytes`) when it could not be stored or exceeds 64 KiB, or null for a step
              without a recorded input, such as a run from before inputs were stored. Secrets
              are redacted before storing, best effort and by key name only: a value is
              replaced with `[REDACTED]` at any depth when its key, read as words
              (`clientSecret`, `x-auth-token`), contains `password`, `passwd`, `passphrase`,
              `secret`, `token`, `authorization`, `cookie`, `credential`, `signature`,
              `api key`, `private key`, `client key` or `card number`, or is exactly `pwd`,
              `otp`, `totp`, `pin`, `cvv` or `cvc`. `Bearer`, `Basic` and `Token`
              authorization values in strings are masked too. Secrets inside other strings
              (for example agent prompts) or under other key names are not detected. The
              content of file uploads is never stored, only its size, encoding and type.
              Without `include` the response has no `input` fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._get(
            path_template("/executions/{execution_id}", execution_id=execution_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, execution_retrieve_params.ExecutionRetrieveParams),
            ),
            cast_to=ExecutionRetrieveResponse,
        )

    def list(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        invocation_id: str | Omit = omit,
        kind: List[Literal["live", "dry_run", "verification"]] | Omit = omit,
        order_by: Literal["startedAt", "finishedAt", "status"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        trigger_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionListResponse:
        """Return a paginated history of flow executions.

        Supports filtering by `flowId`,
        `triggerId`, `invocationId` (the client/verify key), `status`, `kind` (one or
        more execution kinds), and a `from`/`to` time range, plus free-text `search` and
        ordering by startedAt, finishedAt, or status.

        Args:
          kind: Only include these execution kinds. Omit to include all kinds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/executions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "flow_id": flow_id,
                        "from_": from_,
                        "invocation_id": invocation_id,
                        "kind": kind,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                        "to": to,
                        "trigger_id": trigger_id,
                    },
                    execution_list_params.ExecutionListParams,
                ),
            ),
            cast_to=ExecutionListResponse,
        )

    def abort(
        self,
        execution_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ExecutionAbortResponse:
        """Stops the execution between steps and marks it cancelled.

        Idempotent-ish:
        already-terminal executions return 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._post(
            path_template("/executions/{execution_id}/abort", execution_id=execution_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExecutionAbortResponse,
        )

    def get_metrics(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        trigger_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionGetMetricsResponse:
        """
        Return aggregate execution metrics — total count, counts by status, average
        duration, and the last execution time. Can be scoped by `flowId`, `triggerId`,
        and a `from`/`to` time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/executions/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "flow_id": flow_id,
                        "from_": from_,
                        "to": to,
                        "trigger_id": trigger_id,
                    },
                    execution_get_metrics_params.ExecutionGetMetricsParams,
                ),
            ),
            cast_to=ExecutionGetMetricsResponse,
        )


class AsyncExecutionsResource(AsyncAPIResource):
    @cached_property
    def screenshots(self) -> AsyncScreenshotsResource:
        return AsyncScreenshotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncExecutionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        execution_id: str,
        *,
        include: Literal["input"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionRetrieveResponse:
        """
        Fetch a single flow execution by its ID, including its status, kind, result or
        error, and start/finish timestamps. Add `include=input` to get what each step
        ran with. Returns 404 if no execution matches.

        Args:
          include: Extra data to add to each step of `result.steps` (loop children included).
              `input` adds a field `input` per step: what the step ran with, resolved after
              templating and without values the platform adds (ids, session and idempotency
              keys, script state). For sandbox steps, nested `input` is the effective input
              when available, otherwise the submitted input. The value is the input object, a
              marker `{ "notRecorded": "too_large" | "invalid" | "unavailable" }` (`too_large`
              adds `bytes`) when it could not be stored or exceeds 64 KiB, or null for a step
              without a recorded input, such as a run from before inputs were stored. Secrets
              are redacted before storing, best effort and by key name only: a value is
              replaced with `[REDACTED]` at any depth when its key, read as words
              (`clientSecret`, `x-auth-token`), contains `password`, `passwd`, `passphrase`,
              `secret`, `token`, `authorization`, `cookie`, `credential`, `signature`,
              `api key`, `private key`, `client key` or `card number`, or is exactly `pwd`,
              `otp`, `totp`, `pin`, `cvv` or `cvc`. `Bearer`, `Basic` and `Token`
              authorization values in strings are masked too. Secrets inside other strings
              (for example agent prompts) or under other key names are not detected. The
              content of file uploads is never stored, only its size, encoding and type.
              Without `include` the response has no `input` fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return await self._get(
            path_template("/executions/{execution_id}", execution_id=execution_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include": include}, execution_retrieve_params.ExecutionRetrieveParams
                ),
            ),
            cast_to=ExecutionRetrieveResponse,
        )

    async def list(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        invocation_id: str | Omit = omit,
        kind: List[Literal["live", "dry_run", "verification"]] | Omit = omit,
        order_by: Literal["startedAt", "finishedAt", "status"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        trigger_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionListResponse:
        """Return a paginated history of flow executions.

        Supports filtering by `flowId`,
        `triggerId`, `invocationId` (the client/verify key), `status`, `kind` (one or
        more execution kinds), and a `from`/`to` time range, plus free-text `search` and
        ordering by startedAt, finishedAt, or status.

        Args:
          kind: Only include these execution kinds. Omit to include all kinds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/executions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "flow_id": flow_id,
                        "from_": from_,
                        "invocation_id": invocation_id,
                        "kind": kind,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                        "to": to,
                        "trigger_id": trigger_id,
                    },
                    execution_list_params.ExecutionListParams,
                ),
            ),
            cast_to=ExecutionListResponse,
        )

    async def abort(
        self,
        execution_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ExecutionAbortResponse:
        """Stops the execution between steps and marks it cancelled.

        Idempotent-ish:
        already-terminal executions return 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return await self._post(
            path_template("/executions/{execution_id}/abort", execution_id=execution_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExecutionAbortResponse,
        )

    async def get_metrics(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Union[str, datetime, None] | Omit = omit,
        to: Union[str, datetime, None] | Omit = omit,
        trigger_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionGetMetricsResponse:
        """
        Return aggregate execution metrics — total count, counts by status, average
        duration, and the last execution time. Can be scoped by `flowId`, `triggerId`,
        and a `from`/`to` time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/executions/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "flow_id": flow_id,
                        "from_": from_,
                        "to": to,
                        "trigger_id": trigger_id,
                    },
                    execution_get_metrics_params.ExecutionGetMetricsParams,
                ),
            ),
            cast_to=ExecutionGetMetricsResponse,
        )


class ExecutionsResourceWithRawResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = to_raw_response_wrapper(
            executions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            executions.list,
        )
        self.abort = to_raw_response_wrapper(
            executions.abort,
        )
        self.get_metrics = to_raw_response_wrapper(
            executions.get_metrics,
        )

    @cached_property
    def screenshots(self) -> ScreenshotsResourceWithRawResponse:
        return ScreenshotsResourceWithRawResponse(self._executions.screenshots)


class AsyncExecutionsResourceWithRawResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = async_to_raw_response_wrapper(
            executions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            executions.list,
        )
        self.abort = async_to_raw_response_wrapper(
            executions.abort,
        )
        self.get_metrics = async_to_raw_response_wrapper(
            executions.get_metrics,
        )

    @cached_property
    def screenshots(self) -> AsyncScreenshotsResourceWithRawResponse:
        return AsyncScreenshotsResourceWithRawResponse(self._executions.screenshots)


class ExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            executions.list,
        )
        self.abort = to_streamed_response_wrapper(
            executions.abort,
        )
        self.get_metrics = to_streamed_response_wrapper(
            executions.get_metrics,
        )

    @cached_property
    def screenshots(self) -> ScreenshotsResourceWithStreamingResponse:
        return ScreenshotsResourceWithStreamingResponse(self._executions.screenshots)


class AsyncExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = async_to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            executions.list,
        )
        self.abort = async_to_streamed_response_wrapper(
            executions.abort,
        )
        self.get_metrics = async_to_streamed_response_wrapper(
            executions.get_metrics,
        )

    @cached_property
    def screenshots(self) -> AsyncScreenshotsResourceWithStreamingResponse:
        return AsyncScreenshotsResourceWithStreamingResponse(self._executions.screenshots)
