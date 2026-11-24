# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types import (
    RoutineFileListResponse,
    RoutineFileDeleteManyResponse,
    RoutineFileListFoldersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutineFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        routine_file = client.routine_files.list()
        assert_matches_type(RoutineFileListResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        routine_file = client.routine_files.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            folder="x",
            page=1,
            page_size=1,
        )
        assert_matches_type(RoutineFileListResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.routine_files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = response.parse()
        assert_matches_type(RoutineFileListResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.routine_files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = response.parse()
            assert_matches_type(RoutineFileListResponse, routine_file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        routine_file = client.routine_files.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert routine_file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.routine_files.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = response.parse()
        assert routine_file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.routine_files.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = response.parse()
            assert routine_file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.routine_files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_many(self, client: Mobilerun) -> None:
        routine_file = client.routine_files.delete_many()
        assert_matches_type(RoutineFileDeleteManyResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_many_with_all_params(self, client: Mobilerun) -> None:
        routine_file = client.routine_files.delete_many(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            folder="x",
        )
        assert_matches_type(RoutineFileDeleteManyResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_many(self, client: Mobilerun) -> None:
        response = client.routine_files.with_raw_response.delete_many()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = response.parse()
        assert_matches_type(RoutineFileDeleteManyResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_many(self, client: Mobilerun) -> None:
        with client.routine_files.with_streaming_response.delete_many() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = response.parse()
            assert_matches_type(RoutineFileDeleteManyResponse, routine_file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download(self, client: Mobilerun) -> None:
        routine_file = client.routine_files.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert routine_file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download(self, client: Mobilerun) -> None:
        response = client.routine_files.with_raw_response.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = response.parse()
        assert routine_file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download(self, client: Mobilerun) -> None:
        with client.routine_files.with_streaming_response.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = response.parse()
            assert routine_file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_download(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.routine_files.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_folders(self, client: Mobilerun) -> None:
        routine_file = client.routine_files.list_folders()
        assert_matches_type(RoutineFileListFoldersResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_folders_with_all_params(self, client: Mobilerun) -> None:
        routine_file = client.routine_files.list_folders(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=1,
            page_size=1,
        )
        assert_matches_type(RoutineFileListFoldersResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_folders(self, client: Mobilerun) -> None:
        response = client.routine_files.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = response.parse()
        assert_matches_type(RoutineFileListFoldersResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_folders(self, client: Mobilerun) -> None:
        with client.routine_files.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = response.parse()
            assert_matches_type(RoutineFileListFoldersResponse, routine_file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoutineFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        routine_file = await async_client.routine_files.list()
        assert_matches_type(RoutineFileListResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        routine_file = await async_client.routine_files.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            folder="x",
            page=1,
            page_size=1,
        )
        assert_matches_type(RoutineFileListResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.routine_files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = await response.parse()
        assert_matches_type(RoutineFileListResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.routine_files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = await response.parse()
            assert_matches_type(RoutineFileListResponse, routine_file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        routine_file = await async_client.routine_files.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert routine_file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.routine_files.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = await response.parse()
        assert routine_file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.routine_files.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = await response.parse()
            assert routine_file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.routine_files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_many(self, async_client: AsyncMobilerun) -> None:
        routine_file = await async_client.routine_files.delete_many()
        assert_matches_type(RoutineFileDeleteManyResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_many_with_all_params(self, async_client: AsyncMobilerun) -> None:
        routine_file = await async_client.routine_files.delete_many(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            folder="x",
        )
        assert_matches_type(RoutineFileDeleteManyResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_many(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.routine_files.with_raw_response.delete_many()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = await response.parse()
        assert_matches_type(RoutineFileDeleteManyResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_many(self, async_client: AsyncMobilerun) -> None:
        async with async_client.routine_files.with_streaming_response.delete_many() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = await response.parse()
            assert_matches_type(RoutineFileDeleteManyResponse, routine_file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download(self, async_client: AsyncMobilerun) -> None:
        routine_file = await async_client.routine_files.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert routine_file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.routine_files.with_raw_response.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = await response.parse()
        assert routine_file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncMobilerun) -> None:
        async with async_client.routine_files.with_streaming_response.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = await response.parse()
            assert routine_file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_download(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.routine_files.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_folders(self, async_client: AsyncMobilerun) -> None:
        routine_file = await async_client.routine_files.list_folders()
        assert_matches_type(RoutineFileListFoldersResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_folders_with_all_params(self, async_client: AsyncMobilerun) -> None:
        routine_file = await async_client.routine_files.list_folders(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=1,
            page_size=1,
        )
        assert_matches_type(RoutineFileListFoldersResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_folders(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.routine_files.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine_file = await response.parse()
        assert_matches_type(RoutineFileListFoldersResponse, routine_file, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_folders(self, async_client: AsyncMobilerun) -> None:
        async with async_client.routine_files.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine_file = await response.parse()
            assert_matches_type(RoutineFileListFoldersResponse, routine_file, path=["response"])

        assert cast(Any, response.is_closed) is True
