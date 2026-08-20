# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk._utils import parse_datetime
from mobilerun_sdk.types.connect import (
    ProxyBuyResponse,
    ProxyListResponse,
    ProxyPingResponse,
    ProxyRetrieveResponse,
    ProxyListConnectionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProxies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        proxy = client.connect.proxies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.connect.proxies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.connect.proxies.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connect.proxies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        proxy = client.connect.proxies.list()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        proxy = client.connect.proxies.list(
            country="country",
            page=1,
            page_size=1,
        )
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.connect.proxies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.connect.proxies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyListResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_buy(self, client: Mobilerun) -> None:
        proxy = client.connect.proxies.buy(
            country="country",
            type="dedicated_residential",
        )
        assert_matches_type(ProxyBuyResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_buy(self, client: Mobilerun) -> None:
        response = client.connect.proxies.with_raw_response.buy(
            country="country",
            type="dedicated_residential",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyBuyResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_buy(self, client: Mobilerun) -> None:
        with client.connect.proxies.with_streaming_response.buy(
            country="country",
            type="dedicated_residential",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyBuyResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Mobilerun) -> None:
        proxy = client.connect.proxies.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Mobilerun) -> None:
        response = client.connect.proxies.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Mobilerun) -> None:
        with client.connect.proxies.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert proxy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connect.proxies.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_connections(self, client: Mobilerun) -> None:
        proxy = client.connect.proxies.list_connections(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyListConnectionsResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_connections_with_all_params(self, client: Mobilerun) -> None:
        proxy = client.connect.proxies.list_connections(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            close_reason="closeReason",
            country="country",
            dst_host="dstHost",
            dst_port=0,
            ended_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            ended_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_bytes_in=0,
            max_bytes_out=0,
            max_duration_ms=0,
            max_total_bytes=0,
            min_bytes_in=0,
            min_bytes_out=0,
            min_duration_ms=0,
            min_total_bytes=0,
            order="asc",
            order_by="startedAt",
            page=1,
            page_size=1,
            protocol="tcp",
            provider="provider",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            started_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            started_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="active",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyListConnectionsResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_connections(self, client: Mobilerun) -> None:
        response = client.connect.proxies.with_raw_response.list_connections(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyListConnectionsResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_connections(self, client: Mobilerun) -> None:
        with client.connect.proxies.with_streaming_response.list_connections(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyListConnectionsResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_connections(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connect.proxies.with_raw_response.list_connections(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ping(self, client: Mobilerun) -> None:
        proxy = client.connect.proxies.ping(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyPingResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ping(self, client: Mobilerun) -> None:
        response = client.connect.proxies.with_raw_response.ping(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyPingResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ping(self, client: Mobilerun) -> None:
        with client.connect.proxies.with_streaming_response.ping(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyPingResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_ping(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connect.proxies.with_raw_response.ping(
                "",
            )


class TestAsyncProxies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.connect.proxies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.connect.proxies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.connect.proxies.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connect.proxies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.connect.proxies.list()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.connect.proxies.list(
            country="country",
            page=1,
            page_size=1,
        )
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.connect.proxies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.connect.proxies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyListResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_buy(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.connect.proxies.buy(
            country="country",
            type="dedicated_residential",
        )
        assert_matches_type(ProxyBuyResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_buy(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.connect.proxies.with_raw_response.buy(
            country="country",
            type="dedicated_residential",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyBuyResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_buy(self, async_client: AsyncMobilerun) -> None:
        async with async_client.connect.proxies.with_streaming_response.buy(
            country="country",
            type="dedicated_residential",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyBuyResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.connect.proxies.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.connect.proxies.with_raw_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncMobilerun) -> None:
        async with async_client.connect.proxies.with_streaming_response.cancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert proxy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connect.proxies.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_connections(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.connect.proxies.list_connections(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyListConnectionsResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_connections_with_all_params(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.connect.proxies.list_connections(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            close_reason="closeReason",
            country="country",
            dst_host="dstHost",
            dst_port=0,
            ended_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            ended_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_bytes_in=0,
            max_bytes_out=0,
            max_duration_ms=0,
            max_total_bytes=0,
            min_bytes_in=0,
            min_bytes_out=0,
            min_duration_ms=0,
            min_total_bytes=0,
            order="asc",
            order_by="startedAt",
            page=1,
            page_size=1,
            protocol="tcp",
            provider="provider",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            started_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            started_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="active",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyListConnectionsResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_connections(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.connect.proxies.with_raw_response.list_connections(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyListConnectionsResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_connections(self, async_client: AsyncMobilerun) -> None:
        async with async_client.connect.proxies.with_streaming_response.list_connections(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyListConnectionsResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_connections(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connect.proxies.with_raw_response.list_connections(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ping(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.connect.proxies.ping(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyPingResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ping(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.connect.proxies.with_raw_response.ping(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyPingResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ping(self, async_client: AsyncMobilerun) -> None:
        async with async_client.connect.proxies.with_streaming_response.ping(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyPingResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_ping(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connect.proxies.with_raw_response.ping(
                "",
            )
