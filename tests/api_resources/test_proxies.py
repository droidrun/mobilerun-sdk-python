# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mobilerun import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun.types import (
    ProxyListResponse,
    ProxyCreateResponse,
    ProxyDeleteResponse,
    ProxyUpdateResponse,
    ProxyRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProxies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Mobilerun) -> None:
        proxy = client.proxies.create(
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        )
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Mobilerun) -> None:
        response = client.proxies.with_raw_response.create(
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Mobilerun) -> None:
        with client.proxies.with_streaming_response.create(
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Mobilerun) -> None:
        proxy = client.proxies.create(
            config="x",
            name="xxx",
            protocol="wireguard",
        )
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Mobilerun) -> None:
        response = client.proxies.with_raw_response.create(
            config="x",
            name="xxx",
            protocol="wireguard",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Mobilerun) -> None:
        with client.proxies.with_streaming_response.create(
            config="x",
            name="xxx",
            protocol="wireguard",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        proxy = client.proxies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.proxies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.proxies.with_streaming_response.retrieve(
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_id` but received ''"):
            client.proxies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: Mobilerun) -> None:
        proxy = client.proxies.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        )
        assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Mobilerun) -> None:
        response = client.proxies.with_raw_response.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Mobilerun) -> None:
        with client.proxies.with_streaming_response.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_id` but received ''"):
            client.proxies.with_raw_response.update(
                proxy_id="",
                host="x",
                name="xxx",
                password="x",
                port=1,
                protocol="socks5",
                user="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: Mobilerun) -> None:
        proxy = client.proxies.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config="x",
            name="xxx",
            protocol="wireguard",
        )
        assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Mobilerun) -> None:
        response = client.proxies.with_raw_response.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config="x",
            name="xxx",
            protocol="wireguard",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Mobilerun) -> None:
        with client.proxies.with_streaming_response.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config="x",
            name="xxx",
            protocol="wireguard",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_id` but received ''"):
            client.proxies.with_raw_response.update(
                proxy_id="",
                config="x",
                name="xxx",
                protocol="wireguard",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        proxy = client.proxies.list()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        proxy = client.proxies.list(
            protocol="socks5",
        )
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.proxies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.proxies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyListResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        proxy = client.proxies.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.proxies.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.proxies.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_id` but received ''"):
            client.proxies.with_raw_response.delete(
                "",
            )


class TestAsyncProxies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.proxies.create(
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        )
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.proxies.with_raw_response.create(
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncMobilerun) -> None:
        async with async_client.proxies.with_streaming_response.create(
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.proxies.create(
            config="x",
            name="xxx",
            protocol="wireguard",
        )
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.proxies.with_raw_response.create(
            config="x",
            name="xxx",
            protocol="wireguard",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncMobilerun) -> None:
        async with async_client.proxies.with_streaming_response.create(
            config="x",
            name="xxx",
            protocol="wireguard",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyCreateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.proxies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.proxies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyRetrieveResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.proxies.with_streaming_response.retrieve(
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_id` but received ''"):
            await async_client.proxies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.proxies.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        )
        assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.proxies.with_raw_response.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncMobilerun) -> None:
        async with async_client.proxies.with_streaming_response.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            host="x",
            name="xxx",
            password="x",
            port=1,
            protocol="socks5",
            user="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_id` but received ''"):
            await async_client.proxies.with_raw_response.update(
                proxy_id="",
                host="x",
                name="xxx",
                password="x",
                port=1,
                protocol="socks5",
                user="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.proxies.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config="x",
            name="xxx",
            protocol="wireguard",
        )
        assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.proxies.with_raw_response.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config="x",
            name="xxx",
            protocol="wireguard",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncMobilerun) -> None:
        async with async_client.proxies.with_streaming_response.update(
            proxy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config="x",
            name="xxx",
            protocol="wireguard",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyUpdateResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_id` but received ''"):
            await async_client.proxies.with_raw_response.update(
                proxy_id="",
                config="x",
                name="xxx",
                protocol="wireguard",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.proxies.list()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.proxies.list(
            protocol="socks5",
        )
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.proxies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyListResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.proxies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyListResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.proxies.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.proxies.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.proxies.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_id` but received ''"):
            await async_client.proxies.with_raw_response.delete(
                "",
            )
