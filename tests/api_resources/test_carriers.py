# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mobilerun import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun.types import (
    Carrier,
    CarrierListResponse,
    CarrierDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCarriers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        carrier = client.carriers.create(
            country="x",
            mcc="x",
            mnc="x",
            operator="x",
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        carrier = client.carriers.create(
            country="x",
            mcc="x",
            mnc="x",
            operator="x",
            company="company",
            country_code="country_code",
            country_iso="xx",
            detail_url="detail_url",
            gsm_bands="gsm_bands",
            lte_bands="lte_bands",
            mobile_prefix="mobile_prefix",
            nsn_size="nsn_size",
            number_format="number_format",
            protocols="protocols",
            umts_bands="umts_bands",
            website="website",
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.carriers.with_raw_response.create(
            country="x",
            mcc="x",
            mnc="x",
            operator="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = response.parse()
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.carriers.with_streaming_response.create(
            country="x",
            mcc="x",
            mnc="x",
            operator="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = response.parse()
            assert_matches_type(Carrier, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        carrier = client.carriers.retrieve(
            1,
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.carriers.with_raw_response.retrieve(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = response.parse()
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.carriers.with_streaming_response.retrieve(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = response.parse()
            assert_matches_type(Carrier, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Mobilerun) -> None:
        carrier = client.carriers.update(
            carrier_id=1,
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Mobilerun) -> None:
        carrier = client.carriers.update(
            carrier_id=1,
            company="company",
            country="country",
            country_code="country_code",
            country_iso="xx",
            detail_url="detail_url",
            gsm_bands="gsm_bands",
            lte_bands="lte_bands",
            mobile_prefix="mobile_prefix",
            nsn_size="nsn_size",
            number_format="number_format",
            operator="operator",
            protocols="protocols",
            umts_bands="umts_bands",
            website="website",
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Mobilerun) -> None:
        response = client.carriers.with_raw_response.update(
            carrier_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = response.parse()
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Mobilerun) -> None:
        with client.carriers.with_streaming_response.update(
            carrier_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = response.parse()
            assert_matches_type(Carrier, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        carrier = client.carriers.list()
        assert_matches_type(CarrierListResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        carrier = client.carriers.list(
            country="country",
            country_iso="xx",
            order_by="id",
            order_dir="asc",
            page=1,
            page_size=1,
        )
        assert_matches_type(CarrierListResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.carriers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = response.parse()
        assert_matches_type(CarrierListResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.carriers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = response.parse()
            assert_matches_type(CarrierListResponse, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        carrier = client.carriers.delete(
            1,
        )
        assert_matches_type(CarrierDeleteResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.carriers.with_raw_response.delete(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = response.parse()
        assert_matches_type(CarrierDeleteResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.carriers.with_streaming_response.delete(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = response.parse()
            assert_matches_type(CarrierDeleteResponse, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup(self, client: Mobilerun) -> None:
        carrier = client.carriers.lookup(
            mcc="x",
            mnc="x",
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup(self, client: Mobilerun) -> None:
        response = client.carriers.with_raw_response.lookup(
            mcc="x",
            mnc="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = response.parse()
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup(self, client: Mobilerun) -> None:
        with client.carriers.with_streaming_response.lookup(
            mcc="x",
            mnc="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = response.parse()
            assert_matches_type(Carrier, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCarriers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        carrier = await async_client.carriers.create(
            country="x",
            mcc="x",
            mnc="x",
            operator="x",
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        carrier = await async_client.carriers.create(
            country="x",
            mcc="x",
            mnc="x",
            operator="x",
            company="company",
            country_code="country_code",
            country_iso="xx",
            detail_url="detail_url",
            gsm_bands="gsm_bands",
            lte_bands="lte_bands",
            mobile_prefix="mobile_prefix",
            nsn_size="nsn_size",
            number_format="number_format",
            protocols="protocols",
            umts_bands="umts_bands",
            website="website",
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.carriers.with_raw_response.create(
            country="x",
            mcc="x",
            mnc="x",
            operator="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = await response.parse()
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.carriers.with_streaming_response.create(
            country="x",
            mcc="x",
            mnc="x",
            operator="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = await response.parse()
            assert_matches_type(Carrier, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        carrier = await async_client.carriers.retrieve(
            1,
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.carriers.with_raw_response.retrieve(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = await response.parse()
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.carriers.with_streaming_response.retrieve(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = await response.parse()
            assert_matches_type(Carrier, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMobilerun) -> None:
        carrier = await async_client.carriers.update(
            carrier_id=1,
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMobilerun) -> None:
        carrier = await async_client.carriers.update(
            carrier_id=1,
            company="company",
            country="country",
            country_code="country_code",
            country_iso="xx",
            detail_url="detail_url",
            gsm_bands="gsm_bands",
            lte_bands="lte_bands",
            mobile_prefix="mobile_prefix",
            nsn_size="nsn_size",
            number_format="number_format",
            operator="operator",
            protocols="protocols",
            umts_bands="umts_bands",
            website="website",
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.carriers.with_raw_response.update(
            carrier_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = await response.parse()
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMobilerun) -> None:
        async with async_client.carriers.with_streaming_response.update(
            carrier_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = await response.parse()
            assert_matches_type(Carrier, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        carrier = await async_client.carriers.list()
        assert_matches_type(CarrierListResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        carrier = await async_client.carriers.list(
            country="country",
            country_iso="xx",
            order_by="id",
            order_dir="asc",
            page=1,
            page_size=1,
        )
        assert_matches_type(CarrierListResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.carriers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = await response.parse()
        assert_matches_type(CarrierListResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.carriers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = await response.parse()
            assert_matches_type(CarrierListResponse, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        carrier = await async_client.carriers.delete(
            1,
        )
        assert_matches_type(CarrierDeleteResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.carriers.with_raw_response.delete(
            1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = await response.parse()
        assert_matches_type(CarrierDeleteResponse, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.carriers.with_streaming_response.delete(
            1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = await response.parse()
            assert_matches_type(CarrierDeleteResponse, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup(self, async_client: AsyncMobilerun) -> None:
        carrier = await async_client.carriers.lookup(
            mcc="x",
            mnc="x",
        )
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.carriers.with_raw_response.lookup(
            mcc="x",
            mnc="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        carrier = await response.parse()
        assert_matches_type(Carrier, carrier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncMobilerun) -> None:
        async with async_client.carriers.with_streaming_response.lookup(
            mcc="x",
            mnc="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            carrier = await response.parse()
            assert_matches_type(Carrier, carrier, path=["response"])

        assert cast(Any, response.is_closed) is True
