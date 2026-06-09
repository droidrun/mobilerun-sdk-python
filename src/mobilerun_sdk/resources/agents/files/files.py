# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .file_id import (
    FileIDResource,
    AsyncFileIDResource,
    FileIDResourceWithRawResponse,
    AsyncFileIDResourceWithRawResponse,
    FileIDResourceWithStreamingResponse,
    AsyncFileIDResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents import file_list_files_params, file_mint_upload_url_params
from ....types.agents.file_list_files_response import FileListFilesResponse
from ....types.agents.file_mint_upload_url_response import FileMintUploadURLResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def file_id(self) -> FileIDResource:
        return FileIDResource(self._client)

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def list_files(
        self,
        *,
        zone: Literal["user", "agent", "workflow", "skills"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListFilesResponse:
        """
        List the user's ready files, optionally filtered by zone

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/agents/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"zone": zone}, file_list_files_params.FileListFilesParams),
            ),
            cast_to=FileListFilesResponse,
        )

    def mint_upload_url(
        self,
        *,
        filename: str,
        mime_type: str,
        size_bytes: int,
        zone: Literal["user", "skills"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileMintUploadURLResponse:
        """
        Mint a presigned PUT URL for a user file upload

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/agents/files/upload-url",
            body=maybe_transform(
                {
                    "filename": filename,
                    "mime_type": mime_type,
                    "size_bytes": size_bytes,
                    "zone": zone,
                },
                file_mint_upload_url_params.FileMintUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileMintUploadURLResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def file_id(self) -> AsyncFileIDResource:
        return AsyncFileIDResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def list_files(
        self,
        *,
        zone: Literal["user", "agent", "workflow", "skills"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListFilesResponse:
        """
        List the user's ready files, optionally filtered by zone

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/agents/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"zone": zone}, file_list_files_params.FileListFilesParams),
            ),
            cast_to=FileListFilesResponse,
        )

    async def mint_upload_url(
        self,
        *,
        filename: str,
        mime_type: str,
        size_bytes: int,
        zone: Literal["user", "skills"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileMintUploadURLResponse:
        """
        Mint a presigned PUT URL for a user file upload

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/agents/files/upload-url",
            body=await async_maybe_transform(
                {
                    "filename": filename,
                    "mime_type": mime_type,
                    "size_bytes": size_bytes,
                    "zone": zone,
                },
                file_mint_upload_url_params.FileMintUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileMintUploadURLResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list_files = to_raw_response_wrapper(
            files.list_files,
        )
        self.mint_upload_url = to_raw_response_wrapper(
            files.mint_upload_url,
        )

    @cached_property
    def file_id(self) -> FileIDResourceWithRawResponse:
        return FileIDResourceWithRawResponse(self._files.file_id)


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list_files = async_to_raw_response_wrapper(
            files.list_files,
        )
        self.mint_upload_url = async_to_raw_response_wrapper(
            files.mint_upload_url,
        )

    @cached_property
    def file_id(self) -> AsyncFileIDResourceWithRawResponse:
        return AsyncFileIDResourceWithRawResponse(self._files.file_id)


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list_files = to_streamed_response_wrapper(
            files.list_files,
        )
        self.mint_upload_url = to_streamed_response_wrapper(
            files.mint_upload_url,
        )

    @cached_property
    def file_id(self) -> FileIDResourceWithStreamingResponse:
        return FileIDResourceWithStreamingResponse(self._files.file_id)


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list_files = async_to_streamed_response_wrapper(
            files.list_files,
        )
        self.mint_upload_url = async_to_streamed_response_wrapper(
            files.mint_upload_url,
        )

    @cached_property
    def file_id(self) -> AsyncFileIDResourceWithStreamingResponse:
        return AsyncFileIDResourceWithStreamingResponse(self._files.file_id)
