# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import carrier_list_params, carrier_create_params, carrier_lookup_params, carrier_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.carrier_list_response import CarrierListResponse
from ..types.carrier_create_response import CarrierCreateResponse
from ..types.carrier_delete_response import CarrierDeleteResponse
from ..types.carrier_lookup_response import CarrierLookupResponse
from ..types.carrier_update_response import CarrierUpdateResponse
from ..types.carrier_retrieve_response import CarrierRetrieveResponse

__all__ = ["CarriersResource", "AsyncCarriersResource"]


class CarriersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CarriersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CarriersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CarriersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return CarriersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        country: str,
        mcc: str,
        mnc: str,
        operator: str,
        company: str | Omit = omit,
        country_code: str | Omit = omit,
        country_iso: str | Omit = omit,
        detail_url: str | Omit = omit,
        gsm_bands: str | Omit = omit,
        lte_bands: str | Omit = omit,
        mobile_prefix: str | Omit = omit,
        nsn_size: str | Omit = omit,
        number_format: str | Omit = omit,
        protocols: str | Omit = omit,
        umts_bands: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierCreateResponse:
        """
        Create a new carrier

        Args:
          country: Country name

          mcc: Mobile Country Code

          mnc: Mobile Network Code

          operator: Operator name

          company: Company name

          country_code: Country dialing code (e.g., +1)

          country_iso: ISO country code

          detail_url: URL to carrier details page

          gsm_bands: Supported GSM bands

          lte_bands: Supported LTE bands

          mobile_prefix: Mobile number prefix

          nsn_size: National Significant Number size

          number_format: Phone number format

          protocols: Supported protocols (comma-separated)

          umts_bands: Supported UMTS bands

          website: Company website

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/carriers",
            body=maybe_transform(
                {
                    "country": country,
                    "mcc": mcc,
                    "mnc": mnc,
                    "operator": operator,
                    "company": company,
                    "country_code": country_code,
                    "country_iso": country_iso,
                    "detail_url": detail_url,
                    "gsm_bands": gsm_bands,
                    "lte_bands": lte_bands,
                    "mobile_prefix": mobile_prefix,
                    "nsn_size": nsn_size,
                    "number_format": number_format,
                    "protocols": protocols,
                    "umts_bands": umts_bands,
                    "website": website,
                },
                carrier_create_params.CarrierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierCreateResponse,
        )

    def retrieve(
        self,
        carrier_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierRetrieveResponse:
        """
        Get carrier by ID

        Args:
          carrier_id: Carrier ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/carriers/{carrier_id}", carrier_id=carrier_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierRetrieveResponse,
        )

    def update(
        self,
        carrier_id: int,
        *,
        company: str | Omit = omit,
        country: str | Omit = omit,
        country_code: str | Omit = omit,
        country_iso: str | Omit = omit,
        detail_url: str | Omit = omit,
        gsm_bands: str | Omit = omit,
        lte_bands: str | Omit = omit,
        mobile_prefix: str | Omit = omit,
        nsn_size: str | Omit = omit,
        number_format: str | Omit = omit,
        operator: str | Omit = omit,
        protocols: str | Omit = omit,
        umts_bands: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierUpdateResponse:
        """
        Update a carrier

        Args:
          carrier_id: Carrier ID

          company: Company name

          country: Country name

          country_code: Country dialing code

          country_iso: ISO country code

          detail_url: URL to carrier details

          gsm_bands: Supported GSM bands

          lte_bands: Supported LTE bands

          mobile_prefix: Mobile number prefix

          nsn_size: NSN size

          number_format: Phone number format

          operator: Operator name

          protocols: Supported protocols

          umts_bands: Supported UMTS bands

          website: Company website

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/carriers/{carrier_id}", carrier_id=carrier_id),
            body=maybe_transform(
                {
                    "company": company,
                    "country": country,
                    "country_code": country_code,
                    "country_iso": country_iso,
                    "detail_url": detail_url,
                    "gsm_bands": gsm_bands,
                    "lte_bands": lte_bands,
                    "mobile_prefix": mobile_prefix,
                    "nsn_size": nsn_size,
                    "number_format": number_format,
                    "operator": operator,
                    "protocols": protocols,
                    "umts_bands": umts_bands,
                    "website": website,
                },
                carrier_update_params.CarrierUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierUpdateResponse,
        )

    def list(
        self,
        *,
        country: str | Omit = omit,
        country_iso: str | Omit = omit,
        order_by: Literal["id", "mcc", "mnc", "operator", "country", "country_iso"] | Omit = omit,
        order_dir: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierListResponse:
        """
        List carriers with pagination

        Args:
          country: Filter by country name

          country_iso: Filter by country ISO code

          order_by: Field to order by

          order_dir: Order direction

          page: Page number

          page_size: Items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/carriers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "country_iso": country_iso,
                        "order_by": order_by,
                        "order_dir": order_dir,
                        "page": page,
                        "page_size": page_size,
                    },
                    carrier_list_params.CarrierListParams,
                ),
            ),
            cast_to=CarrierListResponse,
        )

    def delete(
        self,
        carrier_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierDeleteResponse:
        """
        Delete a carrier

        Args:
          carrier_id: Carrier ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/carriers/{carrier_id}", carrier_id=carrier_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierDeleteResponse,
        )

    def lookup(
        self,
        *,
        mcc: str,
        mnc: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierLookupResponse:
        """
        Get carrier by MCC and MNC

        Args:
          mcc: Mobile Country Code

          mnc: Mobile Network Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/carriers/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "mcc": mcc,
                        "mnc": mnc,
                    },
                    carrier_lookup_params.CarrierLookupParams,
                ),
            ),
            cast_to=CarrierLookupResponse,
        )


class AsyncCarriersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCarriersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCarriersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCarriersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncCarriersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        country: str,
        mcc: str,
        mnc: str,
        operator: str,
        company: str | Omit = omit,
        country_code: str | Omit = omit,
        country_iso: str | Omit = omit,
        detail_url: str | Omit = omit,
        gsm_bands: str | Omit = omit,
        lte_bands: str | Omit = omit,
        mobile_prefix: str | Omit = omit,
        nsn_size: str | Omit = omit,
        number_format: str | Omit = omit,
        protocols: str | Omit = omit,
        umts_bands: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierCreateResponse:
        """
        Create a new carrier

        Args:
          country: Country name

          mcc: Mobile Country Code

          mnc: Mobile Network Code

          operator: Operator name

          company: Company name

          country_code: Country dialing code (e.g., +1)

          country_iso: ISO country code

          detail_url: URL to carrier details page

          gsm_bands: Supported GSM bands

          lte_bands: Supported LTE bands

          mobile_prefix: Mobile number prefix

          nsn_size: National Significant Number size

          number_format: Phone number format

          protocols: Supported protocols (comma-separated)

          umts_bands: Supported UMTS bands

          website: Company website

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/carriers",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "mcc": mcc,
                    "mnc": mnc,
                    "operator": operator,
                    "company": company,
                    "country_code": country_code,
                    "country_iso": country_iso,
                    "detail_url": detail_url,
                    "gsm_bands": gsm_bands,
                    "lte_bands": lte_bands,
                    "mobile_prefix": mobile_prefix,
                    "nsn_size": nsn_size,
                    "number_format": number_format,
                    "protocols": protocols,
                    "umts_bands": umts_bands,
                    "website": website,
                },
                carrier_create_params.CarrierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierCreateResponse,
        )

    async def retrieve(
        self,
        carrier_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierRetrieveResponse:
        """
        Get carrier by ID

        Args:
          carrier_id: Carrier ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/carriers/{carrier_id}", carrier_id=carrier_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierRetrieveResponse,
        )

    async def update(
        self,
        carrier_id: int,
        *,
        company: str | Omit = omit,
        country: str | Omit = omit,
        country_code: str | Omit = omit,
        country_iso: str | Omit = omit,
        detail_url: str | Omit = omit,
        gsm_bands: str | Omit = omit,
        lte_bands: str | Omit = omit,
        mobile_prefix: str | Omit = omit,
        nsn_size: str | Omit = omit,
        number_format: str | Omit = omit,
        operator: str | Omit = omit,
        protocols: str | Omit = omit,
        umts_bands: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierUpdateResponse:
        """
        Update a carrier

        Args:
          carrier_id: Carrier ID

          company: Company name

          country: Country name

          country_code: Country dialing code

          country_iso: ISO country code

          detail_url: URL to carrier details

          gsm_bands: Supported GSM bands

          lte_bands: Supported LTE bands

          mobile_prefix: Mobile number prefix

          nsn_size: NSN size

          number_format: Phone number format

          operator: Operator name

          protocols: Supported protocols

          umts_bands: Supported UMTS bands

          website: Company website

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/carriers/{carrier_id}", carrier_id=carrier_id),
            body=await async_maybe_transform(
                {
                    "company": company,
                    "country": country,
                    "country_code": country_code,
                    "country_iso": country_iso,
                    "detail_url": detail_url,
                    "gsm_bands": gsm_bands,
                    "lte_bands": lte_bands,
                    "mobile_prefix": mobile_prefix,
                    "nsn_size": nsn_size,
                    "number_format": number_format,
                    "operator": operator,
                    "protocols": protocols,
                    "umts_bands": umts_bands,
                    "website": website,
                },
                carrier_update_params.CarrierUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierUpdateResponse,
        )

    async def list(
        self,
        *,
        country: str | Omit = omit,
        country_iso: str | Omit = omit,
        order_by: Literal["id", "mcc", "mnc", "operator", "country", "country_iso"] | Omit = omit,
        order_dir: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierListResponse:
        """
        List carriers with pagination

        Args:
          country: Filter by country name

          country_iso: Filter by country ISO code

          order_by: Field to order by

          order_dir: Order direction

          page: Page number

          page_size: Items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/carriers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "country_iso": country_iso,
                        "order_by": order_by,
                        "order_dir": order_dir,
                        "page": page,
                        "page_size": page_size,
                    },
                    carrier_list_params.CarrierListParams,
                ),
            ),
            cast_to=CarrierListResponse,
        )

    async def delete(
        self,
        carrier_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierDeleteResponse:
        """
        Delete a carrier

        Args:
          carrier_id: Carrier ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/carriers/{carrier_id}", carrier_id=carrier_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierDeleteResponse,
        )

    async def lookup(
        self,
        *,
        mcc: str,
        mnc: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CarrierLookupResponse:
        """
        Get carrier by MCC and MNC

        Args:
          mcc: Mobile Country Code

          mnc: Mobile Network Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/carriers/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "mcc": mcc,
                        "mnc": mnc,
                    },
                    carrier_lookup_params.CarrierLookupParams,
                ),
            ),
            cast_to=CarrierLookupResponse,
        )


