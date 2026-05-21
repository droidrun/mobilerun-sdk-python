# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types import (
    Profile,
    ProfileListResponse,
    ProfileDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        profile = client.profiles.create(
            name="x",
            spec={},
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        profile = client.profiles.create(
            name="x",
            spec={
                "android_version": 0,
                "apps": ["string"],
                "carrier": {
                    "gsm_operator_alpha": "GsmOperatorAlpha",
                    "gsm_operator_numeric": 0,
                    "gsm_sim_operator_alpha": "GsmSimOperatorAlpha",
                    "gsm_sim_operator_iso_country": "GsmSimOperatorIsoCountry",
                    "gsm_sim_operator_numeric": 0,
                    "persist_sys_timezone": "PersistSysTimezone",
                },
                "country": "country",
                "files": ["string"],
                "identifiers": {
                    "bootloader_serial_number": "BootloaderSerialNumber",
                    "identifier_android_id": "IdentifierAndroidID",
                    "identifier_app_set_id": "IdentifierAppSetID",
                    "identifier_bluetooth_mac": "IdentifierBluetoothMAC",
                    "identifier_gaid": "IdentifierGAID",
                    "identifier_gsfid": "IdentifierGSFID",
                    "identifier_iccid": "IdentifierICCID",
                    "identifier_imei": "IdentifierIMEI",
                    "identifier_imsi": "IdentifierIMSI",
                    "identifier_media_drmid": "IdentifierMediaDRMID",
                    "identifier_meid": "IdentifierMEID",
                    "identifier_phone_number": "IdentifierPhoneNumber",
                    "identifier_serial": "IdentifierSerial",
                    "identifier_wifi_mac": "IdentifierWifiMAC",
                    "serial_number": "SerialNumber",
                },
                "locale": "locale",
                "location": {
                    "latitude": 0,
                    "longitude": 0,
                },
                "name": "name",
                "proxy": {
                    "name": "name",
                    "smart_ip": True,
                    "socks5": {
                        "host": "host",
                        "password": "password",
                        "port": 0,
                        "user": "user",
                    },
                },
                "timezone": "timezone",
            },
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.profiles.with_raw_response.create(
            name="x",
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.profiles.with_streaming_response.create(
            name="x",
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        profile = client.profiles.retrieve(
            "profileId",
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.profiles.with_raw_response.retrieve(
            "profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.profiles.with_streaming_response.retrieve(
            "profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Mobilerun) -> None:
        profile = client.profiles.update(
            profile_id="profileId",
            name="x",
            spec={},
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Mobilerun) -> None:
        profile = client.profiles.update(
            profile_id="profileId",
            name="x",
            spec={
                "android_version": 0,
                "apps": ["string"],
                "carrier": {
                    "gsm_operator_alpha": "GsmOperatorAlpha",
                    "gsm_operator_numeric": 0,
                    "gsm_sim_operator_alpha": "GsmSimOperatorAlpha",
                    "gsm_sim_operator_iso_country": "GsmSimOperatorIsoCountry",
                    "gsm_sim_operator_numeric": 0,
                    "persist_sys_timezone": "PersistSysTimezone",
                },
                "country": "country",
                "files": ["string"],
                "identifiers": {
                    "bootloader_serial_number": "BootloaderSerialNumber",
                    "identifier_android_id": "IdentifierAndroidID",
                    "identifier_app_set_id": "IdentifierAppSetID",
                    "identifier_bluetooth_mac": "IdentifierBluetoothMAC",
                    "identifier_gaid": "IdentifierGAID",
                    "identifier_gsfid": "IdentifierGSFID",
                    "identifier_iccid": "IdentifierICCID",
                    "identifier_imei": "IdentifierIMEI",
                    "identifier_imsi": "IdentifierIMSI",
                    "identifier_media_drmid": "IdentifierMediaDRMID",
                    "identifier_meid": "IdentifierMEID",
                    "identifier_phone_number": "IdentifierPhoneNumber",
                    "identifier_serial": "IdentifierSerial",
                    "identifier_wifi_mac": "IdentifierWifiMAC",
                    "serial_number": "SerialNumber",
                },
                "locale": "locale",
                "location": {
                    "latitude": 0,
                    "longitude": 0,
                },
                "name": "name",
                "proxy": {
                    "name": "name",
                    "smart_ip": True,
                    "socks5": {
                        "host": "host",
                        "password": "password",
                        "port": 0,
                        "user": "user",
                    },
                },
                "timezone": "timezone",
            },
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Mobilerun) -> None:
        response = client.profiles.with_raw_response.update(
            profile_id="profileId",
            name="x",
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Mobilerun) -> None:
        with client.profiles.with_streaming_response.update(
            profile_id="profileId",
            name="x",
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.update(
                profile_id="",
                name="x",
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        profile = client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        profile = client.profiles.list(
            name="name",
            order_by="name",
            order_by_direction="asc",
            page=0,
            page_size=0,
        )
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        profile = client.profiles.delete(
            "profileId",
        )
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.profiles.with_raw_response.delete(
            "profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.profiles.with_streaming_response.delete(
            "profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.delete(
                "",
            )


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.profiles.create(
            name="x",
            spec={},
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.profiles.create(
            name="x",
            spec={
                "android_version": 0,
                "apps": ["string"],
                "carrier": {
                    "gsm_operator_alpha": "GsmOperatorAlpha",
                    "gsm_operator_numeric": 0,
                    "gsm_sim_operator_alpha": "GsmSimOperatorAlpha",
                    "gsm_sim_operator_iso_country": "GsmSimOperatorIsoCountry",
                    "gsm_sim_operator_numeric": 0,
                    "persist_sys_timezone": "PersistSysTimezone",
                },
                "country": "country",
                "files": ["string"],
                "identifiers": {
                    "bootloader_serial_number": "BootloaderSerialNumber",
                    "identifier_android_id": "IdentifierAndroidID",
                    "identifier_app_set_id": "IdentifierAppSetID",
                    "identifier_bluetooth_mac": "IdentifierBluetoothMAC",
                    "identifier_gaid": "IdentifierGAID",
                    "identifier_gsfid": "IdentifierGSFID",
                    "identifier_iccid": "IdentifierICCID",
                    "identifier_imei": "IdentifierIMEI",
                    "identifier_imsi": "IdentifierIMSI",
                    "identifier_media_drmid": "IdentifierMediaDRMID",
                    "identifier_meid": "IdentifierMEID",
                    "identifier_phone_number": "IdentifierPhoneNumber",
                    "identifier_serial": "IdentifierSerial",
                    "identifier_wifi_mac": "IdentifierWifiMAC",
                    "serial_number": "SerialNumber",
                },
                "locale": "locale",
                "location": {
                    "latitude": 0,
                    "longitude": 0,
                },
                "name": "name",
                "proxy": {
                    "name": "name",
                    "smart_ip": True,
                    "socks5": {
                        "host": "host",
                        "password": "password",
                        "port": 0,
                        "user": "user",
                    },
                },
                "timezone": "timezone",
            },
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.profiles.with_raw_response.create(
            name="x",
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.profiles.with_streaming_response.create(
            name="x",
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.profiles.retrieve(
            "profileId",
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.profiles.with_raw_response.retrieve(
            "profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.profiles.with_streaming_response.retrieve(
            "profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.profiles.update(
            profile_id="profileId",
            name="x",
            spec={},
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.profiles.update(
            profile_id="profileId",
            name="x",
            spec={
                "android_version": 0,
                "apps": ["string"],
                "carrier": {
                    "gsm_operator_alpha": "GsmOperatorAlpha",
                    "gsm_operator_numeric": 0,
                    "gsm_sim_operator_alpha": "GsmSimOperatorAlpha",
                    "gsm_sim_operator_iso_country": "GsmSimOperatorIsoCountry",
                    "gsm_sim_operator_numeric": 0,
                    "persist_sys_timezone": "PersistSysTimezone",
                },
                "country": "country",
                "files": ["string"],
                "identifiers": {
                    "bootloader_serial_number": "BootloaderSerialNumber",
                    "identifier_android_id": "IdentifierAndroidID",
                    "identifier_app_set_id": "IdentifierAppSetID",
                    "identifier_bluetooth_mac": "IdentifierBluetoothMAC",
                    "identifier_gaid": "IdentifierGAID",
                    "identifier_gsfid": "IdentifierGSFID",
                    "identifier_iccid": "IdentifierICCID",
                    "identifier_imei": "IdentifierIMEI",
                    "identifier_imsi": "IdentifierIMSI",
                    "identifier_media_drmid": "IdentifierMediaDRMID",
                    "identifier_meid": "IdentifierMEID",
                    "identifier_phone_number": "IdentifierPhoneNumber",
                    "identifier_serial": "IdentifierSerial",
                    "identifier_wifi_mac": "IdentifierWifiMAC",
                    "serial_number": "SerialNumber",
                },
                "locale": "locale",
                "location": {
                    "latitude": 0,
                    "longitude": 0,
                },
                "name": "name",
                "proxy": {
                    "name": "name",
                    "smart_ip": True,
                    "socks5": {
                        "host": "host",
                        "password": "password",
                        "port": 0,
                        "user": "user",
                    },
                },
                "timezone": "timezone",
            },
        )
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.profiles.with_raw_response.update(
            profile_id="profileId",
            name="x",
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(Profile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMobilerun) -> None:
        async with async_client.profiles.with_streaming_response.update(
            profile_id="profileId",
            name="x",
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(Profile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.update(
                profile_id="",
                name="x",
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.profiles.list(
            name="name",
            order_by="name",
            order_by_direction="asc",
            page=0,
            page_size=0,
        )
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        profile = await async_client.profiles.delete(
            "profileId",
        )
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.profiles.with_raw_response.delete(
            "profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.profiles.with_streaming_response.delete(
            "profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.delete(
                "",
            )
