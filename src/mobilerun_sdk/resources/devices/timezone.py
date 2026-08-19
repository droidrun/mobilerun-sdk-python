# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, strip_not_given, is_given, maybe_transform, async_maybe_transform

from ...types.devices.timezone_get_response import TimezoneGetResponse

from ..._types import not_given, Omit, omit, NotGiven

from ..._base_client import make_request_options

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.devices import timezone_set_params

__all__ = ["TimezoneResource", "AsyncTimezoneResource"]

class TimezoneResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimezoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TimezoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimezoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return TimezoneResourceWithStreamingResponse(self)

    def get(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TimezoneGetResponse:
        """Returns the device's current timezone identifier.

        Devices that do not support
        timezone control return an unsupported-feature error.

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
            path_template("/devices/{device_id}/timezone", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TimezoneGetResponse,
        )

    def set(self,
    device_id: str,
    *,
    timezone: str,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """Sets the device timezone to the identifier in the request body.

        Devices that do
        not support timezone control return an unsupported-feature error.

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
            path_template("/devices/{device_id}/timezone", device_id=device_id),
            body=maybe_transform({
                "timezone": timezone
            }, timezone_set_params.TimezoneSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class AsyncTimezoneResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimezoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimezoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimezoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncTimezoneResourceWithStreamingResponse(self)

    async def get(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> TimezoneGetResponse:
        """Returns the device's current timezone identifier.

        Devices that do not support
        timezone control return an unsupported-feature error.

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
            path_template("/devices/{device_id}/timezone", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TimezoneGetResponse,
        )

    async def set(self,
    device_id: str,
    *,
    timezone: str,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """Sets the device timezone to the identifier in the request body.

        Devices that do
        not support timezone control return an unsupported-feature error.

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
            path_template("/devices/{device_id}/timezone", device_id=device_id),
            body=await async_maybe_transform({
                "timezone": timezone
            }, timezone_set_params.TimezoneSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

class TimezoneResourceWithRawResponse:
    def __init__(self, timezone: TimezoneResource) -> None:
        self._timezone = timezone

        self.get = to_raw_response_wrapper(
            timezone.get,
        )
        self.set = to_raw_response_wrapper(
            timezone.set,
        )

class AsyncTimezoneResourceWithRawResponse:
    def __init__(self, timezone: AsyncTimezoneResource) -> None:
        self._timezone = timezone

        self.get = async_to_raw_response_wrapper(
            timezone.get,
        )
        self.set = async_to_raw_response_wrapper(
            timezone.set,
        )

class TimezoneResourceWithStreamingResponse:
    def __init__(self, timezone: TimezoneResource) -> None:
        self._timezone = timezone

        self.get = to_streamed_response_wrapper(
            timezone.get,
        )
        self.set = to_streamed_response_wrapper(
            timezone.set,
        )

class AsyncTimezoneResourceWithStreamingResponse:
    def __init__(self, timezone: AsyncTimezoneResource) -> None:
        self._timezone = timezone

        self.get = async_to_streamed_response_wrapper(
            timezone.get,
        )
        self.set = async_to_streamed_response_wrapper(
            timezone.set,
        )