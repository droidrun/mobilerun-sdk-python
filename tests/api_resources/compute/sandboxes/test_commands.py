# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.compute.sandboxes import CommandListResponse, CommandRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommands:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        command = client.compute.sandboxes.commands.retrieve(
            command_id="550e8400-e29b-41d4-a716-446655440000",
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CommandRetrieveResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Mobilerun) -> None:
        command = client.compute.sandboxes.commands.retrieve(
            command_id="550e8400-e29b-41d4-a716-446655440000",
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            wait_s=0,
        )
        assert_matches_type(CommandRetrieveResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.compute.sandboxes.commands.with_raw_response.retrieve(
            command_id="550e8400-e29b-41d4-a716-446655440000",
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(CommandRetrieveResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.compute.sandboxes.commands.with_streaming_response.retrieve(
            command_id="550e8400-e29b-41d4-a716-446655440000",
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(CommandRetrieveResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.compute.sandboxes.commands.with_raw_response.retrieve(
                command_id="550e8400-e29b-41d4-a716-446655440000",
                sandbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command_id` but received ''"):
            client.compute.sandboxes.commands.with_raw_response.retrieve(
                command_id="",
                sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        command = client.compute.sandboxes.commands.list(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CommandListResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.compute.sandboxes.commands.with_raw_response.list(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(CommandListResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.compute.sandboxes.commands.with_streaming_response.list(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(CommandListResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.compute.sandboxes.commands.with_raw_response.list(
                "",
            )


class TestAsyncCommands:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        command = await async_client.compute.sandboxes.commands.retrieve(
            command_id="550e8400-e29b-41d4-a716-446655440000",
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CommandRetrieveResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMobilerun) -> None:
        command = await async_client.compute.sandboxes.commands.retrieve(
            command_id="550e8400-e29b-41d4-a716-446655440000",
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            wait_s=0,
        )
        assert_matches_type(CommandRetrieveResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.compute.sandboxes.commands.with_raw_response.retrieve(
            command_id="550e8400-e29b-41d4-a716-446655440000",
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(CommandRetrieveResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.compute.sandboxes.commands.with_streaming_response.retrieve(
            command_id="550e8400-e29b-41d4-a716-446655440000",
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(CommandRetrieveResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.compute.sandboxes.commands.with_raw_response.retrieve(
                command_id="550e8400-e29b-41d4-a716-446655440000",
                sandbox_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command_id` but received ''"):
            await async_client.compute.sandboxes.commands.with_raw_response.retrieve(
                command_id="",
                sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        command = await async_client.compute.sandboxes.commands.list(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CommandListResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.compute.sandboxes.commands.with_raw_response.list(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(CommandListResponse, command, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.compute.sandboxes.commands.with_streaming_response.list(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(CommandListResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.compute.sandboxes.commands.with_raw_response.list(
                "",
            )
