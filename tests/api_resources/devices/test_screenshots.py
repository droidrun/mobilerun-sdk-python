# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.devices import (
    ScreenshotListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScreenshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        screenshot = client.devices.screenshots.list(
            device_id="deviceId",
        )
        assert_matches_type(ScreenshotListResponse, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        screenshot = client.devices.screenshots.list(
            device_id="deviceId",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ScreenshotListResponse, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.devices.screenshots.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = response.parse()
        assert_matches_type(ScreenshotListResponse, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.devices.screenshots.with_streaming_response.list(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = response.parse()
            assert_matches_type(ScreenshotListResponse, screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.screenshots.with_raw_response.list(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        screenshot = client.devices.screenshots.delete(
            screenshot_id="screenshotId",
            device_id="deviceId",
        )
        assert screenshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.devices.screenshots.with_raw_response.delete(
            screenshot_id="screenshotId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = response.parse()
        assert screenshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.devices.screenshots.with_streaming_response.delete(
            screenshot_id="screenshotId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = response.parse()
            assert screenshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.screenshots.with_raw_response.delete(
                screenshot_id="screenshotId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screenshot_id` but received ''"):
            client.devices.screenshots.with_raw_response.delete(
                screenshot_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_capture(self, client: Mobilerun) -> None:
        screenshot = client.devices.screenshots.capture(
            device_id="deviceId",
        )
        assert_matches_type(str, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_capture_with_all_params(self, client: Mobilerun) -> None:
        screenshot = client.devices.screenshots.capture(
            device_id="deviceId",
            hide_overlay=True,
            save=True,
            x_device_display_id=0,
        )
        assert_matches_type(str, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_capture(self, client: Mobilerun) -> None:
        response = client.devices.screenshots.with_raw_response.capture(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = response.parse()
        assert_matches_type(str, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_capture(self, client: Mobilerun) -> None:
        with client.devices.screenshots.with_streaming_response.capture(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = response.parse()
            assert_matches_type(str, screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_capture(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.screenshots.with_raw_response.capture(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_image(self, client: Mobilerun) -> None:
        screenshot = client.devices.screenshots.image(
            screenshot_id="screenshotId",
            device_id="deviceId",
        )
        assert screenshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_image(self, client: Mobilerun) -> None:
        response = client.devices.screenshots.with_raw_response.image(
            screenshot_id="screenshotId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = response.parse()
        assert screenshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_image(self, client: Mobilerun) -> None:
        with client.devices.screenshots.with_streaming_response.image(
            screenshot_id="screenshotId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = response.parse()
            assert screenshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_image(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.screenshots.with_raw_response.image(
                screenshot_id="screenshotId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screenshot_id` but received ''"):
            client.devices.screenshots.with_raw_response.image(
                screenshot_id="",
                device_id="deviceId",
            )


class TestAsyncScreenshots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        screenshot = await async_client.devices.screenshots.list(
            device_id="deviceId",
        )
        assert_matches_type(ScreenshotListResponse, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        screenshot = await async_client.devices.screenshots.list(
            device_id="deviceId",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ScreenshotListResponse, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.screenshots.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = await response.parse()
        assert_matches_type(ScreenshotListResponse, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.screenshots.with_streaming_response.list(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = await response.parse()
            assert_matches_type(ScreenshotListResponse, screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.screenshots.with_raw_response.list(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        screenshot = await async_client.devices.screenshots.delete(
            screenshot_id="screenshotId",
            device_id="deviceId",
        )
        assert screenshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.screenshots.with_raw_response.delete(
            screenshot_id="screenshotId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = await response.parse()
        assert screenshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.screenshots.with_streaming_response.delete(
            screenshot_id="screenshotId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = await response.parse()
            assert screenshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.screenshots.with_raw_response.delete(
                screenshot_id="screenshotId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screenshot_id` but received ''"):
            await async_client.devices.screenshots.with_raw_response.delete(
                screenshot_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_capture(self, async_client: AsyncMobilerun) -> None:
        screenshot = await async_client.devices.screenshots.capture(
            device_id="deviceId",
        )
        assert_matches_type(str, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_capture_with_all_params(self, async_client: AsyncMobilerun) -> None:
        screenshot = await async_client.devices.screenshots.capture(
            device_id="deviceId",
            hide_overlay=True,
            save=True,
            x_device_display_id=0,
        )
        assert_matches_type(str, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_capture(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.screenshots.with_raw_response.capture(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = await response.parse()
        assert_matches_type(str, screenshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_capture(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.screenshots.with_streaming_response.capture(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = await response.parse()
            assert_matches_type(str, screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_capture(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.screenshots.with_raw_response.capture(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_image(self, async_client: AsyncMobilerun) -> None:
        screenshot = await async_client.devices.screenshots.image(
            screenshot_id="screenshotId",
            device_id="deviceId",
        )
        assert screenshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_image(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.screenshots.with_raw_response.image(
            screenshot_id="screenshotId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = await response.parse()
        assert screenshot is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_image(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.screenshots.with_streaming_response.image(
            screenshot_id="screenshotId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = await response.parse()
            assert screenshot is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_image(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.screenshots.with_raw_response.image(
                screenshot_id="screenshotId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `screenshot_id` but received ''"):
            await async_client.devices.screenshots.with_raw_response.image(
                screenshot_id="",
                device_id="deviceId",
            )
