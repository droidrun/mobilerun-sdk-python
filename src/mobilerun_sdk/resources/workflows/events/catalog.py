# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.workflows.events import catalog_list_params, catalog_register_params
from ....types.workflows.events.catalog_list_response import CatalogListResponse
from ....types.workflows.events.catalog_register_response import CatalogRegisterResponse

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

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        source: Literal["device", "system", "webhook"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogListResponse:
        """
        List event catalog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/events/catalog",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "source": source,
                    },
                    catalog_list_params.CatalogListParams,
                ),
            ),
            cast_to=CatalogListResponse,
        )

    def register(
        self,
        *,
        events: Iterable[catalog_register_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogRegisterResponse:
        """
        Register event types in the catalog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/events/catalog/register",
            body=maybe_transform({"events": events}, catalog_register_params.CatalogRegisterParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogRegisterResponse,
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

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        source: Literal["device", "system", "webhook"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogListResponse:
        """
        List event catalog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/events/catalog",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "source": source,
                    },
                    catalog_list_params.CatalogListParams,
                ),
            ),
            cast_to=CatalogListResponse,
        )

    async def register(
        self,
        *,
        events: Iterable[catalog_register_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CatalogRegisterResponse:
        """
        Register event types in the catalog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/events/catalog/register",
            body=await async_maybe_transform({"events": events}, catalog_register_params.CatalogRegisterParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CatalogRegisterResponse,
        )


class CatalogResourceWithRawResponse:
    def __init__(self, catalog: CatalogResource) -> None:
        self._catalog = catalog

        self.list = to_raw_response_wrapper(
            catalog.list,
        )
        self.register = to_raw_response_wrapper(
            catalog.register,
        )


class AsyncCatalogResourceWithRawResponse:
    def __init__(self, catalog: AsyncCatalogResource) -> None:
        self._catalog = catalog

        self.list = async_to_raw_response_wrapper(
            catalog.list,
        )
        self.register = async_to_raw_response_wrapper(
            catalog.register,
        )


class CatalogResourceWithStreamingResponse:
    def __init__(self, catalog: CatalogResource) -> None:
        self._catalog = catalog

        self.list = to_streamed_response_wrapper(
            catalog.list,
        )
        self.register = to_streamed_response_wrapper(
            catalog.register,
        )


class AsyncCatalogResourceWithStreamingResponse:
    def __init__(self, catalog: AsyncCatalogResource) -> None:
        self._catalog = catalog

        self.list = async_to_streamed_response_wrapper(
            catalog.list,
        )
        self.register = async_to_streamed_response_wrapper(
            catalog.register,
        )
