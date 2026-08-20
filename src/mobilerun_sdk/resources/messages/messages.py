# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import message_list_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .conversations import (
    ConversationsResource,
    AsyncConversationsResource,
    ConversationsResourceWithRawResponse,
    AsyncConversationsResourceWithRawResponse,
    ConversationsResourceWithStreamingResponse,
    AsyncConversationsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.message_list_response import MessageListResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def conversations(self) -> ConversationsResource:
        return ConversationsResource(self._client)

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
        *,
        direction: Literal["all", "inbound", "outbound"] | Omit = omit,
        esim_id: str | Omit = omit,
        number_id: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        peer_key: str | Omit = omit,
        peer_number: str | Omit = omit,
        status: Literal[
            "all", "received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """Lists the caller's own SMS messages, newest first.

        Supports filtering by
        direction, esimId, numberId, status, peerNumber (substring search, min 3
        characters), and peerKey (exact thread match). Each row includes its canonical
        thread key (`peerKey`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/numbers/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "esim_id": esim_id,
                        "number_id": number_id,
                        "page": page,
                        "page_size": page_size,
                        "peer_key": peer_key,
                        "peer_number": peer_number,
                        "status": status,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        return AsyncConversationsResource(self._client)

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
        *,
        direction: Literal["all", "inbound", "outbound"] | Omit = omit,
        esim_id: str | Omit = omit,
        number_id: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        peer_key: str | Omit = omit,
        peer_number: str | Omit = omit,
        status: Literal[
            "all", "received", "queued", "claimed", "sending", "sent", "sent_unconfirmed", "delivered", "failed"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """Lists the caller's own SMS messages, newest first.

        Supports filtering by
        direction, esimId, numberId, status, peerNumber (substring search, min 3
        characters), and peerKey (exact thread match). Each row includes its canonical
        thread key (`peerKey`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/numbers/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "esim_id": esim_id,
                        "number_id": number_id,
                        "page": page,
                        "page_size": page_size,
                        "peer_key": peer_key,
                        "peer_number": peer_number,
                        "status": status,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )

    @cached_property
    def conversations(self) -> ConversationsResourceWithRawResponse:
        return ConversationsResourceWithRawResponse(self._messages.conversations)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithRawResponse:
        return AsyncConversationsResourceWithRawResponse(self._messages.conversations)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )

    @cached_property
    def conversations(self) -> ConversationsResourceWithStreamingResponse:
        return ConversationsResourceWithStreamingResponse(self._messages.conversations)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithStreamingResponse:
        return AsyncConversationsResourceWithStreamingResponse(self._messages.conversations)
