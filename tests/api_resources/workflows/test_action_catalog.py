# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from mobilerun_sdk.types.workflows import ActionCatalogRetrieveResponse, ActionCatalogListResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types.workflows import action_catalog_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestActionCatalog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        action_catalog = client.workflows.action_catalog.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionCatalogRetrieveResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:

        response = client.workflows.action_catalog.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action_catalog = response.parse()
        assert_matches_type(ActionCatalogRetrieveResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.workflows.action_catalog.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action_catalog = response.parse()
            assert_matches_type(ActionCatalogRetrieveResponse, action_catalog, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `catalog_entry_id` but received ''"):
          client.workflows.action_catalog.with_raw_response.retrieve(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        action_catalog = client.workflows.action_catalog.list()
        assert_matches_type(ActionCatalogListResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        action_catalog = client.workflows.action_catalog.list(
            page=1,
            page_size=1,
            service="tasks_api",
        )
        assert_matches_type(ActionCatalogListResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:

        response = client.workflows.action_catalog.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action_catalog = response.parse()
        assert_matches_type(ActionCatalogListResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.workflows.action_catalog.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action_catalog = response.parse()
            assert_matches_type(ActionCatalogListResponse, action_catalog, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncActionCatalog:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        action_catalog = await async_client.workflows.action_catalog.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionCatalogRetrieveResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.action_catalog.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action_catalog = await response.parse()
        assert_matches_type(ActionCatalogRetrieveResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.action_catalog.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action_catalog = await response.parse()
            assert_matches_type(ActionCatalogRetrieveResponse, action_catalog, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `catalog_entry_id` but received ''"):
          await async_client.workflows.action_catalog.with_raw_response.retrieve(
              "",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        action_catalog = await async_client.workflows.action_catalog.list()
        assert_matches_type(ActionCatalogListResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        action_catalog = await async_client.workflows.action_catalog.list(
            page=1,
            page_size=1,
            service="tasks_api",
        )
        assert_matches_type(ActionCatalogListResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.action_catalog.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action_catalog = await response.parse()
        assert_matches_type(ActionCatalogListResponse, action_catalog, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.action_catalog.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action_catalog = await response.parse()
            assert_matches_type(ActionCatalogListResponse, action_catalog, path=['response'])

        assert cast(Any, response.is_closed) is True