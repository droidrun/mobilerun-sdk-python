# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.devices import browser_execute_script_params
from ...types.devices.browser_execute_script_response import BrowserExecuteScriptResponse

__all__ = ["BrowserResource", "AsyncBrowserResource"]


class BrowserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return BrowserResourceWithStreamingResponse(self)

    def execute_script(
        self,
        device_id: str,
        *,
        script: str,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserExecuteScriptResponse:
        """
        Evaluates a JavaScript expression in the device's foreground Chrome tab via the
        Chrome DevTools Protocol and returns its JSON-serialized result. Devices without
        browser support return an unsupported-feature error.

        Args:
          script: JavaScript expression to evaluate in the device's foreground Chrome tab (CDP
              Runtime.evaluate). It is an expression, not a function body — the expression's
              value is returned (no top-level 'return'). Must evaluate to a JSON-serializable
              value; wrap multi-statement logic in an IIFE, e.g. (() => { ... ; return x })().

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
        return self._post(
            path_template("/devices/{device_id}/browser/execute-script", device_id=device_id),
            body=maybe_transform({"script": script}, browser_execute_script_params.BrowserExecuteScriptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserExecuteScriptResponse,
        )


class AsyncBrowserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncBrowserResourceWithStreamingResponse(self)

    async def execute_script(
        self,
        device_id: str,
        *,
        script: str,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserExecuteScriptResponse:
        """
        Evaluates a JavaScript expression in the device's foreground Chrome tab via the
        Chrome DevTools Protocol and returns its JSON-serialized result. Devices without
        browser support return an unsupported-feature error.

        Args:
          script: JavaScript expression to evaluate in the device's foreground Chrome tab (CDP
              Runtime.evaluate). It is an expression, not a function body — the expression's
              value is returned (no top-level 'return'). Must evaluate to a JSON-serializable
              value; wrap multi-statement logic in an IIFE, e.g. (() => { ... ; return x })().

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
        return await self._post(
            path_template("/devices/{device_id}/browser/execute-script", device_id=device_id),
            body=await async_maybe_transform(
                {"script": script}, browser_execute_script_params.BrowserExecuteScriptParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserExecuteScriptResponse,
        )


class BrowserResourceWithRawResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

        self.execute_script = to_raw_response_wrapper(
            browser.execute_script,
        )


class AsyncBrowserResourceWithRawResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

        self.execute_script = async_to_raw_response_wrapper(
            browser.execute_script,
        )


class BrowserResourceWithStreamingResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

        self.execute_script = to_streamed_response_wrapper(
            browser.execute_script,
        )


class AsyncBrowserResourceWithStreamingResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

        self.execute_script = async_to_streamed_response_wrapper(
            browser.execute_script,
        )
