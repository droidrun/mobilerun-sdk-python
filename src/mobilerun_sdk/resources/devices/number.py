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
from ...types.devices import number_bind_params
from ...types.devices.number_bind_response import NumberBindResponse
from ...types.devices.number_unbind_response import NumberUnbindResponse
from ...types.devices.number_retrieve_response import NumberRetrieveResponse

__all__ = ["NumberResource", "AsyncNumberResource"]


class NumberResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return NumberResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> NumberRetrieveResponse:
        """
        Returns the cloud number bound to the device and the SIM line the device
        presents (carrier, number).

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
            path_template("/devices/{device_id}/number", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberRetrieveResponse,
        )

    def bind(
        self,
        device_id: str,
        *,
        number_id: str,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NumberBindResponse:
        """Binds one of your cloud numbers to the device.

        The device's SIM shows the number
        and every SMS it receives is delivered into the device's messages app. Available
        on devices whose capabilities report telephony. A number can be bound to one
        device, and a device holds one number; unbind first to move it.

        Args:
          number_id: The cloud number's id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
            path_template("/devices/{device_id}/number", device_id=device_id),
            body=maybe_transform({"number_id": number_id}, number_bind_params.NumberBindParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NumberBindResponse,
        )

    def unbind(
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
        idempotency_key: str | None = None,
    ) -> NumberUnbindResponse:
        """Releases the number bound to the device.

        The device returns to its own default
        line; SMS to the number stop reaching the device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/devices/{device_id}/number", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NumberUnbindResponse,
        )


class AsyncNumberResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncNumberResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> NumberRetrieveResponse:
        """
        Returns the cloud number bound to the device and the SIM line the device
        presents (carrier, number).

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
            path_template("/devices/{device_id}/number", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberRetrieveResponse,
        )

    async def bind(
        self,
        device_id: str,
        *,
        number_id: str,
        x_device_display_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> NumberBindResponse:
        """Binds one of your cloud numbers to the device.

        The device's SIM shows the number
        and every SMS it receives is delivered into the device's messages app. Available
        on devices whose capabilities report telephony. A number can be bound to one
        device, and a device holds one number; unbind first to move it.

        Args:
          number_id: The cloud number's id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
            path_template("/devices/{device_id}/number", device_id=device_id),
            body=await async_maybe_transform({"number_id": number_id}, number_bind_params.NumberBindParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NumberBindResponse,
        )

    async def unbind(
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
        idempotency_key: str | None = None,
    ) -> NumberUnbindResponse:
        """Releases the number bound to the device.

        The device returns to its own default
        line; SMS to the number stop reaching the device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {
            **strip_not_given(
                {"X-Device-Display-ID": str(x_device_display_id) if is_given(x_device_display_id) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/devices/{device_id}/number", device_id=device_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NumberUnbindResponse,
        )


class NumberResourceWithRawResponse:
    def __init__(self, number: NumberResource) -> None:
        self._number = number

        self.retrieve = to_raw_response_wrapper(
            number.retrieve,
        )
        self.bind = to_raw_response_wrapper(
            number.bind,
        )
        self.unbind = to_raw_response_wrapper(
            number.unbind,
        )


class AsyncNumberResourceWithRawResponse:
    def __init__(self, number: AsyncNumberResource) -> None:
        self._number = number

        self.retrieve = async_to_raw_response_wrapper(
            number.retrieve,
        )
        self.bind = async_to_raw_response_wrapper(
            number.bind,
        )
        self.unbind = async_to_raw_response_wrapper(
            number.unbind,
        )


class NumberResourceWithStreamingResponse:
    def __init__(self, number: NumberResource) -> None:
        self._number = number

        self.retrieve = to_streamed_response_wrapper(
            number.retrieve,
        )
        self.bind = to_streamed_response_wrapper(
            number.bind,
        )
        self.unbind = to_streamed_response_wrapper(
            number.unbind,
        )


class AsyncNumberResourceWithStreamingResponse:
    def __init__(self, number: AsyncNumberResource) -> None:
        self._number = number

        self.retrieve = async_to_streamed_response_wrapper(
            number.retrieve,
        )
        self.bind = async_to_streamed_response_wrapper(
            number.bind,
        )
        self.unbind = async_to_streamed_response_wrapper(
            number.unbind,
        )
