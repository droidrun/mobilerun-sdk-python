# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.agents.files import (
    FileIDDeleteFileResponse,
    FileIDConfirmUploadResponse,
    FileIDUpdateMetadataResponse,
    FileIDCancelPendingUploadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFileID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_pending_upload(self, client: Mobilerun) -> None:
        file_id = client.agents.files.file_id.cancel_pending_upload()
        assert_matches_type(FileIDCancelPendingUploadResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_pending_upload(self, client: Mobilerun) -> None:
        response = client.agents.files.file_id.with_raw_response.cancel_pending_upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = response.parse()
        assert_matches_type(FileIDCancelPendingUploadResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_pending_upload(self, client: Mobilerun) -> None:
        with client.agents.files.file_id.with_streaming_response.cancel_pending_upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = response.parse()
            assert_matches_type(FileIDCancelPendingUploadResponse, file_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_confirm_upload(self, client: Mobilerun) -> None:
        file_id = client.agents.files.file_id.confirm_upload()
        assert_matches_type(FileIDConfirmUploadResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_confirm_upload(self, client: Mobilerun) -> None:
        response = client.agents.files.file_id.with_raw_response.confirm_upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = response.parse()
        assert_matches_type(FileIDConfirmUploadResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_confirm_upload(self, client: Mobilerun) -> None:
        with client.agents.files.file_id.with_streaming_response.confirm_upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = response.parse()
            assert_matches_type(FileIDConfirmUploadResponse, file_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_file(self, client: Mobilerun) -> None:
        file_id = client.agents.files.file_id.delete_file()
        assert_matches_type(FileIDDeleteFileResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_file(self, client: Mobilerun) -> None:
        response = client.agents.files.file_id.with_raw_response.delete_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = response.parse()
        assert_matches_type(FileIDDeleteFileResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_file(self, client: Mobilerun) -> None:
        with client.agents.files.file_id.with_streaming_response.delete_file() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = response.parse()
            assert_matches_type(FileIDDeleteFileResponse, file_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download_file(self, client: Mobilerun) -> None:
        file_id = client.agents.files.file_id.download_file()
        assert file_id is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download_file(self, client: Mobilerun) -> None:
        response = client.agents.files.file_id.with_raw_response.download_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = response.parse()
        assert file_id is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download_file(self, client: Mobilerun) -> None:
        with client.agents.files.file_id.with_streaming_response.download_file() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = response.parse()
            assert file_id is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_metadata(self, client: Mobilerun) -> None:
        file_id = client.agents.files.file_id.update_metadata()
        assert_matches_type(FileIDUpdateMetadataResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_metadata_with_all_params(self, client: Mobilerun) -> None:
        file_id = client.agents.files.file_id.update_metadata(
            display_name="x",
            enabled=True,
        )
        assert_matches_type(FileIDUpdateMetadataResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_metadata(self, client: Mobilerun) -> None:
        response = client.agents.files.file_id.with_raw_response.update_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = response.parse()
        assert_matches_type(FileIDUpdateMetadataResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_metadata(self, client: Mobilerun) -> None:
        with client.agents.files.file_id.with_streaming_response.update_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = response.parse()
            assert_matches_type(FileIDUpdateMetadataResponse, file_id, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFileID:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_pending_upload(self, async_client: AsyncMobilerun) -> None:
        file_id = await async_client.agents.files.file_id.cancel_pending_upload()
        assert_matches_type(FileIDCancelPendingUploadResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_pending_upload(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.files.file_id.with_raw_response.cancel_pending_upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = await response.parse()
        assert_matches_type(FileIDCancelPendingUploadResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_pending_upload(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.files.file_id.with_streaming_response.cancel_pending_upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = await response.parse()
            assert_matches_type(FileIDCancelPendingUploadResponse, file_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_confirm_upload(self, async_client: AsyncMobilerun) -> None:
        file_id = await async_client.agents.files.file_id.confirm_upload()
        assert_matches_type(FileIDConfirmUploadResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_confirm_upload(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.files.file_id.with_raw_response.confirm_upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = await response.parse()
        assert_matches_type(FileIDConfirmUploadResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_confirm_upload(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.files.file_id.with_streaming_response.confirm_upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = await response.parse()
            assert_matches_type(FileIDConfirmUploadResponse, file_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_file(self, async_client: AsyncMobilerun) -> None:
        file_id = await async_client.agents.files.file_id.delete_file()
        assert_matches_type(FileIDDeleteFileResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_file(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.files.file_id.with_raw_response.delete_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = await response.parse()
        assert_matches_type(FileIDDeleteFileResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_file(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.files.file_id.with_streaming_response.delete_file() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = await response.parse()
            assert_matches_type(FileIDDeleteFileResponse, file_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download_file(self, async_client: AsyncMobilerun) -> None:
        file_id = await async_client.agents.files.file_id.download_file()
        assert file_id is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download_file(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.files.file_id.with_raw_response.download_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = await response.parse()
        assert file_id is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download_file(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.files.file_id.with_streaming_response.download_file() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = await response.parse()
            assert file_id is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_metadata(self, async_client: AsyncMobilerun) -> None:
        file_id = await async_client.agents.files.file_id.update_metadata()
        assert_matches_type(FileIDUpdateMetadataResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_metadata_with_all_params(self, async_client: AsyncMobilerun) -> None:
        file_id = await async_client.agents.files.file_id.update_metadata(
            display_name="x",
            enabled=True,
        )
        assert_matches_type(FileIDUpdateMetadataResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_metadata(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.files.file_id.with_raw_response.update_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_id = await response.parse()
        assert_matches_type(FileIDUpdateMetadataResponse, file_id, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_metadata(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.files.file_id.with_streaming_response.update_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_id = await response.parse()
            assert_matches_type(FileIDUpdateMetadataResponse, file_id, path=["response"])

        assert cast(Any, response.is_closed) is True
