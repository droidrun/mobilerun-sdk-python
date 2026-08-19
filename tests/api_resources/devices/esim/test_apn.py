# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from typing import Optional, cast, Any

from mobilerun_sdk.types.devices.esim import ApnListResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types.devices.esim import apn_select_params
from mobilerun_sdk.types.devices.esim import apn_set_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestApn:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        apn = client.devices.esim.apn.list(
            device_id="deviceId",
        )
        assert_matches_type(Optional[ApnListResponse], apn, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        apn = client.devices.esim.apn.list(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(Optional[ApnListResponse], apn, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:

        response = client.devices.esim.apn.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        apn = response.parse()
        assert_matches_type(Optional[ApnListResponse], apn, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.devices.esim.apn.with_streaming_response.list(
            device_id="deviceId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            apn = response.parse()
            assert_matches_type(Optional[ApnListResponse], apn, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.esim.apn.with_raw_response.list(
              device_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_select(self, client: Mobilerun) -> None:
        apn = client.devices.esim.apn.select(
            device_id="deviceId",
            apn_id=0,
            sub_id=0,
        )
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_select_with_all_params(self, client: Mobilerun) -> None:
        apn = client.devices.esim.apn.select(
            device_id="deviceId",
            apn_id=0,
            sub_id=0,
            x_device_display_id=0,
        )
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_select(self, client: Mobilerun) -> None:

        response = client.devices.esim.apn.with_raw_response.select(
            device_id="deviceId",
            apn_id=0,
            sub_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        apn = response.parse()
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_select(self, client: Mobilerun) -> None:
        with client.devices.esim.apn.with_streaming_response.select(
            device_id="deviceId",
            apn_id=0,
            sub_id=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            apn = response.parse()
            assert apn is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_select(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.esim.apn.with_raw_response.select(
              device_id="",
              apn_id=0,
              sub_id=0,
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set(self, client: Mobilerun) -> None:
        apn = client.devices.esim.apn.set(
            device_id="deviceId",
            apn="apn",
            mcc="mcc",
            mnc="mnc",
            name="name",
            protocol="protocol",
            roaming_protocol="roamingProtocol",
            sub_id=0,
            type="type",
        )
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_with_all_params(self, client: Mobilerun) -> None:
        apn = client.devices.esim.apn.set(
            device_id="deviceId",
            apn="apn",
            mcc="mcc",
            mnc="mnc",
            name="name",
            protocol="protocol",
            roaming_protocol="roamingProtocol",
            sub_id=0,
            type="type",
            x_device_display_id=0,
        )
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: Mobilerun) -> None:

        response = client.devices.esim.apn.with_raw_response.set(
            device_id="deviceId",
            apn="apn",
            mcc="mcc",
            mnc="mnc",
            name="name",
            protocol="protocol",
            roaming_protocol="roamingProtocol",
            sub_id=0,
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        apn = response.parse()
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: Mobilerun) -> None:
        with client.devices.esim.apn.with_streaming_response.set(
            device_id="deviceId",
            apn="apn",
            mcc="mcc",
            mnc="mnc",
            name="name",
            protocol="protocol",
            roaming_protocol="roamingProtocol",
            sub_id=0,
            type="type",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            apn = response.parse()
            assert apn is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.esim.apn.with_raw_response.set(
              device_id="",
              apn="apn",
              mcc="mcc",
              mnc="mnc",
              name="name",
              protocol="protocol",
              roaming_protocol="roamingProtocol",
              sub_id=0,
              type="type",
          )
class TestAsyncApn:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        apn = await async_client.devices.esim.apn.list(
            device_id="deviceId",
        )
        assert_matches_type(Optional[ApnListResponse], apn, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        apn = await async_client.devices.esim.apn.list(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(Optional[ApnListResponse], apn, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.esim.apn.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        apn = await response.parse()
        assert_matches_type(Optional[ApnListResponse], apn, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.esim.apn.with_streaming_response.list(
            device_id="deviceId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            apn = await response.parse()
            assert_matches_type(Optional[ApnListResponse], apn, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.esim.apn.with_raw_response.list(
              device_id="",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_select(self, async_client: AsyncMobilerun) -> None:
        apn = await async_client.devices.esim.apn.select(
            device_id="deviceId",
            apn_id=0,
            sub_id=0,
        )
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_select_with_all_params(self, async_client: AsyncMobilerun) -> None:
        apn = await async_client.devices.esim.apn.select(
            device_id="deviceId",
            apn_id=0,
            sub_id=0,
            x_device_display_id=0,
        )
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_select(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.esim.apn.with_raw_response.select(
            device_id="deviceId",
            apn_id=0,
            sub_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        apn = await response.parse()
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_select(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.esim.apn.with_streaming_response.select(
            device_id="deviceId",
            apn_id=0,
            sub_id=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            apn = await response.parse()
            assert apn is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_select(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.esim.apn.with_raw_response.select(
              device_id="",
              apn_id=0,
              sub_id=0,
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncMobilerun) -> None:
        apn = await async_client.devices.esim.apn.set(
            device_id="deviceId",
            apn="apn",
            mcc="mcc",
            mnc="mnc",
            name="name",
            protocol="protocol",
            roaming_protocol="roamingProtocol",
            sub_id=0,
            type="type",
        )
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncMobilerun) -> None:
        apn = await async_client.devices.esim.apn.set(
            device_id="deviceId",
            apn="apn",
            mcc="mcc",
            mnc="mnc",
            name="name",
            protocol="protocol",
            roaming_protocol="roamingProtocol",
            sub_id=0,
            type="type",
            x_device_display_id=0,
        )
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.esim.apn.with_raw_response.set(
            device_id="deviceId",
            apn="apn",
            mcc="mcc",
            mnc="mnc",
            name="name",
            protocol="protocol",
            roaming_protocol="roamingProtocol",
            sub_id=0,
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        apn = await response.parse()
        assert apn is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.esim.apn.with_streaming_response.set(
            device_id="deviceId",
            apn="apn",
            mcc="mcc",
            mnc="mnc",
            name="name",
            protocol="protocol",
            roaming_protocol="roamingProtocol",
            sub_id=0,
            type="type",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            apn = await response.parse()
            assert apn is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.esim.apn.with_raw_response.set(
              device_id="",
              apn="apn",
              mcc="mcc",
              mnc="mnc",
              name="name",
              protocol="protocol",
              roaming_protocol="roamingProtocol",
              sub_id=0,
              type="type",
          )