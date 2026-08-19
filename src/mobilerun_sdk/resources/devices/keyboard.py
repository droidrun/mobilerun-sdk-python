# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, strip_not_given, is_given, maybe_transform, async_maybe_transform

from ..._types import not_given, Omit, omit, NotGiven

from ..._base_client import make_request_options

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.devices import keyboard_key_params
from ...types.devices import keyboard_write_params

__all__ = ["KeyboardResource", "AsyncKeyboardResource"]

class KeyboardResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeyboardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return KeyboardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeyboardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return KeyboardResourceWithStreamingResponse(self)

    def clear(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Clears the contents of the currently focused text input field.

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
        return self._delete(
            path_template("/devices/{device_id}/keyboard", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def key(self,
    device_id: str,
    *,
    key: int,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Sends a single Android key event to the device, identified by its key code.

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
        return self._put(
            path_template("/devices/{device_id}/keyboard", device_id=device_id),
            body=maybe_transform({
                "key": key
            }, keyboard_key_params.KeyboardKeyParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def write(self,
    device_id: str,
    *,
    text: str,
    clear: bool | Omit = omit,
    error_rate: float | Omit = omit,
    stealth: bool | Omit = omit,
    wpm: int | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """Types the given text into the focused input field.

        Supports optionally clearing
        the field first and a stealth mode that emulates human typing speed and error
        rate on supported devices.

        Args:
          error_rate: Per-character mistake rate for humantouch typing. -1 uses server default.

          wpm: Words per minute for stealth typing. 0 uses portal default.

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
            path_template("/devices/{device_id}/keyboard", device_id=device_id),
            body=maybe_transform({
                "text": text,
                "clear": clear,
                "error_rate": error_rate,
                "stealth": stealth,
                "wpm": wpm,
            }, keyboard_write_params.KeyboardWriteParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class AsyncKeyboardResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeyboardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeyboardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeyboardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncKeyboardResourceWithStreamingResponse(self)

    async def clear(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Clears the contents of the currently focused text input field.

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
        return await self._delete(
            path_template("/devices/{device_id}/keyboard", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def key(self,
    device_id: str,
    *,
    key: int,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Sends a single Android key event to the device, identified by its key code.

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
        return await self._put(
            path_template("/devices/{device_id}/keyboard", device_id=device_id),
            body=await async_maybe_transform({
                "key": key
            }, keyboard_key_params.KeyboardKeyParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def write(self,
    device_id: str,
    *,
    text: str,
    clear: bool | Omit = omit,
    error_rate: float | Omit = omit,
    stealth: bool | Omit = omit,
    wpm: int | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """Types the given text into the focused input field.

        Supports optionally clearing
        the field first and a stealth mode that emulates human typing speed and error
        rate on supported devices.

        Args:
          error_rate: Per-character mistake rate for humantouch typing. -1 uses server default.

          wpm: Words per minute for stealth typing. 0 uses portal default.

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
            path_template("/devices/{device_id}/keyboard", device_id=device_id),
            body=await async_maybe_transform({
                "text": text,
                "clear": clear,
                "error_rate": error_rate,
                "stealth": stealth,
                "wpm": wpm,
            }, keyboard_write_params.KeyboardWriteParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class KeyboardResourceWithRawResponse:
    def __init__(self, keyboard: KeyboardResource) -> None:
        self._keyboard = keyboard

        self.clear = to_raw_response_wrapper(
            keyboard.clear,
        )
        self.key = to_raw_response_wrapper(
            keyboard.key,
        )
        self.write = to_raw_response_wrapper(
            keyboard.write,
        )

class AsyncKeyboardResourceWithRawResponse:
    def __init__(self, keyboard: AsyncKeyboardResource) -> None:
        self._keyboard = keyboard

        self.clear = async_to_raw_response_wrapper(
            keyboard.clear,
        )
        self.key = async_to_raw_response_wrapper(
            keyboard.key,
        )
        self.write = async_to_raw_response_wrapper(
            keyboard.write,
        )

class KeyboardResourceWithStreamingResponse:
    def __init__(self, keyboard: KeyboardResource) -> None:
        self._keyboard = keyboard

        self.clear = to_streamed_response_wrapper(
            keyboard.clear,
        )
        self.key = to_streamed_response_wrapper(
            keyboard.key,
        )
        self.write = to_streamed_response_wrapper(
            keyboard.write,
        )

class AsyncKeyboardResourceWithStreamingResponse:
    def __init__(self, keyboard: AsyncKeyboardResource) -> None:
        self._keyboard = keyboard

        self.clear = async_to_streamed_response_wrapper(
            keyboard.clear,
        )
        self.key = async_to_streamed_response_wrapper(
            keyboard.key,
        )
        self.write = async_to_streamed_response_wrapper(
            keyboard.write,
        )