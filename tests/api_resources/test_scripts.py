# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types import (
    ScriptListResponse,
    ScriptCreateResponse,
    ScriptSourceResponse,
    ScriptRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScripts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        script = client.scripts.create(
            name="x",
            source="x",
        )
        assert_matches_type(ScriptCreateResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        script = client.scripts.create(
            name="x",
            source="x",
            description="description",
            manifest={
                "credentials": [
                    {
                        "name": "x",
                        "package_name": "x",
                    }
                ],
                "hosts": ["string"],
                "scopes": ["_lk___klzn__.____uu"],
            },
        )
        assert_matches_type(ScriptCreateResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.scripts.with_raw_response.create(
            name="x",
            source="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(ScriptCreateResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.scripts.with_streaming_response.create(
            name="x",
            source="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(ScriptCreateResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        script = client.scripts.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ScriptRetrieveResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.scripts.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(ScriptRetrieveResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.scripts.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(ScriptRetrieveResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            client.scripts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        script = client.scripts.list()
        assert_matches_type(ScriptListResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        script = client.scripts.list(
            latest="true",
            name="x",
            page=1,
            page_size=1,
            search="x",
        )
        assert_matches_type(ScriptListResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.scripts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(ScriptListResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.scripts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(ScriptListResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        script = client.scripts.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert script is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.scripts.with_raw_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert script is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.scripts.with_streaming_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert script is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            client.scripts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_source(self, client: Mobilerun) -> None:
        script = client.scripts.source(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ScriptSourceResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_source(self, client: Mobilerun) -> None:
        response = client.scripts.with_raw_response.source(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(ScriptSourceResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_source(self, client: Mobilerun) -> None:
        with client.scripts.with_streaming_response.source(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(ScriptSourceResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_source(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            client.scripts.with_raw_response.source(
                "",
            )


class TestAsyncScripts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        script = await async_client.scripts.create(
            name="x",
            source="x",
        )
        assert_matches_type(ScriptCreateResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        script = await async_client.scripts.create(
            name="x",
            source="x",
            description="description",
            manifest={
                "credentials": [
                    {
                        "name": "x",
                        "package_name": "x",
                    }
                ],
                "hosts": ["string"],
                "scopes": ["_lk___klzn__.____uu"],
            },
        )
        assert_matches_type(ScriptCreateResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.scripts.with_raw_response.create(
            name="x",
            source="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(ScriptCreateResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.scripts.with_streaming_response.create(
            name="x",
            source="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(ScriptCreateResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        script = await async_client.scripts.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ScriptRetrieveResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.scripts.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(ScriptRetrieveResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.scripts.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(ScriptRetrieveResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            await async_client.scripts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        script = await async_client.scripts.list()
        assert_matches_type(ScriptListResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        script = await async_client.scripts.list(
            latest="true",
            name="x",
            page=1,
            page_size=1,
            search="x",
        )
        assert_matches_type(ScriptListResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.scripts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(ScriptListResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.scripts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(ScriptListResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        script = await async_client.scripts.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert script is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.scripts.with_raw_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert script is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.scripts.with_streaming_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert script is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            await async_client.scripts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_source(self, async_client: AsyncMobilerun) -> None:
        script = await async_client.scripts.source(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ScriptSourceResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_source(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.scripts.with_raw_response.source(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(ScriptSourceResponse, script, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_source(self, async_client: AsyncMobilerun) -> None:
        async with async_client.scripts.with_streaming_response.source(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(ScriptSourceResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_source(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            await async_client.scripts.with_raw_response.source(
                "",
            )
