# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import number_list_params, number_create_params, number_update_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.number_list_response import NumberListResponse
from ...types.number_create_response import NumberCreateResponse
from ...types.number_delete_response import NumberDeleteResponse
from ...types.number_update_response import NumberUpdateResponse
from ...types.number_purposes_response import NumberPurposesResponse
from ...types.number_retrieve_response import NumberRetrieveResponse
from ...types.number_countries_response import NumberCountriesResponse

__all__ = ["NumbersResource", "AsyncNumbersResource"]


class NumbersResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> NumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return NumbersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        billing_preference: Literal["included", "included_only", "rent"] | Omit = omit,
        country: str | Omit = omit,
        label: Optional[str] | Omit = omit,
        purpose: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberCreateResponse:
        """Starts a phone-number purchase.

        Poll the returned phone number for status
        updates. `purpose` and `country` cannot be combined.

        Args:
          billing_preference: Use included capacity when available, require included capacity without paid
              fallback (included_only), or start a paid checkout (rent).

          country: Optional ISO 3166-1 alpha-2 country code from GET /numbers/phones/countries.
              Cannot be combined with `purpose`.

          label: User-defined display label — NFC-normalized, up to 100 GRAPHEMES (not UTF-16
              code units; an emoji/flag may span several). Display-only, never used for
              routing. Also seeds the billing entity name at purchase.

          purpose: Optional purpose from GET /numbers/phones/purposes.

          idempotency_key: Optional request idempotency key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/numbers/phones",
            body=maybe_transform(
                {
                    "billing_preference": billing_preference,
                    "country": country,
                    "label": label,
                    "purpose": purpose,
                },
                number_create_params.NumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRetrieveResponse:
        """
        Retrieves a single phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/numbers/phones/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        label: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberUpdateResponse:
        """Updates the display label.

        Omitting `label` leaves it unchanged; null or an
        empty string clears it.

        Args:
          label: User-defined display label — NFC-normalized, up to 100 GRAPHEMES (not UTF-16
              code units; an emoji/flag may span several). Display-only, never used for
              routing. Also seeds the billing entity name at purchase.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/numbers/phones/{id}", id=id),
            body=maybe_transform({"label": label}, number_update_params.NumberUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberListResponse:
        """
        Lists the caller's phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/numbers/phones",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    number_list_params.NumberListParams,
                ),
            ),
            cast_to=NumberListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberDeleteResponse:
        """
        Cancels a pending purchase or schedules cancellation of an active paid phone
        number. Repeating a scheduled cancellation is safe. Returns 409 when
        cancellation is not available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/numbers/phones/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberDeleteResponse,
        )

    def countries(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberCountriesResponse:
        """Lists available countries and current phone-number availability."""
        return self._get(
            "/numbers/phones/countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberCountriesResponse,
        )

    def purposes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberPurposesResponse:
        """Lists the optional purposes currently available for a Mobilerun Phone."""
        return self._get(
            "/numbers/phones/purposes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberPurposesResponse,
        )


class AsyncNumbersResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncNumbersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        billing_preference: Literal["included", "included_only", "rent"] | Omit = omit,
        country: str | Omit = omit,
        label: Optional[str] | Omit = omit,
        purpose: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberCreateResponse:
        """Starts a phone-number purchase.

        Poll the returned phone number for status
        updates. `purpose` and `country` cannot be combined.

        Args:
          billing_preference: Use included capacity when available, require included capacity without paid
              fallback (included_only), or start a paid checkout (rent).

          country: Optional ISO 3166-1 alpha-2 country code from GET /numbers/phones/countries.
              Cannot be combined with `purpose`.

          label: User-defined display label — NFC-normalized, up to 100 GRAPHEMES (not UTF-16
              code units; an emoji/flag may span several). Display-only, never used for
              routing. Also seeds the billing entity name at purchase.

          purpose: Optional purpose from GET /numbers/phones/purposes.

          idempotency_key: Optional request idempotency key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/numbers/phones",
            body=await async_maybe_transform(
                {
                    "billing_preference": billing_preference,
                    "country": country,
                    "label": label,
                    "purpose": purpose,
                },
                number_create_params.NumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRetrieveResponse:
        """
        Retrieves a single phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/numbers/phones/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        label: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberUpdateResponse:
        """Updates the display label.

        Omitting `label` leaves it unchanged; null or an
        empty string clears it.

        Args:
          label: User-defined display label — NFC-normalized, up to 100 GRAPHEMES (not UTF-16
              code units; an emoji/flag may span several). Display-only, never used for
              routing. Also seeds the billing entity name at purchase.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/numbers/phones/{id}", id=id),
            body=await async_maybe_transform({"label": label}, number_update_params.NumberUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberListResponse:
        """
        Lists the caller's phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/numbers/phones",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    number_list_params.NumberListParams,
                ),
            ),
            cast_to=NumberListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberDeleteResponse:
        """
        Cancels a pending purchase or schedules cancellation of an active paid phone
        number. Repeating a scheduled cancellation is safe. Returns 409 when
        cancellation is not available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/numbers/phones/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberDeleteResponse,
        )

    async def countries(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberCountriesResponse:
        """Lists available countries and current phone-number availability."""
        return await self._get(
            "/numbers/phones/countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberCountriesResponse,
        )

    async def purposes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberPurposesResponse:
        """Lists the optional purposes currently available for a Mobilerun Phone."""
        return await self._get(
            "/numbers/phones/purposes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberPurposesResponse,
        )


class NumbersResourceWithRawResponse:
    def __init__(self, numbers: NumbersResource) -> None:
        self._numbers = numbers

        self.create = to_raw_response_wrapper(
            numbers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            numbers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            numbers.update,
        )
        self.list = to_raw_response_wrapper(
            numbers.list,
        )
        self.delete = to_raw_response_wrapper(
            numbers.delete,
        )
        self.countries = to_raw_response_wrapper(
            numbers.countries,
        )
        self.purposes = to_raw_response_wrapper(
            numbers.purposes,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._numbers.messages)


class AsyncNumbersResourceWithRawResponse:
    def __init__(self, numbers: AsyncNumbersResource) -> None:
        self._numbers = numbers

        self.create = async_to_raw_response_wrapper(
            numbers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            numbers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            numbers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            numbers.delete,
        )
        self.countries = async_to_raw_response_wrapper(
            numbers.countries,
        )
        self.purposes = async_to_raw_response_wrapper(
            numbers.purposes,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._numbers.messages)


class NumbersResourceWithStreamingResponse:
    def __init__(self, numbers: NumbersResource) -> None:
        self._numbers = numbers

        self.create = to_streamed_response_wrapper(
            numbers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            numbers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            numbers.update,
        )
        self.list = to_streamed_response_wrapper(
            numbers.list,
        )
        self.delete = to_streamed_response_wrapper(
            numbers.delete,
        )
        self.countries = to_streamed_response_wrapper(
            numbers.countries,
        )
        self.purposes = to_streamed_response_wrapper(
            numbers.purposes,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._numbers.messages)


class AsyncNumbersResourceWithStreamingResponse:
    def __init__(self, numbers: AsyncNumbersResource) -> None:
        self._numbers = numbers

        self.create = async_to_streamed_response_wrapper(
            numbers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            numbers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            numbers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            numbers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            numbers.delete,
        )
        self.countries = async_to_streamed_response_wrapper(
            numbers.countries,
        )
        self.purposes = async_to_streamed_response_wrapper(
            numbers.purposes,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._numbers.messages)
