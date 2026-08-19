# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, maybe_transform, async_maybe_transform

from ...types.esims.message_list_response import MessageListResponse

from ..._base_client import make_request_options

from typing_extensions import Literal

from ..._types import Omit, omit, NotGiven

from ...types.esims.message_send_response import MessageSendResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.esims import message_list_params
from ...types.esims import message_send_params

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

    def list(self,
    id: str,
    *,
    direction: Literal["all", "inbound", "outbound"] | Omit = omit,
    number_id: str | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    peer_key: str | Omit = omit,
    peer_number: str | Omit = omit,
    status: Literal["all", "received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MessageListResponse:
        """
        List messages for one eSIM

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
          raise ValueError(
            f'Expected a non-empty value for `id` but received {id!r}'
          )
        return self._get(
            path_template("/numbers/esims/{id}/messages", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "direction": direction,
                "number_id": number_id,
                "page": page,
                "page_size": page_size,
                "peer_key": peer_key,
                "peer_number": peer_number,
                "status": status,
            }, message_list_params.MessageListParams)),
            cast_to=MessageListResponse,
        )

    def send(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MessageSendResponse:
        """
        Send an SMS through one eSIM

        Args:
          body: SMS body text (max 320 chars — smaller than the admin tier's cap; see the
              schema's own doc comment for why)

          to: Recipient phone number — normalized to E.164 (spaces/dashes/dots stripped);
              rejected with 400 if it doesn't validate as E.164 afterward.

          client_request_id: Client-supplied idempotency key, scoped to (owner, esimId, key). Replaying the
              same key + identical payload returns the original send; the same key with a
              DIFFERENT payload is a 409 conflict.

          delivery_report: Wait for physedge to confirm carrier delivery before completing the send (adds
              executor-side latency, never on this request — sends are always async/202).
              Defaults to false for the public tier (opt-in, unlike the admin tier's
              default-true).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
          raise ValueError(
            f'Expected a non-empty value for `id` but received {id!r}'
          )
        return self._post(
            path_template("/numbers/esims/{id}/messages", id=id),
            body=maybe_transform({
                "body": body,
                "to": to,
                "client_request_id": client_request_id,
                "delivery_report": delivery_report,
            }, message_send_params.MessageSendParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
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

    async def list(self,
    id: str,
    *,
    direction: Literal["all", "inbound", "outbound"] | Omit = omit,
    number_id: str | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    peer_key: str | Omit = omit,
    peer_number: str | Omit = omit,
    status: Literal["all", "received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MessageListResponse:
        """
        List messages for one eSIM

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
          raise ValueError(
            f'Expected a non-empty value for `id` but received {id!r}'
          )
        return await self._get(
            path_template("/numbers/esims/{id}/messages", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "direction": direction,
                "number_id": number_id,
                "page": page,
                "page_size": page_size,
                "peer_key": peer_key,
                "peer_number": peer_number,
                "status": status,
            }, message_list_params.MessageListParams)),
            cast_to=MessageListResponse,
        )

    async def send(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MessageSendResponse:
        """
        Send an SMS through one eSIM

        Args:
          body: SMS body text (max 320 chars — smaller than the admin tier's cap; see the
              schema's own doc comment for why)

          to: Recipient phone number — normalized to E.164 (spaces/dashes/dots stripped);
              rejected with 400 if it doesn't validate as E.164 afterward.

          client_request_id: Client-supplied idempotency key, scoped to (owner, esimId, key). Replaying the
              same key + identical payload returns the original send; the same key with a
              DIFFERENT payload is a 409 conflict.

          delivery_report: Wait for physedge to confirm carrier delivery before completing the send (adds
              executor-side latency, never on this request — sends are always async/202).
              Defaults to false for the public tier (opt-in, unlike the admin tier's
              default-true).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
          raise ValueError(
            f'Expected a non-empty value for `id` but received {id!r}'
          )
        return await self._post(
            path_template("/numbers/esims/{id}/messages", id=id),
            body=await async_maybe_transform({
                "body": body,
                "to": to,
                "client_request_id": client_request_id,
                "delivery_report": delivery_report,
            }, message_send_params.MessageSendParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
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