class CarriersResourceWithRawResponse:
    def __init__(self, carriers: CarriersResource) -> None:
        self._carriers = carriers

        self.create = to_raw_response_wrapper(
            carriers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            carriers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            carriers.update,
        )
        self.list = to_raw_response_wrapper(
            carriers.list,
        )
        self.delete = to_raw_response_wrapper(
            carriers.delete,
        )
        self.lookup = to_raw_response_wrapper(
            carriers.lookup,
        )


class AsyncCarriersResourceWithRawResponse:
    def __init__(self, carriers: AsyncCarriersResource) -> None:
        self._carriers = carriers

        self.create = async_to_raw_response_wrapper(
            carriers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            carriers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            carriers.update,
        )
        self.list = async_to_raw_response_wrapper(
            carriers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            carriers.delete,
        )
        self.lookup = async_to_raw_response_wrapper(
            carriers.lookup,
        )


class CarriersResourceWithStreamingResponse:
    def __init__(self, carriers: CarriersResource) -> None:
        self._carriers = carriers

        self.create = to_streamed_response_wrapper(
            carriers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            carriers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            carriers.update,
        )
        self.list = to_streamed_response_wrapper(
            carriers.list,
        )
        self.delete = to_streamed_response_wrapper(
            carriers.delete,
        )
        self.lookup = to_streamed_response_wrapper(
            carriers.lookup,
        )


class AsyncCarriersResourceWithStreamingResponse:
    def __init__(self, carriers: AsyncCarriersResource) -> None:
        self._carriers = carriers

        self.create = async_to_streamed_response_wrapper(
            carriers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            carriers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            carriers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            carriers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            carriers.delete,
        )
        self.lookup = async_to_streamed_response_wrapper(
            carriers.lookup,
        )
