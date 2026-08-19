# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, maybe_transform, is_given, async_maybe_transform

from ...types.devices.media_session_create_response import MediaSessionCreateResponse

from ..._base_client import make_request_options

from ..._types import NotGiven

from ...types.devices.media_session_activate_response import MediaSessionActivateResponse

from ...types.devices.media_session_retrieve_current_response import MediaSessionRetrieveCurrentResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.devices import media_session_create_params

__all__ = ["MediaSessionsResource", "AsyncMediaSessionsResource"]

class MediaSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediaSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MediaSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return MediaSessionsResourceWithStreamingResponse(self)

    def create(self,
    device_id: str,
    *,
    camera: bool,
    microphone: bool,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MediaSessionCreateResponse:
        """
        Allocates an exclusive relay path and returns one-time publish and control
        credentials. The relay publisher must be established before activation.

        Args:
          camera: Publish combined browser audio and H264 video into the device's virtual
              microphone and camera. Requires microphone=true.

          microphone: Publish browser audio into the device's virtual microphone.

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
            path_template("/devices/{device_id}/media-sessions", device_id=device_id),
            body=maybe_transform({
                "camera": camera,
                "microphone": microphone,
            }, media_session_create_params.MediaSessionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MediaSessionCreateResponse,
        )

    def delete(self,
    session_id: str,
    *,
    device_id: str,
    x_media_control_token: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Immediately revokes relay authorization, detaches virtual media inputs, and
        kicks the relay publisher.

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
        if not session_id:
          raise ValueError(
            f'Expected a non-empty value for `session_id` but received {session_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"X-Media-Control-Token": x_media_control_token})
        return self._delete(
            path_template("/devices/{device_id}/media-sessions/{session_id}", device_id=device_id, session_id=session_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def activate(self,
    session_id: str,
    *,
    device_id: str,
    x_media_control_token: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MediaSessionActivateResponse:
        """
        Validates relay codecs and attaches one private RTSP source to either the
        virtual microphone or the combined microphone-and-camera pipeline.

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
        if not session_id:
          raise ValueError(
            f'Expected a non-empty value for `session_id` but received {session_id!r}'
          )
        extra_headers = {"X-Media-Control-Token": x_media_control_token, **(extra_headers or {})}
        return self._post(
            path_template("/devices/{device_id}/media-sessions/{session_id}/activate", device_id=device_id, session_id=session_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MediaSessionActivateResponse,
        )

    def retrieve_current(self,
    device_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MediaSessionRetrieveCurrentResponse:
        """Returns status only.

        Publish URLs and credentials are never replayed after
        creation.

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
            path_template("/devices/{device_id}/media-sessions/current", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MediaSessionRetrieveCurrentResponse,
        )

class AsyncMediaSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediaSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncMediaSessionsResourceWithStreamingResponse(self)

    async def create(self,
    device_id: str,
    *,
    camera: bool,
    microphone: bool,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MediaSessionCreateResponse:
        """
        Allocates an exclusive relay path and returns one-time publish and control
        credentials. The relay publisher must be established before activation.

        Args:
          camera: Publish combined browser audio and H264 video into the device's virtual
              microphone and camera. Requires microphone=true.

          microphone: Publish browser audio into the device's virtual microphone.

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
            path_template("/devices/{device_id}/media-sessions", device_id=device_id),
            body=await async_maybe_transform({
                "camera": camera,
                "microphone": microphone,
            }, media_session_create_params.MediaSessionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MediaSessionCreateResponse,
        )

    async def delete(self,
    session_id: str,
    *,
    device_id: str,
    x_media_control_token: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Immediately revokes relay authorization, detaches virtual media inputs, and
        kicks the relay publisher.

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
        if not session_id:
          raise ValueError(
            f'Expected a non-empty value for `session_id` but received {session_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"X-Media-Control-Token": x_media_control_token})
        return await self._delete(
            path_template("/devices/{device_id}/media-sessions/{session_id}", device_id=device_id, session_id=session_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def activate(self,
    session_id: str,
    *,
    device_id: str,
    x_media_control_token: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MediaSessionActivateResponse:
        """
        Validates relay codecs and attaches one private RTSP source to either the
        virtual microphone or the combined microphone-and-camera pipeline.

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
        if not session_id:
          raise ValueError(
            f'Expected a non-empty value for `session_id` but received {session_id!r}'
          )
        extra_headers = {"X-Media-Control-Token": x_media_control_token, **(extra_headers or {})}
        return await self._post(
            path_template("/devices/{device_id}/media-sessions/{session_id}/activate", device_id=device_id, session_id=session_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MediaSessionActivateResponse,
        )

    async def retrieve_current(self,
    device_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MediaSessionRetrieveCurrentResponse:
        """Returns status only.

        Publish URLs and credentials are never replayed after
        creation.

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
            path_template("/devices/{device_id}/media-sessions/current", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MediaSessionRetrieveCurrentResponse,
        )

class MediaSessionsResourceWithRawResponse:
    def __init__(self, media_sessions: MediaSessionsResource) -> None:
        self._media_sessions = media_sessions

        self.create = to_raw_response_wrapper(
            media_sessions.create,
        )
        self.delete = to_raw_response_wrapper(
            media_sessions.delete,
        )
        self.activate = to_raw_response_wrapper(
            media_sessions.activate,
        )
        self.retrieve_current = to_raw_response_wrapper(
            media_sessions.retrieve_current,
        )

class AsyncMediaSessionsResourceWithRawResponse:
    def __init__(self, media_sessions: AsyncMediaSessionsResource) -> None:
        self._media_sessions = media_sessions

        self.create = async_to_raw_response_wrapper(
            media_sessions.create,
        )
        self.delete = async_to_raw_response_wrapper(
            media_sessions.delete,
        )
        self.activate = async_to_raw_response_wrapper(
            media_sessions.activate,
        )
        self.retrieve_current = async_to_raw_response_wrapper(
            media_sessions.retrieve_current,
        )

class MediaSessionsResourceWithStreamingResponse:
    def __init__(self, media_sessions: MediaSessionsResource) -> None:
        self._media_sessions = media_sessions

        self.create = to_streamed_response_wrapper(
            media_sessions.create,
        )
        self.delete = to_streamed_response_wrapper(
            media_sessions.delete,
        )
        self.activate = to_streamed_response_wrapper(
            media_sessions.activate,
        )
        self.retrieve_current = to_streamed_response_wrapper(
            media_sessions.retrieve_current,
        )

class AsyncMediaSessionsResourceWithStreamingResponse:
    def __init__(self, media_sessions: AsyncMediaSessionsResource) -> None:
        self._media_sessions = media_sessions

        self.create = async_to_streamed_response_wrapper(
            media_sessions.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            media_sessions.delete,
        )
        self.activate = async_to_streamed_response_wrapper(
            media_sessions.activate,
        )
        self.retrieve_current = async_to_streamed_response_wrapper(
            media_sessions.retrieve_current,
        )