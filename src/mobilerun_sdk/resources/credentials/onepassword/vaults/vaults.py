# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .items.items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["VaultsResource", "AsyncVaultsResource"]


class VaultsResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VaultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return VaultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VaultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return VaultsResourceWithStreamingResponse(self)


class AsyncVaultsResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVaultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVaultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVaultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncVaultsResourceWithStreamingResponse(self)


class VaultsResourceWithRawResponse:
    def __init__(self, vaults: VaultsResource) -> None:
        self._vaults = vaults

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._vaults.items)


class AsyncVaultsResourceWithRawResponse:
    def __init__(self, vaults: AsyncVaultsResource) -> None:
        self._vaults = vaults

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._vaults.items)


class VaultsResourceWithStreamingResponse:
    def __init__(self, vaults: VaultsResource) -> None:
        self._vaults = vaults

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._vaults.items)


class AsyncVaultsResourceWithStreamingResponse:
    def __init__(self, vaults: AsyncVaultsResource) -> None:
        self._vaults = vaults

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._vaults.items)
