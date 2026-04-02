# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mobilerun import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun.types.devices import TimeTimezoneResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_timezone(self, client: Mobilerun) -> None:
        time = client.devices.time.set_timezone(
            device_id="deviceId",
            timezone="timezone",
        )
        assert time is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_timezone_with_all_params(self, client: Mobilerun) -> None:
        time = client.devices.time.set_timezone(
            device_id="deviceId",
            timezone="timezone",
            x_device_display_id=0,
        )
        assert time is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_timezone(self, client: Mobilerun) -> None:
        response = client.devices.time.with_raw_response.set_timezone(
            device_id="deviceId",
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time = response.parse()
        assert time is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_timezone(self, client: Mobilerun) -> None:
        with client.devices.time.with_streaming_response.set_timezone(
            device_id="deviceId",
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time = response.parse()
            assert time is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_timezone(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.time.with_raw_response.set_timezone(
                device_id="",
                timezone="timezone",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_time(self, client: Mobilerun) -> None:
        time = client.devices.time.time(
            device_id="deviceId",
        )
        assert_matches_type(str, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_time_with_all_params(self, client: Mobilerun) -> None:
        time = client.devices.time.time(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(str, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_time(self, client: Mobilerun) -> None:
        response = client.devices.time.with_raw_response.time(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time = response.parse()
        assert_matches_type(str, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_time(self, client: Mobilerun) -> None:
        with client.devices.time.with_streaming_response.time(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time = response.parse()
            assert_matches_type(str, time, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_time(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.time.with_raw_response.time(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_timezone(self, client: Mobilerun) -> None:
        time = client.devices.time.timezone(
            device_id="deviceId",
        )
        assert_matches_type(TimeTimezoneResponse, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_timezone_with_all_params(self, client: Mobilerun) -> None:
        time = client.devices.time.timezone(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(TimeTimezoneResponse, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_timezone(self, client: Mobilerun) -> None:
        response = client.devices.time.with_raw_response.timezone(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time = response.parse()
        assert_matches_type(TimeTimezoneResponse, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_timezone(self, client: Mobilerun) -> None:
        with client.devices.time.with_streaming_response.timezone(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time = response.parse()
            assert_matches_type(TimeTimezoneResponse, time, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_timezone(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.time.with_raw_response.timezone(
                device_id="",
            )


class TestAsyncTime:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_timezone(self, async_client: AsyncMobilerun) -> None:
        time = await async_client.devices.time.set_timezone(
            device_id="deviceId",
            timezone="timezone",
        )
        assert time is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_timezone_with_all_params(self, async_client: AsyncMobilerun) -> None:
        time = await async_client.devices.time.set_timezone(
            device_id="deviceId",
            timezone="timezone",
            x_device_display_id=0,
        )
        assert time is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_timezone(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.time.with_raw_response.set_timezone(
            device_id="deviceId",
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time = await response.parse()
        assert time is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_timezone(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.time.with_streaming_response.set_timezone(
            device_id="deviceId",
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time = await response.parse()
            assert time is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_timezone(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.time.with_raw_response.set_timezone(
                device_id="",
                timezone="timezone",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_time(self, async_client: AsyncMobilerun) -> None:
        time = await async_client.devices.time.time(
            device_id="deviceId",
        )
        assert_matches_type(str, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_time_with_all_params(self, async_client: AsyncMobilerun) -> None:
        time = await async_client.devices.time.time(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(str, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_time(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.time.with_raw_response.time(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time = await response.parse()
        assert_matches_type(str, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_time(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.time.with_streaming_response.time(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time = await response.parse()
            assert_matches_type(str, time, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_time(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.time.with_raw_response.time(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_timezone(self, async_client: AsyncMobilerun) -> None:
        time = await async_client.devices.time.timezone(
            device_id="deviceId",
        )
        assert_matches_type(TimeTimezoneResponse, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_timezone_with_all_params(self, async_client: AsyncMobilerun) -> None:
        time = await async_client.devices.time.timezone(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(TimeTimezoneResponse, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_timezone(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.time.with_raw_response.timezone(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        time = await response.parse()
        assert_matches_type(TimeTimezoneResponse, time, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_timezone(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.time.with_streaming_response.timezone(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            time = await response.parse()
            assert_matches_type(TimeTimezoneResponse, time, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_timezone(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.time.with_raw_response.timezone(
                device_id="",
            )
