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
from ...types.compute import run_list_params, run_retrieve_params
from ...types.compute.run_list_response import RunListResponse
from ...types.compute.run_logs_response import RunLogsResponse
from ...types.compute.run_cancel_response import RunCancelResponse
from ...types.compute.run_retrieve_response import RunRetrieveResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        run_id: str,
        *,
        wait_s: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveResponse:
        """
        Get a run

        Args:
          wait_s: Seconds the reply waits for the run to end; 202 when it is still running.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/compute/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"wait_s": wait_s}, run_retrieve_params.RunRetrieveParams),
            ),
            cast_to=RunRetrieveResponse,
        )

    def list(
        self,
        *,
        function_id: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["running", "done", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """
        List the runs started on the public routes, newest first

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/compute/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "function_id": function_id,
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    def cancel(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RunCancelResponse:
        """
        Cancel a run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            path_template("/compute/runs/{run_id}/cancel", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RunCancelResponse,
        )

    def logs(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunLogsResponse:
        """
        Get a short-lived download link for the full log of a run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/compute/runs/{run_id}/logs", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunLogsResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        run_id: str,
        *,
        wait_s: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveResponse:
        """
        Get a run

        Args:
          wait_s: Seconds the reply waits for the run to end; 202 when it is still running.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/compute/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"wait_s": wait_s}, run_retrieve_params.RunRetrieveParams),
            ),
            cast_to=RunRetrieveResponse,
        )

    async def list(
        self,
        *,
        function_id: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["running", "done", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunListResponse:
        """
        List the runs started on the public routes, newest first

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/compute/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "function_id": function_id,
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    async def cancel(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RunCancelResponse:
        """
        Cancel a run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            path_template("/compute/runs/{run_id}/cancel", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RunCancelResponse,
        )

    async def logs(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunLogsResponse:
        """
        Get a short-lived download link for the full log of a run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/compute/runs/{run_id}/logs", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunLogsResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.cancel = to_raw_response_wrapper(
            runs.cancel,
        )
        self.logs = to_raw_response_wrapper(
            runs.logs,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            runs.cancel,
        )
        self.logs = async_to_raw_response_wrapper(
            runs.logs,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.cancel = to_streamed_response_wrapper(
            runs.cancel,
        )
        self.logs = to_streamed_response_wrapper(
            runs.logs,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            runs.cancel,
        )
        self.logs = async_to_streamed_response_wrapper(
            runs.logs,
        )
