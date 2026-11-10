# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.devices import (
    NumberBindResponse,
    NumberUnbindResponse,
    NumberRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumber:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        number = client.devices.number.retrieve(
            device_id="deviceId",
        )
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Mobilerun) -> None:
        number = client.devices.number.retrieve(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.devices.number.with_raw_response.retrieve(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = response.parse()
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.devices.number.with_streaming_response.retrieve(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = response.parse()
            assert_matches_type(NumberRetrieveResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.number.with_raw_response.retrieve(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bind(self, client: Mobilerun) -> None:
        number = client.devices.number.bind(
            device_id="deviceId",
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NumberBindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bind_with_all_params(self, client: Mobilerun) -> None:
        number = client.devices.number.bind(
            device_id="deviceId",
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_device_display_id=0,
        )
        assert_matches_type(NumberBindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bind(self, client: Mobilerun) -> None:
        response = client.devices.number.with_raw_response.bind(
            device_id="deviceId",
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = response.parse()
        assert_matches_type(NumberBindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bind(self, client: Mobilerun) -> None:
        with client.devices.number.with_streaming_response.bind(
            device_id="deviceId",
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = response.parse()
            assert_matches_type(NumberBindResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_bind(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.number.with_raw_response.bind(
                device_id="",
                number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unbind(self, client: Mobilerun) -> None:
        number = client.devices.number.unbind(
            device_id="deviceId",
        )
        assert_matches_type(NumberUnbindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unbind_with_all_params(self, client: Mobilerun) -> None:
        number = client.devices.number.unbind(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(NumberUnbindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unbind(self, client: Mobilerun) -> None:
        response = client.devices.number.with_raw_response.unbind(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = response.parse()
        assert_matches_type(NumberUnbindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unbind(self, client: Mobilerun) -> None:
        with client.devices.number.with_streaming_response.unbind(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = response.parse()
            assert_matches_type(NumberUnbindResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unbind(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.number.with_raw_response.unbind(
                device_id="",
            )


class TestAsyncNumber:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        number = await async_client.devices.number.retrieve(
            device_id="deviceId",
        )
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMobilerun) -> None:
        number = await async_client.devices.number.retrieve(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.number.with_raw_response.retrieve(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = await response.parse()
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.number.with_streaming_response.retrieve(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = await response.parse()
            assert_matches_type(NumberRetrieveResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.number.with_raw_response.retrieve(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bind(self, async_client: AsyncMobilerun) -> None:
        number = await async_client.devices.number.bind(
            device_id="deviceId",
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NumberBindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bind_with_all_params(self, async_client: AsyncMobilerun) -> None:
        number = await async_client.devices.number.bind(
            device_id="deviceId",
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_device_display_id=0,
        )
        assert_matches_type(NumberBindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bind(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.number.with_raw_response.bind(
            device_id="deviceId",
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = await response.parse()
        assert_matches_type(NumberBindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bind(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.number.with_streaming_response.bind(
            device_id="deviceId",
            number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = await response.parse()
            assert_matches_type(NumberBindResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_bind(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.number.with_raw_response.bind(
                device_id="",
                number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unbind(self, async_client: AsyncMobilerun) -> None:
        number = await async_client.devices.number.unbind(
            device_id="deviceId",
        )
        assert_matches_type(NumberUnbindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unbind_with_all_params(self, async_client: AsyncMobilerun) -> None:
        number = await async_client.devices.number.unbind(
            device_id="deviceId",
            x_device_display_id=0,
        )
        assert_matches_type(NumberUnbindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unbind(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.number.with_raw_response.unbind(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = await response.parse()
        assert_matches_type(NumberUnbindResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unbind(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.number.with_streaming_response.unbind(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = await response.parse()
            assert_matches_type(NumberUnbindResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unbind(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.number.with_raw_response.unbind(
                device_id="",
            )
