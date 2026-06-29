# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mobilerun_sdk import Mobilerun, AsyncMobilerun

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Mobilerun) -> None:
        profile = client.devices.profile.update(
            device_id="deviceId",
            profile_id="profileId",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Mobilerun) -> None:
        profile = client.devices.profile.update(
            device_id="deviceId",
            profile_id="profileId",
            x_device_display_id=0,
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Mobilerun) -> None:
        response = client.devices.profile.with_raw_response.update(
            device_id="deviceId",
            profile_id="profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Mobilerun) -> None:
        with client.devices.profile.with_streaming_response.update(
            device_id="deviceId",
            profile_id="profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.profile.with_raw_response.update(
                device_id="",
                profile_id="profileId",
            )


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.devices.profile.update(
            device_id="deviceId",
            profile_id="profileId",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.devices.profile.update(
            device_id="deviceId",
            profile_id="profileId",
            x_device_display_id=0,
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.profile.with_raw_response.update(
            device_id="deviceId",
            profile_id="profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.profile.with_streaming_response.update(
            device_id="deviceId",
            profile_id="profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.profile.with_raw_response.update(
                device_id="",
                profile_id="profileId",
            )
