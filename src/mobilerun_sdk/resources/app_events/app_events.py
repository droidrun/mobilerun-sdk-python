# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from .catalog import CatalogResource, AsyncCatalogResource, CatalogResourceWithRawResponse, AsyncCatalogResourceWithRawResponse, CatalogResourceWithStreamingResponse, AsyncCatalogResourceWithStreamingResponse

from ..._compat import cached_property

from ..._utils import path_template, maybe_transform, async_maybe_transform

from ...types.app_event_retrieve_response import AppEventRetrieveResponse

from ..._base_client import make_request_options

from ..._types import NotGiven, Omit, omit

from ...types.app_event_list_response import AppEventListResponse

from typing import Optional

from typing_extensions import Literal

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types import app_event_list_params

__all__ = ["AppEventsResource", "AsyncAppEventsResource"]

class AppEventsResource(SyncAPIResource):
    @cached_property
    def catalog(self) -> CatalogResource:
        return CatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> AppEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AppEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AppEventsResourceWithStreamingResponse(self)

    def retrieve(self,
    id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppEventRetrieveResponse:
        """
        Fetch a single structured app event by its ID, including its typed payload,
        source, and originating device. Returns 404 if no event matches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
          raise ValueError(
            f'Expected a non-empty value for `id` but received {id!r}'
          )
        return self._get(
            path_template("/app-events/{id}", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppEventRetrieveResponse,
        )

    def list(self,
    *,
    device_id: str | Omit = omit,
    event_type: str | Omit = omit,
    from_: Optional[str] | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    source: Literal["app", "system", "device", "webhook"] | Omit = omit,
    to: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppEventListResponse:
        """Structured, app-scoped events (e.g.

        app.whatsapp.message_received) derived from
        raw device notifications. Typed columns — not raw payloads (those stay in the
        event log).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/app-events",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "device_id": device_id,
                "event_type": event_type,
                "from_": from_,
                "page": page,
                "page_size": page_size,
                "source": source,
                "to": to,
            }, app_event_list_params.AppEventListParams)),
            cast_to=AppEventListResponse,
        )

class AsyncAppEventsResource(AsyncAPIResource):
    @cached_property
    def catalog(self) -> AsyncCatalogResource:
        return AsyncCatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAppEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncAppEventsResourceWithStreamingResponse(self)

    async def retrieve(self,
    id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppEventRetrieveResponse:
        """
        Fetch a single structured app event by its ID, including its typed payload,
        source, and originating device. Returns 404 if no event matches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
          raise ValueError(
            f'Expected a non-empty value for `id` but received {id!r}'
          )
        return await self._get(
            path_template("/app-events/{id}", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppEventRetrieveResponse,
        )

    async def list(self,
    *,
    device_id: str | Omit = omit,
    event_type: str | Omit = omit,
    from_: Optional[str] | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    source: Literal["app", "system", "device", "webhook"] | Omit = omit,
    to: Optional[str] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppEventListResponse:
        """Structured, app-scoped events (e.g.

        app.whatsapp.message_received) derived from
        raw device notifications. Typed columns — not raw payloads (those stay in the
        event log).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/app-events",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "device_id": device_id,
                "event_type": event_type,
                "from_": from_,
                "page": page,
                "page_size": page_size,
                "source": source,
                "to": to,
            }, app_event_list_params.AppEventListParams)),
            cast_to=AppEventListResponse,
        )

class AppEventsResourceWithRawResponse:
    def __init__(self, app_events: AppEventsResource) -> None:
        self._app_events = app_events

        self.retrieve = to_raw_response_wrapper(
            app_events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            app_events.list,
        )

    @cached_property
    def catalog(self) -> CatalogResourceWithRawResponse:
        return CatalogResourceWithRawResponse(self._app_events.catalog)

class AsyncAppEventsResourceWithRawResponse:
    def __init__(self, app_events: AsyncAppEventsResource) -> None:
        self._app_events = app_events

        self.retrieve = async_to_raw_response_wrapper(
            app_events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            app_events.list,
        )

    @cached_property
    def catalog(self) -> AsyncCatalogResourceWithRawResponse:
        return AsyncCatalogResourceWithRawResponse(self._app_events.catalog)

class AppEventsResourceWithStreamingResponse:
    def __init__(self, app_events: AppEventsResource) -> None:
        self._app_events = app_events

        self.retrieve = to_streamed_response_wrapper(
            app_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            app_events.list,
        )

    @cached_property
    def catalog(self) -> CatalogResourceWithStreamingResponse:
        return CatalogResourceWithStreamingResponse(self._app_events.catalog)

class AsyncAppEventsResourceWithStreamingResponse:
    def __init__(self, app_events: AsyncAppEventsResource) -> None:
        self._app_events = app_events

        self.retrieve = async_to_streamed_response_wrapper(
            app_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            app_events.list,
        )

    @cached_property
    def catalog(self) -> AsyncCatalogResourceWithStreamingResponse:
        return AsyncCatalogResourceWithStreamingResponse(self._app_events.catalog)