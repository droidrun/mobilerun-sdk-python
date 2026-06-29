# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.devices import TimezoneGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimezone:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Mobilerun) -> None:
        timezone = client.devices.timezone.get(
            device_id="deviceId",
        )
        assert_matches_type(TimezoneGetResponse, timezone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Mobilerun) -> None:
        timezone = client.devices.timezone.get(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(TimezoneGetResponse, timezone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Mobilerun) -> None:
        response = client.devices.timezone.with_raw_response.get(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timezone = response.parse()
        assert_matches_type(TimezoneGetResponse, timezone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Mobilerun) -> None:
        with client.devices.timezone.with_streaming_response.get(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timezone = response.parse()
            assert_matches_type(TimezoneGetResponse, timezone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.timezone.with_raw_response.get(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set(self, client: Mobilerun) -> None:
        timezone = client.devices.timezone.set(
            device_id="deviceId",
            timezone="timezone",
        )
        assert timezone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_with_all_params(self, client: Mobilerun) -> None:
        timezone = client.devices.timezone.set(
            device_id="deviceId",
            timezone="timezone",
            x_device_display_id=0,
        )
        assert timezone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: Mobilerun) -> None:
        response = client.devices.timezone.with_raw_response.set(
            device_id="deviceId",
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timezone = response.parse()
        assert timezone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: Mobilerun) -> None:
        with client.devices.timezone.with_streaming_response.set(
            device_id="deviceId",
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timezone = response.parse()
            assert timezone is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.timezone.with_raw_response.set(
                device_id="",
                timezone="timezone",
            )


class TestAsyncTimezone:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncMobilerun) -> None:
        timezone = await async_client.devices.timezone.get(
            device_id="deviceId",
        )
        assert_matches_type(TimezoneGetResponse, timezone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncMobilerun) -> None:
        timezone = await async_client.devices.timezone.get(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(TimezoneGetResponse, timezone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.timezone.with_raw_response.get(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timezone = await response.parse()
        assert_matches_type(TimezoneGetResponse, timezone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.timezone.with_streaming_response.get(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timezone = await response.parse()
            assert_matches_type(TimezoneGetResponse, timezone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.timezone.with_raw_response.get(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncMobilerun) -> None:
        timezone = await async_client.devices.timezone.set(
            device_id="deviceId",
            timezone="timezone",
        )
        assert timezone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncMobilerun) -> None:
        timezone = await async_client.devices.timezone.set(
            device_id="deviceId",
            timezone="timezone",
            x_device_display_id=0,
        )
        assert timezone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.timezone.with_raw_response.set(
            device_id="deviceId",
            timezone="timezone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timezone = await response.parse()
        assert timezone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.timezone.with_streaming_response.set(
            device_id="deviceId",
            timezone="timezone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timezone = await response.parse()
            assert timezone is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.timezone.with_raw_response.set(
                device_id="",
                timezone="timezone",
            )
