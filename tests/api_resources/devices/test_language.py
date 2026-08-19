# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from mobilerun_sdk.types.devices import LanguageGetResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types.devices import language_set_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestLanguage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Mobilerun) -> None:
        language = client.devices.language.get(
            device_id="deviceId",
        )
        assert_matches_type(LanguageGetResponse, language, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Mobilerun) -> None:
        language = client.devices.language.get(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(LanguageGetResponse, language, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Mobilerun) -> None:

        response = client.devices.language.with_raw_response.get(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        language = response.parse()
        assert_matches_type(LanguageGetResponse, language, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Mobilerun) -> None:
        with client.devices.language.with_streaming_response.get(
            device_id="deviceId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            language = response.parse()
            assert_matches_type(LanguageGetResponse, language, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.language.with_raw_response.get(
              device_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set(self, client: Mobilerun) -> None:
        language = client.devices.language.set(
            device_id="deviceId",
            locale="sqf-Kkif-BB",
        )
        assert language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_with_all_params(self, client: Mobilerun) -> None:
        language = client.devices.language.set(
            device_id="deviceId",
            locale="sqf-Kkif-BB",
            restart=True,
            x_device_display_id=0,
        )
        assert language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: Mobilerun) -> None:

        response = client.devices.language.with_raw_response.set(
            device_id="deviceId",
            locale="sqf-Kkif-BB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        language = response.parse()
        assert language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: Mobilerun) -> None:
        with client.devices.language.with_streaming_response.set(
            device_id="deviceId",
            locale="sqf-Kkif-BB",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            language = response.parse()
            assert language is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.language.with_raw_response.set(
              device_id="",
              locale="sqf-Kkif-BB",
          )
class TestAsyncLanguage:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncMobilerun) -> None:
        language = await async_client.devices.language.get(
            device_id="deviceId",
        )
        assert_matches_type(LanguageGetResponse, language, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncMobilerun) -> None:
        language = await async_client.devices.language.get(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(LanguageGetResponse, language, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.language.with_raw_response.get(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        language = await response.parse()
        assert_matches_type(LanguageGetResponse, language, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.language.with_streaming_response.get(
            device_id="deviceId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            language = await response.parse()
            assert_matches_type(LanguageGetResponse, language, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.language.with_raw_response.get(
              device_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncMobilerun) -> None:
        language = await async_client.devices.language.set(
            device_id="deviceId",
            locale="sqf-Kkif-BB",
        )
        assert language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncMobilerun) -> None:
        language = await async_client.devices.language.set(
            device_id="deviceId",
            locale="sqf-Kkif-BB",
            restart=True,
            x_device_display_id=0,
        )
        assert language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.language.with_raw_response.set(
            device_id="deviceId",
            locale="sqf-Kkif-BB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        language = await response.parse()
        assert language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.language.with_streaming_response.set(
            device_id="deviceId",
            locale="sqf-Kkif-BB",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            language = await response.parse()
            assert language is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.language.with_raw_response.set(
              device_id="",
              locale="sqf-Kkif-BB",
          )