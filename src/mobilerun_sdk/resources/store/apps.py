# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, maybe_transform, async_maybe_transform

from ...types.store.app_retrieve_response import AppRetrieveResponse

from ..._base_client import make_request_options

from ..._types import NotGiven, Omit, omit

from ...types.store.app_list_response import AppListResponse

from ...types.store.app_add_to_workspace_response import AppAddToWorkspaceResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.store import app_list_params

__all__ = ["AppsResource", "AsyncAppsResource"]

class AppsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    def retrieve(self,
    app_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppRetrieveResponse:
        """
        Retrieves a single published store listing, including freshly-resolved
        screenshotUrls. 404 for a draft or absent listing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
          raise ValueError(
            f'Expected a non-empty value for `app_id` but received {app_id!r}'
          )
        return self._get(
            path_template("/store/apps/{app_id}", app_id=app_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppRetrieveResponse,
        )

    def list(self,
    *,
    category: str | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    query: str | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppListResponse:
        """
        Paginated list of published store listings, ordered featured desc, sortOrder
        asc, displayName asc.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/store/apps",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "category": category,
                "page": page,
                "page_size": page_size,
                "query": query,
            }, app_list_params.AppListParams)),
            cast_to=AppListResponse,
        )

    def add_to_workspace(self,
    app_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppAddToWorkspaceResponse:
        """
        Installs a published store app into the caller's workspace — the existing
        device-install path takes over from there. 404 if no published listing exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
          raise ValueError(
            f'Expected a non-empty value for `app_id` but received {app_id!r}'
          )
        return self._post(
            path_template("/store/apps/{app_id}/add", app_id=app_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppAddToWorkspaceResponse,
        )

class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    async def retrieve(self,
    app_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppRetrieveResponse:
        """
        Retrieves a single published store listing, including freshly-resolved
        screenshotUrls. 404 for a draft or absent listing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
          raise ValueError(
            f'Expected a non-empty value for `app_id` but received {app_id!r}'
          )
        return await self._get(
            path_template("/store/apps/{app_id}", app_id=app_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppRetrieveResponse,
        )

    async def list(self,
    *,
    category: str | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    query: str | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppListResponse:
        """
        Paginated list of published store listings, ordered featured desc, sortOrder
        asc, displayName asc.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/store/apps",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "category": category,
                "page": page,
                "page_size": page_size,
                "query": query,
            }, app_list_params.AppListParams)),
            cast_to=AppListResponse,
        )

    async def add_to_workspace(self,
    app_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> AppAddToWorkspaceResponse:
        """
        Installs a published store app into the caller's workspace — the existing
        device-install path takes over from there. 404 if no published listing exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
          raise ValueError(
            f'Expected a non-empty value for `app_id` but received {app_id!r}'
          )
        return await self._post(
            path_template("/store/apps/{app_id}/add", app_id=app_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppAddToWorkspaceResponse,
        )

class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.retrieve = to_raw_response_wrapper(
            apps.retrieve,
        )
        self.list = to_raw_response_wrapper(
            apps.list,
        )
        self.add_to_workspace = to_raw_response_wrapper(
            apps.add_to_workspace,
        )

class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.retrieve = async_to_raw_response_wrapper(
            apps.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            apps.list,
        )
        self.add_to_workspace = async_to_raw_response_wrapper(
            apps.add_to_workspace,
        )

class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.retrieve = to_streamed_response_wrapper(
            apps.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            apps.list,
        )
        self.add_to_workspace = to_streamed_response_wrapper(
            apps.add_to_workspace,
        )

class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.retrieve = async_to_streamed_response_wrapper(
            apps.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            apps.list,
        )
        self.add_to_workspace = async_to_streamed_response_wrapper(
            apps.add_to_workspace,
        )