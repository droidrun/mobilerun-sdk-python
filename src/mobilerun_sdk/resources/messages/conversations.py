# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ...types.messages.conversation_list_response import ConversationListResponse

from ..._base_client import make_request_options

from ..._utils import maybe_transform, async_maybe_transform

from ..._types import Omit, omit, NotGiven

from typing import Union

from datetime import datetime

from ...types.messages.conversation_mark_read_response import ConversationMarkReadResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.messages import conversation_list_params
from ...types.messages import conversation_mark_read_params

__all__ = ["ConversationsResource", "AsyncConversationsResource"]

class ConversationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def list(self,
    *,
    cursor_last_message_id: str | Omit = omit,
    cursor_last_occurred_at: Union[str, datetime] | Omit = omit,
    esim_id: str | Omit = omit,
    limit: int | Omit = omit,
    number_id: str | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ConversationListResponse:
        """Lists the caller's own SMS conversations, one row per thread.

        Each row includes
        the most recent message in the thread, its unread inbound count, and the eSIMs
        it was seen through. Optional `esimId` or `numberId` narrows to threads on one
        eSIM or number.

        Cursor-paginated via `limit` (default 20, max 100) and
        `cursorLastOccurredAt`/`cursorLastMessageId` (both required together, taken from
        a previous page's `nextCursor`). Pagination follows each thread's most recent
        activity rather than a fixed snapshot, so a thread with new activity can move
        ahead of an in-progress page fetch. Clients that need a stable ordering should
        snapshot their own view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/numbers/messages/conversations",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "cursor_last_message_id": cursor_last_message_id,
                "cursor_last_occurred_at": cursor_last_occurred_at,
                "esim_id": esim_id,
                "limit": limit,
                "number_id": number_id,
            }, conversation_list_params.ConversationListParams)),
            cast_to=ConversationListResponse,
        )

    def mark_read(self,
    *,
    peer_key: str,
    up_to_message_id: str,
    up_to_occurred_at: Union[str, datetime],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ConversationMarkReadResponse:
        """
        Marks the caller's own inbound messages in a conversation thread as read, up to
        and including the given `(upToOccurredAt, upToMessageId)` cursor — typically a
        conversation row's `lastMessage`. Idempotent: repeating the call with the same
        cursor updates 0 rows. Returns the number of rows updated.

        Args:
          peer_key: The thread's canonical peer key (see GET .../conversations)

          up_to_occurred_at: Mark inbound messages read up to (and including) this occurredAt/upToMessageId
              cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/numbers/messages/conversations/read",
            body=maybe_transform({
                "peer_key": peer_key,
                "up_to_message_id": up_to_message_id,
                "up_to_occurred_at": up_to_occurred_at,
            }, conversation_mark_read_params.ConversationMarkReadParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ConversationMarkReadResponse,
        )

class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def list(self,
    *,
    cursor_last_message_id: str | Omit = omit,
    cursor_last_occurred_at: Union[str, datetime] | Omit = omit,
    esim_id: str | Omit = omit,
    limit: int | Omit = omit,
    number_id: str | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ConversationListResponse:
        """Lists the caller's own SMS conversations, one row per thread.

        Each row includes
        the most recent message in the thread, its unread inbound count, and the eSIMs
        it was seen through. Optional `esimId` or `numberId` narrows to threads on one
        eSIM or number.

        Cursor-paginated via `limit` (default 20, max 100) and
        `cursorLastOccurredAt`/`cursorLastMessageId` (both required together, taken from
        a previous page's `nextCursor`). Pagination follows each thread's most recent
        activity rather than a fixed snapshot, so a thread with new activity can move
        ahead of an in-progress page fetch. Clients that need a stable ordering should
        snapshot their own view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/numbers/messages/conversations",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "cursor_last_message_id": cursor_last_message_id,
                "cursor_last_occurred_at": cursor_last_occurred_at,
                "esim_id": esim_id,
                "limit": limit,
                "number_id": number_id,
            }, conversation_list_params.ConversationListParams)),
            cast_to=ConversationListResponse,
        )

    async def mark_read(self,
    *,
    peer_key: str,
    up_to_message_id: str,
    up_to_occurred_at: Union[str, datetime],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ConversationMarkReadResponse:
        """
        Marks the caller's own inbound messages in a conversation thread as read, up to
        and including the given `(upToOccurredAt, upToMessageId)` cursor — typically a
        conversation row's `lastMessage`. Idempotent: repeating the call with the same
        cursor updates 0 rows. Returns the number of rows updated.

        Args:
          peer_key: The thread's canonical peer key (see GET .../conversations)

          up_to_occurred_at: Mark inbound messages read up to (and including) this occurredAt/upToMessageId
              cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/numbers/messages/conversations/read",
            body=await async_maybe_transform({
                "peer_key": peer_key,
                "up_to_message_id": up_to_message_id,
                "up_to_occurred_at": up_to_occurred_at,
            }, conversation_mark_read_params.ConversationMarkReadParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ConversationMarkReadResponse,
        )

class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.list = to_raw_response_wrapper(
            conversations.list,
        )
        self.mark_read = to_raw_response_wrapper(
            conversations.mark_read,
        )

class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.list = async_to_raw_response_wrapper(
            conversations.list,
        )
        self.mark_read = async_to_raw_response_wrapper(
            conversations.mark_read,
        )

class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.list = to_streamed_response_wrapper(
            conversations.list,
        )
        self.mark_read = to_streamed_response_wrapper(
            conversations.mark_read,
        )

class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.list = async_to_streamed_response_wrapper(
            conversations.list,
        )
        self.mark_read = async_to_streamed_response_wrapper(
            conversations.mark_read,
        )