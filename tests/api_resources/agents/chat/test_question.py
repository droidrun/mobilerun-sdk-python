# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.agents.chat import (
    QuestionDismissResponse,
    QuestionDeliverAnswerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuestion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deliver_answer(self, client: Mobilerun) -> None:
        question = client.agents.chat.question.deliver_answer(
            answers=[[{"label": "x"}]],
            question_id="x",
        )
        assert_matches_type(QuestionDeliverAnswerResponse, question, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deliver_answer(self, client: Mobilerun) -> None:
        response = client.agents.chat.question.with_raw_response.deliver_answer(
            answers=[[{"label": "x"}]],
            question_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = response.parse()
        assert_matches_type(QuestionDeliverAnswerResponse, question, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deliver_answer(self, client: Mobilerun) -> None:
        with client.agents.chat.question.with_streaming_response.deliver_answer(
            answers=[[{"label": "x"}]],
            question_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = response.parse()
            assert_matches_type(QuestionDeliverAnswerResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_dismiss(self, client: Mobilerun) -> None:
        question = client.agents.chat.question.dismiss(
            question_id="x",
        )
        assert_matches_type(QuestionDismissResponse, question, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_dismiss(self, client: Mobilerun) -> None:
        response = client.agents.chat.question.with_raw_response.dismiss(
            question_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = response.parse()
        assert_matches_type(QuestionDismissResponse, question, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_dismiss(self, client: Mobilerun) -> None:
        with client.agents.chat.question.with_streaming_response.dismiss(
            question_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = response.parse()
            assert_matches_type(QuestionDismissResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuestion:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deliver_answer(self, async_client: AsyncMobilerun) -> None:
        question = await async_client.agents.chat.question.deliver_answer(
            answers=[[{"label": "x"}]],
            question_id="x",
        )
        assert_matches_type(QuestionDeliverAnswerResponse, question, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deliver_answer(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.question.with_raw_response.deliver_answer(
            answers=[[{"label": "x"}]],
            question_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = await response.parse()
        assert_matches_type(QuestionDeliverAnswerResponse, question, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deliver_answer(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.question.with_streaming_response.deliver_answer(
            answers=[[{"label": "x"}]],
            question_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = await response.parse()
            assert_matches_type(QuestionDeliverAnswerResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_dismiss(self, async_client: AsyncMobilerun) -> None:
        question = await async_client.agents.chat.question.dismiss(
            question_id="x",
        )
        assert_matches_type(QuestionDismissResponse, question, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_dismiss(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.question.with_raw_response.dismiss(
            question_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = await response.parse()
        assert_matches_type(QuestionDismissResponse, question, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_dismiss(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.question.with_streaming_response.dismiss(
            question_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = await response.parse()
            assert_matches_type(QuestionDismissResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True
