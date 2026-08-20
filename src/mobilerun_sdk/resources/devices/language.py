# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.devices import language_set_params
from ...types.devices.language_get_response import LanguageGetResponse

__all__ = ["LanguageResource", "AsyncLanguageResource"]


class LanguageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LanguageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LanguageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LanguageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return LanguageResourceWithStreamingResponse(self)

    def get(
        self,
        device_id: str,
        *,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LanguageGetResponse:
        """
        Returns the device's current language/locale as a BCP-47 locale string.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/devices/{device_id}/language", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageGetResponse,
        )

    def set(
        self,
        device_id: str,
        *,
        locale: str,
        restart: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sets the device language/locale to the BCP-47 locale in the request body.

        An
        optional restart flag applies the change immediately by restarting the zygote
        instead of waiting for the next reboot.

        Args:
          locale: BCP-47 locale: a 2–3 letter language tag, optionally followed by a 4-letter
              script and/or a 2-letter region (e.g. en-US, de-DE, ja-JP, zh-Hans-CN).

          restart: Restart zygote so the locale change takes full effect immediately. Without it,
              the locale is written but won't fully apply until the next reboot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/devices/{device_id}/language", device_id=device_id),
            body=maybe_transform(
                {
                    "locale": locale,
                    "restart": restart,
                },
                language_set_params.LanguageSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLanguageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLanguageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLanguageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLanguageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncLanguageResourceWithStreamingResponse(self)

    async def get(
        self,
        device_id: str,
        *,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LanguageGetResponse:
        """
        Returns the device's current language/locale as a BCP-47 locale string.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/devices/{device_id}/language", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageGetResponse,
        )

    async def set(
        self,
        device_id: str,
        *,
        locale: str,
        restart: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sets the device language/locale to the BCP-47 locale in the request body.

        An
        optional restart flag applies the change immediately by restarting the zygote
        instead of waiting for the next reboot.

        Args:
          locale: BCP-47 locale: a 2–3 letter language tag, optionally followed by a 4-letter
              script and/or a 2-letter region (e.g. en-US, de-DE, ja-JP, zh-Hans-CN).

          restart: Restart zygote so the locale change takes full effect immediately. Without it,
              the locale is written but won't fully apply until the next reboot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/devices/{device_id}/language", device_id=device_id),
            body=await async_maybe_transform(
                {
                    "locale": locale,
                    "restart": restart,
                },
                language_set_params.LanguageSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LanguageResourceWithRawResponse:
    def __init__(self, language: LanguageResource) -> None:
        self._language = language

        self.get = to_raw_response_wrapper(
            language.get,
        )
        self.set = to_raw_response_wrapper(
            language.set,
        )


class AsyncLanguageResourceWithRawResponse:
    def __init__(self, language: AsyncLanguageResource) -> None:
        self._language = language

        self.get = async_to_raw_response_wrapper(
            language.get,
        )
        self.set = async_to_raw_response_wrapper(
            language.set,
        )


class LanguageResourceWithStreamingResponse:
    def __init__(self, language: LanguageResource) -> None:
        self._language = language

        self.get = to_streamed_response_wrapper(
            language.get,
        )
        self.set = to_streamed_response_wrapper(
            language.set,
        )


class AsyncLanguageResourceWithStreamingResponse:
    def __init__(self, language: AsyncLanguageResource) -> None:
        self._language = language

        self.get = async_to_streamed_response_wrapper(
            language.get,
        )
        self.set = async_to_streamed_response_wrapper(
            language.set,
        )
