# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from mobilerun import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun.types.devices import (
    EsimListResponse,
    EsimActivateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEsim:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        esim = client.devices.esim.list(
            device_id="deviceId",
        )
        assert_matches_type(Optional[EsimListResponse], esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        esim = client.devices.esim.list(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(Optional[EsimListResponse], esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.devices.esim.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(Optional[EsimListResponse], esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.devices.esim.with_streaming_response.list(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(Optional[EsimListResponse], esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.esim.with_raw_response.list(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activate(self, client: Mobilerun) -> None:
        esim = client.devices.esim.activate(
            device_id="deviceId",
            enable=True,
            matching_id="matchingId",
            sm_dp_addr="smDpAddr",
        )
        assert_matches_type(EsimActivateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activate_with_all_params(self, client: Mobilerun) -> None:
        esim = client.devices.esim.activate(
            device_id="deviceId",
            enable=True,
            matching_id="matchingId",
            sm_dp_addr="smDpAddr",
            x_device_display_id=0,
        )
        assert_matches_type(EsimActivateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_activate(self, client: Mobilerun) -> None:
        response = client.devices.esim.with_raw_response.activate(
            device_id="deviceId",
            enable=True,
            matching_id="matchingId",
            sm_dp_addr="smDpAddr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimActivateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_activate(self, client: Mobilerun) -> None:
        with client.devices.esim.with_streaming_response.activate(
            device_id="deviceId",
            enable=True,
            matching_id="matchingId",
            sm_dp_addr="smDpAddr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimActivateResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_activate(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.esim.with_raw_response.activate(
                device_id="",
                enable=True,
                matching_id="matchingId",
                sm_dp_addr="smDpAddr",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable(self, client: Mobilerun) -> None:
        esim = client.devices.esim.enable(
            device_id="deviceId",
            sub_id=0,
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable_with_all_params(self, client: Mobilerun) -> None:
        esim = client.devices.esim.enable(
            device_id="deviceId",
            sub_id=0,
            x_device_display_id=0,
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enable(self, client: Mobilerun) -> None:
        response = client.devices.esim.with_raw_response.enable(
            device_id="deviceId",
            sub_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enable(self, client: Mobilerun) -> None:
        with client.devices.esim.with_streaming_response.enable(
            device_id="deviceId",
            sub_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert esim is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_enable(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.esim.with_raw_response.enable(
                device_id="",
                sub_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Mobilerun) -> None:
        esim = client.devices.esim.remove(
            device_id="deviceId",
            sub_id=0,
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_with_all_params(self, client: Mobilerun) -> None:
        esim = client.devices.esim.remove(
            device_id="deviceId",
            sub_id=0,
            x_device_display_id=0,
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Mobilerun) -> None:
        response = client.devices.esim.with_raw_response.remove(
            device_id="deviceId",
            sub_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Mobilerun) -> None:
        with client.devices.esim.with_streaming_response.remove(
            device_id="deviceId",
            sub_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert esim is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.esim.with_raw_response.remove(
                device_id="",
                sub_id=0,
            )


class TestAsyncEsim:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.devices.esim.list(
            device_id="deviceId",
        )
        assert_matches_type(Optional[EsimListResponse], esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.devices.esim.list(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(Optional[EsimListResponse], esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.esim.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(Optional[EsimListResponse], esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.esim.with_streaming_response.list(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(Optional[EsimListResponse], esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.esim.with_raw_response.list(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activate(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.devices.esim.activate(
            device_id="deviceId",
            enable=True,
            matching_id="matchingId",
            sm_dp_addr="smDpAddr",
        )
        assert_matches_type(EsimActivateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activate_with_all_params(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.devices.esim.activate(
            device_id="deviceId",
            enable=True,
            matching_id="matchingId",
            sm_dp_addr="smDpAddr",
            x_device_display_id=0,
        )
        assert_matches_type(EsimActivateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.esim.with_raw_response.activate(
            device_id="deviceId",
            enable=True,
            matching_id="matchingId",
            sm_dp_addr="smDpAddr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimActivateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.esim.with_streaming_response.activate(
            device_id="deviceId",
            enable=True,
            matching_id="matchingId",
            sm_dp_addr="smDpAddr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimActivateResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_activate(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.esim.with_raw_response.activate(
                device_id="",
                enable=True,
                matching_id="matchingId",
                sm_dp_addr="smDpAddr",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.devices.esim.enable(
            device_id="deviceId",
            sub_id=0,
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable_with_all_params(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.devices.esim.enable(
            device_id="deviceId",
            sub_id=0,
            x_device_display_id=0,
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.esim.with_raw_response.enable(
            device_id="deviceId",
            sub_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.esim.with_streaming_response.enable(
            device_id="deviceId",
            sub_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert esim is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_enable(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.esim.with_raw_response.enable(
                device_id="",
                sub_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.devices.esim.remove(
            device_id="deviceId",
            sub_id=0,
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.devices.esim.remove(
            device_id="deviceId",
            sub_id=0,
            x_device_display_id=0,
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.esim.with_raw_response.remove(
            device_id="deviceId",
            sub_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.esim.with_streaming_response.remove(
            device_id="deviceId",
            sub_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert esim is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.esim.with_raw_response.remove(
                device_id="",
                sub_id=0,
            )
