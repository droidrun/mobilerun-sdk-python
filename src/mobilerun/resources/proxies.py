# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import proxy_create_params, proxy_update_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.proxy_list_response import ProxyListResponse
from ..types.proxy_create_response import ProxyCreateResponse
from ..types.proxy_delete_response import ProxyDeleteResponse
from ..types.proxy_update_response import ProxyUpdateResponse
from ..types.proxy_retrieve_response import ProxyRetrieveResponse

__all__ = ["ProxiesResource", "AsyncProxiesResource"]


class ProxiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ProxiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        host: str,
        name: str,
        password: str,
        port: int,
        user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyCreateResponse:
        """
        Create a new proxy config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/proxies",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "password": password,
                    "port": port,
                    "user": user,
                },
                proxy_create_params.ProxyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyCreateResponse,
        )

    def retrieve(
        self,
        proxy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyRetrieveResponse:
        """
        Get a specific proxy config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy_id:
            raise ValueError(f"Expected a non-empty value for `proxy_id` but received {proxy_id!r}")
        return self._get(
            f"/proxies/{proxy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyRetrieveResponse,
        )

    def update(
        self,
        proxy_id: str,
        *,
        host: str,
        name: str,
        password: str,
        port: int,
        user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyUpdateResponse:
        """
        Update a proxy config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy_id:
            raise ValueError(f"Expected a non-empty value for `proxy_id` but received {proxy_id!r}")
        return self._put(
            f"/proxies/{proxy_id}",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "password": password,
                    "port": port,
                    "user": user,
                },
                proxy_update_params.ProxyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyUpdateResponse,
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
    ) -> ProxyListResponse:
        """List all proxy configs for the authenticated user"""
        return self._get(
            "/proxies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyListResponse,
        )

    def delete(
        self,
        proxy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyDeleteResponse:
        """
        Delete a proxy config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy_id:
            raise ValueError(f"Expected a non-empty value for `proxy_id` but received {proxy_id!r}")
        return self._delete(
            f"/proxies/{proxy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyDeleteResponse,
        )


class AsyncProxiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncProxiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        host: str,
        name: str,
        password: str,
        port: int,
        user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyCreateResponse:
        """
        Create a new proxy config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/proxies",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "password": password,
                    "port": port,
                    "user": user,
                },
                proxy_create_params.ProxyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyCreateResponse,
        )

    async def retrieve(
        self,
        proxy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyRetrieveResponse:
        """
        Get a specific proxy config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy_id:
            raise ValueError(f"Expected a non-empty value for `proxy_id` but received {proxy_id!r}")
        return await self._get(
            f"/proxies/{proxy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyRetrieveResponse,
        )

    async def update(
        self,
        proxy_id: str,
        *,
        host: str,
        name: str,
        password: str,
        port: int,
        user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyUpdateResponse:
        """
        Update a proxy config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy_id:
            raise ValueError(f"Expected a non-empty value for `proxy_id` but received {proxy_id!r}")
        return await self._put(
            f"/proxies/{proxy_id}",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "password": password,
                    "port": port,
                    "user": user,
                },
                proxy_update_params.ProxyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyUpdateResponse,
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
    ) -> ProxyListResponse:
        """List all proxy configs for the authenticated user"""
        return await self._get(
            "/proxies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyListResponse,
        )

    async def delete(
        self,
        proxy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProxyDeleteResponse:
        """
        Delete a proxy config

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy_id:
            raise ValueError(f"Expected a non-empty value for `proxy_id` but received {proxy_id!r}")
        return await self._delete(
            f"/proxies/{proxy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyDeleteResponse,
        )


class ProxiesResourceWithRawResponse:
    def __init__(self, proxies: ProxiesResource) -> None:
        self._proxies = proxies

        self.create = to_raw_response_wrapper(
            proxies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            proxies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            proxies.update,
        )
        self.list = to_raw_response_wrapper(
            proxies.list,
        )
        self.delete = to_raw_response_wrapper(
            proxies.delete,
        )


class AsyncProxiesResourceWithRawResponse:
    def __init__(self, proxies: AsyncProxiesResource) -> None:
        self._proxies = proxies

        self.create = async_to_raw_response_wrapper(
            proxies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            proxies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            proxies.update,
        )
        self.list = async_to_raw_response_wrapper(
            proxies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            proxies.delete,
        )


class ProxiesResourceWithStreamingResponse:
    def __init__(self, proxies: ProxiesResource) -> None:
        self._proxies = proxies

        self.create = to_streamed_response_wrapper(
            proxies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            proxies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            proxies.update,
        )
        self.list = to_streamed_response_wrapper(
            proxies.list,
        )
        self.delete = to_streamed_response_wrapper(
            proxies.delete,
        )


class AsyncProxiesResourceWithStreamingResponse:
    def __init__(self, proxies: AsyncProxiesResource) -> None:
        self._proxies = proxies

        self.create = async_to_streamed_response_wrapper(
            proxies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            proxies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            proxies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            proxies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            proxies.delete,
        )
