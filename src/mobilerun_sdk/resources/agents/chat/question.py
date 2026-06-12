# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

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
from ....types.agents.chat import question_dismiss_params, question_deliver_answer_params
from ....types.agents.chat.question_dismiss_response import QuestionDismissResponse
from ....types.agents.chat.question_deliver_answer_response import QuestionDeliverAnswerResponse

__all__ = ["QuestionResource", "AsyncQuestionResource"]


class QuestionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuestionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return QuestionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuestionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return QuestionResourceWithStreamingResponse(self)

    def deliver_answer(
        self,
        *,
        answers: Iterable[Iterable[question_deliver_answer_params.Answer]],
        question_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuestionDeliverAnswerResponse:
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
            "/agents/chat/question",
            body=maybe_transform(
                {
                    "answers": answers,
                    "question_id": question_id,
                },
                question_deliver_answer_params.QuestionDeliverAnswerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuestionDeliverAnswerResponse,
        )

    def dismiss(
        self,
        *,
        question_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuestionDismissResponse:
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
            "/agents/chat/question/reject",
            body=maybe_transform({"question_id": question_id}, question_dismiss_params.QuestionDismissParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuestionDismissResponse,
        )


class AsyncQuestionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuestionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuestionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuestionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncQuestionResourceWithStreamingResponse(self)

    async def deliver_answer(
        self,
        *,
        answers: Iterable[Iterable[question_deliver_answer_params.Answer]],
        question_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuestionDeliverAnswerResponse:
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
            "/agents/chat/question",
            body=await async_maybe_transform(
                {
                    "answers": answers,
                    "question_id": question_id,
                },
                question_deliver_answer_params.QuestionDeliverAnswerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuestionDeliverAnswerResponse,
        )

    async def dismiss(
        self,
        *,
        question_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuestionDismissResponse:
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
            "/agents/chat/question/reject",
            body=await async_maybe_transform(
                {"question_id": question_id}, question_dismiss_params.QuestionDismissParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuestionDismissResponse,
        )


class QuestionResourceWithRawResponse:
    def __init__(self, question: QuestionResource) -> None:
        self._question = question

        self.deliver_answer = to_raw_response_wrapper(
            question.deliver_answer,
        )
        self.dismiss = to_raw_response_wrapper(
            question.dismiss,
        )


class AsyncQuestionResourceWithRawResponse:
    def __init__(self, question: AsyncQuestionResource) -> None:
        self._question = question

        self.deliver_answer = async_to_raw_response_wrapper(
            question.deliver_answer,
        )
        self.dismiss = async_to_raw_response_wrapper(
            question.dismiss,
        )


class QuestionResourceWithStreamingResponse:
    def __init__(self, question: QuestionResource) -> None:
        self._question = question

        self.deliver_answer = to_streamed_response_wrapper(
            question.deliver_answer,
        )
        self.dismiss = to_streamed_response_wrapper(
            question.dismiss,
        )


class AsyncQuestionResourceWithStreamingResponse:
    def __init__(self, question: AsyncQuestionResource) -> None:
        self._question = question

        self.deliver_answer = async_to_streamed_response_wrapper(
            question.deliver_answer,
        )
        self.dismiss = async_to_streamed_response_wrapper(
            question.dismiss,
        )
