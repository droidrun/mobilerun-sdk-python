# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.workflows import execution_list_params, execution_get_metrics_params
from ...types.workflows.execution_list_response import ExecutionListResponse
from ...types.workflows.execution_retrieve_response import ExecutionRetrieveResponse
from ...types.workflows.execution_get_metrics_response import ExecutionGetMetricsResponse

__all__ = ["ExecutionsResource", "AsyncExecutionsResource"]


class ExecutionsResource(SyncAPIResource):
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionRetrieveResponse:
        """
        Fetch a single flow execution by its ID, including its status, kind, result or
        error, and start/finish timestamps. Returns 404 if no execution matches.

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionRetrieveResponse,
        )

    def list(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Optional[str] | Omit = omit,
        order_by: Literal["startedAt", "finishedAt", "status"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"] | Omit = omit,
        to: Optional[str] | Omit = omit,
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
        `triggerId`, `status`, and a `from`/`to` time range, plus free-text `search` and
        ordering by startedAt, finishedAt, or status.

        Args:
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

    def get_metrics(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Optional[str] | Omit = omit,
        to: Optional[str] | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionRetrieveResponse:
        """
        Fetch a single flow execution by its ID, including its status, kind, result or
        error, and start/finish timestamps. Returns 404 if no execution matches.

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionRetrieveResponse,
        )

    async def list(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Optional[str] | Omit = omit,
        order_by: Literal["startedAt", "finishedAt", "status"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["pending", "running", "success", "failed", "cancelled", "skipped", "invalid"] | Omit = omit,
        to: Optional[str] | Omit = omit,
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
        `triggerId`, `status`, and a `from`/`to` time range, plus free-text `search` and
        ordering by startedAt, finishedAt, or status.

        Args:
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

    async def get_metrics(
        self,
        *,
        flow_id: str | Omit = omit,
        from_: Optional[str] | Omit = omit,
        to: Optional[str] | Omit = omit,
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
        self.get_metrics = to_raw_response_wrapper(
            executions.get_metrics,
        )


class AsyncExecutionsResourceWithRawResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = async_to_raw_response_wrapper(
            executions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            executions.list,
        )
        self.get_metrics = async_to_raw_response_wrapper(
            executions.get_metrics,
        )


class ExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            executions.list,
        )
        self.get_metrics = to_streamed_response_wrapper(
            executions.get_metrics,
        )


class AsyncExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = async_to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            executions.list,
        )
        self.get_metrics = async_to_streamed_response_wrapper(
            executions.get_metrics,
        )
