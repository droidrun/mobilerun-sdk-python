# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.workflows import event_ingest_params, event_dry_run_params
from ...types.workflows.event_ingest_response import EventIngestResponse
from ...types.workflows.event_dry_run_response import EventDryRunResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def dry_run(
        self,
        *,
        event_type: str,
        device_id: str | Omit = omit,
        payload: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDryRunResponse:
        """Simulate an event against all configured flows.

        Returns which flows would match
        and what actions would run, without storing the event or enqueuing jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/events/dry-run",
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "device_id": device_id,
                    "payload": payload,
                },
                event_dry_run_params.EventDryRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDryRunResponse,
        )

    def ingest(
        self,
        *,
        event_type: str,
        device_id: str | Omit = omit,
        payload: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventIngestResponse:
        """Ingest an event for trigger evaluation.

        Returns immediately with 202 Accepted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/events/ingest",
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "device_id": device_id,
                    "payload": payload,
                },
                event_ingest_params.EventIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventIngestResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def dry_run(
        self,
        *,
        event_type: str,
        device_id: str | Omit = omit,
        payload: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDryRunResponse:
        """Simulate an event against all configured flows.

        Returns which flows would match
        and what actions would run, without storing the event or enqueuing jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/events/dry-run",
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "device_id": device_id,
                    "payload": payload,
                },
                event_dry_run_params.EventDryRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDryRunResponse,
        )

    async def ingest(
        self,
        *,
        event_type: str,
        device_id: str | Omit = omit,
        payload: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventIngestResponse:
        """Ingest an event for trigger evaluation.

        Returns immediately with 202 Accepted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/events/ingest",
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "device_id": device_id,
                    "payload": payload,
                },
                event_ingest_params.EventIngestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventIngestResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.dry_run = to_raw_response_wrapper(
            events.dry_run,
        )
        self.ingest = to_raw_response_wrapper(
            events.ingest,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.dry_run = async_to_raw_response_wrapper(
            events.dry_run,
        )
        self.ingest = async_to_raw_response_wrapper(
            events.ingest,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.dry_run = to_streamed_response_wrapper(
            events.dry_run,
        )
        self.ingest = to_streamed_response_wrapper(
            events.ingest,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.dry_run = async_to_streamed_response_wrapper(
            events.dry_run,
        )
        self.ingest = async_to_streamed_response_wrapper(
            events.ingest,
        )
