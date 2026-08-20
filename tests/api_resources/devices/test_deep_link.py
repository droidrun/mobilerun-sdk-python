# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mobilerun_sdk import Mobilerun, AsyncMobilerun

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeepLink:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_deep_link(self, client: Mobilerun) -> None:
        deep_link = client.devices.deep_link.execute_deep_link(
            device_id="deviceId",
            deep_link="x",
        )
        assert deep_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_deep_link_with_all_params(self, client: Mobilerun) -> None:
        deep_link = client.devices.deep_link.execute_deep_link(
            device_id="deviceId",
            deep_link="x",
            action="action",
            bundle_id="bundleId",
            package_name="packageName",
            x_device_display_id=0,
        )
        assert deep_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_deep_link(self, client: Mobilerun) -> None:
        response = client.devices.deep_link.with_raw_response.execute_deep_link(
            device_id="deviceId",
            deep_link="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deep_link = response.parse()
        assert deep_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_deep_link(self, client: Mobilerun) -> None:
        with client.devices.deep_link.with_streaming_response.execute_deep_link(
            device_id="deviceId",
            deep_link="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deep_link = response.parse()
            assert deep_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute_deep_link(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.deep_link.with_raw_response.execute_deep_link(
                device_id="",
                deep_link="x",
            )


class TestAsyncDeepLink:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_deep_link(self, async_client: AsyncMobilerun) -> None:
        deep_link = await async_client.devices.deep_link.execute_deep_link(
            device_id="deviceId",
            deep_link="x",
        )
        assert deep_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_deep_link_with_all_params(self, async_client: AsyncMobilerun) -> None:
        deep_link = await async_client.devices.deep_link.execute_deep_link(
            device_id="deviceId",
            deep_link="x",
            action="action",
            bundle_id="bundleId",
            package_name="packageName",
            x_device_display_id=0,
        )
        assert deep_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_deep_link(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.deep_link.with_raw_response.execute_deep_link(
            device_id="deviceId",
            deep_link="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deep_link = await response.parse()
        assert deep_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_deep_link(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.deep_link.with_streaming_response.execute_deep_link(
            device_id="deviceId",
            deep_link="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deep_link = await response.parse()
            assert deep_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute_deep_link(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.deep_link.with_raw_response.execute_deep_link(
                device_id="",
                deep_link="x",
            )
