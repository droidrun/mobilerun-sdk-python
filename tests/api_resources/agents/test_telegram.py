# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mobilerun_sdk import Mobilerun, AsyncMobilerun

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelegram:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_receive_update(self, client: Mobilerun) -> None:
        telegram = client.agents.telegram.receive_update(
            update_id=0,
        )
        assert telegram is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_receive_update_with_all_params(self, client: Mobilerun) -> None:
        telegram = client.agents.telegram.receive_update(
            update_id=0,
            message={
                "chat": {
                    "id": 0,
                    "type": "type",
                },
                "message_id": 0,
                "caption": "caption",
                "from": {
                    "id": 0,
                    "first_name": "first_name",
                    "is_bot": True,
                    "username": "username",
                },
                "text": "text",
            },
        )
        assert telegram is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_receive_update(self, client: Mobilerun) -> None:
        response = client.agents.telegram.with_raw_response.receive_update(
            update_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telegram = response.parse()
        assert telegram is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_receive_update(self, client: Mobilerun) -> None:
        with client.agents.telegram.with_streaming_response.receive_update(
            update_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telegram = response.parse()
            assert telegram is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTelegram:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_receive_update(self, async_client: AsyncMobilerun) -> None:
        telegram = await async_client.agents.telegram.receive_update(
            update_id=0,
        )
        assert telegram is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_receive_update_with_all_params(self, async_client: AsyncMobilerun) -> None:
        telegram = await async_client.agents.telegram.receive_update(
            update_id=0,
            message={
                "chat": {
                    "id": 0,
                    "type": "type",
                },
                "message_id": 0,
                "caption": "caption",
                "from": {
                    "id": 0,
                    "first_name": "first_name",
                    "is_bot": True,
                    "username": "username",
                },
                "text": "text",
            },
        )
        assert telegram is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_receive_update(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.telegram.with_raw_response.receive_update(
            update_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telegram = await response.parse()
        assert telegram is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_receive_update(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.telegram.with_streaming_response.receive_update(
            update_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telegram = await response.parse()
            assert telegram is None

        assert cast(Any, response.is_closed) is True
