# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.devices import NumberBindingListResponse, NumberBindingListCandidatesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumberBindings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        number_binding = client.devices.number_bindings.list()
        assert_matches_type(NumberBindingListResponse, number_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.devices.number_bindings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_binding = response.parse()
        assert_matches_type(NumberBindingListResponse, number_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.devices.number_bindings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_binding = response.parse()
            assert_matches_type(NumberBindingListResponse, number_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_candidates(self, client: Mobilerun) -> None:
        number_binding = client.devices.number_bindings.list_candidates()
        assert_matches_type(NumberBindingListCandidatesResponse, number_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_candidates(self, client: Mobilerun) -> None:
        response = client.devices.number_bindings.with_raw_response.list_candidates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_binding = response.parse()
        assert_matches_type(NumberBindingListCandidatesResponse, number_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_candidates(self, client: Mobilerun) -> None:
        with client.devices.number_bindings.with_streaming_response.list_candidates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_binding = response.parse()
            assert_matches_type(NumberBindingListCandidatesResponse, number_binding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNumberBindings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        number_binding = await async_client.devices.number_bindings.list()
        assert_matches_type(NumberBindingListResponse, number_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.number_bindings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_binding = await response.parse()
        assert_matches_type(NumberBindingListResponse, number_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.number_bindings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_binding = await response.parse()
            assert_matches_type(NumberBindingListResponse, number_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_candidates(self, async_client: AsyncMobilerun) -> None:
        number_binding = await async_client.devices.number_bindings.list_candidates()
        assert_matches_type(NumberBindingListCandidatesResponse, number_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_candidates(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.number_bindings.with_raw_response.list_candidates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_binding = await response.parse()
        assert_matches_type(NumberBindingListCandidatesResponse, number_binding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_candidates(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.number_bindings.with_streaming_response.list_candidates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_binding = await response.parse()
            assert_matches_type(NumberBindingListCandidatesResponse, number_binding, path=["response"])

        assert cast(Any, response.is_closed) is True
