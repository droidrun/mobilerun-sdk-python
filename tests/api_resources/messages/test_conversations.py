# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from mobilerun_sdk.types.messages import ConversationListResponse, ConversationMarkReadResponse

from mobilerun_sdk._utils import parse_datetime

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types.messages import conversation_list_params
from mobilerun_sdk.types.messages import conversation_mark_read_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        conversation = client.messages.conversations.list()
        assert_matches_type(ConversationListResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        conversation = client.messages.conversations.list(
            cursor_last_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor_last_occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            esim_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationListResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:

        response = client.messages.conversations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        conversation = response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.messages.conversations.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            conversation = response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mark_read(self, client: Mobilerun) -> None:
        conversation = client.messages.conversations.mark_read(
            peer_key="x",
            up_to_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            up_to_occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConversationMarkReadResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mark_read(self, client: Mobilerun) -> None:

        response = client.messages.conversations.with_raw_response.mark_read(
            peer_key="x",
            up_to_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            up_to_occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        conversation = response.parse()
        assert_matches_type(ConversationMarkReadResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mark_read(self, client: Mobilerun) -> None:
        with client.messages.conversations.with_streaming_response.mark_read(
            peer_key="x",
            up_to_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            up_to_occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            conversation = response.parse()
            assert_matches_type(ConversationMarkReadResponse, conversation, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncConversations:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        conversation = await async_client.messages.conversations.list()
        assert_matches_type(ConversationListResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        conversation = await async_client.messages.conversations.list(
            cursor_last_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor_last_occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            esim_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationListResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.messages.conversations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        conversation = await response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.messages.conversations.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            conversation = await response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mark_read(self, async_client: AsyncMobilerun) -> None:
        conversation = await async_client.messages.conversations.mark_read(
            peer_key="x",
            up_to_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            up_to_occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ConversationMarkReadResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mark_read(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.messages.conversations.with_raw_response.mark_read(
            peer_key="x",
            up_to_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            up_to_occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        conversation = await response.parse()
        assert_matches_type(ConversationMarkReadResponse, conversation, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mark_read(self, async_client: AsyncMobilerun) -> None:
        async with async_client.messages.conversations.with_streaming_response.mark_read(
            peer_key="x",
            up_to_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            up_to_occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            conversation = await response.parse()
            assert_matches_type(ConversationMarkReadResponse, conversation, path=['response'])

        assert cast(Any, response.is_closed) is True