# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, strip_not_given, is_given, maybe_transform, async_maybe_transform

from ..._types import not_given, Omit, omit, NotGiven

from ..._base_client import make_request_options

from ...types.devices.action_overlay_visible_response import ActionOverlayVisibleResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.devices import action_global_params
from ...types.devices import action_set_overlay_visible_params
from ...types.devices import action_swipe_params
from ...types.devices import action_tap_params

__all__ = ["ActionsResource", "AsyncActionsResource"]

class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def global_(self,
    device_id: str,
    *,
    action: int,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Performs a global system action on the device, such as navigating back or going
        to the home screen, identified by an action code.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._post(
            path_template("/devices/{device_id}/global", device_id=device_id),
            body=maybe_transform({
                "action": action
            }, action_global_params.ActionGlobalParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def overlay_visible(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionOverlayVisibleResponse:
        """
        Returns whether the accessibility overlay is currently visible on the device.

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
            path_template("/devices/{device_id}/overlay", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionOverlayVisibleResponse,
        )

    def set_overlay_visible(self,
    device_id: str,
    *,
    visible: bool,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Shows or hides the accessibility overlay on the device based on the visibility
        flag in the request body.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._post(
            path_template("/devices/{device_id}/overlay", device_id=device_id),
            body=maybe_transform({
                "visible": visible
            }, action_set_overlay_visible_params.ActionSetOverlayVisibleParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def swipe(self,
    device_id: str,
    *,
    duration: int,
    end_x: int,
    end_y: int,
    start_x: int,
    start_y: int,
    stealth: bool | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Swipes from a start coordinate to an end coordinate over the given duration in
        milliseconds. An optional stealth flag applies human-like jitter and curved
        paths on devices that support it.

        Args:
          duration: Swipe duration in milliseconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._post(
            path_template("/devices/{device_id}/swipe", device_id=device_id),
            body=maybe_transform({
                "duration": duration,
                "end_x": end_x,
                "end_y": end_y,
                "start_x": start_x,
                "start_y": start_y,
                "stealth": stealth,
            }, action_swipe_params.ActionSwipeParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def tap(self,
    device_id: str,
    *,
    x: int,
    y: int,
    stealth: bool | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """Taps the device screen at the given x/y coordinates.

        An optional stealth flag
        routes the tap through human-like input on devices that support it.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return self._post(
            path_template("/devices/{device_id}/tap", device_id=device_id),
            body=maybe_transform({
                "x": x,
                "y": y,
                "stealth": stealth,
            }, action_tap_params.ActionTapParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def global_(self,
    device_id: str,
    *,
    action: int,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Performs a global system action on the device, such as navigating back or going
        to the home screen, identified by an action code.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._post(
            path_template("/devices/{device_id}/global", device_id=device_id),
            body=await async_maybe_transform({
                "action": action
            }, action_global_params.ActionGlobalParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def overlay_visible(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionOverlayVisibleResponse:
        """
        Returns whether the accessibility overlay is currently visible on the device.

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
            path_template("/devices/{device_id}/overlay", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionOverlayVisibleResponse,
        )

    async def set_overlay_visible(self,
    device_id: str,
    *,
    visible: bool,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Shows or hides the accessibility overlay on the device based on the visibility
        flag in the request body.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._post(
            path_template("/devices/{device_id}/overlay", device_id=device_id),
            body=await async_maybe_transform({
                "visible": visible
            }, action_set_overlay_visible_params.ActionSetOverlayVisibleParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def swipe(self,
    device_id: str,
    *,
    duration: int,
    end_x: int,
    end_y: int,
    start_x: int,
    start_y: int,
    stealth: bool | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Swipes from a start coordinate to an end coordinate over the given duration in
        milliseconds. An optional stealth flag applies human-like jitter and curved
        paths on devices that support it.

        Args:
          duration: Swipe duration in milliseconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
          raise ValueError(
            f'Expected a non-empty value for `device_id` but received {device_id!r}'
          )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._post(
            path_template("/devices/{device_id}/swipe", device_id=device_id),
            body=await async_maybe_transform({
                "duration": duration,
                "end_x": end_x,
                "end_y": end_y,
                "start_x": start_x,
                "start_y": start_y,
                "stealth": stealth,
            }, action_swipe_params.ActionSwipeParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def tap(self,
    device_id: str,
    *,
    x: int,
    y: int,
    stealth: bool | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """Taps the device screen at the given x/y coordinates.

        An optional stealth flag
        routes the tap through human-like input on devices that support it.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = { **strip_not_given({
            "X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given
        }), **(extra_headers or {}) }
        return await self._post(
            path_template("/devices/{device_id}/tap", device_id=device_id),
            body=await async_maybe_transform({
                "x": x,
                "y": y,
                "stealth": stealth,
            }, action_tap_params.ActionTapParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.global_ = to_raw_response_wrapper(
            actions.global_,
        )
        self.overlay_visible = to_raw_response_wrapper(
            actions.overlay_visible,
        )
        self.set_overlay_visible = to_raw_response_wrapper(
            actions.set_overlay_visible,
        )
        self.swipe = to_raw_response_wrapper(
            actions.swipe,
        )
        self.tap = to_raw_response_wrapper(
            actions.tap,
        )

class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.global_ = async_to_raw_response_wrapper(
            actions.global_,
        )
        self.overlay_visible = async_to_raw_response_wrapper(
            actions.overlay_visible,
        )
        self.set_overlay_visible = async_to_raw_response_wrapper(
            actions.set_overlay_visible,
        )
        self.swipe = async_to_raw_response_wrapper(
            actions.swipe,
        )
        self.tap = async_to_raw_response_wrapper(
            actions.tap,
        )

class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.global_ = to_streamed_response_wrapper(
            actions.global_,
        )
        self.overlay_visible = to_streamed_response_wrapper(
            actions.overlay_visible,
        )
        self.set_overlay_visible = to_streamed_response_wrapper(
            actions.set_overlay_visible,
        )
        self.swipe = to_streamed_response_wrapper(
            actions.swipe,
        )
        self.tap = to_streamed_response_wrapper(
            actions.tap,
        )

class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.global_ = async_to_streamed_response_wrapper(
            actions.global_,
        )
        self.overlay_visible = async_to_streamed_response_wrapper(
            actions.overlay_visible,
        )
        self.set_overlay_visible = async_to_streamed_response_wrapper(
            actions.set_overlay_visible,
        )
        self.swipe = async_to_streamed_response_wrapper(
            actions.swipe,
        )
        self.tap = async_to_streamed_response_wrapper(
            actions.tap,
        )