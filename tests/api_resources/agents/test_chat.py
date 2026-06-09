# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.agents import (
    ChatSendMessageResponse,
    ChatGetChatStateResponse,
    ChatRehydrateChatResponse,
    ChatDeliverPermissionResponse,
    ChatListSlashCommandsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deliver_permission(self, client: Mobilerun) -> None:
        chat = client.agents.chat.deliver_permission(
            permission_id="x",
            response="once",
        )
        assert_matches_type(ChatDeliverPermissionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deliver_permission(self, client: Mobilerun) -> None:
        response = client.agents.chat.with_raw_response.deliver_permission(
            permission_id="x",
            response="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatDeliverPermissionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deliver_permission(self, client: Mobilerun) -> None:
        with client.agents.chat.with_streaming_response.deliver_permission(
            permission_id="x",
            response="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatDeliverPermissionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_chat_state(self, client: Mobilerun) -> None:
        chat = client.agents.chat.get_chat_state()
        assert_matches_type(ChatGetChatStateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_chat_state(self, client: Mobilerun) -> None:
        response = client.agents.chat.with_raw_response.get_chat_state()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatGetChatStateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_chat_state(self, client: Mobilerun) -> None:
        with client.agents.chat.with_streaming_response.get_chat_state() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatGetChatStateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_slash_commands(self, client: Mobilerun) -> None:
        chat = client.agents.chat.list_slash_commands()
        assert_matches_type(ChatListSlashCommandsResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_slash_commands(self, client: Mobilerun) -> None:
        response = client.agents.chat.with_raw_response.list_slash_commands()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatListSlashCommandsResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_slash_commands(self, client: Mobilerun) -> None:
        with client.agents.chat.with_streaming_response.list_slash_commands() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatListSlashCommandsResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rehydrate_chat(self, client: Mobilerun) -> None:
        chat = client.agents.chat.rehydrate_chat()
        assert_matches_type(ChatRehydrateChatResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rehydrate_chat(self, client: Mobilerun) -> None:
        response = client.agents.chat.with_raw_response.rehydrate_chat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatRehydrateChatResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rehydrate_chat(self, client: Mobilerun) -> None:
        with client.agents.chat.with_streaming_response.rehydrate_chat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatRehydrateChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_message(self, client: Mobilerun) -> None:
        chat = client.agents.chat.send_message(
            message="x",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_message_with_all_params(self, client: Mobilerun) -> None:
        chat = client.agents.chat.send_message(
            message="x",
            agent="agent",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_message(self, client: Mobilerun) -> None:
        response = client.agents.chat.with_raw_response.send_message(
            message="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_message(self, client: Mobilerun) -> None:
        with client.agents.chat.with_streaming_response.send_message(
            message="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_prompt(self, client: Mobilerun) -> None:
        chat_stream = client.agents.chat.send_prompt(
            messages=[
                {
                    "id": "id",
                    "parts": [{"type": "type"}],
                    "role": "user",
                }
            ],
        )
        chat_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_prompt_with_all_params(self, client: Mobilerun) -> None:
        chat_stream = client.agents.chat.send_prompt(
            messages=[
                {
                    "id": "id",
                    "parts": [{"type": "type"}],
                    "role": "user",
                    "metadata": {"foo": "bar"},
                }
            ],
            id="id",
            agent="agent",
            context="x",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={"foo": "bar"},
            trigger="submit-message",
        )
        chat_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_prompt(self, client: Mobilerun) -> None:
        response = client.agents.chat.with_raw_response.send_prompt(
            messages=[
                {
                    "id": "id",
                    "parts": [{"type": "type"}],
                    "role": "user",
                }
            ],
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_prompt(self, client: Mobilerun) -> None:
        with client.agents.chat.with_streaming_response.send_prompt(
            messages=[
                {
                    "id": "id",
                    "parts": [{"type": "type"}],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_subscribe_events(self, client: Mobilerun) -> None:
        chat_stream = client.agents.chat.subscribe_events()
        chat_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_subscribe_events(self, client: Mobilerun) -> None:
        response = client.agents.chat.with_raw_response.subscribe_events()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_subscribe_events(self, client: Mobilerun) -> None:
        with client.agents.chat.with_streaming_response.subscribe_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deliver_permission(self, async_client: AsyncMobilerun) -> None:
        chat = await async_client.agents.chat.deliver_permission(
            permission_id="x",
            response="once",
        )
        assert_matches_type(ChatDeliverPermissionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deliver_permission(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.with_raw_response.deliver_permission(
            permission_id="x",
            response="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatDeliverPermissionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deliver_permission(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.with_streaming_response.deliver_permission(
            permission_id="x",
            response="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatDeliverPermissionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_chat_state(self, async_client: AsyncMobilerun) -> None:
        chat = await async_client.agents.chat.get_chat_state()
        assert_matches_type(ChatGetChatStateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_chat_state(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.with_raw_response.get_chat_state()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatGetChatStateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_chat_state(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.with_streaming_response.get_chat_state() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatGetChatStateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_slash_commands(self, async_client: AsyncMobilerun) -> None:
        chat = await async_client.agents.chat.list_slash_commands()
        assert_matches_type(ChatListSlashCommandsResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_slash_commands(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.with_raw_response.list_slash_commands()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatListSlashCommandsResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_slash_commands(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.with_streaming_response.list_slash_commands() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatListSlashCommandsResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rehydrate_chat(self, async_client: AsyncMobilerun) -> None:
        chat = await async_client.agents.chat.rehydrate_chat()
        assert_matches_type(ChatRehydrateChatResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rehydrate_chat(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.with_raw_response.rehydrate_chat()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatRehydrateChatResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rehydrate_chat(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.with_streaming_response.rehydrate_chat() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatRehydrateChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_message(self, async_client: AsyncMobilerun) -> None:
        chat = await async_client.agents.chat.send_message(
            message="x",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_message_with_all_params(self, async_client: AsyncMobilerun) -> None:
        chat = await async_client.agents.chat.send_message(
            message="x",
            agent="agent",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.with_raw_response.send_message(
            message="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.with_streaming_response.send_message(
            message="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_prompt(self, async_client: AsyncMobilerun) -> None:
        chat_stream = await async_client.agents.chat.send_prompt(
            messages=[
                {
                    "id": "id",
                    "parts": [{"type": "type"}],
                    "role": "user",
                }
            ],
        )
        await chat_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_prompt_with_all_params(self, async_client: AsyncMobilerun) -> None:
        chat_stream = await async_client.agents.chat.send_prompt(
            messages=[
                {
                    "id": "id",
                    "parts": [{"type": "type"}],
                    "role": "user",
                    "metadata": {"foo": "bar"},
                }
            ],
            id="id",
            agent="agent",
            context="x",
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={"foo": "bar"},
            trigger="submit-message",
        )
        await chat_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_prompt(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.with_raw_response.send_prompt(
            messages=[
                {
                    "id": "id",
                    "parts": [{"type": "type"}],
                    "role": "user",
                }
            ],
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_prompt(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.with_streaming_response.send_prompt(
            messages=[
                {
                    "id": "id",
                    "parts": [{"type": "type"}],
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_subscribe_events(self, async_client: AsyncMobilerun) -> None:
        chat_stream = await async_client.agents.chat.subscribe_events()
        await chat_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_subscribe_events(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.chat.with_raw_response.subscribe_events()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_subscribe_events(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.chat.with_streaming_response.subscribe_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
