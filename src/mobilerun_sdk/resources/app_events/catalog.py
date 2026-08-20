# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.app_events.catalog_list_response import CatalogListResponse
from ...types.app_events.catalog_retrieve_response import CatalogRetrieveResponse

__all__ = ["CatalogResource", "AsyncCatalogResource"]


class CatalogResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return CatalogResourceWithStreamingResponse(self)

    def retrieve(
        self,
        app_event_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogRetrieveResponse:
        """
        Fetch a single selectable app event by its appEventType (e.g.
        app.whatsapp.message_received).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_event_type:
            raise ValueError(f"Expected a non-empty value for `app_event_type` but received {app_event_type!r}")
        return self._get(
            path_template("/app-events/catalog/{app_event_type}", app_event_type=app_event_type),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogListResponse:
        """Selectable app-based trigger events (e.g.

        app.whatsapp.message_received) with
        their predefined payload — served from the JSON definition registry (always in
        sync, no DB).
        """
        return self._get(
            "/app-events/catalog",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogListResponse,
        )


class AsyncCatalogResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncCatalogResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        app_event_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogRetrieveResponse:
        """
        Fetch a single selectable app event by its appEventType (e.g.
        app.whatsapp.message_received).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_event_type:
            raise ValueError(f"Expected a non-empty value for `app_event_type` but received {app_event_type!r}")
        return await self._get(
            path_template("/app-events/catalog/{app_event_type}", app_event_type=app_event_type),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogListResponse:
        """Selectable app-based trigger events (e.g.

        app.whatsapp.message_received) with
        their predefined payload — served from the JSON definition registry (always in
        sync, no DB).
        """
        return await self._get(
            "/app-events/catalog",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogListResponse,
        )


class CatalogResourceWithRawResponse:
    def __init__(self, catalog: CatalogResource) -> None:
        self._catalog = catalog

        self.retrieve = to_raw_response_wrapper(
            catalog.retrieve,
        )
        self.list = to_raw_response_wrapper(
            catalog.list,
        )


class AsyncCatalogResourceWithRawResponse:
    def __init__(self, catalog: AsyncCatalogResource) -> None:
        self._catalog = catalog

        self.retrieve = async_to_raw_response_wrapper(
            catalog.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            catalog.list,
        )


class CatalogResourceWithStreamingResponse:
    def __init__(self, catalog: CatalogResource) -> None:
        self._catalog = catalog

        self.retrieve = to_streamed_response_wrapper(
            catalog.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            catalog.list,
        )


class AsyncCatalogResourceWithStreamingResponse:
    def __init__(self, catalog: AsyncCatalogResource) -> None:
        self._catalog = catalog

        self.retrieve = async_to_streamed_response_wrapper(
            catalog.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            catalog.list,
        )
