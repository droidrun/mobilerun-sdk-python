# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents.files import file_id_update_metadata_params
from ....types.agents.files.file_id_delete_file_response import FileIDDeleteFileResponse
from ....types.agents.files.file_id_confirm_upload_response import FileIDConfirmUploadResponse
from ....types.agents.files.file_id_update_metadata_response import FileIDUpdateMetadataResponse
from ....types.agents.files.file_id_cancel_pending_upload_response import FileIDCancelPendingUploadResponse

__all__ = ["FileIDResource", "AsyncFileIDResource"]


class FileIDResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FileIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return FileIDResourceWithStreamingResponse(self)

    def cancel_pending_upload(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileIDCancelPendingUploadResponse:
        """Soft-cancels an in-flight upload before confirm.

        Only acts on `pending` rows —
        refuses to touch `ready` to avoid wiping confirmed files. Idempotent:
        `{ cancelled: false }` if the row exists but is no longer pending.
        """
        return self._delete(
            "/agents/files/:fileId/pending",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileIDCancelPendingUploadResponse,
        )

    def confirm_upload(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileIDConfirmUploadResponse:
        """Confirm a file upload by server-side HEAD validation"""
        return self._post(
            "/agents/files/:fileId/confirm",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileIDConfirmUploadResponse,
        )

    def delete_file(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileIDDeleteFileResponse:
        """Hard-delete a file"""
        return self._delete(
            "/agents/files/:fileId",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileIDDeleteFileResponse,
        )

    def download_file(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Redirect to a presigned GET URL for a file (FE owner only)"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/agents/files/:fileId/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_metadata(
        self,
        *,
        display_name: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileIDUpdateMetadataResponse:
        """Partial update of `displayName` and/or `enabled`.

        Only files with `zone=skills`
        are mutable; other zones return 422 `unsupported_zone`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/agents/files/:fileId",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "enabled": enabled,
                },
                file_id_update_metadata_params.FileIDUpdateMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileIDUpdateMetadataResponse,
        )


class AsyncFileIDResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncFileIDResourceWithStreamingResponse(self)

    async def cancel_pending_upload(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileIDCancelPendingUploadResponse:
        """Soft-cancels an in-flight upload before confirm.

        Only acts on `pending` rows —
        refuses to touch `ready` to avoid wiping confirmed files. Idempotent:
        `{ cancelled: false }` if the row exists but is no longer pending.
        """
        return await self._delete(
            "/agents/files/:fileId/pending",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileIDCancelPendingUploadResponse,
        )

    async def confirm_upload(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileIDConfirmUploadResponse:
        """Confirm a file upload by server-side HEAD validation"""
        return await self._post(
            "/agents/files/:fileId/confirm",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileIDConfirmUploadResponse,
        )

    async def delete_file(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileIDDeleteFileResponse:
        """Hard-delete a file"""
        return await self._delete(
            "/agents/files/:fileId",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileIDDeleteFileResponse,
        )

    async def download_file(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Redirect to a presigned GET URL for a file (FE owner only)"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/agents/files/:fileId/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_metadata(
        self,
        *,
        display_name: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileIDUpdateMetadataResponse:
        """Partial update of `displayName` and/or `enabled`.

        Only files with `zone=skills`
        are mutable; other zones return 422 `unsupported_zone`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/agents/files/:fileId",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "enabled": enabled,
                },
                file_id_update_metadata_params.FileIDUpdateMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileIDUpdateMetadataResponse,
        )


class FileIDResourceWithRawResponse:
    def __init__(self, file_id: FileIDResource) -> None:
        self._file_id = file_id

        self.cancel_pending_upload = to_raw_response_wrapper(
            file_id.cancel_pending_upload,
        )
        self.confirm_upload = to_raw_response_wrapper(
            file_id.confirm_upload,
        )
        self.delete_file = to_raw_response_wrapper(
            file_id.delete_file,
        )
        self.download_file = to_raw_response_wrapper(
            file_id.download_file,
        )
        self.update_metadata = to_raw_response_wrapper(
            file_id.update_metadata,
        )


class AsyncFileIDResourceWithRawResponse:
    def __init__(self, file_id: AsyncFileIDResource) -> None:
        self._file_id = file_id

        self.cancel_pending_upload = async_to_raw_response_wrapper(
            file_id.cancel_pending_upload,
        )
        self.confirm_upload = async_to_raw_response_wrapper(
            file_id.confirm_upload,
        )
        self.delete_file = async_to_raw_response_wrapper(
            file_id.delete_file,
        )
        self.download_file = async_to_raw_response_wrapper(
            file_id.download_file,
        )
        self.update_metadata = async_to_raw_response_wrapper(
            file_id.update_metadata,
        )


class FileIDResourceWithStreamingResponse:
    def __init__(self, file_id: FileIDResource) -> None:
        self._file_id = file_id

        self.cancel_pending_upload = to_streamed_response_wrapper(
            file_id.cancel_pending_upload,
        )
        self.confirm_upload = to_streamed_response_wrapper(
            file_id.confirm_upload,
        )
        self.delete_file = to_streamed_response_wrapper(
            file_id.delete_file,
        )
        self.download_file = to_streamed_response_wrapper(
            file_id.download_file,
        )
        self.update_metadata = to_streamed_response_wrapper(
            file_id.update_metadata,
        )


class AsyncFileIDResourceWithStreamingResponse:
    def __init__(self, file_id: AsyncFileIDResource) -> None:
        self._file_id = file_id

        self.cancel_pending_upload = async_to_streamed_response_wrapper(
            file_id.cancel_pending_upload,
        )
        self.confirm_upload = async_to_streamed_response_wrapper(
            file_id.confirm_upload,
        )
        self.delete_file = async_to_streamed_response_wrapper(
            file_id.delete_file,
        )
        self.download_file = async_to_streamed_response_wrapper(
            file_id.download_file,
        )
        self.update_metadata = async_to_streamed_response_wrapper(
            file_id.update_metadata,
        )
