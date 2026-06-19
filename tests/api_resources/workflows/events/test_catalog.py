# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.workflows.events import (
    CatalogListResponse,
    CatalogRegisterResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCatalog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        catalog = client.workflows.events.catalog.list()
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        catalog = client.workflows.events.catalog.list(
            page=1,
            page_size=1,
            source="device",
        )
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.workflows.events.catalog.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = response.parse()
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.workflows.events.catalog.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = response.parse()
            assert_matches_type(CatalogListResponse, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_register(self, client: Mobilerun) -> None:
        catalog = client.workflows.events.catalog.register(
            events=[
                {
                    "event_type": "x",
                    "label": "x",
                }
            ],
        )
        assert_matches_type(CatalogRegisterResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_register(self, client: Mobilerun) -> None:
        response = client.workflows.events.catalog.with_raw_response.register(
            events=[
                {
                    "event_type": "x",
                    "label": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = response.parse()
        assert_matches_type(CatalogRegisterResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_register(self, client: Mobilerun) -> None:
        with client.workflows.events.catalog.with_streaming_response.register(
            events=[
                {
                    "event_type": "x",
                    "label": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = response.parse()
            assert_matches_type(CatalogRegisterResponse, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCatalog:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        catalog = await async_client.workflows.events.catalog.list()
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        catalog = await async_client.workflows.events.catalog.list(
            page=1,
            page_size=1,
            source="device",
        )
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.events.catalog.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = await response.parse()
        assert_matches_type(CatalogListResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.events.catalog.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = await response.parse()
            assert_matches_type(CatalogListResponse, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_register(self, async_client: AsyncMobilerun) -> None:
        catalog = await async_client.workflows.events.catalog.register(
            events=[
                {
                    "event_type": "x",
                    "label": "x",
                }
            ],
        )
        assert_matches_type(CatalogRegisterResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.events.catalog.with_raw_response.register(
            events=[
                {
                    "event_type": "x",
                    "label": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog = await response.parse()
        assert_matches_type(CatalogRegisterResponse, catalog, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.events.catalog.with_streaming_response.register(
            events=[
                {
                    "event_type": "x",
                    "label": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog = await response.parse()
            assert_matches_type(CatalogRegisterResponse, catalog, path=["response"])

        assert cast(Any, response.is_closed) is True
