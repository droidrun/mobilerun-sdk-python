# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, strip_not_given, is_given, maybe_transform, async_maybe_transform

from ..._types import not_given, Omit, omit, NotGiven

from ..._base_client import make_request_options

from ...types.devices.state_screenshot_response import StateScreenshotResponse

from ...types.devices.state_time_response import StateTimeResponse

from ...types.devices.state_ui_response import StateUiResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.devices import state_screenshot_params
from ...types.devices import state_ui_params

__all__ = ["StateResource", "AsyncStateResource"]

class StateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return StateResourceWithStreamingResponse(self)

    def screenshot(self,
    device_id: str,
    *,
    hide_overlay: bool | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> str:
        """Captures the device screen and returns it as a PNG image.

        An optional
        hideOverlay query parameter excludes the accessibility overlay from the capture.

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
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._get(
            path_template("/devices/{device_id}/screenshot", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "hide_overlay": hide_overlay
            }, state_screenshot_params.StateScreenshotParams)),
            cast_to=str,
        )

    def time(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> str:
        """
        Returns the device's current wall-clock time as an RFC 3339 timestamp.

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
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._get(
            path_template("/devices/{device_id}/time", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )

    def ui(self,
    device_id: str,
    *,
    filter: bool | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> StateUiResponse:
        """
        Returns the current accessibility UI state of the device as a structured tree of
        on-screen elements. An optional filter query reduces the result to interactive
        elements.

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
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._get(
            path_template("/devices/{device_id}/ui-state", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "filter": filter
            }, state_ui_params.StateUiParams)),
            cast_to=StateUiResponse,
        )

class AsyncStateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncStateResourceWithStreamingResponse(self)

    async def screenshot(self,
    device_id: str,
    *,
    hide_overlay: bool | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> str:
        """Captures the device screen and returns it as a PNG image.

        An optional
        hideOverlay query parameter excludes the accessibility overlay from the capture.

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
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._get(
            path_template("/devices/{device_id}/screenshot", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "hide_overlay": hide_overlay
            }, state_screenshot_params.StateScreenshotParams)),
            cast_to=str,
        )

    async def time(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> str:
        """
        Returns the device's current wall-clock time as an RFC 3339 timestamp.

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
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._get(
            path_template("/devices/{device_id}/time", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )

    async def ui(self,
    device_id: str,
    *,
    filter: bool | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> StateUiResponse:
        """
        Returns the current accessibility UI state of the device as a structured tree of
        on-screen elements. An optional filter query reduces the result to interactive
        elements.

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
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._get(
            path_template("/devices/{device_id}/ui-state", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "filter": filter
            }, state_ui_params.StateUiParams)),
            cast_to=StateUiResponse,
        )

class StateResourceWithRawResponse:
    def __init__(self, state: StateResource) -> None:
        self._state = state

        self.screenshot = to_raw_response_wrapper(
            state.screenshot,
        )
        self.time = to_raw_response_wrapper(
            state.time,
        )
        self.ui = to_raw_response_wrapper(
            state.ui,
        )

class AsyncStateResourceWithRawResponse:
    def __init__(self, state: AsyncStateResource) -> None:
        self._state = state

        self.screenshot = async_to_raw_response_wrapper(
            state.screenshot,
        )
        self.time = async_to_raw_response_wrapper(
            state.time,
        )
        self.ui = async_to_raw_response_wrapper(
            state.ui,
        )

class StateResourceWithStreamingResponse:
    def __init__(self, state: StateResource) -> None:
        self._state = state

        self.screenshot = to_streamed_response_wrapper(
            state.screenshot,
        )
        self.time = to_streamed_response_wrapper(
            state.time,
        )
        self.ui = to_streamed_response_wrapper(
            state.ui,
        )

class AsyncStateResourceWithStreamingResponse:
    def __init__(self, state: AsyncStateResource) -> None:
        self._state = state

        self.screenshot = async_to_streamed_response_wrapper(
            state.screenshot,
        )
        self.time = async_to_streamed_response_wrapper(
            state.time,
        )
        self.ui = async_to_streamed_response_wrapper(
            state.ui,
        )