# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.devices.esim import apn_set_params, apn_select_params
from ....types.devices.esim.apn_list_response import ApnListResponse

__all__ = ["ApnResource", "AsyncApnResource"]


class ApnResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ApnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ApnResourceWithStreamingResponse(self)

    def list(
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
    ) -> Optional[ApnListResponse]:
        """
        Returns the access point names (APNs) configured for the device's active eSIM
        subscriptions.

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
            path_template("/devices/{device_id}/esim/apn", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApnListResponse,
        )

    def select(
        self,
        device_id: str,
        *,
        apn_id: int,
        sub_id: int,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Marks an existing APN, identified by apnId, as the preferred APN for the given
        eSIM subscription in the request body.

        Args:
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
        return self._put(
            path_template("/devices/{device_id}/esim/apn", device_id=device_id),
            body=maybe_transform(
                {
                    "apn_id": apn_id,
                    "sub_id": sub_id,
                },
                apn_select_params.ApnSelectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set(
        self,
        device_id: str,
        *,
        apn: str,
        mcc: str,
        mnc: str,
        name: str,
        protocol: str,
        roaming_protocol: str,
        sub_id: int,
        type: str,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates an access point name (APN) from the request body and applies it to the
        given eSIM subscription. Type, protocol, and roaming protocol default to common
        values when omitted.

        Args:
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
            path_template("/devices/{device_id}/esim/apn", device_id=device_id),
            body=maybe_transform(
                {
                    "apn": apn,
                    "mcc": mcc,
                    "mnc": mnc,
                    "name": name,
                    "protocol": protocol,
                    "roaming_protocol": roaming_protocol,
                    "sub_id": sub_id,
                    "type": type,
                },
                apn_set_params.ApnSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncApnResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncApnResourceWithStreamingResponse(self)

    async def list(
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
    ) -> Optional[ApnListResponse]:
        """
        Returns the access point names (APNs) configured for the device's active eSIM
        subscriptions.

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
            path_template("/devices/{device_id}/esim/apn", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApnListResponse,
        )

    async def select(
        self,
        device_id: str,
        *,
        apn_id: int,
        sub_id: int,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Marks an existing APN, identified by apnId, as the preferred APN for the given
        eSIM subscription in the request body.

        Args:
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
        return await self._put(
            path_template("/devices/{device_id}/esim/apn", device_id=device_id),
            body=await async_maybe_transform(
                {
                    "apn_id": apn_id,
                    "sub_id": sub_id,
                },
                apn_select_params.ApnSelectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set(
        self,
        device_id: str,
        *,
        apn: str,
        mcc: str,
        mnc: str,
        name: str,
        protocol: str,
        roaming_protocol: str,
        sub_id: int,
        type: str,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates an access point name (APN) from the request body and applies it to the
        given eSIM subscription. Type, protocol, and roaming protocol default to common
        values when omitted.

        Args:
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
            path_template("/devices/{device_id}/esim/apn", device_id=device_id),
            body=await async_maybe_transform(
                {
                    "apn": apn,
                    "mcc": mcc,
                    "mnc": mnc,
                    "name": name,
                    "protocol": protocol,
                    "roaming_protocol": roaming_protocol,
                    "sub_id": sub_id,
                    "type": type,
                },
                apn_set_params.ApnSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ApnResourceWithRawResponse:
    def __init__(self, apn: ApnResource) -> None:
        self._apn = apn

        self.list = to_raw_response_wrapper(
            apn.list,
        )
        self.select = to_raw_response_wrapper(
            apn.select,
        )
        self.set = to_raw_response_wrapper(
            apn.set,
        )


class AsyncApnResourceWithRawResponse:
    def __init__(self, apn: AsyncApnResource) -> None:
        self._apn = apn

        self.list = async_to_raw_response_wrapper(
            apn.list,
        )
        self.select = async_to_raw_response_wrapper(
            apn.select,
        )
        self.set = async_to_raw_response_wrapper(
            apn.set,
        )


class ApnResourceWithStreamingResponse:
    def __init__(self, apn: ApnResource) -> None:
        self._apn = apn

        self.list = to_streamed_response_wrapper(
            apn.list,
        )
        self.select = to_streamed_response_wrapper(
            apn.select,
        )
        self.set = to_streamed_response_wrapper(
            apn.set,
        )


class AsyncApnResourceWithStreamingResponse:
    def __init__(self, apn: AsyncApnResource) -> None:
        self._apn = apn

        self.list = async_to_streamed_response_wrapper(
            apn.list,
        )
        self.select = async_to_streamed_response_wrapper(
            apn.select,
        )
        self.set = async_to_streamed_response_wrapper(
            apn.set,
        )
