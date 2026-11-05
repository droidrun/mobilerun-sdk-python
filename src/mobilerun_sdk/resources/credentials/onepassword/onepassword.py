# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .vaults.vaults import (
    VaultsResource,
    AsyncVaultsResource,
    VaultsResourceWithRawResponse,
    AsyncVaultsResourceWithRawResponse,
    VaultsResourceWithStreamingResponse,
    AsyncVaultsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.credentials import onepassword_connect_params
from ....types.credentials.onepassword_connect_response import OnepasswordConnectResponse
from ....types.credentials.onepassword_retrieve_response import OnepasswordRetrieveResponse
from ....types.credentials.onepassword_disconnect_response import OnepasswordDisconnectResponse

__all__ = ["OnepasswordResource", "AsyncOnepasswordResource"]


class OnepasswordResource(SyncAPIResource):
    @cached_property
    def vaults(self) -> VaultsResource:
        return VaultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OnepasswordResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OnepasswordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnepasswordResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return OnepasswordResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnepasswordRetrieveResponse:
        """Get 1Password connection"""
        return self._get(
            "/credentials/onepassword",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnepasswordRetrieveResponse,
        )

    def connect(
        self,
        *,
        service_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> OnepasswordConnectResponse:
        """
        Connect a 1Password service account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._put(
            "/credentials/onepassword",
            body=maybe_transform(
                {"service_account_token": service_account_token}, onepassword_connect_params.OnepasswordConnectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OnepasswordConnectResponse,
        )

    def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> OnepasswordDisconnectResponse:
        """Disconnect 1Password"""
        return self._delete(
            "/credentials/onepassword",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OnepasswordDisconnectResponse,
        )


class AsyncOnepasswordResource(AsyncAPIResource):
    @cached_property
    def vaults(self) -> AsyncVaultsResource:
        return AsyncVaultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOnepasswordResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOnepasswordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnepasswordResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncOnepasswordResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnepasswordRetrieveResponse:
        """Get 1Password connection"""
        return await self._get(
            "/credentials/onepassword",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnepasswordRetrieveResponse,
        )

    async def connect(
        self,
        *,
        service_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> OnepasswordConnectResponse:
        """
        Connect a 1Password service account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._put(
            "/credentials/onepassword",
            body=await async_maybe_transform(
                {"service_account_token": service_account_token}, onepassword_connect_params.OnepasswordConnectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OnepasswordConnectResponse,
        )

    async def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> OnepasswordDisconnectResponse:
        """Disconnect 1Password"""
        return await self._delete(
            "/credentials/onepassword",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=OnepasswordDisconnectResponse,
        )


class OnepasswordResourceWithRawResponse:
    def __init__(self, onepassword: OnepasswordResource) -> None:
        self._onepassword = onepassword

        self.retrieve = to_raw_response_wrapper(
            onepassword.retrieve,
        )
        self.connect = to_raw_response_wrapper(
            onepassword.connect,
        )
        self.disconnect = to_raw_response_wrapper(
            onepassword.disconnect,
        )

    @cached_property
    def vaults(self) -> VaultsResourceWithRawResponse:
        return VaultsResourceWithRawResponse(self._onepassword.vaults)


class AsyncOnepasswordResourceWithRawResponse:
    def __init__(self, onepassword: AsyncOnepasswordResource) -> None:
        self._onepassword = onepassword

        self.retrieve = async_to_raw_response_wrapper(
            onepassword.retrieve,
        )
        self.connect = async_to_raw_response_wrapper(
            onepassword.connect,
        )
        self.disconnect = async_to_raw_response_wrapper(
            onepassword.disconnect,
        )

    @cached_property
    def vaults(self) -> AsyncVaultsResourceWithRawResponse:
        return AsyncVaultsResourceWithRawResponse(self._onepassword.vaults)


class OnepasswordResourceWithStreamingResponse:
    def __init__(self, onepassword: OnepasswordResource) -> None:
        self._onepassword = onepassword

        self.retrieve = to_streamed_response_wrapper(
            onepassword.retrieve,
        )
        self.connect = to_streamed_response_wrapper(
            onepassword.connect,
        )
        self.disconnect = to_streamed_response_wrapper(
            onepassword.disconnect,
        )

    @cached_property
    def vaults(self) -> VaultsResourceWithStreamingResponse:
        return VaultsResourceWithStreamingResponse(self._onepassword.vaults)


class AsyncOnepasswordResourceWithStreamingResponse:
    def __init__(self, onepassword: AsyncOnepasswordResource) -> None:
        self._onepassword = onepassword

        self.retrieve = async_to_streamed_response_wrapper(
            onepassword.retrieve,
        )
        self.connect = async_to_streamed_response_wrapper(
            onepassword.connect,
        )
        self.disconnect = async_to_streamed_response_wrapper(
            onepassword.disconnect,
        )

    @cached_property
    def vaults(self) -> AsyncVaultsResourceWithStreamingResponse:
        return AsyncVaultsResourceWithStreamingResponse(self._onepassword.vaults)
