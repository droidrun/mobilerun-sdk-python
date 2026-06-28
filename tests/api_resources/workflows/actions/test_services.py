# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.workflows.actions import ServiceListResponse, ServiceListMethodsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        service = client.workflows.actions.services.list()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.workflows.actions.services.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.workflows.actions.services.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_methods(self, client: Mobilerun) -> None:
        service = client.workflows.actions.services.list_methods(
            "x",
        )
        assert_matches_type(ServiceListMethodsResponse, service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_methods(self, client: Mobilerun) -> None:
        response = client.workflows.actions.services.with_raw_response.list_methods(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceListMethodsResponse, service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_methods(self, client: Mobilerun) -> None:
        with client.workflows.actions.services.with_streaming_response.list_methods(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceListMethodsResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_methods(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service` but received ''"):
            client.workflows.actions.services.with_raw_response.list_methods(
                "",
            )


class TestAsyncServices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        service = await async_client.workflows.actions.services.list()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.actions.services.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.actions.services.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_methods(self, async_client: AsyncMobilerun) -> None:
        service = await async_client.workflows.actions.services.list_methods(
            "x",
        )
        assert_matches_type(ServiceListMethodsResponse, service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_methods(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.actions.services.with_raw_response.list_methods(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceListMethodsResponse, service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_methods(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.actions.services.with_streaming_response.list_methods(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceListMethodsResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_methods(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service` but received ''"):
            await async_client.workflows.actions.services.with_raw_response.list_methods(
                "",
            )
