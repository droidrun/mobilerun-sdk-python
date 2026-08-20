# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types import (
    EsimListResponse,
    EsimCreateResponse,
    EsimImportResponse,
    EsimUpdateResponse,
    EsimInstallResponse,
    EsimCapacityResponse,
    EsimRetrieveResponse,
    EsimSelectorResponse,
    EsimInstallStatusResponse,
    EsimConfirmPaymentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEsims:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        esim = client.esims.create()
        assert_matches_type(EsimCreateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        esim = client.esims.create(
            idempotency_key="idempotencyKey",
        )
        assert_matches_type(EsimCreateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimCreateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimCreateResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        esim = client.esims.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimRetrieveResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimRetrieveResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimRetrieveResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.esims.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Mobilerun) -> None:
        esim = client.esims.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimUpdateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Mobilerun) -> None:
        esim = client.esims.update(
            id="550e8400-e29b-41d4-a716-446655440000",
            msisdn="+33612345678",
            name="Mom's phone",
        )
        assert_matches_type(EsimUpdateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimUpdateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimUpdateResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.esims.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        esim = client.esims.list()
        assert_matches_type(EsimListResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        esim = client.esims.list(
            mine="true",
            page=1,
            page_size=1,
            status="all",
        )
        assert_matches_type(EsimListResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimListResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimListResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        esim = client.esims.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert esim is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.esims.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_capacity(self, client: Mobilerun) -> None:
        esim = client.esims.capacity()
        assert_matches_type(EsimCapacityResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_capacity(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.capacity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimCapacityResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_capacity(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.capacity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimCapacityResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_confirm_payment(self, client: Mobilerun) -> None:
        esim = client.esims.confirm_payment(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimConfirmPaymentResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_confirm_payment(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.confirm_payment(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimConfirmPaymentResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_confirm_payment(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.confirm_payment(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimConfirmPaymentResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_confirm_payment(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.esims.with_raw_response.confirm_payment(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import(self, client: Mobilerun) -> None:
        esim = client.esims.import_()
        assert_matches_type(EsimImportResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_with_all_params(self, client: Mobilerun) -> None:
        esim = client.esims.import_(
            auto_install=True,
            carrier_name="carrierName",
            confirmation_code="confirmationCode",
            country_code="countryCode",
            device_id="physedge-dev-8f3a2c",
            idempotency_key="x",
            lpa_code="LPA:1$smdp.example.com$QR-MATCH-1",
            matching_id="matchingId",
            msisdn="+33612345678",
            name="Mom's phone",
            notes="notes",
            smdp_address="smdp.example.com",
        )
        assert_matches_type(EsimImportResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.import_()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimImportResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.import_() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimImportResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_install(self, client: Mobilerun) -> None:
        esim = client.esims.install(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimInstallResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_install_with_all_params(self, client: Mobilerun) -> None:
        esim = client.esims.install(
            id="550e8400-e29b-41d4-a716-446655440000",
            device_id="physedge-dev-8f3a2c",
        )
        assert_matches_type(EsimInstallResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_install(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.install(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimInstallResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_install(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.install(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimInstallResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_install(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.esims.with_raw_response.install(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_install_status(self, client: Mobilerun) -> None:
        esim = client.esims.install_status(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimInstallStatusResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_install_status(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.install_status(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimInstallStatusResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_install_status(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.install_status(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimInstallStatusResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_install_status(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.esims.with_raw_response.install_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_selector(self, client: Mobilerun) -> None:
        esim = client.esims.selector()
        assert_matches_type(EsimSelectorResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_selector(self, client: Mobilerun) -> None:
        response = client.esims.with_raw_response.selector()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = response.parse()
        assert_matches_type(EsimSelectorResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_selector(self, client: Mobilerun) -> None:
        with client.esims.with_streaming_response.selector() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = response.parse()
            assert_matches_type(EsimSelectorResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEsims:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.create()
        assert_matches_type(EsimCreateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.create(
            idempotency_key="idempotencyKey",
        )
        assert_matches_type(EsimCreateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimCreateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimCreateResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimRetrieveResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimRetrieveResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimRetrieveResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.esims.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimUpdateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.update(
            id="550e8400-e29b-41d4-a716-446655440000",
            msisdn="+33612345678",
            name="Mom's phone",
        )
        assert_matches_type(EsimUpdateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimUpdateResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.update(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimUpdateResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.esims.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.list()
        assert_matches_type(EsimListResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.list(
            mine="true",
            page=1,
            page_size=1,
            status="all",
        )
        assert_matches_type(EsimListResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimListResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimListResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert esim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.delete(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert esim is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.esims.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_capacity(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.capacity()
        assert_matches_type(EsimCapacityResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_capacity(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.capacity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimCapacityResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_capacity(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.capacity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimCapacityResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_confirm_payment(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.confirm_payment(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimConfirmPaymentResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_confirm_payment(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.confirm_payment(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimConfirmPaymentResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_confirm_payment(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.confirm_payment(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimConfirmPaymentResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_confirm_payment(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.esims.with_raw_response.confirm_payment(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.import_()
        assert_matches_type(EsimImportResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.import_(
            auto_install=True,
            carrier_name="carrierName",
            confirmation_code="confirmationCode",
            country_code="countryCode",
            device_id="physedge-dev-8f3a2c",
            idempotency_key="x",
            lpa_code="LPA:1$smdp.example.com$QR-MATCH-1",
            matching_id="matchingId",
            msisdn="+33612345678",
            name="Mom's phone",
            notes="notes",
            smdp_address="smdp.example.com",
        )
        assert_matches_type(EsimImportResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.import_()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimImportResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.import_() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimImportResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_install(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.install(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimInstallResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_install_with_all_params(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.install(
            id="550e8400-e29b-41d4-a716-446655440000",
            device_id="physedge-dev-8f3a2c",
        )
        assert_matches_type(EsimInstallResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_install(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.install(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimInstallResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_install(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.install(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimInstallResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_install(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.esims.with_raw_response.install(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_install_status(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.install_status(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(EsimInstallStatusResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_install_status(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.install_status(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimInstallStatusResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_install_status(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.install_status(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimInstallStatusResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_install_status(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.esims.with_raw_response.install_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_selector(self, async_client: AsyncMobilerun) -> None:
        esim = await async_client.esims.selector()
        assert_matches_type(EsimSelectorResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_selector(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.esims.with_raw_response.selector()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        esim = await response.parse()
        assert_matches_type(EsimSelectorResponse, esim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_selector(self, async_client: AsyncMobilerun) -> None:
        async with async_client.esims.with_streaming_response.selector() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            esim = await response.parse()
            assert_matches_type(EsimSelectorResponse, esim, path=["response"])

        assert cast(Any, response.is_closed) is True
