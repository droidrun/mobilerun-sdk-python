# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.workflows.flows import scheduled_run_list_params, scheduled_run_create_params
from ....types.workflows.flows.scheduled_run_list_response import ScheduledRunListResponse
from ....types.workflows.flows.scheduled_run_cancel_response import ScheduledRunCancelResponse
from ....types.workflows.flows.scheduled_run_create_response import ScheduledRunCreateResponse

__all__ = ["ScheduledRunsResource", "AsyncScheduledRunsResource"]


class ScheduledRunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduledRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ScheduledRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduledRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ScheduledRunsResourceWithStreamingResponse(self)

    def create(
        self,
        flow_id: str,
        *,
        run_at: Union[str, datetime],
        payload: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ScheduledRunCreateResponse:
        """
        Plan Run now for a future time, using the same devices, payload rules and
        admission at fire time. A flow can have at most 100 scheduled runs. Supports an
        optional Idempotency-Key; a replay returns the current scheduled run with the
        original 201 status.

        Args:
          run_at: RFC 3339 time with an offset; between one minute and 365 days from now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._post(
            path_template("/flows/{flow_id}/scheduled-runs", flow_id=flow_id),
            body=maybe_transform(
                {
                    "run_at": run_at,
                    "payload": payload,
                },
                scheduled_run_create_params.ScheduledRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ScheduledRunCreateResponse,
        )

    def list(
        self,
        flow_id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["scheduled", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledRunListResponse:
        """Lists upcoming runs by default, including claimed runs awaiting dispatch.

        Set
        status=all to include terminal rows. Ordered by runAt ascending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._get(
            path_template("/flows/{flow_id}/scheduled-runs", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                    },
                    scheduled_run_list_params.ScheduledRunListParams,
                ),
            ),
            cast_to=ScheduledRunListResponse,
        )

    def cancel(
        self,
        scheduled_run_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ScheduledRunCancelResponse:
        """
        Cancel a planned flow run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not scheduled_run_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_run_id` but received {scheduled_run_id!r}")
        return self._post(
            path_template(
                "/flows/{flow_id}/scheduled-runs/{scheduled_run_id}/cancel",
                flow_id=flow_id,
                scheduled_run_id=scheduled_run_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ScheduledRunCancelResponse,
        )


class AsyncScheduledRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduledRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduledRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduledRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncScheduledRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        flow_id: str,
        *,
        run_at: Union[str, datetime],
        payload: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ScheduledRunCreateResponse:
        """
        Plan Run now for a future time, using the same devices, payload rules and
        admission at fire time. A flow can have at most 100 scheduled runs. Supports an
        optional Idempotency-Key; a replay returns the current scheduled run with the
        original 201 status.

        Args:
          run_at: RFC 3339 time with an offset; between one minute and 365 days from now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._post(
            path_template("/flows/{flow_id}/scheduled-runs", flow_id=flow_id),
            body=await async_maybe_transform(
                {
                    "run_at": run_at,
                    "payload": payload,
                },
                scheduled_run_create_params.ScheduledRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ScheduledRunCreateResponse,
        )

    async def list(
        self,
        flow_id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["scheduled", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledRunListResponse:
        """Lists upcoming runs by default, including claimed runs awaiting dispatch.

        Set
        status=all to include terminal rows. Ordered by runAt ascending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._get(
            path_template("/flows/{flow_id}/scheduled-runs", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                    },
                    scheduled_run_list_params.ScheduledRunListParams,
                ),
            ),
            cast_to=ScheduledRunListResponse,
        )

    async def cancel(
        self,
        scheduled_run_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ScheduledRunCancelResponse:
        """
        Cancel a planned flow run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not scheduled_run_id:
            raise ValueError(f"Expected a non-empty value for `scheduled_run_id` but received {scheduled_run_id!r}")
        return await self._post(
            path_template(
                "/flows/{flow_id}/scheduled-runs/{scheduled_run_id}/cancel",
                flow_id=flow_id,
                scheduled_run_id=scheduled_run_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ScheduledRunCancelResponse,
        )


class ScheduledRunsResourceWithRawResponse:
    def __init__(self, scheduled_runs: ScheduledRunsResource) -> None:
        self._scheduled_runs = scheduled_runs

        self.create = to_raw_response_wrapper(
            scheduled_runs.create,
        )
        self.list = to_raw_response_wrapper(
            scheduled_runs.list,
        )
        self.cancel = to_raw_response_wrapper(
            scheduled_runs.cancel,
        )


class AsyncScheduledRunsResourceWithRawResponse:
    def __init__(self, scheduled_runs: AsyncScheduledRunsResource) -> None:
        self._scheduled_runs = scheduled_runs

        self.create = async_to_raw_response_wrapper(
            scheduled_runs.create,
        )
        self.list = async_to_raw_response_wrapper(
            scheduled_runs.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            scheduled_runs.cancel,
        )


class ScheduledRunsResourceWithStreamingResponse:
    def __init__(self, scheduled_runs: ScheduledRunsResource) -> None:
        self._scheduled_runs = scheduled_runs

        self.create = to_streamed_response_wrapper(
            scheduled_runs.create,
        )
        self.list = to_streamed_response_wrapper(
            scheduled_runs.list,
        )
        self.cancel = to_streamed_response_wrapper(
            scheduled_runs.cancel,
        )


class AsyncScheduledRunsResourceWithStreamingResponse:
    def __init__(self, scheduled_runs: AsyncScheduledRunsResource) -> None:
        self._scheduled_runs = scheduled_runs

        self.create = async_to_streamed_response_wrapper(
            scheduled_runs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            scheduled_runs.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            scheduled_runs.cancel,
        )
