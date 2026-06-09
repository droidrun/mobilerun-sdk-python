# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.agents import (
    FileListFilesResponse,
    FileMintUploadURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_files(self, client: Mobilerun) -> None:
        file = client.agents.files.list_files()
        assert_matches_type(FileListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_files_with_all_params(self, client: Mobilerun) -> None:
        file = client.agents.files.list_files(
            zone="user",
        )
        assert_matches_type(FileListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_files(self, client: Mobilerun) -> None:
        response = client.agents.files.with_raw_response.list_files()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_files(self, client: Mobilerun) -> None:
        with client.agents.files.with_streaming_response.list_files() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListFilesResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mint_upload_url(self, client: Mobilerun) -> None:
        file = client.agents.files.mint_upload_url(
            filename="x",
            mime_type="x",
            size_bytes=1,
        )
        assert_matches_type(FileMintUploadURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mint_upload_url_with_all_params(self, client: Mobilerun) -> None:
        file = client.agents.files.mint_upload_url(
            filename="x",
            mime_type="x",
            size_bytes=1,
            zone="user",
            idempotency_key="x",
        )
        assert_matches_type(FileMintUploadURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mint_upload_url(self, client: Mobilerun) -> None:
        response = client.agents.files.with_raw_response.mint_upload_url(
            filename="x",
            mime_type="x",
            size_bytes=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileMintUploadURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mint_upload_url(self, client: Mobilerun) -> None:
        with client.agents.files.with_streaming_response.mint_upload_url(
            filename="x",
            mime_type="x",
            size_bytes=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileMintUploadURLResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_files(self, async_client: AsyncMobilerun) -> None:
        file = await async_client.agents.files.list_files()
        assert_matches_type(FileListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_files_with_all_params(self, async_client: AsyncMobilerun) -> None:
        file = await async_client.agents.files.list_files(
            zone="user",
        )
        assert_matches_type(FileListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_files(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.files.with_raw_response.list_files()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListFilesResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_files(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.files.with_streaming_response.list_files() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListFilesResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mint_upload_url(self, async_client: AsyncMobilerun) -> None:
        file = await async_client.agents.files.mint_upload_url(
            filename="x",
            mime_type="x",
            size_bytes=1,
        )
        assert_matches_type(FileMintUploadURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mint_upload_url_with_all_params(self, async_client: AsyncMobilerun) -> None:
        file = await async_client.agents.files.mint_upload_url(
            filename="x",
            mime_type="x",
            size_bytes=1,
            zone="user",
            idempotency_key="x",
        )
        assert_matches_type(FileMintUploadURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mint_upload_url(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.files.with_raw_response.mint_upload_url(
            filename="x",
            mime_type="x",
            size_bytes=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileMintUploadURLResponse, file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mint_upload_url(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.files.with_streaming_response.mint_upload_url(
            filename="x",
            mime_type="x",
            size_bytes=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileMintUploadURLResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
