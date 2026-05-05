# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import app_list_params, app_create_signed_upload_url_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.app_list_response import AppListResponse
from ..types.app_delete_response import AppDeleteResponse
from ..types.app_retrieve_response import AppRetrieveResponse
from ..types.app_mark_failed_response import AppMarkFailedResponse
from ..types.app_confirm_upload_response import AppConfirmUploadResponse
from ..types.app_create_signed_upload_url_response import AppCreateSignedUploadURLResponse

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
    ) -> AppRetrieveResponse:
        """
        Retrieves an app by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/apps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppRetrieveResponse,
        )

    def list(
        self,
        *,
        order: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        query: str | Omit = omit,
        sort_by: Literal["createdAt", "name"] | Omit = omit,
        source: Literal["all", "uploaded", "store", "queued"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppListResponse:
        """
        Retrieves a paginated list of apps with filtering and search capabilities

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                        "query": query,
                        "sort_by": sort_by,
                        "source": source,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            cast_to=AppListResponse,
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
    ) -> AppDeleteResponse:
        """Deletes an uploaded app by ID.

        Removes files from R2 storage and the database
        entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/apps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppDeleteResponse,
        )

    def confirm_upload(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppConfirmUploadResponse:
        """
        Verifies the APK file exists in R2 and sets the app status to available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/apps/{id}/confirm-upload", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppConfirmUploadResponse,
        )

    def create_signed_upload_url(
        self,
        *,
        display_name: str,
        files: Iterable[app_create_signed_upload_url_params.File],
        package_name: str,
        size_bytes: float,
        target_sdk: float,
        version_code: float,
        version_name: str,
        category_name: str | Omit = omit,
        country: str | Omit = omit,
        description: str | Omit = omit,
        developer_name: str | Omit = omit,
        icon_url: str | Omit = omit,
        rating_count: float | Omit = omit,
        rating_score: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppCreateSignedUploadURLResponse:
        """
        Creates or updates an app and returns pre-signed Cloudflare R2 upload URLs for
        each file

        Args:
          country: Country code for Search Results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/apps/create-signed-upload-url",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "files": files,
                    "package_name": package_name,
                    "size_bytes": size_bytes,
                    "target_sdk": target_sdk,
                    "version_code": version_code,
                    "version_name": version_name,
                    "category_name": category_name,
                    "country": country,
                    "description": description,
                    "developer_name": developer_name,
                    "icon_url": icon_url,
                    "rating_count": rating_count,
                    "rating_score": rating_score,
                },
                app_create_signed_upload_url_params.AppCreateSignedUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppCreateSignedUploadURLResponse,
        )

    def mark_failed(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppMarkFailedResponse:
        """
        Sets the app status to failed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/apps/{id}/mark-failed", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppMarkFailedResponse,
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
    ) -> AppRetrieveResponse:
        """
        Retrieves an app by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/apps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppRetrieveResponse,
        )

    async def list(
        self,
        *,
        order: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        query: str | Omit = omit,
        sort_by: Literal["createdAt", "name"] | Omit = omit,
        source: Literal["all", "uploaded", "store", "queued"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppListResponse:
        """
        Retrieves a paginated list of apps with filtering and search capabilities

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                        "query": query,
                        "sort_by": sort_by,
                        "source": source,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            cast_to=AppListResponse,
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
    ) -> AppDeleteResponse:
        """Deletes an uploaded app by ID.

        Removes files from R2 storage and the database
        entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/apps/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppDeleteResponse,
        )

    async def confirm_upload(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppConfirmUploadResponse:
        """
        Verifies the APK file exists in R2 and sets the app status to available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/apps/{id}/confirm-upload", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppConfirmUploadResponse,
        )

    async def create_signed_upload_url(
        self,
        *,
        display_name: str,
        files: Iterable[app_create_signed_upload_url_params.File],
        package_name: str,
        size_bytes: float,
        target_sdk: float,
        version_code: float,
        version_name: str,
        category_name: str | Omit = omit,
        country: str | Omit = omit,
        description: str | Omit = omit,
        developer_name: str | Omit = omit,
        icon_url: str | Omit = omit,
        rating_count: float | Omit = omit,
        rating_score: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppCreateSignedUploadURLResponse:
        """
        Creates or updates an app and returns pre-signed Cloudflare R2 upload URLs for
        each file

        Args:
          country: Country code for Search Results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/apps/create-signed-upload-url",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "files": files,
                    "package_name": package_name,
                    "size_bytes": size_bytes,
                    "target_sdk": target_sdk,
                    "version_code": version_code,
                    "version_name": version_name,
                    "category_name": category_name,
                    "country": country,
                    "description": description,
                    "developer_name": developer_name,
                    "icon_url": icon_url,
                    "rating_count": rating_count,
                    "rating_score": rating_score,
                },
                app_create_signed_upload_url_params.AppCreateSignedUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppCreateSignedUploadURLResponse,
        )

    async def mark_failed(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppMarkFailedResponse:
        """
        Sets the app status to failed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/apps/{id}/mark-failed", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppMarkFailedResponse,
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
        self.delete = to_raw_response_wrapper(
            apps.delete,
        )
        self.confirm_upload = to_raw_response_wrapper(
            apps.confirm_upload,
        )
        self.create_signed_upload_url = to_raw_response_wrapper(
            apps.create_signed_upload_url,
        )
        self.mark_failed = to_raw_response_wrapper(
            apps.mark_failed,
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
        self.delete = async_to_raw_response_wrapper(
            apps.delete,
        )
        self.confirm_upload = async_to_raw_response_wrapper(
            apps.confirm_upload,
        )
        self.create_signed_upload_url = async_to_raw_response_wrapper(
            apps.create_signed_upload_url,
        )
        self.mark_failed = async_to_raw_response_wrapper(
            apps.mark_failed,
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
        self.delete = to_streamed_response_wrapper(
            apps.delete,
        )
        self.confirm_upload = to_streamed_response_wrapper(
            apps.confirm_upload,
        )
        self.create_signed_upload_url = to_streamed_response_wrapper(
            apps.create_signed_upload_url,
        )
        self.mark_failed = to_streamed_response_wrapper(
            apps.mark_failed,
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
        self.delete = async_to_streamed_response_wrapper(
            apps.delete,
        )
        self.confirm_upload = async_to_streamed_response_wrapper(
            apps.confirm_upload,
        )
        self.create_signed_upload_url = async_to_streamed_response_wrapper(
            apps.create_signed_upload_url,
        )
        self.mark_failed = async_to_streamed_response_wrapper(
            apps.mark_failed,
        )
