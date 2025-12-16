# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mobilerun import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun.types import Device, DeviceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        device = client.devices.create(
            apps=["string"],
            files=["string"],
            x_user_id="X-User-ID",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        device = client.devices.create(
            apps=["string"],
            files=["string"],
            x_user_id="X-User-ID",
            country="country",
            name="name",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.devices.with_raw_response.create(
            apps=["string"],
            files=["string"],
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.devices.with_streaming_response.create(
            apps=["string"],
            files=["string"],
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        device = client.devices.retrieve(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.devices.with_raw_response.retrieve(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.devices.with_streaming_response.retrieve(
            device_id="deviceId",
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.retrieve(
                device_id="",
                x_user_id="X-User-ID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        device = client.devices.list(
            x_user_id="X-User-ID",
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        device = client.devices.list(
            x_user_id="X-User-ID",
            country="country",
            order_by="id",
            order_by_direction="asc",
            page=0,
            page_size=0,
            state="creating",
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.devices.with_raw_response.list(
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.devices.with_streaming_response.list(
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_terminate(self, client: Mobilerun) -> None:
        device = client.devices.terminate(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )
        assert device is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_terminate(self, client: Mobilerun) -> None:
        response = client.devices.with_raw_response.terminate(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert device is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_terminate(self, client: Mobilerun) -> None:
        with client.devices.with_streaming_response.terminate(
            device_id="deviceId",
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_terminate(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.terminate(
                device_id="",
                x_user_id="X-User-ID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_wait_ready(self, client: Mobilerun) -> None:
        device = client.devices.wait_ready(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_wait_ready(self, client: Mobilerun) -> None:
        response = client.devices.with_raw_response.wait_ready(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_wait_ready(self, client: Mobilerun) -> None:
        with client.devices.with_streaming_response.wait_ready(
            device_id="deviceId",
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_wait_ready(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.with_raw_response.wait_ready(
                device_id="",
                x_user_id="X-User-ID",
            )


class TestAsyncDevices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        device = await async_client.devices.create(
            apps=["string"],
            files=["string"],
            x_user_id="X-User-ID",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        device = await async_client.devices.create(
            apps=["string"],
            files=["string"],
            x_user_id="X-User-ID",
            country="country",
            name="name",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.with_raw_response.create(
            apps=["string"],
            files=["string"],
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.with_streaming_response.create(
            apps=["string"],
            files=["string"],
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        device = await async_client.devices.retrieve(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.with_raw_response.retrieve(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.with_streaming_response.retrieve(
            device_id="deviceId",
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.retrieve(
                device_id="",
                x_user_id="X-User-ID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        device = await async_client.devices.list(
            x_user_id="X-User-ID",
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        device = await async_client.devices.list(
            x_user_id="X-User-ID",
            country="country",
            order_by="id",
            order_by_direction="asc",
            page=0,
            page_size=0,
            state="creating",
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.with_raw_response.list(
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.with_streaming_response.list(
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_terminate(self, async_client: AsyncMobilerun) -> None:
        device = await async_client.devices.terminate(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )
        assert device is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_terminate(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.with_raw_response.terminate(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert device is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_terminate(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.with_streaming_response.terminate(
            device_id="deviceId",
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_terminate(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.terminate(
                device_id="",
                x_user_id="X-User-ID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_wait_ready(self, async_client: AsyncMobilerun) -> None:
        device = await async_client.devices.wait_ready(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_wait_ready(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.with_raw_response.wait_ready(
            device_id="deviceId",
            x_user_id="X-User-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_wait_ready(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.with_streaming_response.wait_ready(
            device_id="deviceId",
            x_user_id="X-User-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_wait_ready(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.with_raw_response.wait_ready(
                device_id="",
                x_user_id="X-User-ID",
            )
