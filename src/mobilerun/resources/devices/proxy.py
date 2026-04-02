# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.devices import proxy_connect_params

__all__ = ["ProxyResource", "AsyncProxyResource"]


class ProxyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProxyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ProxyResourceWithStreamingResponse(self)

    def connect(
        self,
        device_id: str,
        *,
        host: str | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        port: int | Omit = omit,
        smart_ip: bool | Omit = omit,
        socks5: proxy_connect_params.Socks5 | Omit = omit,
        user: str | Omit = omit,
        wireguard: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Connect proxy

        Args:
          name: Proxy name (used for wireguard tunnel name)

          socks5: SOCKS5 proxy configuration (required for socks5).

          wireguard: WireGuard tunnel configuration file content (required for wireguard).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "password": password,
                    "port": port,
                    "smart_ip": smart_ip,
                    "socks5": socks5,
                    "user": user,
                    "wireguard": wireguard,
                },
                proxy_connect_params.ProxyConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def disconnect(
        self,
        device_id: str,
        *,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disconnect proxy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncProxyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProxyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncProxyResourceWithStreamingResponse(self)

    async def connect(
        self,
        device_id: str,
        *,
        host: str | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        port: int | Omit = omit,
        smart_ip: bool | Omit = omit,
        socks5: proxy_connect_params.Socks5 | Omit = omit,
        user: str | Omit = omit,
        wireguard: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Connect proxy

        Args:
          name: Proxy name (used for wireguard tunnel name)

          socks5: SOCKS5 proxy configuration (required for socks5).

          wireguard: WireGuard tunnel configuration file content (required for wireguard).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "password": password,
                    "port": port,
                    "smart_ip": smart_ip,
                    "socks5": socks5,
                    "user": user,
                    "wireguard": wireguard,
                },
                proxy_connect_params.ProxyConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def disconnect(
        self,
        device_id: str,
        *,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disconnect proxy

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ProxyResourceWithRawResponse:
    def __init__(self, proxy: ProxyResource) -> None:
        self._proxy = proxy

        self.connect = to_raw_response_wrapper(
            proxy.connect,
        )
        self.disconnect = to_raw_response_wrapper(
            proxy.disconnect,
        )


class AsyncProxyResourceWithRawResponse:
    def __init__(self, proxy: AsyncProxyResource) -> None:
        self._proxy = proxy

        self.connect = async_to_raw_response_wrapper(
            proxy.connect,
        )
        self.disconnect = async_to_raw_response_wrapper(
            proxy.disconnect,
        )


class ProxyResourceWithStreamingResponse:
    def __init__(self, proxy: ProxyResource) -> None:
        self._proxy = proxy

        self.connect = to_streamed_response_wrapper(
            proxy.connect,
        )
        self.disconnect = to_streamed_response_wrapper(
            proxy.disconnect,
        )


class AsyncProxyResourceWithStreamingResponse:
    def __init__(self, proxy: AsyncProxyResource) -> None:
        self._proxy = proxy

        self.connect = async_to_streamed_response_wrapper(
            proxy.connect,
        )
        self.disconnect = async_to_streamed_response_wrapper(
            proxy.disconnect,
        )
