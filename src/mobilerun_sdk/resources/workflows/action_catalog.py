# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.workflows import action_catalog_list_params
from ...types.workflows.action_catalog_list_response import ActionCatalogListResponse
from ...types.workflows.action_catalog_retrieve_response import ActionCatalogRetrieveResponse

__all__ = ["ActionCatalogResource", "AsyncActionCatalogResource"]


class ActionCatalogResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ActionCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ActionCatalogResourceWithStreamingResponse(self)

    def retrieve(
        self,
        catalog_entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCatalogRetrieveResponse:
        """
        Fetch a single action catalog entry by its ID, including its service, method,
        and parameter schema. Returns 404 if no entry matches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not catalog_entry_id:
            raise ValueError(f"Expected a non-empty value for `catalog_entry_id` but received {catalog_entry_id!r}")
        return self._get(
            path_template("/action-catalog/{catalog_entry_id}", catalog_entry_id=catalog_entry_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionCatalogRetrieveResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCatalogListResponse:
        """
        Return a paginated list of catalog entries — the service/method templates that
        actions are created from, each carrying its parameter schema. Supports filtering
        by `service`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/action-catalog",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "service": service,
                    },
                    action_catalog_list_params.ActionCatalogListParams,
                ),
            ),
            cast_to=ActionCatalogListResponse,
        )


class AsyncActionCatalogResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncActionCatalogResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        catalog_entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCatalogRetrieveResponse:
        """
        Fetch a single action catalog entry by its ID, including its service, method,
        and parameter schema. Returns 404 if no entry matches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not catalog_entry_id:
            raise ValueError(f"Expected a non-empty value for `catalog_entry_id` but received {catalog_entry_id!r}")
        return await self._get(
            path_template("/action-catalog/{catalog_entry_id}", catalog_entry_id=catalog_entry_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionCatalogRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCatalogListResponse:
        """
        Return a paginated list of catalog entries — the service/method templates that
        actions are created from, each carrying its parameter schema. Supports filtering
        by `service`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/action-catalog",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "service": service,
                    },
                    action_catalog_list_params.ActionCatalogListParams,
                ),
            ),
            cast_to=ActionCatalogListResponse,
        )


class ActionCatalogResourceWithRawResponse:
    def __init__(self, action_catalog: ActionCatalogResource) -> None:
        self._action_catalog = action_catalog

        self.retrieve = to_raw_response_wrapper(
            action_catalog.retrieve,
        )
        self.list = to_raw_response_wrapper(
            action_catalog.list,
        )


class AsyncActionCatalogResourceWithRawResponse:
    def __init__(self, action_catalog: AsyncActionCatalogResource) -> None:
        self._action_catalog = action_catalog

        self.retrieve = async_to_raw_response_wrapper(
            action_catalog.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            action_catalog.list,
        )


class ActionCatalogResourceWithStreamingResponse:
    def __init__(self, action_catalog: ActionCatalogResource) -> None:
        self._action_catalog = action_catalog

        self.retrieve = to_streamed_response_wrapper(
            action_catalog.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            action_catalog.list,
        )


class AsyncActionCatalogResourceWithStreamingResponse:
    def __init__(self, action_catalog: AsyncActionCatalogResource) -> None:
        self._action_catalog = action_catalog

        self.retrieve = async_to_streamed_response_wrapper(
            action_catalog.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            action_catalog.list,
        )
