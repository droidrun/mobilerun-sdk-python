# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .apps import (
    AppsResource,
    AsyncAppsResource,
    AppsResourceWithRawResponse,
    AsyncAppsResourceWithRawResponse,
    AppsResourceWithStreamingResponse,
    AsyncAppsResourceWithStreamingResponse,
)
from .esim import (
    EsimResource,
    AsyncEsimResource,
    EsimResourceWithRawResponse,
    AsyncEsimResourceWithRawResponse,
    EsimResourceWithStreamingResponse,
    AsyncEsimResourceWithStreamingResponse,
)
from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .proxy import (
    ProxyResource,
    AsyncProxyResource,
    ProxyResourceWithRawResponse,
    AsyncProxyResourceWithRawResponse,
    ProxyResourceWithStreamingResponse,
    AsyncProxyResourceWithStreamingResponse,
)
from .state import (
    StateResource,
    AsyncStateResource,
    StateResourceWithRawResponse,
    AsyncStateResourceWithRawResponse,
    StateResourceWithStreamingResponse,
    AsyncStateResourceWithStreamingResponse,
)
from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from ...types import device_list_params, device_create_params, device_set_name_params, device_terminate_params
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
from .keyboard import (
    KeyboardResource,
    AsyncKeyboardResource,
    KeyboardResourceWithRawResponse,
    AsyncKeyboardResourceWithRawResponse,
    KeyboardResourceWithStreamingResponse,
    AsyncKeyboardResourceWithStreamingResponse,
)
from .language import (
    LanguageResource,
    AsyncLanguageResource,
    LanguageResourceWithRawResponse,
    AsyncLanguageResourceWithRawResponse,
    LanguageResourceWithStreamingResponse,
    AsyncLanguageResourceWithStreamingResponse,
)
from .location import (
    LocationResource,
    AsyncLocationResource,
    LocationResourceWithRawResponse,
    AsyncLocationResourceWithRawResponse,
    LocationResourceWithStreamingResponse,
    AsyncLocationResourceWithStreamingResponse,
)
from .packages import (
    PackagesResource,
    AsyncPackagesResource,
    PackagesResourceWithRawResponse,
    AsyncPackagesResourceWithRawResponse,
    PackagesResourceWithStreamingResponse,
    AsyncPackagesResourceWithStreamingResponse,
)
from .timezone import (
    TimezoneResource,
    AsyncTimezoneResource,
    TimezoneResourceWithRawResponse,
    AsyncTimezoneResourceWithRawResponse,
    TimezoneResourceWithStreamingResponse,
    AsyncTimezoneResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.device import Device
from ...types.device_list_response import DeviceListResponse
from ...types.device_count_response import DeviceCountResponse
from ...types.shared_params.location import Location
from ...types.device_fingerprint_response import DeviceFingerprintResponse
from ...types.shared_params.device_carrier import DeviceCarrier
from ...types.shared_params.device_identifiers import DeviceIdentifiers

__all__ = ["DevicesResource", "AsyncDevicesResource"]


class DevicesResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def apps(self) -> AppsResource:
        return AppsResource(self._client)

    @cached_property
    def esim(self) -> EsimResource:
        return EsimResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def keyboard(self) -> KeyboardResource:
        return KeyboardResource(self._client)

    @cached_property
    def location(self) -> LocationResource:
        return LocationResource(self._client)

    @cached_property
    def packages(self) -> PackagesResource:
        return PackagesResource(self._client)

    @cached_property
    def profile(self) -> ProfileResource:
        return ProfileResource(self._client)

    @cached_property
    def proxy(self) -> ProxyResource:
        return ProxyResource(self._client)

    @cached_property
    def state(self) -> StateResource:
        return StateResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def timezone(self) -> TimezoneResource:
        return TimezoneResource(self._client)

    @cached_property
    def language(self) -> LanguageResource:
        return LanguageResource(self._client)

    @cached_property
    def with_raw_response(self) -> DevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return DevicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        billing: Literal["auto", "subscription", "minute"] | Omit = omit,
        query_country: str | Omit = omit,
        device_type: Literal[
            "dedicated_premium_device", "dedicated_ios_device", "dedicated_emulated_device", "ios_simulator"
        ]
        | Omit = omit,
        profile_id: str | Omit = omit,
        android_version: int | Omit = omit,
        apps: Optional[SequenceNotStr[str]] | Omit = omit,
        carrier: DeviceCarrier | Omit = omit,
        body_country: str | Omit = omit,
        files: Optional[SequenceNotStr[str]] | Omit = omit,
        identifiers: DeviceIdentifiers | Omit = omit,
        locale: str | Omit = omit,
        location: Location | Omit = omit,
        name: str | Omit = omit,
        proxy: device_create_params.Proxy | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Requests a new device for the authenticated user from the device spec in the
        request body. Optional query parameters select the device type, target country,
        billing mode, and a profile to use as the base spec; the response returns the
        device and its stream token.

        Args:
          billing: Billing mode. 'auto' uses a subscription slot when available and otherwise bills
              per minute; 'subscription' requires an available subscription slot; 'minute'
              bills per minute. Only cloud phone and cloud emulator devices support per-minute
              billing.

          query_country: ISO 3166-1 alpha-2 country code. If omitted the system picks the country with
              the most availability.

          profile_id: Profile ID to use as device spec

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/devices",
            body=maybe_transform(
                {
                    "android_version": android_version,
                    "apps": apps,
                    "carrier": carrier,
                    "body_country": body_country,
                    "files": files,
                    "identifiers": identifiers,
                    "locale": locale,
                    "location": location,
                    "name": name,
                    "proxy": proxy,
                    "timezone": timezone,
                },
                device_create_params.DeviceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "billing": billing,
                        "query_country": query_country,
                        "device_type": device_type,
                        "profile_id": profile_id,
                    },
                    device_create_params.DeviceCreateParams,
                ),
            ),
            cast_to=Device,
        )

    def retrieve(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Returns the current state and metadata for a single device, including its
        lifecycle state, type, stream URL, billing strategy, and timestamps. A stream
        token is included while the device is active.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get(
            path_template("/devices/{device_id}", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    def list(
        self,
        *,
        country: str | Omit = omit,
        created_by: str | Omit = omit,
        mine: bool | Omit = omit,
        name: str | Omit = omit,
        order_by: Literal["id", "createdAt", "updatedAt", "assignedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        provider_id: str | Omit = omit,
        state: Optional[
            List[
                Literal[
                    "creating",
                    "assigned",
                    "ready",
                    "rebooting",
                    "migrating",
                    "resetting",
                    "terminated",
                    "maintenance",
                    "unknown",
                ]
            ]
        ]
        | Omit = omit,
        type: Literal["dedicated_premium_device", "dedicated_ios_device", "dedicated_emulated_device", "ios_simulator"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceListResponse:
        """
        Returns a paginated list of the user's devices along with pagination metadata.

        Args:
          created_by: Filter to devices created by this user id. Mutually exclusive with mine.

          mine: When true, only return devices created by the calling user (resolved from
              X-User-ID, never a client-supplied id).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "created_by": created_by,
                        "mine": mine,
                        "name": name,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "provider_id": provider_id,
                        "state": state,
                        "type": type,
                    },
                    device_list_params.DeviceListParams,
                ),
            ),
            cast_to=DeviceListResponse,
        )

    def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceCountResponse:
        """Returns the number of claimed devices for the user, broken down by device type."""
        return self._get(
            "/devices/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCountResponse,
        )

    def fingerprint(
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
    ) -> DeviceFingerprintResponse:
        """
        Returns a live snapshot of the device's spoofed identity, including model,
        display, identifiers, and carrier. Devices without fingerprint support return an
        unsupported-feature error.

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
            path_template("/devices/{device_id}/fingerprint", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceFingerprintResponse,
        )

    def reboot(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Triggers a reboot of the device.

        The device transitions through its reboot
        lifecycle and becomes ready again once the restart completes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/devices/{device_id}/reboot", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def reset(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resets the device back to a clean state, clearing installed apps and user data
        accumulated during the session. The device transitions through its reset
        lifecycle before becoming ready again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/devices/{device_id}/reset", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set_name(
        self,
        device_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Sets the display name for a device from the name in the request body and returns
        the updated device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._put(
            path_template("/devices/{device_id}/name", device_id=device_id),
            body=maybe_transform({"name": name}, device_set_name_params.DeviceSetNameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    def terminate(
        self,
        device_id: str,
        *,
        previous_device_id: str | Omit = omit,
        terminate_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Terminates the device and releases its resources.

        Termination can be scheduled
        for a future time or chained from a previous device via the request body, in
        which case a service key is required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/devices/{device_id}", device_id=device_id),
            body=maybe_transform(
                {
                    "previous_device_id": previous_device_id,
                    "terminate_at": terminate_at,
                },
                device_terminate_params.DeviceTerminateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def wait_ready(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Blocks until the device reaches the ready state, then returns the same payload
        as Get device info. The call returns early with an error if the wait is
        cancelled or times out.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get(
            path_template("/devices/{device_id}/wait", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )


class AsyncDevicesResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def apps(self) -> AsyncAppsResource:
        return AsyncAppsResource(self._client)

    @cached_property
    def esim(self) -> AsyncEsimResource:
        return AsyncEsimResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def keyboard(self) -> AsyncKeyboardResource:
        return AsyncKeyboardResource(self._client)

    @cached_property
    def location(self) -> AsyncLocationResource:
        return AsyncLocationResource(self._client)

    @cached_property
    def packages(self) -> AsyncPackagesResource:
        return AsyncPackagesResource(self._client)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        return AsyncProfileResource(self._client)

    @cached_property
    def proxy(self) -> AsyncProxyResource:
        return AsyncProxyResource(self._client)

    @cached_property
    def state(self) -> AsyncStateResource:
        return AsyncStateResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def timezone(self) -> AsyncTimezoneResource:
        return AsyncTimezoneResource(self._client)

    @cached_property
    def language(self) -> AsyncLanguageResource:
        return AsyncLanguageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncDevicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        billing: Literal["auto", "subscription", "minute"] | Omit = omit,
        query_country: str | Omit = omit,
        device_type: Literal[
            "dedicated_premium_device", "dedicated_ios_device", "dedicated_emulated_device", "ios_simulator"
        ]
        | Omit = omit,
        profile_id: str | Omit = omit,
        android_version: int | Omit = omit,
        apps: Optional[SequenceNotStr[str]] | Omit = omit,
        carrier: DeviceCarrier | Omit = omit,
        body_country: str | Omit = omit,
        files: Optional[SequenceNotStr[str]] | Omit = omit,
        identifiers: DeviceIdentifiers | Omit = omit,
        locale: str | Omit = omit,
        location: Location | Omit = omit,
        name: str | Omit = omit,
        proxy: device_create_params.Proxy | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Requests a new device for the authenticated user from the device spec in the
        request body. Optional query parameters select the device type, target country,
        billing mode, and a profile to use as the base spec; the response returns the
        device and its stream token.

        Args:
          billing: Billing mode. 'auto' uses a subscription slot when available and otherwise bills
              per minute; 'subscription' requires an available subscription slot; 'minute'
              bills per minute. Only cloud phone and cloud emulator devices support per-minute
              billing.

          query_country: ISO 3166-1 alpha-2 country code. If omitted the system picks the country with
              the most availability.

          profile_id: Profile ID to use as device spec

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/devices",
            body=await async_maybe_transform(
                {
                    "android_version": android_version,
                    "apps": apps,
                    "carrier": carrier,
                    "body_country": body_country,
                    "files": files,
                    "identifiers": identifiers,
                    "locale": locale,
                    "location": location,
                    "name": name,
                    "proxy": proxy,
                    "timezone": timezone,
                },
                device_create_params.DeviceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "billing": billing,
                        "query_country": query_country,
                        "device_type": device_type,
                        "profile_id": profile_id,
                    },
                    device_create_params.DeviceCreateParams,
                ),
            ),
            cast_to=Device,
        )

    async def retrieve(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Returns the current state and metadata for a single device, including its
        lifecycle state, type, stream URL, billing strategy, and timestamps. A stream
        token is included while the device is active.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._get(
            path_template("/devices/{device_id}", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    async def list(
        self,
        *,
        country: str | Omit = omit,
        created_by: str | Omit = omit,
        mine: bool | Omit = omit,
        name: str | Omit = omit,
        order_by: Literal["id", "createdAt", "updatedAt", "assignedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        provider_id: str | Omit = omit,
        state: Optional[
            List[
                Literal[
                    "creating",
                    "assigned",
                    "ready",
                    "rebooting",
                    "migrating",
                    "resetting",
                    "terminated",
                    "maintenance",
                    "unknown",
                ]
            ]
        ]
        | Omit = omit,
        type: Literal["dedicated_premium_device", "dedicated_ios_device", "dedicated_emulated_device", "ios_simulator"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceListResponse:
        """
        Returns a paginated list of the user's devices along with pagination metadata.

        Args:
          created_by: Filter to devices created by this user id. Mutually exclusive with mine.

          mine: When true, only return devices created by the calling user (resolved from
              X-User-ID, never a client-supplied id).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/devices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "created_by": created_by,
                        "mine": mine,
                        "name": name,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "provider_id": provider_id,
                        "state": state,
                        "type": type,
                    },
                    device_list_params.DeviceListParams,
                ),
            ),
            cast_to=DeviceListResponse,
        )

    async def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceCountResponse:
        """Returns the number of claimed devices for the user, broken down by device type."""
        return await self._get(
            "/devices/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceCountResponse,
        )

    async def fingerprint(
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
    ) -> DeviceFingerprintResponse:
        """
        Returns a live snapshot of the device's spoofed identity, including model,
        display, identifiers, and carrier. Devices without fingerprint support return an
        unsupported-feature error.

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
            path_template("/devices/{device_id}/fingerprint", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceFingerprintResponse,
        )

    async def reboot(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Triggers a reboot of the device.

        The device transitions through its reboot
        lifecycle and becomes ready again once the restart completes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/devices/{device_id}/reboot", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def reset(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resets the device back to a clean state, clearing installed apps and user data
        accumulated during the session. The device transitions through its reset
        lifecycle before becoming ready again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/devices/{device_id}/reset", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set_name(
        self,
        device_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Sets the display name for a device from the name in the request body and returns
        the updated device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._put(
            path_template("/devices/{device_id}/name", device_id=device_id),
            body=await async_maybe_transform({"name": name}, device_set_name_params.DeviceSetNameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )

    async def terminate(
        self,
        device_id: str,
        *,
        previous_device_id: str | Omit = omit,
        terminate_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Terminates the device and releases its resources.

        Termination can be scheduled
        for a future time or chained from a previous device via the request body, in
        which case a service key is required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/devices/{device_id}", device_id=device_id),
            body=await async_maybe_transform(
                {
                    "previous_device_id": previous_device_id,
                    "terminate_at": terminate_at,
                },
                device_terminate_params.DeviceTerminateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def wait_ready(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Blocks until the device reaches the ready state, then returns the same payload
        as Get device info. The call returns early with an error if the wait is
        cancelled or times out.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._get(
            path_template("/devices/{device_id}/wait", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )


class DevicesResourceWithRawResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.create = to_raw_response_wrapper(
            devices.create,
        )
        self.retrieve = to_raw_response_wrapper(
            devices.retrieve,
        )
        self.list = to_raw_response_wrapper(
            devices.list,
        )
        self.count = to_raw_response_wrapper(
            devices.count,
        )
        self.fingerprint = to_raw_response_wrapper(
            devices.fingerprint,
        )
        self.reboot = to_raw_response_wrapper(
            devices.reboot,
        )
        self.reset = to_raw_response_wrapper(
            devices.reset,
        )
        self.set_name = to_raw_response_wrapper(
            devices.set_name,
        )
        self.terminate = to_raw_response_wrapper(
            devices.terminate,
        )
        self.wait_ready = to_raw_response_wrapper(
            devices.wait_ready,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._devices.actions)

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self._devices.apps)

    @cached_property
    def esim(self) -> EsimResourceWithRawResponse:
        return EsimResourceWithRawResponse(self._devices.esim)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._devices.files)

    @cached_property
    def keyboard(self) -> KeyboardResourceWithRawResponse:
        return KeyboardResourceWithRawResponse(self._devices.keyboard)

    @cached_property
    def location(self) -> LocationResourceWithRawResponse:
        return LocationResourceWithRawResponse(self._devices.location)

    @cached_property
    def packages(self) -> PackagesResourceWithRawResponse:
        return PackagesResourceWithRawResponse(self._devices.packages)

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self._devices.profile)

    @cached_property
    def proxy(self) -> ProxyResourceWithRawResponse:
        return ProxyResourceWithRawResponse(self._devices.proxy)

    @cached_property
    def state(self) -> StateResourceWithRawResponse:
        return StateResourceWithRawResponse(self._devices.state)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._devices.tasks)

    @cached_property
    def timezone(self) -> TimezoneResourceWithRawResponse:
        return TimezoneResourceWithRawResponse(self._devices.timezone)

    @cached_property
    def language(self) -> LanguageResourceWithRawResponse:
        return LanguageResourceWithRawResponse(self._devices.language)


class AsyncDevicesResourceWithRawResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.create = async_to_raw_response_wrapper(
            devices.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            devices.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            devices.list,
        )
        self.count = async_to_raw_response_wrapper(
            devices.count,
        )
        self.fingerprint = async_to_raw_response_wrapper(
            devices.fingerprint,
        )
        self.reboot = async_to_raw_response_wrapper(
            devices.reboot,
        )
        self.reset = async_to_raw_response_wrapper(
            devices.reset,
        )
        self.set_name = async_to_raw_response_wrapper(
            devices.set_name,
        )
        self.terminate = async_to_raw_response_wrapper(
            devices.terminate,
        )
        self.wait_ready = async_to_raw_response_wrapper(
            devices.wait_ready,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._devices.actions)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self._devices.apps)

    @cached_property
    def esim(self) -> AsyncEsimResourceWithRawResponse:
        return AsyncEsimResourceWithRawResponse(self._devices.esim)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._devices.files)

    @cached_property
    def keyboard(self) -> AsyncKeyboardResourceWithRawResponse:
        return AsyncKeyboardResourceWithRawResponse(self._devices.keyboard)

    @cached_property
    def location(self) -> AsyncLocationResourceWithRawResponse:
        return AsyncLocationResourceWithRawResponse(self._devices.location)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithRawResponse:
        return AsyncPackagesResourceWithRawResponse(self._devices.packages)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self._devices.profile)

    @cached_property
    def proxy(self) -> AsyncProxyResourceWithRawResponse:
        return AsyncProxyResourceWithRawResponse(self._devices.proxy)

    @cached_property
    def state(self) -> AsyncStateResourceWithRawResponse:
        return AsyncStateResourceWithRawResponse(self._devices.state)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._devices.tasks)

    @cached_property
    def timezone(self) -> AsyncTimezoneResourceWithRawResponse:
        return AsyncTimezoneResourceWithRawResponse(self._devices.timezone)

    @cached_property
    def language(self) -> AsyncLanguageResourceWithRawResponse:
        return AsyncLanguageResourceWithRawResponse(self._devices.language)


class DevicesResourceWithStreamingResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.create = to_streamed_response_wrapper(
            devices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            devices.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            devices.list,
        )
        self.count = to_streamed_response_wrapper(
            devices.count,
        )
        self.fingerprint = to_streamed_response_wrapper(
            devices.fingerprint,
        )
        self.reboot = to_streamed_response_wrapper(
            devices.reboot,
        )
        self.reset = to_streamed_response_wrapper(
            devices.reset,
        )
        self.set_name = to_streamed_response_wrapper(
            devices.set_name,
        )
        self.terminate = to_streamed_response_wrapper(
            devices.terminate,
        )
        self.wait_ready = to_streamed_response_wrapper(
            devices.wait_ready,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._devices.actions)

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self._devices.apps)

    @cached_property
    def esim(self) -> EsimResourceWithStreamingResponse:
        return EsimResourceWithStreamingResponse(self._devices.esim)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._devices.files)

    @cached_property
    def keyboard(self) -> KeyboardResourceWithStreamingResponse:
        return KeyboardResourceWithStreamingResponse(self._devices.keyboard)

    @cached_property
    def location(self) -> LocationResourceWithStreamingResponse:
        return LocationResourceWithStreamingResponse(self._devices.location)

    @cached_property
    def packages(self) -> PackagesResourceWithStreamingResponse:
        return PackagesResourceWithStreamingResponse(self._devices.packages)

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self._devices.profile)

    @cached_property
    def proxy(self) -> ProxyResourceWithStreamingResponse:
        return ProxyResourceWithStreamingResponse(self._devices.proxy)

    @cached_property
    def state(self) -> StateResourceWithStreamingResponse:
        return StateResourceWithStreamingResponse(self._devices.state)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._devices.tasks)

    @cached_property
    def timezone(self) -> TimezoneResourceWithStreamingResponse:
        return TimezoneResourceWithStreamingResponse(self._devices.timezone)

    @cached_property
    def language(self) -> LanguageResourceWithStreamingResponse:
        return LanguageResourceWithStreamingResponse(self._devices.language)


class AsyncDevicesResourceWithStreamingResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.create = async_to_streamed_response_wrapper(
            devices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            devices.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            devices.list,
        )
        self.count = async_to_streamed_response_wrapper(
            devices.count,
        )
        self.fingerprint = async_to_streamed_response_wrapper(
            devices.fingerprint,
        )
        self.reboot = async_to_streamed_response_wrapper(
            devices.reboot,
        )
        self.reset = async_to_streamed_response_wrapper(
            devices.reset,
        )
        self.set_name = async_to_streamed_response_wrapper(
            devices.set_name,
        )
        self.terminate = async_to_streamed_response_wrapper(
            devices.terminate,
        )
        self.wait_ready = async_to_streamed_response_wrapper(
            devices.wait_ready,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._devices.actions)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self._devices.apps)

    @cached_property
    def esim(self) -> AsyncEsimResourceWithStreamingResponse:
        return AsyncEsimResourceWithStreamingResponse(self._devices.esim)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._devices.files)

    @cached_property
    def keyboard(self) -> AsyncKeyboardResourceWithStreamingResponse:
        return AsyncKeyboardResourceWithStreamingResponse(self._devices.keyboard)

    @cached_property
    def location(self) -> AsyncLocationResourceWithStreamingResponse:
        return AsyncLocationResourceWithStreamingResponse(self._devices.location)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithStreamingResponse:
        return AsyncPackagesResourceWithStreamingResponse(self._devices.packages)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self._devices.profile)

    @cached_property
    def proxy(self) -> AsyncProxyResourceWithStreamingResponse:
        return AsyncProxyResourceWithStreamingResponse(self._devices.proxy)

    @cached_property
    def state(self) -> AsyncStateResourceWithStreamingResponse:
        return AsyncStateResourceWithStreamingResponse(self._devices.state)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._devices.tasks)

    @cached_property
    def timezone(self) -> AsyncTimezoneResourceWithStreamingResponse:
        return AsyncTimezoneResourceWithStreamingResponse(self._devices.timezone)

    @cached_property
    def language(self) -> AsyncLanguageResourceWithStreamingResponse:
        return AsyncLanguageResourceWithStreamingResponse(self._devices.language)
