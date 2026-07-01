# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.connect import country_list_params
from ...types.connect.country_list_response import CountryListResponse

__all__ = ["CountriesResource", "AsyncCountriesResource"]


class CountriesResource(SyncAPIResource):
    """Mobilerun Connect country coverage information"""

    @cached_property
    def with_raw_response(self) -> CountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return CountriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        type: Literal["dedicated_residential", "residential", "mobile"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryListResponse:
        """
        Lookup of countries that can be selected when creating a proxy.

        Args:
          page: Page number (1-based).

          page_size: Number of items per page.

          type: Filter to countries offering this proxy type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/connect/countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "type": type,
                    },
                    country_list_params.CountryListParams,
                ),
            ),
            cast_to=CountryListResponse,
        )


class AsyncCountriesResource(AsyncAPIResource):
    """Mobilerun Connect country coverage information"""

    @cached_property
    def with_raw_response(self) -> AsyncCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncCountriesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        type: Literal["dedicated_residential", "residential", "mobile"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryListResponse:
        """
        Lookup of countries that can be selected when creating a proxy.

        Args:
          page: Page number (1-based).

          page_size: Number of items per page.

          type: Filter to countries offering this proxy type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/connect/countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "type": type,
                    },
                    country_list_params.CountryListParams,
                ),
            ),
            cast_to=CountryListResponse,
        )


class CountriesResourceWithRawResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.list = to_raw_response_wrapper(
            countries.list,
        )


class AsyncCountriesResourceWithRawResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.list = async_to_raw_response_wrapper(
            countries.list,
        )


class CountriesResourceWithStreamingResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.list = to_streamed_response_wrapper(
            countries.list,
        )


class AsyncCountriesResourceWithStreamingResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.list = async_to_streamed_response_wrapper(
            countries.list,
        )
