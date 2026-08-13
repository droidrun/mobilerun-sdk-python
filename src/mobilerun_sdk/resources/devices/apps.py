# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import is_given, path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.devices import app_list_params, app_stop_params, app_start_params, app_install_params
from ...types.devices.app_list_response import AppListResponse

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    def list(
        self,
        device_id: str,
        *,
        include_protected_apps: bool | Omit = omit,
        include_system_apps: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AppListResponse]:
        """
        Returns detailed information about apps installed on the device, including
        package name and label. System and protected apps are excluded unless the
        corresponding query parameters are set.

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
            path_template("/devices/{device_id}/apps", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_protected_apps": include_protected_apps,
                        "include_system_apps": include_system_apps,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            cast_to=AppListResponse,
        )

    def delete(
        self,
        package_name: str,
        *,
        device_id: str,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Uninstalls the app identified by the path package name from the device.
        Protected packages cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/devices/{device_id}/apps/{package_name}", device_id=device_id, package_name=package_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    def install(
        self,
        device_id: str,
        *,
        bundle_id: str,
        background: bool | Omit = omit,
        package_name: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Requests an app install on the device.

        The request body must supply exactly one
        of an Android packageName or an iOS bundleId; protected packages are rejected.
        background (default false) selects the response contract: false installs inline
        and returns the outcome directly (200 on success, an error status on failure);
        true accepts the request and runs the download + install in the background,
        returning 202 immediately — poll list-app-installs for the backend's view of
        that attempt's status. Refuses with 409 once 2 other installs are already
        running on the device, in either mode; a repeat request for an app that already
        has an install running is also refused with 409 rather than superseding it —
        retry once that attempt reaches a terminal state.

        Args:
          bundle_id: iOS bundle identifier (e.g. com.example.app)

          background: true: return 202 immediately and install in the background (poll
              list-app-installs). false/omitted: install inline and return the outcome
              directly (200 on success, an error status on failure).

          package_name: Android package name (e.g. com.example.app)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def install(
        self,
        device_id: str,
        *,
        package_name: str,
        background: bool | Omit = omit,
        bundle_id: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Requests an app install on the device.

        The request body must supply exactly one
        of an Android packageName or an iOS bundleId; protected packages are rejected.
        background (default false) selects the response contract: false installs inline
        and returns the outcome directly (200 on success, an error status on failure);
        true accepts the request and runs the download + install in the background,
        returning 202 immediately — poll list-app-installs for the backend's view of
        that attempt's status. Refuses with 409 once 2 other installs are already
        running on the device, in either mode; a repeat request for an app that already
        has an install running is also refused with 409 rather than superseding it —
        retry once that attempt reaches a terminal state.

        Args:
          package_name: Android package name (e.g. com.example.app)

          background: true: return 202 immediately and install in the background (poll
              list-app-installs). false/omitted: install inline and return the outcome
              directly (200 on success, an error status on failure).

          bundle_id: iOS bundle identifier (e.g. com.example.app)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["bundle_id"], ["package_name"])
    def install(
        self,
        device_id: str,
        *,
        bundle_id: str | Omit = omit,
        background: bool | Omit = omit,
        package_name: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
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
            path_template("/devices/{device_id}/apps", device_id=device_id),
            body=maybe_transform(
                {
                    "bundle_id": bundle_id,
                    "background": background,
                    "package_name": package_name,
                },
                app_install_params.AppInstallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def start(
        self,
        package_name: str,
        *,
        device_id: str,
        activity: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Launches the app identified by the path package name, optionally starting a
        specific activity given in the request body. Protected packages cannot be
        started.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._put(
            path_template("/devices/{device_id}/apps/{package_name}", device_id=device_id, package_name=package_name),
            body=maybe_transform({"activity": activity}, app_start_params.AppStartParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stop(
        self,
        package_name: str,
        *,
        device_id: str,
        clear_data: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Force-stops the app identified by the path package name.

        When clearData is set
        in the request body, the app's data is also cleared. Protected packages cannot
        be stopped.

        Args:
          clear_data: If true, clears all app data (pm clear) in addition to stopping the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/devices/{device_id}/apps/{package_name}", device_id=device_id, package_name=package_name),
            body=maybe_transform({"clear_data": clear_data}, app_stop_params.AppStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    async def list(
        self,
        device_id: str,
        *,
        include_protected_apps: bool | Omit = omit,
        include_system_apps: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AppListResponse]:
        """
        Returns detailed information about apps installed on the device, including
        package name and label. System and protected apps are excluded unless the
        corresponding query parameters are set.

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
            path_template("/devices/{device_id}/apps", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_protected_apps": include_protected_apps,
                        "include_system_apps": include_system_apps,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            cast_to=AppListResponse,
        )

    async def delete(
        self,
        package_name: str,
        *,
        device_id: str,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Uninstalls the app identified by the path package name from the device.
        Protected packages cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/devices/{device_id}/apps/{package_name}", device_id=device_id, package_name=package_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    async def install(
        self,
        device_id: str,
        *,
        bundle_id: str,
        background: bool | Omit = omit,
        package_name: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Requests an app install on the device.

        The request body must supply exactly one
        of an Android packageName or an iOS bundleId; protected packages are rejected.
        background (default false) selects the response contract: false installs inline
        and returns the outcome directly (200 on success, an error status on failure);
        true accepts the request and runs the download + install in the background,
        returning 202 immediately — poll list-app-installs for the backend's view of
        that attempt's status. Refuses with 409 once 2 other installs are already
        running on the device, in either mode; a repeat request for an app that already
        has an install running is also refused with 409 rather than superseding it —
        retry once that attempt reaches a terminal state.

        Args:
          bundle_id: iOS bundle identifier (e.g. com.example.app)

          background: true: return 202 immediately and install in the background (poll
              list-app-installs). false/omitted: install inline and return the outcome
              directly (200 on success, an error status on failure).

          package_name: Android package name (e.g. com.example.app)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def install(
        self,
        device_id: str,
        *,
        package_name: str,
        background: bool | Omit = omit,
        bundle_id: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Requests an app install on the device.

        The request body must supply exactly one
        of an Android packageName or an iOS bundleId; protected packages are rejected.
        background (default false) selects the response contract: false installs inline
        and returns the outcome directly (200 on success, an error status on failure);
        true accepts the request and runs the download + install in the background,
        returning 202 immediately — poll list-app-installs for the backend's view of
        that attempt's status. Refuses with 409 once 2 other installs are already
        running on the device, in either mode; a repeat request for an app that already
        has an install running is also refused with 409 rather than superseding it —
        retry once that attempt reaches a terminal state.

        Args:
          package_name: Android package name (e.g. com.example.app)

          background: true: return 202 immediately and install in the background (poll
              list-app-installs). false/omitted: install inline and return the outcome
              directly (200 on success, an error status on failure).

          bundle_id: iOS bundle identifier (e.g. com.example.app)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["bundle_id"], ["package_name"])
    async def install(
        self,
        device_id: str,
        *,
        bundle_id: str | Omit = omit,
        background: bool | Omit = omit,
        package_name: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
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
            path_template("/devices/{device_id}/apps", device_id=device_id),
            body=await async_maybe_transform(
                {
                    "bundle_id": bundle_id,
                    "background": background,
                    "package_name": package_name,
                },
                app_install_params.AppInstallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def start(
        self,
        package_name: str,
        *,
        device_id: str,
        activity: str | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Launches the app identified by the path package name, optionally starting a
        specific activity given in the request body. Protected packages cannot be
        started.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            path_template("/devices/{device_id}/apps/{package_name}", device_id=device_id, package_name=package_name),
            body=await async_maybe_transform({"activity": activity}, app_start_params.AppStartParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stop(
        self,
        package_name: str,
        *,
        device_id: str,
        clear_data: bool | Omit = omit,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Force-stops the app identified by the path package name.

        When clearData is set
        in the request body, the app's data is also cleared. Protected packages cannot
        be stopped.

        Args:
          clear_data: If true, clears all app data (pm clear) in addition to stopping the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/devices/{device_id}/apps/{package_name}", device_id=device_id, package_name=package_name),
            body=await async_maybe_transform({"clear_data": clear_data}, app_stop_params.AppStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.list = to_raw_response_wrapper(
            apps.list,
        )
        self.delete = to_raw_response_wrapper(
            apps.delete,
        )
        self.install = to_raw_response_wrapper(
            apps.install,
        )
        self.start = to_raw_response_wrapper(
            apps.start,
        )
        self.stop = to_raw_response_wrapper(
            apps.stop,
        )


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.list = async_to_raw_response_wrapper(
            apps.list,
        )
        self.delete = async_to_raw_response_wrapper(
            apps.delete,
        )
        self.install = async_to_raw_response_wrapper(
            apps.install,
        )
        self.start = async_to_raw_response_wrapper(
            apps.start,
        )
        self.stop = async_to_raw_response_wrapper(
            apps.stop,
        )


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.list = to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = to_streamed_response_wrapper(
            apps.delete,
        )
        self.install = to_streamed_response_wrapper(
            apps.install,
        )
        self.start = to_streamed_response_wrapper(
            apps.start,
        )
        self.stop = to_streamed_response_wrapper(
            apps.stop,
        )


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.list = async_to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            apps.delete,
        )
        self.install = async_to_streamed_response_wrapper(
            apps.install,
        )
        self.start = async_to_streamed_response_wrapper(
            apps.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            apps.stop,
        )
