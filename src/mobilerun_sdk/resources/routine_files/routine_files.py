# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import routine_file_list_params, routine_file_delete_all_params
from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.routine_file_list_response import RoutineFileListResponse
from ...types.routine_file_delete_all_response import RoutineFileDeleteAllResponse

__all__ = ["RoutineFilesResource", "AsyncRoutineFilesResource"]


class RoutineFilesResource(SyncAPIResource):
    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def with_raw_response(self) -> RoutineFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RoutineFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutineFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return RoutineFilesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        execution_id: str | Omit = omit,
        flow_id: str | Omit = omit,
        folder: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutineFileListResponse:
        """
        Lists the files saved in Mobilerun storage for routines whose delivery
        destination is Mobilerun with a folder: the run recording, screenshots and
        files.upload outputs. Newest first; filter by `folder`, `flowId` or
        `executionId`. Files stay until you delete them or delete their routine.

        Args:
          folder: Exact folder (canonicalized: "//" collapsed, trailing "/" stripped).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/routine-files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "execution_id": execution_id,
                        "flow_id": flow_id,
                        "folder": folder,
                        "page": page,
                        "page_size": page_size,
                    },
                    routine_file_list_params.RoutineFileListParams,
                ),
            ),
            cast_to=RoutineFileListResponse,
        )

    def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes one saved file permanently and frees its storage (the file disappears at
        once; the stored object is removed right after). Idempotent: an already deleted
        file returns 204 too.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/routine-files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def delete_all(
        self,
        *,
        execution_id: str | Omit = omit,
        folder: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RoutineFileDeleteAllResponse:
        """
        Deletes every saved file of exactly one folder (`folder`) or one run
        (`executionId`) permanently. Pass exactly one of the two. Returns how many files
        were deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._delete(
            "/routine-files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "execution_id": execution_id,
                        "folder": folder,
                    },
                    routine_file_delete_all_params.RoutineFileDeleteAllParams,
                ),
            ),
            cast_to=RoutineFileDeleteAllResponse,
        )

    def download(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Redirects (302) to a time-limited (at most 5 minutes) download URL for the file.
        404 when the file does not exist or belongs to someone else.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/routine-files/{file_id}/download", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRoutineFilesResource(AsyncAPIResource):
    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoutineFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutineFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutineFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncRoutineFilesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        execution_id: str | Omit = omit,
        flow_id: str | Omit = omit,
        folder: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutineFileListResponse:
        """
        Lists the files saved in Mobilerun storage for routines whose delivery
        destination is Mobilerun with a folder: the run recording, screenshots and
        files.upload outputs. Newest first; filter by `folder`, `flowId` or
        `executionId`. Files stay until you delete them or delete their routine.

        Args:
          folder: Exact folder (canonicalized: "//" collapsed, trailing "/" stripped).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/routine-files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "execution_id": execution_id,
                        "flow_id": flow_id,
                        "folder": folder,
                        "page": page,
                        "page_size": page_size,
                    },
                    routine_file_list_params.RoutineFileListParams,
                ),
            ),
            cast_to=RoutineFileListResponse,
        )

    async def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Deletes one saved file permanently and frees its storage (the file disappears at
        once; the stored object is removed right after). Idempotent: an already deleted
        file returns 204 too.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/routine-files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def delete_all(
        self,
        *,
        execution_id: str | Omit = omit,
        folder: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RoutineFileDeleteAllResponse:
        """
        Deletes every saved file of exactly one folder (`folder`) or one run
        (`executionId`) permanently. Pass exactly one of the two. Returns how many files
        were deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._delete(
            "/routine-files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=await async_maybe_transform(
                    {
                        "execution_id": execution_id,
                        "folder": folder,
                    },
                    routine_file_delete_all_params.RoutineFileDeleteAllParams,
                ),
            ),
            cast_to=RoutineFileDeleteAllResponse,
        )

    async def download(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Redirects (302) to a time-limited (at most 5 minutes) download URL for the file.
        404 when the file does not exist or belongs to someone else.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/routine-files/{file_id}/download", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RoutineFilesResourceWithRawResponse:
    def __init__(self, routine_files: RoutineFilesResource) -> None:
        self._routine_files = routine_files

        self.list = to_raw_response_wrapper(
            routine_files.list,
        )
        self.delete = to_raw_response_wrapper(
            routine_files.delete,
        )
        self.delete_all = to_raw_response_wrapper(
            routine_files.delete_all,
        )
        self.download = to_raw_response_wrapper(
            routine_files.download,
        )

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._routine_files.folders)


class AsyncRoutineFilesResourceWithRawResponse:
    def __init__(self, routine_files: AsyncRoutineFilesResource) -> None:
        self._routine_files = routine_files

        self.list = async_to_raw_response_wrapper(
            routine_files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            routine_files.delete,
        )
        self.delete_all = async_to_raw_response_wrapper(
            routine_files.delete_all,
        )
        self.download = async_to_raw_response_wrapper(
            routine_files.download,
        )

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._routine_files.folders)


class RoutineFilesResourceWithStreamingResponse:
    def __init__(self, routine_files: RoutineFilesResource) -> None:
        self._routine_files = routine_files

        self.list = to_streamed_response_wrapper(
            routine_files.list,
        )
        self.delete = to_streamed_response_wrapper(
            routine_files.delete,
        )
        self.delete_all = to_streamed_response_wrapper(
            routine_files.delete_all,
        )
        self.download = to_streamed_response_wrapper(
            routine_files.download,
        )

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._routine_files.folders)


class AsyncRoutineFilesResourceWithStreamingResponse:
    def __init__(self, routine_files: AsyncRoutineFilesResource) -> None:
        self._routine_files = routine_files

        self.list = async_to_streamed_response_wrapper(
            routine_files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            routine_files.delete,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            routine_files.delete_all,
        )
        self.download = async_to_streamed_response_wrapper(
            routine_files.download,
        )

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._routine_files.folders)
