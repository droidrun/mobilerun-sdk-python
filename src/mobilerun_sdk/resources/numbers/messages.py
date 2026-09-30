# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.numbers import message_list_params, message_send_params
from ...types.numbers.message_list_response import MessageListResponse
from ...types.numbers.message_send_response import MessageSendResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        direction: Literal["all", "inbound", "outbound"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        Returns SMS messages on the number, inbound and outbound, scoped to the
        authenticated user. Newest first. Messages stay with the number across device
        switches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/numbers/phones/{id}/messages", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "page_size": page_size,
                        "since": since,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    def send(
        self,
        id: str,
        *,
        body: str,
        to: str,
        client_request_id: str | Omit = omit,
        delivery_report: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MessageSendResponse:
        """Queues an SMS from one of the caller's numbers that can send.

        Same idempotency
        contract as the eSIM send: replaying an Idempotency-Key with the same payload
        returns the original message, reusing it with a different payload returns 422.
        409 capability_unavailable: this number cannot send right now. 422
        invalid_recipient / unsupported_destination / body_too_long: the recipient or
        text does not fit the number. 429 daily_limit_reached: the rolling 24 h limit
        for the account is used up; 429 rate_limited: too many sends in a short window.
        403 send_disabled: self-service SMS send is switched off.

        Args:
          body: SMS body text, up to 1600 characters (rejected with 400 beyond that, before
              hashing). A number's own limit may be lower and is answered 422 body_too_long.

          to: Recipient phone number, as E.164 or a US 10/11-digit number. Destinations the
              number cannot send to are rejected with 422 unsupported_destination, non-numbers
              with 422 invalid_recipient.

          client_request_id: Deprecated: use the Idempotency-Key header instead. Optional idempotency key.
              Replaying the same key and payload returns the original send.

          delivery_report: Request a delivery report. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/numbers/phones/{id}/messages", id=id),
            body=maybe_transform(
                {
                    "body": body,
                    "to": to,
                    "client_request_id": client_request_id,
                    "delivery_report": delivery_report,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MessageSendResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        direction: Literal["all", "inbound", "outbound"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        Returns SMS messages on the number, inbound and outbound, scoped to the
        authenticated user. Newest first. Messages stay with the number across device
        switches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/numbers/phones/{id}/messages", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "page_size": page_size,
                        "since": since,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    async def send(
        self,
        id: str,
        *,
        body: str,
        to: str,
        client_request_id: str | Omit = omit,
        delivery_report: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MessageSendResponse:
        """Queues an SMS from one of the caller's numbers that can send.

        Same idempotency
        contract as the eSIM send: replaying an Idempotency-Key with the same payload
        returns the original message, reusing it with a different payload returns 422.
        409 capability_unavailable: this number cannot send right now. 422
        invalid_recipient / unsupported_destination / body_too_long: the recipient or
        text does not fit the number. 429 daily_limit_reached: the rolling 24 h limit
        for the account is used up; 429 rate_limited: too many sends in a short window.
        403 send_disabled: self-service SMS send is switched off.

        Args:
          body: SMS body text, up to 1600 characters (rejected with 400 beyond that, before
              hashing). A number's own limit may be lower and is answered 422 body_too_long.

          to: Recipient phone number, as E.164 or a US 10/11-digit number. Destinations the
              number cannot send to are rejected with 422 unsupported_destination, non-numbers
              with 422 invalid_recipient.

          client_request_id: Deprecated: use the Idempotency-Key header instead. Optional idempotency key.
              Replaying the same key and payload returns the original send.

          delivery_report: Request a delivery report. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/numbers/phones/{id}/messages", id=id),
            body=await async_maybe_transform(
                {
                    "body": body,
                    "to": to,
                    "client_request_id": client_request_id,
                    "delivery_report": delivery_report,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MessageSendResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
