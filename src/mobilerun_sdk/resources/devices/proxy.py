# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, strip_not_given, is_given, maybe_transform, async_maybe_transform

from ..._types import not_given, Omit, omit, NotGiven

from ..._base_client import make_request_options

from ...types.devices.proxy_status_response import ProxyStatusResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ...types.devices import proxy_connect_params

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
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

    def connect(self,
    device_id: str,
    *,
    connect: proxy_connect_params.Connect | Omit = omit,
    host: str | Omit = omit,
    name: str | Omit = omit,
    password: str | Omit = omit,
    port: int | Omit = omit,
    smart_ip: bool | Omit = omit,
    socks5: proxy_connect_params.Socks5 | Omit = omit,
    user: str | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Routes the device's traffic through a SOCKS5 proxy supplied in the request body,
        replacing any existing connection. A smartIp option can be used to select an IP
        automatically; the legacy flat host/port/user/password fields remain supported.

        Args:
          connect: Mobilerun Connect proxy — pass exactly one of id (use an existing proxy's
              credentials) or country (provision or reuse a rotating residential proxy for the
              device).

          name: Proxy name

          socks5: SOCKS5 proxy configuration (required for socks5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._post(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            body=maybe_transform({
                "connect": connect,
                "host": host,
                "name": name,
                "password": password,
                "port": port,
                "smart_ip": smart_ip,
                "socks5": socks5,
                "user": user,
            }, proxy_connect_params.ProxyConnectParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def disconnect(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Disconnects the device's active proxy connection and clears its stored proxy
        state. Returns successfully if no proxy is connected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._delete(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def status(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ProxyStatusResponse:
        """
        Returns the device's current proxy connection state, including whether a proxy
        is connected and its protocol and name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._get(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProxyStatusResponse,
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

    async def connect(self,
    device_id: str,
    *,
    connect: proxy_connect_params.Connect | Omit = omit,
    host: str | Omit = omit,
    name: str | Omit = omit,
    password: str | Omit = omit,
    port: int | Omit = omit,
    smart_ip: bool | Omit = omit,
    socks5: proxy_connect_params.Socks5 | Omit = omit,
    user: str | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Routes the device's traffic through a SOCKS5 proxy supplied in the request body,
        replacing any existing connection. A smartIp option can be used to select an IP
        automatically; the legacy flat host/port/user/password fields remain supported.

        Args:
          connect: Mobilerun Connect proxy — pass exactly one of id (use an existing proxy's
              credentials) or country (provision or reuse a rotating residential proxy for the
              device).

          name: Proxy name

          socks5: SOCKS5 proxy configuration (required for socks5).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._post(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            body=await async_maybe_transform({
                "connect": connect,
                "host": host,
                "name": name,
                "password": password,
                "port": port,
                "smart_ip": smart_ip,
                "socks5": socks5,
                "user": user,
            }, proxy_connect_params.ProxyConnectParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def disconnect(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Disconnects the device's active proxy connection and clears its stored proxy
        state. Returns successfully if no proxy is connected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._delete(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def status(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ProxyStatusResponse:
        """
        Returns the device's current proxy connection state, including whether a proxy
        is connected and its protocol and name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._get(
            path_template("/devices/{device_id}/proxy", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProxyStatusResponse,
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
        self.status = to_raw_response_wrapper(
            proxy.status,
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
        self.status = async_to_raw_response_wrapper(
            proxy.status,
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
        self.status = to_streamed_response_wrapper(
            proxy.status,
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
        self.status = async_to_streamed_response_wrapper(
            proxy.status,
        )