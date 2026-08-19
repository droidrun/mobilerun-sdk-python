# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from .messages import MessagesResource, AsyncMessagesResource, MessagesResourceWithRawResponse, AsyncMessagesResourceWithRawResponse, MessagesResourceWithStreamingResponse, AsyncMessagesResourceWithStreamingResponse

from ..._compat import cached_property

from ...types.number_create_response import NumberCreateResponse

from ..._utils import strip_not_given, is_given, maybe_transform, path_template, async_maybe_transform

from ..._base_client import make_request_options

from typing_extensions import Literal

from ..._types import Omit, omit, NotGiven

from ...types.number_retrieve_response import NumberRetrieveResponse

from ...types.number_list_response import NumberListResponse

from ...types.number_delete_response import NumberDeleteResponse

from ...types.number_countries_response import NumberCountriesResponse

from ...types.number_purposes_response import NumberPurposesResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types import number_create_params
from ...types import number_list_params

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

    def create(self,
    *,
    billing_preference: Literal["included", "rent"] | Omit = omit,
    country: str | Omit = omit,
    purpose: str | Omit = omit,
    idempotency_key: str | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberCreateResponse:
        """Starts a Mobilerun Phone purchase for the authenticated owner.

        Accepted requests
        always return the same asynchronous envelope; poll GET /numbers/phones/{id} for
        its business state. `purpose` and `country` are mutually exclusive.

        Args:
          billing_preference: Prefer a free package seat ('included', default) or force the paid checkout
              ('rent')

          country: Optional ISO 3166-1 alpha-2 country code from GET /numbers/countries. Cannot be
              combined with `purpose`.

          purpose: Optional Mobilerun Phone purpose slug from GET /numbers/purposes.

          idempotency_key: Optional request idempotency key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = { **strip_not_given({
            "Idempotency-Key": idempotency_key
        }), **(extra_headers or {}) }
        return self._post(
            "/numbers/phones",
            body=maybe_transform({
                "billing_preference": billing_preference,
                "country": country,
                "purpose": purpose,
            }, number_create_params.NumberCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NumberCreateResponse,
        )

    def retrieve(self,
    id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberRetrieveResponse:
        """
        Retrieves a single phone number.

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
            path_template("/numbers/phones/{id}", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NumberRetrieveResponse,
        )

    def list(self,
    *,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberListResponse:
        """
        Lists phone numbers owned by the authenticated user — both BYO (`user`) and
        provisioned (`mobilerun`) numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/numbers/phones",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "page": page,
                "page_size": page_size,
            }, number_list_params.NumberListParams)),
            cast_to=NumberListResponse,
        )

    def delete(self,
    id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberDeleteResponse:
        """Cancels a Mobilerun Phone.

        The outcome depends on the number's current state:

        - If the number is still awaiting payment and no payment for it is currently
          being processed, the checkout is closed immediately and the number is retired.
        - If the number is on the standard paid plan and already paid and in service,
          cancellation is scheduled for the end of the current billing period rather
          than taking effect immediately. The number stays usable through the period
          already paid for, with no partial refund. Calling this again while a
          cancellation is already scheduled is a no-op that returns the same result. The
          response's `state` reflects this as `cancel_scheduled` with
          `cancelAtPeriodEnd: true`; `currentPeriodEnd` is populated once billing
          confirms the cancellation.

        Any other state (already refunding, a permanent billing failure, a payment
        currently being processed, an included-plan number, or a non-hosted/BYO number)
        returns 409 `not_cancellable`. Returns 404 if the number doesn't exist or isn't
        owned by the caller.

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
        return self._delete(
            path_template("/numbers/phones/{id}", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NumberDeleteResponse,
        )

    def countries(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberCountriesResponse:
        """
        Lists the countries currently offered for a dedicated Mobilerun Phone, with live
        stock status. Pass `country` as the `country` field on POST /numbers/phones.
        """
        return self._get(
            "/numbers/phones/countries",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NumberCountriesResponse,
        )

    def purposes(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberPurposesResponse:
        """Lists the optional purposes currently available for a Mobilerun Phone."""
        return self._get(
            "/numbers/phones/purposes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
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

    async def create(self,
    *,
    billing_preference: Literal["included", "rent"] | Omit = omit,
    country: str | Omit = omit,
    purpose: str | Omit = omit,
    idempotency_key: str | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberCreateResponse:
        """Starts a Mobilerun Phone purchase for the authenticated owner.

        Accepted requests
        always return the same asynchronous envelope; poll GET /numbers/phones/{id} for
        its business state. `purpose` and `country` are mutually exclusive.

        Args:
          billing_preference: Prefer a free package seat ('included', default) or force the paid checkout
              ('rent')

          country: Optional ISO 3166-1 alpha-2 country code from GET /numbers/countries. Cannot be
              combined with `purpose`.

          purpose: Optional Mobilerun Phone purpose slug from GET /numbers/purposes.

          idempotency_key: Optional request idempotency key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = { **strip_not_given({
            "Idempotency-Key": idempotency_key
        }), **(extra_headers or {}) }
        return await self._post(
            "/numbers/phones",
            body=await async_maybe_transform({
                "billing_preference": billing_preference,
                "country": country,
                "purpose": purpose,
            }, number_create_params.NumberCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NumberCreateResponse,
        )

    async def retrieve(self,
    id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberRetrieveResponse:
        """
        Retrieves a single phone number.

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
            path_template("/numbers/phones/{id}", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NumberRetrieveResponse,
        )

    async def list(self,
    *,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberListResponse:
        """
        Lists phone numbers owned by the authenticated user — both BYO (`user`) and
        provisioned (`mobilerun`) numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/numbers/phones",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "page": page,
                "page_size": page_size,
            }, number_list_params.NumberListParams)),
            cast_to=NumberListResponse,
        )

    async def delete(self,
    id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberDeleteResponse:
        """Cancels a Mobilerun Phone.

        The outcome depends on the number's current state:

        - If the number is still awaiting payment and no payment for it is currently
          being processed, the checkout is closed immediately and the number is retired.
        - If the number is on the standard paid plan and already paid and in service,
          cancellation is scheduled for the end of the current billing period rather
          than taking effect immediately. The number stays usable through the period
          already paid for, with no partial refund. Calling this again while a
          cancellation is already scheduled is a no-op that returns the same result. The
          response's `state` reflects this as `cancel_scheduled` with
          `cancelAtPeriodEnd: true`; `currentPeriodEnd` is populated once billing
          confirms the cancellation.

        Any other state (already refunding, a permanent billing failure, a payment
        currently being processed, an included-plan number, or a non-hosted/BYO number)
        returns 409 `not_cancellable`. Returns 404 if the number doesn't exist or isn't
        owned by the caller.

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
        return await self._delete(
            path_template("/numbers/phones/{id}", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NumberDeleteResponse,
        )

    async def countries(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberCountriesResponse:
        """
        Lists the countries currently offered for a dedicated Mobilerun Phone, with live
        stock status. Pass `country` as the `country` field on POST /numbers/phones.
        """
        return await self._get(
            "/numbers/phones/countries",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NumberCountriesResponse,
        )

    async def purposes(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> NumberPurposesResponse:
        """Lists the optional purposes currently available for a Mobilerun Phone."""
        return await self._get(
            "/numbers/phones/purposes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
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