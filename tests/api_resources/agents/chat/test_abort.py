# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.agents.chat import AbortPerformResponse, AbortForceClearResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAbort:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_force_clear(self, client: Mobilerun) -> None:
        abort = client.agents.chat.abort.force_clear()
        assert_matches_type(AbortForceClearResponse, abort, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_force_clear(self, client: Mobilerun) -> None:
        response = client.agents.chat.abort.with_raw_response.force_clear()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abort = response.parse()
        assert_matches_type(AbortForceClearResponse, abort, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_force_clear(self, client: Mobilerun) -> None:
        with client.agents.chat.abort.with_streaming_response.force_clear() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abort = response.parse()
            assert_matches_type(AbortForceClearResponse, abort, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_perform(self, client: Mobilerun) -> None:
        abort = client.agents.chat.abort.perform()
        assert_matches_type(AbortPerformResponse, abort, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_perform(self, client: Mobilerun) -> None:
        response = client.agents.chat.abort.with_raw_response.perform()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abort = response.parse()
        assert_matches_type(AbortPerformResponse, abort, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_perform(self, client: Mobilerun) -> None:
        with client.agents.chat.abort.with_streaming_response.perform() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abort = response.parse()
            assert_matches_type(AbortPerformResponse, abort, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAbort:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_force_clear(self, async_client: AsyncMobilerun) -> None:
        abort = await async_client.agents.chat.abort.force_clear()
        assert_matches_type(AbortForceClearResponse, abort, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_force_clear(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.abort.with_raw_response.force_clear()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abort = await response.parse()
        assert_matches_type(AbortForceClearResponse, abort, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_force_clear(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.abort.with_streaming_response.force_clear() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abort = await response.parse()
            assert_matches_type(AbortForceClearResponse, abort, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_perform(self, async_client: AsyncMobilerun) -> None:
        abort = await async_client.agents.chat.abort.perform()
        assert_matches_type(AbortPerformResponse, abort, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_perform(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.abort.with_raw_response.perform()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abort = await response.parse()
        assert_matches_type(AbortPerformResponse, abort, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_perform(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.abort.with_streaming_response.perform() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abort = await response.parse()
            assert_matches_type(AbortPerformResponse, abort, path=["response"])

        assert cast(Any, response.is_closed) is True
