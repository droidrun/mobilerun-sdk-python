# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.assistant import (
    conversation_list_params,
    conversation_send_params,
    conversation_abort_params,
    conversation_create_params,
    conversation_stream_params,
    conversation_update_params,
    conversation_history_params,
    conversation_answer_question_params,
    conversation_reject_question_params,
    conversation_answer_permission_params,
)
from ...types.assistant.conversation_list_response import ConversationListResponse
from ...types.assistant.conversation_send_response import ConversationSendResponse
from ...types.assistant.conversation_abort_response import ConversationAbortResponse
from ...types.assistant.conversation_create_response import ConversationCreateResponse
from ...types.assistant.conversation_stream_response import ConversationStreamResponse
from ...types.assistant.conversation_update_response import ConversationUpdateResponse
from ...types.assistant.conversation_history_response import ConversationHistoryResponse
from ...types.assistant.conversation_answer_question_response import ConversationAnswerQuestionResponse
from ...types.assistant.conversation_reject_question_response import ConversationRejectQuestionResponse
from ...types.assistant.conversation_answer_permission_response import ConversationAnswerPermissionResponse

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

    def create(
        self,
        *,
        title: str,
        agent: str | Omit = omit,
        description: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationCreateResponse:
        """Creates a titled agent session.

        Setup may occur on the first prompt. Idempotent
        via the `Idempotency-Key` header — a duplicate submit by the same authenticated
        caller within the 24-hour idempotency window returns the already-created session
        instead of a second one.

        Args:
          idempotency_key: Optional client key. Reusing the same key with the same request body by the same
              authenticated caller within 24 hours returns the already-created session instead
              of a second one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/assistant/chat/sessions",
            body=maybe_transform(
                {
                    "title": title,
                    "agent": agent,
                    "description": description,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        pinned: bool | Omit = omit,
        status: Literal["active", "archived"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationUpdateResponse:
        """Rename, change status, and/or pin.

        Title updates apply best-effort. Archiving
        always clears the pinned flag. `title` is rejected with 409
        `code: "session_title_managed_by_workflow"` when this chat is bound to a
        workflow — a bound chat's title is managed by the workflow. Other fields
        (description, status, pinned) remain updateable; archiving a bound chat stays
        allowed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/assistant/chat/sessions/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "pinned": pinned,
                    "status": status,
                    "title": title,
                },
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationUpdateResponse,
        )

    def list(
        self,
        *,
        kind: Literal["chat", "agent_workflow"] | Omit = omit,
        mine: Literal["true", "false"] | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """
        Default (`kind` absent or `chat`): active named chat sessions, pinned first then
        most recent activity — `workflowId` must be absent, or the request 400s.
        `mine=true` (only valid with `kind=chat`) narrows to sessions the caller
        created. `kind=agent_workflow`: workflow-linked sessions for one workflow
        (`workflowId` required, or the request 400s), no status filter, newest episode
        first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/assistant/chat/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "kind": kind,
                        "mine": mine,
                        "workflow_id": workflow_id,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    def abort(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationAbortResponse:
        """Abort the in-flight chat turn owned by `sessionId`.

        Idempotent. A turn owned by
        a different session is left untouched (204).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/assistant/chat/abort",
            body=maybe_transform({"session_id": session_id}, conversation_abort_params.ConversationAbortParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationAbortResponse,
        )

    def answer_permission(
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
    ) -> ConversationAnswerPermissionResponse:
        """
        Deliver a HITL approval/rejection for an in-flight turn.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/assistant/chat/permission",
            body=maybe_transform(
                {
                    "permission_id": permission_id,
                    "response": response,
                },
                conversation_answer_permission_params.ConversationAnswerPermissionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationAnswerPermissionResponse,
        )

    def answer_question(
        self,
        *,
        answers: Iterable[Iterable[conversation_answer_question_params.Answer]],
        question_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationAnswerQuestionResponse:
        """Deliver the user's answers to the agent's pending question for an in-flight
        turn.

        Idempotent via the `idempotency-key` header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/assistant/chat/question",
            body=maybe_transform(
                {
                    "answers": answers,
                    "question_id": question_id,
                },
                conversation_answer_question_params.ConversationAnswerQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationAnswerQuestionResponse,
        )

    def history(
        self,
        *,
        session_id: str,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationHistoryResponse:
        """Return the user's chat history for the given session.

        History remains readable
        after the session is no longer active.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/assistant/chat/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "session_id": session_id,
                        "limit": limit,
                    },
                    conversation_history_params.ConversationHistoryParams,
                ),
            ),
            cast_to=ConversationHistoryResponse,
        )

    def reject_question(
        self,
        *,
        question_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationRejectQuestionResponse:
        """Dismiss the agent's pending question.

        Already-resolved questions return 200
        (no-op) so multi-tab dismiss stays idempotent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/assistant/chat/question/reject",
            body=maybe_transform(
                {"question_id": question_id}, conversation_reject_question_params.ConversationRejectQuestionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRejectQuestionResponse,
        )

    def send(
        self,
        *,
        message: str,
        session_id: str,
        agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationSendResponse:
        """Send a single user message.

        The response format follows the Accept header:
        `text/event-stream` for SSE, `application/json` for a buffered assistant reply.
        `sessionId` targets a concrete active chat. The resolved chat session ID is
        returned as `chatSessionId` in the JSON body and as the `X-Chat-Session-Id`
        response header on the SSE response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/assistant/chat/message",
            body=maybe_transform(
                {
                    "message": message,
                    "session_id": session_id,
                    "agent": agent,
                },
                conversation_send_params.ConversationSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationSendResponse,
        )

    def stream(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ConversationStreamResponse]:
        """Reconnect to the in-flight turn stream.

        Replays buffered events from the start
        of the active turn, then continues live until the turn finishes. Responds 204
        when no active turn exists for the requested session. Upstream streaming
        failures return a retryable 503 with `Retry-After`. Resume is best-effort. Does
        not start an inactive session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            "/assistant/chat/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"session_id": session_id}, conversation_stream_params.ConversationStreamParams),
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[ConversationStreamResponse],
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

    async def create(
        self,
        *,
        title: str,
        agent: str | Omit = omit,
        description: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationCreateResponse:
        """Creates a titled agent session.

        Setup may occur on the first prompt. Idempotent
        via the `Idempotency-Key` header — a duplicate submit by the same authenticated
        caller within the 24-hour idempotency window returns the already-created session
        instead of a second one.

        Args:
          idempotency_key: Optional client key. Reusing the same key with the same request body by the same
              authenticated caller within 24 hours returns the already-created session instead
              of a second one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/assistant/chat/sessions",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "agent": agent,
                    "description": description,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        pinned: bool | Omit = omit,
        status: Literal["active", "archived"] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationUpdateResponse:
        """Rename, change status, and/or pin.

        Title updates apply best-effort. Archiving
        always clears the pinned flag. `title` is rejected with 409
        `code: "session_title_managed_by_workflow"` when this chat is bound to a
        workflow — a bound chat's title is managed by the workflow. Other fields
        (description, status, pinned) remain updateable; archiving a bound chat stays
        allowed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/assistant/chat/sessions/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "pinned": pinned,
                    "status": status,
                    "title": title,
                },
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationUpdateResponse,
        )

    async def list(
        self,
        *,
        kind: Literal["chat", "agent_workflow"] | Omit = omit,
        mine: Literal["true", "false"] | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """
        Default (`kind` absent or `chat`): active named chat sessions, pinned first then
        most recent activity — `workflowId` must be absent, or the request 400s.
        `mine=true` (only valid with `kind=chat`) narrows to sessions the caller
        created. `kind=agent_workflow`: workflow-linked sessions for one workflow
        (`workflowId` required, or the request 400s), no status filter, newest episode
        first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/assistant/chat/sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "kind": kind,
                        "mine": mine,
                        "workflow_id": workflow_id,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    async def abort(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationAbortResponse:
        """Abort the in-flight chat turn owned by `sessionId`.

        Idempotent. A turn owned by
        a different session is left untouched (204).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/assistant/chat/abort",
            body=await async_maybe_transform(
                {"session_id": session_id}, conversation_abort_params.ConversationAbortParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationAbortResponse,
        )

    async def answer_permission(
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
    ) -> ConversationAnswerPermissionResponse:
        """
        Deliver a HITL approval/rejection for an in-flight turn.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/assistant/chat/permission",
            body=await async_maybe_transform(
                {
                    "permission_id": permission_id,
                    "response": response,
                },
                conversation_answer_permission_params.ConversationAnswerPermissionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationAnswerPermissionResponse,
        )

    async def answer_question(
        self,
        *,
        answers: Iterable[Iterable[conversation_answer_question_params.Answer]],
        question_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationAnswerQuestionResponse:
        """Deliver the user's answers to the agent's pending question for an in-flight
        turn.

        Idempotent via the `idempotency-key` header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/assistant/chat/question",
            body=await async_maybe_transform(
                {
                    "answers": answers,
                    "question_id": question_id,
                },
                conversation_answer_question_params.ConversationAnswerQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationAnswerQuestionResponse,
        )

    async def history(
        self,
        *,
        session_id: str,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationHistoryResponse:
        """Return the user's chat history for the given session.

        History remains readable
        after the session is no longer active.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/assistant/chat/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "session_id": session_id,
                        "limit": limit,
                    },
                    conversation_history_params.ConversationHistoryParams,
                ),
            ),
            cast_to=ConversationHistoryResponse,
        )

    async def reject_question(
        self,
        *,
        question_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationRejectQuestionResponse:
        """Dismiss the agent's pending question.

        Already-resolved questions return 200
        (no-op) so multi-tab dismiss stays idempotent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/assistant/chat/question/reject",
            body=await async_maybe_transform(
                {"question_id": question_id}, conversation_reject_question_params.ConversationRejectQuestionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRejectQuestionResponse,
        )

    async def send(
        self,
        *,
        message: str,
        session_id: str,
        agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationSendResponse:
        """Send a single user message.

        The response format follows the Accept header:
        `text/event-stream` for SSE, `application/json` for a buffered assistant reply.
        `sessionId` targets a concrete active chat. The resolved chat session ID is
        returned as `chatSessionId` in the JSON body and as the `X-Chat-Session-Id`
        response header on the SSE response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/assistant/chat/message",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "session_id": session_id,
                    "agent": agent,
                },
                conversation_send_params.ConversationSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationSendResponse,
        )

    async def stream(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ConversationStreamResponse]:
        """Reconnect to the in-flight turn stream.

        Replays buffered events from the start
        of the active turn, then continues live until the turn finishes. Responds 204
        when no active turn exists for the requested session. Upstream streaming
        failures return a retryable 503 with `Retry-After`. Resume is best-effort. Does
        not start an inactive session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            "/assistant/chat/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"session_id": session_id}, conversation_stream_params.ConversationStreamParams
                ),
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[ConversationStreamResponse],
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_raw_response_wrapper(
            conversations.create,
        )
        self.update = to_raw_response_wrapper(
            conversations.update,
        )
        self.list = to_raw_response_wrapper(
            conversations.list,
        )
        self.abort = to_raw_response_wrapper(
            conversations.abort,
        )
        self.answer_permission = to_raw_response_wrapper(
            conversations.answer_permission,
        )
        self.answer_question = to_raw_response_wrapper(
            conversations.answer_question,
        )
        self.history = to_raw_response_wrapper(
            conversations.history,
        )
        self.reject_question = to_raw_response_wrapper(
            conversations.reject_question,
        )
        self.send = to_raw_response_wrapper(
            conversations.send,
        )
        self.stream = to_raw_response_wrapper(
            conversations.stream,
        )


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_raw_response_wrapper(
            conversations.create,
        )
        self.update = async_to_raw_response_wrapper(
            conversations.update,
        )
        self.list = async_to_raw_response_wrapper(
            conversations.list,
        )
        self.abort = async_to_raw_response_wrapper(
            conversations.abort,
        )
        self.answer_permission = async_to_raw_response_wrapper(
            conversations.answer_permission,
        )
        self.answer_question = async_to_raw_response_wrapper(
            conversations.answer_question,
        )
        self.history = async_to_raw_response_wrapper(
            conversations.history,
        )
        self.reject_question = async_to_raw_response_wrapper(
            conversations.reject_question,
        )
        self.send = async_to_raw_response_wrapper(
            conversations.send,
        )
        self.stream = async_to_raw_response_wrapper(
            conversations.stream,
        )


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_streamed_response_wrapper(
            conversations.create,
        )
        self.update = to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = to_streamed_response_wrapper(
            conversations.list,
        )
        self.abort = to_streamed_response_wrapper(
            conversations.abort,
        )
        self.answer_permission = to_streamed_response_wrapper(
            conversations.answer_permission,
        )
        self.answer_question = to_streamed_response_wrapper(
            conversations.answer_question,
        )
        self.history = to_streamed_response_wrapper(
            conversations.history,
        )
        self.reject_question = to_streamed_response_wrapper(
            conversations.reject_question,
        )
        self.send = to_streamed_response_wrapper(
            conversations.send,
        )
        self.stream = to_streamed_response_wrapper(
            conversations.stream,
        )


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_streamed_response_wrapper(
            conversations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            conversations.list,
        )
        self.abort = async_to_streamed_response_wrapper(
            conversations.abort,
        )
        self.answer_permission = async_to_streamed_response_wrapper(
            conversations.answer_permission,
        )
        self.answer_question = async_to_streamed_response_wrapper(
            conversations.answer_question,
        )
        self.history = async_to_streamed_response_wrapper(
            conversations.history,
        )
        self.reject_question = async_to_streamed_response_wrapper(
            conversations.reject_question,
        )
        self.send = async_to_streamed_response_wrapper(
            conversations.send,
        )
        self.stream = async_to_streamed_response_wrapper(
            conversations.stream,
        )
