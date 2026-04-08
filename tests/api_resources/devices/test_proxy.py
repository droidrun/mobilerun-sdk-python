# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mobilerun import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun.types.devices import ProxyStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProxy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect(self, client: Mobilerun) -> None:
        proxy = client.devices.proxy.connect(
            device_id="deviceId",
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect_with_all_params(self, client: Mobilerun) -> None:
        proxy = client.devices.proxy.connect(
            device_id="deviceId",
            host="host",
            name="name",
            password="password",
            port=1,
            smart_ip=True,
            socks5={
                "host": "host",
                "port": 1,
                "password": "password",
                "user": "user",
            },
            user="user",
            wireguard="wireguard",
            x_device_display_id=0,
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: Mobilerun) -> None:
        response = client.devices.proxy.with_raw_response.connect(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: Mobilerun) -> None:
        with client.devices.proxy.with_streaming_response.connect(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert proxy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_connect(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.proxy.with_raw_response.connect(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disconnect(self, client: Mobilerun) -> None:
        proxy = client.devices.proxy.disconnect(
            device_id="deviceId",
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disconnect_with_all_params(self, client: Mobilerun) -> None:
        proxy = client.devices.proxy.disconnect(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disconnect(self, client: Mobilerun) -> None:
        response = client.devices.proxy.with_raw_response.disconnect(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disconnect(self, client: Mobilerun) -> None:
        with client.devices.proxy.with_streaming_response.disconnect(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert proxy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disconnect(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.proxy.with_raw_response.disconnect(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status(self, client: Mobilerun) -> None:
        proxy = client.devices.proxy.status(
            device_id="deviceId",
        )
        assert_matches_type(ProxyStatusResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status_with_all_params(self, client: Mobilerun) -> None:
        proxy = client.devices.proxy.status(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(ProxyStatusResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Mobilerun) -> None:
        response = client.devices.proxy.with_raw_response.status(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyStatusResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Mobilerun) -> None:
        with client.devices.proxy.with_streaming_response.status(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyStatusResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.proxy.with_raw_response.status(
                device_id="",
            )


class TestAsyncProxy:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.devices.proxy.connect(
            device_id="deviceId",
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.devices.proxy.connect(
            device_id="deviceId",
            host="host",
            name="name",
            password="password",
            port=1,
            smart_ip=True,
            socks5={
                "host": "host",
                "port": 1,
                "password": "password",
                "user": "user",
            },
            user="user",
            wireguard="wireguard",
            x_device_display_id=0,
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.proxy.with_raw_response.connect(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.proxy.with_streaming_response.connect(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert proxy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_connect(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.proxy.with_raw_response.connect(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disconnect(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.devices.proxy.disconnect(
            device_id="deviceId",
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disconnect_with_all_params(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.devices.proxy.disconnect(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disconnect(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.proxy.with_raw_response.disconnect(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert proxy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disconnect(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.proxy.with_streaming_response.disconnect(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert proxy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disconnect(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.proxy.with_raw_response.disconnect(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.devices.proxy.status(
            device_id="deviceId",
        )
        assert_matches_type(ProxyStatusResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncMobilerun) -> None:
        proxy = await async_client.devices.proxy.status(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(ProxyStatusResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.proxy.with_raw_response.status(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyStatusResponse, proxy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.proxy.with_streaming_response.status(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyStatusResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.proxy.with_raw_response.status(
                device_id="",
            )
