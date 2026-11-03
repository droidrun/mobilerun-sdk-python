# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.credentials import (
    OnepasswordConnectResponse,
    OnepasswordRetrieveResponse,
    OnepasswordDisconnectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnepassword:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        onepassword = client.credentials.onepassword.retrieve()
        assert_matches_type(OnepasswordRetrieveResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.credentials.onepassword.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onepassword = response.parse()
        assert_matches_type(OnepasswordRetrieveResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.credentials.onepassword.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onepassword = response.parse()
            assert_matches_type(OnepasswordRetrieveResponse, onepassword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect(self, client: Mobilerun) -> None:
        onepassword = client.credentials.onepassword.connect(
            service_account_token="serviceAccountToken",
        )
        assert_matches_type(OnepasswordConnectResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: Mobilerun) -> None:
        response = client.credentials.onepassword.with_raw_response.connect(
            service_account_token="serviceAccountToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onepassword = response.parse()
        assert_matches_type(OnepasswordConnectResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: Mobilerun) -> None:
        with client.credentials.onepassword.with_streaming_response.connect(
            service_account_token="serviceAccountToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onepassword = response.parse()
            assert_matches_type(OnepasswordConnectResponse, onepassword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disconnect(self, client: Mobilerun) -> None:
        onepassword = client.credentials.onepassword.disconnect()
        assert_matches_type(OnepasswordDisconnectResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disconnect(self, client: Mobilerun) -> None:
        response = client.credentials.onepassword.with_raw_response.disconnect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onepassword = response.parse()
        assert_matches_type(OnepasswordDisconnectResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disconnect(self, client: Mobilerun) -> None:
        with client.credentials.onepassword.with_streaming_response.disconnect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onepassword = response.parse()
            assert_matches_type(OnepasswordDisconnectResponse, onepassword, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOnepassword:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        onepassword = await async_client.credentials.onepassword.retrieve()
        assert_matches_type(OnepasswordRetrieveResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.credentials.onepassword.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onepassword = await response.parse()
        assert_matches_type(OnepasswordRetrieveResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.credentials.onepassword.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onepassword = await response.parse()
            assert_matches_type(OnepasswordRetrieveResponse, onepassword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncMobilerun) -> None:
        onepassword = await async_client.credentials.onepassword.connect(
            service_account_token="serviceAccountToken",
        )
        assert_matches_type(OnepasswordConnectResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.credentials.onepassword.with_raw_response.connect(
            service_account_token="serviceAccountToken",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onepassword = await response.parse()
        assert_matches_type(OnepasswordConnectResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncMobilerun) -> None:
        async with async_client.credentials.onepassword.with_streaming_response.connect(
            service_account_token="serviceAccountToken",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onepassword = await response.parse()
            assert_matches_type(OnepasswordConnectResponse, onepassword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disconnect(self, async_client: AsyncMobilerun) -> None:
        onepassword = await async_client.credentials.onepassword.disconnect()
        assert_matches_type(OnepasswordDisconnectResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disconnect(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.credentials.onepassword.with_raw_response.disconnect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onepassword = await response.parse()
        assert_matches_type(OnepasswordDisconnectResponse, onepassword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disconnect(self, async_client: AsyncMobilerun) -> None:
        async with async_client.credentials.onepassword.with_streaming_response.disconnect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onepassword = await response.parse()
            assert_matches_type(OnepasswordDisconnectResponse, onepassword, path=["response"])

        assert cast(Any, response.is_closed) is True
