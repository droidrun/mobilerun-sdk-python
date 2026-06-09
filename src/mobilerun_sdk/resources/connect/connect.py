# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .proxies import (
    ProxiesResource,
    AsyncProxiesResource,
    ProxiesResourceWithRawResponse,
    AsyncProxiesResourceWithRawResponse,
    ProxiesResourceWithStreamingResponse,
    AsyncProxiesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .countries import (
    CountriesResource,
    AsyncCountriesResource,
    CountriesResourceWithRawResponse,
    AsyncCountriesResourceWithRawResponse,
    CountriesResourceWithStreamingResponse,
    AsyncCountriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ConnectResource", "AsyncConnectResource"]


class ConnectResource(SyncAPIResource):
    @cached_property
    def countries(self) -> CountriesResource:
        return CountriesResource(self._client)

    @cached_property
    def proxies(self) -> ProxiesResource:
        return ProxiesResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ConnectResourceWithStreamingResponse(self)


class AsyncConnectResource(AsyncAPIResource):
    @cached_property
    def countries(self) -> AsyncCountriesResource:
        return AsyncCountriesResource(self._client)

    @cached_property
    def proxies(self) -> AsyncProxiesResource:
        return AsyncProxiesResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncConnectResourceWithStreamingResponse(self)


class ConnectResourceWithRawResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

    @cached_property
    def countries(self) -> CountriesResourceWithRawResponse:
        return CountriesResourceWithRawResponse(self._connect.countries)

    @cached_property
    def proxies(self) -> ProxiesResourceWithRawResponse:
        return ProxiesResourceWithRawResponse(self._connect.proxies)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._connect.users)


class AsyncConnectResourceWithRawResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithRawResponse:
        return AsyncCountriesResourceWithRawResponse(self._connect.countries)

    @cached_property
    def proxies(self) -> AsyncProxiesResourceWithRawResponse:
        return AsyncProxiesResourceWithRawResponse(self._connect.proxies)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._connect.users)


class ConnectResourceWithStreamingResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

    @cached_property
    def countries(self) -> CountriesResourceWithStreamingResponse:
        return CountriesResourceWithStreamingResponse(self._connect.countries)

    @cached_property
    def proxies(self) -> ProxiesResourceWithStreamingResponse:
        return ProxiesResourceWithStreamingResponse(self._connect.proxies)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._connect.users)


class AsyncConnectResourceWithStreamingResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithStreamingResponse:
        return AsyncCountriesResourceWithStreamingResponse(self._connect.countries)

    @cached_property
    def proxies(self) -> AsyncProxiesResourceWithStreamingResponse:
        return AsyncProxiesResourceWithStreamingResponse(self._connect.proxies)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._connect.users)
