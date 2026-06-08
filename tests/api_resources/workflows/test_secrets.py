# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.workflows import (
    SecretListResponse,
    SecretCreateResponse,
    SecretDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        secret = client.workflows.secrets.create(
            name="name",
            value="x",
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        secret = client.workflows.secrets.create(
            name="name",
            value="x",
            description="description",
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.workflows.secrets.with_raw_response.create(
            name="name",
            value="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.workflows.secrets.with_streaming_response.create(
            name="name",
            value="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        secret = client.workflows.secrets.list()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.workflows.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.workflows.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        secret = client.workflows.secrets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SecretDeleteResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.workflows.secrets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretDeleteResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.workflows.secrets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretDeleteResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.workflows.secrets.with_raw_response.delete(
                "",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        secret = await async_client.workflows.secrets.create(
            name="name",
            value="x",
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        secret = await async_client.workflows.secrets.create(
            name="name",
            value="x",
            description="description",
        )
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.secrets.with_raw_response.create(
            name="name",
            value="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretCreateResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.secrets.with_streaming_response.create(
            name="name",
            value="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretCreateResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        secret = await async_client.workflows.secrets.list()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        secret = await async_client.workflows.secrets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SecretDeleteResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.secrets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretDeleteResponse, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.secrets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretDeleteResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.workflows.secrets.with_raw_response.delete(
                "",
            )
