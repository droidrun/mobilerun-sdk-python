# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._resource import SyncAPIResource, AsyncAPIResource

from .apn import ApnResource, AsyncApnResource, ApnResourceWithRawResponse, AsyncApnResourceWithRawResponse, ApnResourceWithStreamingResponse, AsyncApnResourceWithStreamingResponse

from ...._compat import cached_property

from ...._utils import path_template, strip_not_given, is_given, maybe_transform, async_maybe_transform

from ....types.devices.esim_list_response import EsimListResponse

from ...._types import not_given, Omit, omit, NotGiven

from ...._base_client import make_request_options

from typing import Optional

from ....types.devices.esim_activate_response import EsimActivateResponse

from ....types.devices.esim_status_response import EsimStatusResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ...._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ....types.devices import esim_activate_params
from ....types.devices import esim_enable_params
from ....types.devices import esim_remove_params
from ....types.devices import esim_set_roaming_params

__all__ = ["EsimResource", "AsyncEsimResource"]

class EsimResource(SyncAPIResource):
    @cached_property
    def apn(self) -> ApnResource:
        return ApnResource(self._client)

    @cached_property
    def with_raw_response(self) -> EsimResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EsimResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EsimResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return EsimResourceWithStreamingResponse(self)

    def list(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> Optional[EsimListResponse]:
        """
        Returns the eSIM subscriptions currently provisioned on the device.

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
            path_template("/devices/{device_id}/esim", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EsimListResponse,
        )

    def activate(self,
    device_id: str,
    *,
    enable: bool,
    sm_dp_addr: str,
    confirmation_code: str | Omit = omit,
    matching_id: str | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> EsimActivateResponse:
        """
        Download profile and/or enable subscription.

        Args:
          confirmation_code: Optional carrier-issued confirmation code (the 4th LPA segment). Required only
              for plans whose SM-DP+ challenges the device for one. Requires matchingId — the
              LPA spec only interprets segment 4 when segment 3 is present.

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
        return self._post(
            path_template("/devices/{device_id}/esim", device_id=device_id),
            body=maybe_transform({
                "enable": enable,
                "sm_dp_addr": sm_dp_addr,
                "confirmation_code": confirmation_code,
                "matching_id": matching_id,
            }, esim_activate_params.EsimActivateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EsimActivateResponse,
        )

    def enable(self,
    device_id: str,
    *,
    sub_id: int,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Enables the eSIM subscription identified by the subId in the request body so it
        becomes the active subscription.

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
            path_template("/devices/{device_id}/esim", device_id=device_id),
            body=maybe_transform({
                "sub_id": sub_id
            }, esim_enable_params.EsimEnableParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def remove(self,
    device_id: str,
    *,
    sub_id: int,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Deletes the eSIM subscription identified by the subId query parameter from the
        device.

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
            path_template("/devices/{device_id}/esim", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "sub_id": sub_id
            }, esim_remove_params.EsimRemoveParams)),
            cast_to=NoneType,
        )

    def set_roaming(self,
    device_id: str,
    *,
    enabled: bool,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Enables or disables data roaming for the device's eSIM based on the enabled flag
        in the request body.

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
            path_template("/devices/{device_id}/esim/roaming", device_id=device_id),
            body=maybe_transform({
                "enabled": enabled
            }, esim_set_roaming_params.EsimSetRoamingParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def status(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> Optional[EsimStatusResponse]:
        """
        Returns the connectivity status of the device's eSIM subscriptions.

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
            path_template("/devices/{device_id}/esim/status", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EsimStatusResponse,
        )

class AsyncEsimResource(AsyncAPIResource):
    @cached_property
    def apn(self) -> AsyncApnResource:
        return AsyncApnResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEsimResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEsimResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEsimResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncEsimResourceWithStreamingResponse(self)

    async def list(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> Optional[EsimListResponse]:
        """
        Returns the eSIM subscriptions currently provisioned on the device.

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
            path_template("/devices/{device_id}/esim", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EsimListResponse,
        )

    async def activate(self,
    device_id: str,
    *,
    enable: bool,
    sm_dp_addr: str,
    confirmation_code: str | Omit = omit,
    matching_id: str | Omit = omit,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> EsimActivateResponse:
        """
        Download profile and/or enable subscription.

        Args:
          confirmation_code: Optional carrier-issued confirmation code (the 4th LPA segment). Required only
              for plans whose SM-DP+ challenges the device for one. Requires matchingId — the
              LPA spec only interprets segment 4 when segment 3 is present.

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
        return await self._post(
            path_template("/devices/{device_id}/esim", device_id=device_id),
            body=await async_maybe_transform({
                "enable": enable,
                "sm_dp_addr": sm_dp_addr,
                "confirmation_code": confirmation_code,
                "matching_id": matching_id,
            }, esim_activate_params.EsimActivateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EsimActivateResponse,
        )

    async def enable(self,
    device_id: str,
    *,
    sub_id: int,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Enables the eSIM subscription identified by the subId in the request body so it
        becomes the active subscription.

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
            path_template("/devices/{device_id}/esim", device_id=device_id),
            body=await async_maybe_transform({
                "sub_id": sub_id
            }, esim_enable_params.EsimEnableParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def remove(self,
    device_id: str,
    *,
    sub_id: int,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Deletes the eSIM subscription identified by the subId query parameter from the
        device.

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
            path_template("/devices/{device_id}/esim", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "sub_id": sub_id
            }, esim_remove_params.EsimRemoveParams)),
            cast_to=NoneType,
        )

    async def set_roaming(self,
    device_id: str,
    *,
    enabled: bool,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> None:
        """
        Enables or disables data roaming for the device's eSIM based on the enabled flag
        in the request body.

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
            path_template("/devices/{device_id}/esim/roaming", device_id=device_id),
            body=await async_maybe_transform({
                "enabled": enabled
            }, esim_set_roaming_params.EsimSetRoamingParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def status(self,
    device_id: str,
    *,
    x_device_display_id: int | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> Optional[EsimStatusResponse]:
        """
        Returns the connectivity status of the device's eSIM subscriptions.

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
            path_template("/devices/{device_id}/esim/status", device_id=device_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EsimStatusResponse,
        )

class EsimResourceWithRawResponse:
    def __init__(self, esim: EsimResource) -> None:
        self._esim = esim

        self.list = to_raw_response_wrapper(
            esim.list,
        )
        self.activate = to_raw_response_wrapper(
            esim.activate,
        )
        self.enable = to_raw_response_wrapper(
            esim.enable,
        )
        self.remove = to_raw_response_wrapper(
            esim.remove,
        )
        self.set_roaming = to_raw_response_wrapper(
            esim.set_roaming,
        )
        self.status = to_raw_response_wrapper(
            esim.status,
        )

    @cached_property
    def apn(self) -> ApnResourceWithRawResponse:
        return ApnResourceWithRawResponse(self._esim.apn)

class AsyncEsimResourceWithRawResponse:
    def __init__(self, esim: AsyncEsimResource) -> None:
        self._esim = esim

        self.list = async_to_raw_response_wrapper(
            esim.list,
        )
        self.activate = async_to_raw_response_wrapper(
            esim.activate,
        )
        self.enable = async_to_raw_response_wrapper(
            esim.enable,
        )
        self.remove = async_to_raw_response_wrapper(
            esim.remove,
        )
        self.set_roaming = async_to_raw_response_wrapper(
            esim.set_roaming,
        )
        self.status = async_to_raw_response_wrapper(
            esim.status,
        )

    @cached_property
    def apn(self) -> AsyncApnResourceWithRawResponse:
        return AsyncApnResourceWithRawResponse(self._esim.apn)

class EsimResourceWithStreamingResponse:
    def __init__(self, esim: EsimResource) -> None:
        self._esim = esim

        self.list = to_streamed_response_wrapper(
            esim.list,
        )
        self.activate = to_streamed_response_wrapper(
            esim.activate,
        )
        self.enable = to_streamed_response_wrapper(
            esim.enable,
        )
        self.remove = to_streamed_response_wrapper(
            esim.remove,
        )
        self.set_roaming = to_streamed_response_wrapper(
            esim.set_roaming,
        )
        self.status = to_streamed_response_wrapper(
            esim.status,
        )

    @cached_property
    def apn(self) -> ApnResourceWithStreamingResponse:
        return ApnResourceWithStreamingResponse(self._esim.apn)

class AsyncEsimResourceWithStreamingResponse:
    def __init__(self, esim: AsyncEsimResource) -> None:
        self._esim = esim

        self.list = async_to_streamed_response_wrapper(
            esim.list,
        )
        self.activate = async_to_streamed_response_wrapper(
            esim.activate,
        )
        self.enable = async_to_streamed_response_wrapper(
            esim.enable,
        )
        self.remove = async_to_streamed_response_wrapper(
            esim.remove,
        )
        self.set_roaming = async_to_streamed_response_wrapper(
            esim.set_roaming,
        )
        self.status = async_to_streamed_response_wrapper(
            esim.status,
        )

    @cached_property
    def apn(self) -> AsyncApnResourceWithStreamingResponse:
        return AsyncApnResourceWithStreamingResponse(self._esim.apn)