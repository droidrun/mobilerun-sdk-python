# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.devices import BrowserExecuteScriptResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_script(self, client: Mobilerun) -> None:
        browser = client.devices.browser.execute_script(
            device_id="deviceId",
            script="script",
        )
        assert_matches_type(BrowserExecuteScriptResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_script_with_all_params(self, client: Mobilerun) -> None:
        browser = client.devices.browser.execute_script(
            device_id="deviceId",
            script="script",
            x_device_display_id=0,
        )
        assert_matches_type(BrowserExecuteScriptResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_script(self, client: Mobilerun) -> None:
        response = client.devices.browser.with_raw_response.execute_script(
            device_id="deviceId",
            script="script",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = response.parse()
        assert_matches_type(BrowserExecuteScriptResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_script(self, client: Mobilerun) -> None:
        with client.devices.browser.with_streaming_response.execute_script(
            device_id="deviceId",
            script="script",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = response.parse()
            assert_matches_type(BrowserExecuteScriptResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute_script(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.browser.with_raw_response.execute_script(
                device_id="",
                script="script",
            )


class TestAsyncBrowser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_script(self, async_client: AsyncMobilerun) -> None:
        browser = await async_client.devices.browser.execute_script(
            device_id="deviceId",
            script="script",
        )
        assert_matches_type(BrowserExecuteScriptResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_script_with_all_params(self, async_client: AsyncMobilerun) -> None:
        browser = await async_client.devices.browser.execute_script(
            device_id="deviceId",
            script="script",
            x_device_display_id=0,
        )
        assert_matches_type(BrowserExecuteScriptResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_script(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.browser.with_raw_response.execute_script(
            device_id="deviceId",
            script="script",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser = await response.parse()
        assert_matches_type(BrowserExecuteScriptResponse, browser, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_script(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.browser.with_streaming_response.execute_script(
            device_id="deviceId",
            script="script",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser = await response.parse()
            assert_matches_type(BrowserExecuteScriptResponse, browser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute_script(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.browser.with_raw_response.execute_script(
                device_id="",
                script="script",
            )
