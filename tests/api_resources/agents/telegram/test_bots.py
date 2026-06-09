# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.agents.telegram import BotListResponse, BotRevokeLinkResponse, BotRequestLinkResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        bot = client.agents.telegram.bots.list()
        assert_matches_type(BotListResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.agents.telegram.bots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(BotListResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.agents.telegram.bots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(BotListResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_link(self, client: Mobilerun) -> None:
        bot = client.agents.telegram.bots.request_link()
        assert_matches_type(BotRequestLinkResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_link(self, client: Mobilerun) -> None:
        response = client.agents.telegram.bots.with_raw_response.request_link()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(BotRequestLinkResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_link(self, client: Mobilerun) -> None:
        with client.agents.telegram.bots.with_streaming_response.request_link() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(BotRequestLinkResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke_link(self, client: Mobilerun) -> None:
        bot = client.agents.telegram.bots.revoke_link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BotRevokeLinkResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke_link(self, client: Mobilerun) -> None:
        response = client.agents.telegram.bots.with_raw_response.revoke_link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(BotRevokeLinkResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke_link(self, client: Mobilerun) -> None:
        with client.agents.telegram.bots.with_streaming_response.revoke_link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(BotRevokeLinkResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke_link(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.telegram.bots.with_raw_response.revoke_link(
                "",
            )


class TestAsyncBots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        bot = await async_client.agents.telegram.bots.list()
        assert_matches_type(BotListResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.telegram.bots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(BotListResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.telegram.bots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(BotListResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_link(self, async_client: AsyncMobilerun) -> None:
        bot = await async_client.agents.telegram.bots.request_link()
        assert_matches_type(BotRequestLinkResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_link(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.telegram.bots.with_raw_response.request_link()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(BotRequestLinkResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_link(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.telegram.bots.with_streaming_response.request_link() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(BotRequestLinkResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke_link(self, async_client: AsyncMobilerun) -> None:
        bot = await async_client.agents.telegram.bots.revoke_link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BotRevokeLinkResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke_link(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.telegram.bots.with_raw_response.revoke_link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(BotRevokeLinkResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke_link(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.telegram.bots.with_streaming_response.revoke_link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(BotRevokeLinkResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke_link(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.telegram.bots.with_raw_response.revoke_link(
                "",
            )
