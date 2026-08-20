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
from ...types.devices import deep_link_execute_deep_link_params

__all__ = ["DeepLinkResource", "AsyncDeepLinkResource"]


class DeepLinkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeepLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DeepLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeepLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return DeepLinkResourceWithStreamingResponse(self)

    def execute_deep_link(
        self,
        device_id: str,
        *,
        deep_link: str,
        action: str | Omit = omit,
        bundle_id: str | Omit = omit,
        package_name: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Opens a deep link on the device.

        On Android the link is dispatched as an intent
        — packageName optionally pins it to a specific app and action overrides the
        default android.intent.action.VIEW. On iOS the URL is opened directly and the
        optional fields must be omitted. Protected packages are rejected.

        Args:
          deep_link: Deep link to open (e.g. myapp://path or https://example.com/path)

          action: Android only: intent action to dispatch. Defaults to android.intent.action.VIEW.

          bundle_id: Reserved for targeting a specific iOS app; currently rejected as unsupported.

          package_name: Android only: package to receive the intent (e.g. com.example.app). Omit to let
              the system pick the handler.

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
            path_template("/devices/{device_id}/apps/open-deep-link", device_id=device_id),
            body=maybe_transform(
                {
                    "deep_link": deep_link,
                    "action": action,
                    "bundle_id": bundle_id,
                    "package_name": package_name,
                },
                deep_link_execute_deep_link_params.DeepLinkExecuteDeepLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDeepLinkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeepLinkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeepLinkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeepLinkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncDeepLinkResourceWithStreamingResponse(self)

    async def execute_deep_link(
        self,
        device_id: str,
        *,
        deep_link: str,
        action: str | Omit = omit,
        bundle_id: str | Omit = omit,
        package_name: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Opens a deep link on the device.

        On Android the link is dispatched as an intent
        — packageName optionally pins it to a specific app and action overrides the
        default android.intent.action.VIEW. On iOS the URL is opened directly and the
        optional fields must be omitted. Protected packages are rejected.

        Args:
          deep_link: Deep link to open (e.g. myapp://path or https://example.com/path)

          action: Android only: intent action to dispatch. Defaults to android.intent.action.VIEW.

          bundle_id: Reserved for targeting a specific iOS app; currently rejected as unsupported.

          package_name: Android only: package to receive the intent (e.g. com.example.app). Omit to let
              the system pick the handler.

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
            path_template("/devices/{device_id}/apps/open-deep-link", device_id=device_id),
            body=await async_maybe_transform(
                {
                    "deep_link": deep_link,
                    "action": action,
                    "bundle_id": bundle_id,
                    "package_name": package_name,
                },
                deep_link_execute_deep_link_params.DeepLinkExecuteDeepLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DeepLinkResourceWithRawResponse:
    def __init__(self, deep_link: DeepLinkResource) -> None:
        self._deep_link = deep_link

        self.execute_deep_link = to_raw_response_wrapper(
            deep_link.execute_deep_link,
        )


class AsyncDeepLinkResourceWithRawResponse:
    def __init__(self, deep_link: AsyncDeepLinkResource) -> None:
        self._deep_link = deep_link

        self.execute_deep_link = async_to_raw_response_wrapper(
            deep_link.execute_deep_link,
        )


class DeepLinkResourceWithStreamingResponse:
    def __init__(self, deep_link: DeepLinkResource) -> None:
        self._deep_link = deep_link

        self.execute_deep_link = to_streamed_response_wrapper(
            deep_link.execute_deep_link,
        )


class AsyncDeepLinkResourceWithStreamingResponse:
    def __init__(self, deep_link: AsyncDeepLinkResource) -> None:
        self._deep_link = deep_link

        self.execute_deep_link = async_to_streamed_response_wrapper(
            deep_link.execute_deep_link,
        )
