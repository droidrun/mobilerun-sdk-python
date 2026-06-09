# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .abort import (
    AbortResource,
    AsyncAbortResource,
    AbortResourceWithRawResponse,
    AsyncAbortResourceWithRawResponse,
    AbortResourceWithStreamingResponse,
    AsyncAbortResourceWithStreamingResponse,
)
from .question import (
    QuestionResource,
    AsyncQuestionResource,
    QuestionResourceWithRawResponse,
    AsyncQuestionResourceWithRawResponse,
    QuestionResourceWithStreamingResponse,
    AsyncQuestionResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents import chat_deliver_permission_params
from ....types.agents.chat_get_chat_state_response import ChatGetChatStateResponse
from ....types.agents.chat_rehydrate_chat_response import ChatRehydrateChatResponse
from ....types.agents.chat_deliver_permission_response import ChatDeliverPermissionResponse
from ....types.agents.chat_list_slash_commands_response import ChatListSlashCommandsResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def abort(self) -> AbortResource:
        return AbortResource(self._client)

    @cached_property
    def question(self) -> QuestionResource:
        return QuestionResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def deliver_permission(
        self,
        *,
        permission_id: str,
        response: Literal["once", "always", "reject"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatDeliverPermissionResponse:
        """
        Deliver a HITL approval/rejection for an in-flight turn.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents/chat/permission",
            body=maybe_transform(
                {
                    "permission_id": permission_id,
                    "response": response,
                },
                chat_deliver_permission_params.ChatDeliverPermissionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeliverPermissionResponse,
        )

    def get_chat_state(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGetChatStateResponse:
        """Advisory snapshot of in-flight activity for the caller.

        Returns boolean flags
        for an interactive chat turn, a background workflow run, and a pending graceful
        abort. Intended for FE UI before deciding to invoke /chat/abort/force.
        """
        return self._get(
            "/agents/chat/state",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGetChatStateResponse,
        )

    def list_slash_commands(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListSlashCommandsResponse:
        """List the chat slash-command catalog."""
        return self._get(
            "/agents/chat/slash-commands",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListSlashCommandsResponse,
        )

    def rehydrate_chat(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatRehydrateChatResponse:
        """Rehydrate the user's chat history. Does not wake a hibernated machine."""
        return self._get(
            "/agents/chat/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRehydrateChatResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def abort(self) -> AsyncAbortResource:
        return AsyncAbortResource(self._client)

    @cached_property
    def question(self) -> AsyncQuestionResource:
        return AsyncQuestionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def deliver_permission(
        self,
        *,
        permission_id: str,
        response: Literal["once", "always", "reject"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatDeliverPermissionResponse:
        """
        Deliver a HITL approval/rejection for an in-flight turn.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents/chat/permission",
            body=await async_maybe_transform(
                {
                    "permission_id": permission_id,
                    "response": response,
                },
                chat_deliver_permission_params.ChatDeliverPermissionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatDeliverPermissionResponse,
        )

    async def get_chat_state(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGetChatStateResponse:
        """Advisory snapshot of in-flight activity for the caller.

        Returns boolean flags
        for an interactive chat turn, a background workflow run, and a pending graceful
        abort. Intended for FE UI before deciding to invoke /chat/abort/force.
        """
        return await self._get(
            "/agents/chat/state",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGetChatStateResponse,
        )

    async def list_slash_commands(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListSlashCommandsResponse:
        """List the chat slash-command catalog."""
        return await self._get(
            "/agents/chat/slash-commands",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListSlashCommandsResponse,
        )

    async def rehydrate_chat(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatRehydrateChatResponse:
        """Rehydrate the user's chat history. Does not wake a hibernated machine."""
        return await self._get(
            "/agents/chat/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatRehydrateChatResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.deliver_permission = to_raw_response_wrapper(
            chat.deliver_permission,
        )
        self.get_chat_state = to_raw_response_wrapper(
            chat.get_chat_state,
        )
        self.list_slash_commands = to_raw_response_wrapper(
            chat.list_slash_commands,
        )
        self.rehydrate_chat = to_raw_response_wrapper(
            chat.rehydrate_chat,
        )

    @cached_property
    def abort(self) -> AbortResourceWithRawResponse:
        return AbortResourceWithRawResponse(self._chat.abort)

    @cached_property
    def question(self) -> QuestionResourceWithRawResponse:
        return QuestionResourceWithRawResponse(self._chat.question)


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.deliver_permission = async_to_raw_response_wrapper(
            chat.deliver_permission,
        )
        self.get_chat_state = async_to_raw_response_wrapper(
            chat.get_chat_state,
        )
        self.list_slash_commands = async_to_raw_response_wrapper(
            chat.list_slash_commands,
        )
        self.rehydrate_chat = async_to_raw_response_wrapper(
            chat.rehydrate_chat,
        )

    @cached_property
    def abort(self) -> AsyncAbortResourceWithRawResponse:
        return AsyncAbortResourceWithRawResponse(self._chat.abort)

    @cached_property
    def question(self) -> AsyncQuestionResourceWithRawResponse:
        return AsyncQuestionResourceWithRawResponse(self._chat.question)


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.deliver_permission = to_streamed_response_wrapper(
            chat.deliver_permission,
        )
        self.get_chat_state = to_streamed_response_wrapper(
            chat.get_chat_state,
        )
        self.list_slash_commands = to_streamed_response_wrapper(
            chat.list_slash_commands,
        )
        self.rehydrate_chat = to_streamed_response_wrapper(
            chat.rehydrate_chat,
        )

    @cached_property
    def abort(self) -> AbortResourceWithStreamingResponse:
        return AbortResourceWithStreamingResponse(self._chat.abort)

    @cached_property
    def question(self) -> QuestionResourceWithStreamingResponse:
        return QuestionResourceWithStreamingResponse(self._chat.question)


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.deliver_permission = async_to_streamed_response_wrapper(
            chat.deliver_permission,
        )
        self.get_chat_state = async_to_streamed_response_wrapper(
            chat.get_chat_state,
        )
        self.list_slash_commands = async_to_streamed_response_wrapper(
            chat.list_slash_commands,
        )
        self.rehydrate_chat = async_to_streamed_response_wrapper(
            chat.rehydrate_chat,
        )

    @cached_property
    def abort(self) -> AsyncAbortResourceWithStreamingResponse:
        return AsyncAbortResourceWithStreamingResponse(self._chat.abort)

    @cached_property
    def question(self) -> AsyncQuestionResourceWithStreamingResponse:
        return AsyncQuestionResourceWithStreamingResponse(self._chat.question)
