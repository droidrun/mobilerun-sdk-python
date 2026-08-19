# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, maybe_transform, async_maybe_transform

from ...types.devices.recording_list_response import RecordingListResponse

from ..._base_client import make_request_options

from ..._types import Omit, omit, NotGiven, SequenceNotStr

from typing import Optional

from ...types.devices.recording_start_response import RecordingStartResponse

from ...types.devices.recording_status_response import RecordingStatusResponse

from ...types.devices.recording_stop_response import RecordingStopResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.devices import recording_list_params
from ...types.devices import recording_start_params

__all__ = ["RecordingsResource", "AsyncRecordingsResource"]

class RecordingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return RecordingsResourceWithStreamingResponse(self)

    def list(self,
    device_id: str,
    *,
    status: str | Omit = omit,
    type: str | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> Optional[RecordingListResponse]:
        """
        List device recordings

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
        return self._get(
            path_template("/devices/{device_id}/recordings", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "status": status,
                "type": type,
            }, recording_list_params.RecordingListParams)),
            cast_to=RecordingListResponse,
        )

    def delete(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Delete a device recording

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/devices/{device_id}/recordings/{recording_id}", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def start(self,
    device_id: str,
    *,
    name: str | Omit = omit,
    retention_days: int | Omit = omit,
    types: Optional[SequenceNotStr[str]] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> RecordingStartResponse:
        """
        Start a device recording

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
        return self._post(
            path_template("/devices/{device_id}/recordings", device_id=device_id),
            body=maybe_transform({
                "name": name,
                "retention_days": retention_days,
                "types": types,
            }, recording_start_params.RecordingStartParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RecordingStartResponse,
        )

    def status(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> RecordingStatusResponse:
        """
        Get a device recording

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        return self._get(
            path_template("/devices/{device_id}/recordings/{recording_id}", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RecordingStatusResponse,
        )

    def stop(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> RecordingStopResponse:
        """
        Stop a device recording

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        return self._post(
            path_template("/devices/{device_id}/recordings/{recording_id}", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RecordingStopResponse,
        )

    def trajectory(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Get a device recording trajectory

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/devices/{device_id}/recordings/{recording_id}/trajectory", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def video(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Get a device recording video

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/devices/{device_id}/recordings/{recording_id}/video", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class AsyncRecordingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncRecordingsResourceWithStreamingResponse(self)

    async def list(self,
    device_id: str,
    *,
    status: str | Omit = omit,
    type: str | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> Optional[RecordingListResponse]:
        """
        List device recordings

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
        return await self._get(
            path_template("/devices/{device_id}/recordings", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "status": status,
                "type": type,
            }, recording_list_params.RecordingListParams)),
            cast_to=RecordingListResponse,
        )

    async def delete(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Delete a device recording

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/devices/{device_id}/recordings/{recording_id}", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def start(self,
    device_id: str,
    *,
    name: str | Omit = omit,
    retention_days: int | Omit = omit,
    types: Optional[SequenceNotStr[str]] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> RecordingStartResponse:
        """
        Start a device recording

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
        return await self._post(
            path_template("/devices/{device_id}/recordings", device_id=device_id),
            body=await async_maybe_transform({
                "name": name,
                "retention_days": retention_days,
                "types": types,
            }, recording_start_params.RecordingStartParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RecordingStartResponse,
        )

    async def status(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> RecordingStatusResponse:
        """
        Get a device recording

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        return await self._get(
            path_template("/devices/{device_id}/recordings/{recording_id}", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RecordingStatusResponse,
        )

    async def stop(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> RecordingStopResponse:
        """
        Stop a device recording

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        return await self._post(
            path_template("/devices/{device_id}/recordings/{recording_id}", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RecordingStopResponse,
        )

    async def trajectory(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Get a device recording trajectory

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/devices/{device_id}/recordings/{recording_id}/trajectory", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def video(self,
    recording_id: str,
    *,
    device_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Get a device recording video

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
        if not recording_id:
          raise ValueError(
            f'Expected a non-empty value for `recording_id` but received {recording_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/devices/{device_id}/recordings/{recording_id}/video", device_id=device_id, recording_id=recording_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class RecordingsResourceWithRawResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

        self.list = to_raw_response_wrapper(
            recordings.list,
        )
        self.delete = to_raw_response_wrapper(
            recordings.delete,
        )
        self.start = to_raw_response_wrapper(
            recordings.start,
        )
        self.status = to_raw_response_wrapper(
            recordings.status,
        )
        self.stop = to_raw_response_wrapper(
            recordings.stop,
        )
        self.trajectory = to_raw_response_wrapper(
            recordings.trajectory,
        )
        self.video = to_raw_response_wrapper(
            recordings.video,
        )

class AsyncRecordingsResourceWithRawResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

        self.list = async_to_raw_response_wrapper(
            recordings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            recordings.delete,
        )
        self.start = async_to_raw_response_wrapper(
            recordings.start,
        )
        self.status = async_to_raw_response_wrapper(
            recordings.status,
        )
        self.stop = async_to_raw_response_wrapper(
            recordings.stop,
        )
        self.trajectory = async_to_raw_response_wrapper(
            recordings.trajectory,
        )
        self.video = async_to_raw_response_wrapper(
            recordings.video,
        )

class RecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

        self.list = to_streamed_response_wrapper(
            recordings.list,
        )
        self.delete = to_streamed_response_wrapper(
            recordings.delete,
        )
        self.start = to_streamed_response_wrapper(
            recordings.start,
        )
        self.status = to_streamed_response_wrapper(
            recordings.status,
        )
        self.stop = to_streamed_response_wrapper(
            recordings.stop,
        )
        self.trajectory = to_streamed_response_wrapper(
            recordings.trajectory,
        )
        self.video = to_streamed_response_wrapper(
            recordings.video,
        )

class AsyncRecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

        self.list = async_to_streamed_response_wrapper(
            recordings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            recordings.delete,
        )
        self.start = async_to_streamed_response_wrapper(
            recordings.start,
        )
        self.status = async_to_streamed_response_wrapper(
            recordings.status,
        )
        self.stop = async_to_streamed_response_wrapper(
            recordings.stop,
        )
        self.trajectory = async_to_streamed_response_wrapper(
            recordings.trajectory,
        )
        self.video = async_to_streamed_response_wrapper(
            recordings.video,
        )