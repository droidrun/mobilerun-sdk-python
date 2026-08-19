# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types.devices import kiosk_enable_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestKiosk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable(self, client: Mobilerun) -> None:
        kiosk = client.devices.kiosk.disable(
            device_id="deviceId",
        )
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable_with_all_params(self, client: Mobilerun) -> None:
        kiosk = client.devices.kiosk.disable(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disable(self, client: Mobilerun) -> None:

        response = client.devices.kiosk.with_raw_response.disable(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        kiosk = response.parse()
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disable(self, client: Mobilerun) -> None:
        with client.devices.kiosk.with_streaming_response.disable(
            device_id="deviceId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            kiosk = response.parse()
            assert kiosk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disable(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.kiosk.with_raw_response.disable(
              device_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable(self, client: Mobilerun) -> None:
        kiosk = client.devices.kiosk.enable(
            device_id="deviceId",
            package_name="x",
        )
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable_with_all_params(self, client: Mobilerun) -> None:
        kiosk = client.devices.kiosk.enable(
            device_id="deviceId",
            package_name="x",
            x_device_display_id=0,
        )
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enable(self, client: Mobilerun) -> None:

        response = client.devices.kiosk.with_raw_response.enable(
            device_id="deviceId",
            package_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        kiosk = response.parse()
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enable(self, client: Mobilerun) -> None:
        with client.devices.kiosk.with_streaming_response.enable(
            device_id="deviceId",
            package_name="x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            kiosk = response.parse()
            assert kiosk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_enable(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.kiosk.with_raw_response.enable(
              device_id="",
              package_name="x",
          )
class TestAsyncKiosk:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable(self, async_client: AsyncMobilerun) -> None:
        kiosk = await async_client.devices.kiosk.disable(
            device_id="deviceId",
        )
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable_with_all_params(self, async_client: AsyncMobilerun) -> None:
        kiosk = await async_client.devices.kiosk.disable(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.kiosk.with_raw_response.disable(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        kiosk = await response.parse()
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.kiosk.with_streaming_response.disable(
            device_id="deviceId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            kiosk = await response.parse()
            assert kiosk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disable(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.kiosk.with_raw_response.disable(
              device_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable(self, async_client: AsyncMobilerun) -> None:
        kiosk = await async_client.devices.kiosk.enable(
            device_id="deviceId",
            package_name="x",
        )
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable_with_all_params(self, async_client: AsyncMobilerun) -> None:
        kiosk = await async_client.devices.kiosk.enable(
            device_id="deviceId",
            package_name="x",
            x_device_display_id=0,
        )
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.kiosk.with_raw_response.enable(
            device_id="deviceId",
            package_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        kiosk = await response.parse()
        assert kiosk is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.kiosk.with_streaming_response.enable(
            device_id="deviceId",
            package_name="x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            kiosk = await response.parse()
            assert kiosk is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_enable(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.kiosk.with_raw_response.enable(
              device_id="",
              package_name="x",
          )