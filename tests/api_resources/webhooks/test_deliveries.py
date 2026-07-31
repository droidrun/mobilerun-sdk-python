# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk._utils import parse_datetime
from mobilerun_sdk.types.webhooks import (
    DeliveryListResponse,
    DeliveryStatsResponse,
    DeliveryListForWebhookResponse,
    DeliveryRetrieveAttemptsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeliveries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        delivery = client.webhooks.deliveries.list()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        delivery = client.webhooks.deliveries.list(
            event_id="x",
            page=1,
            page_size=1,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.webhooks.deliveries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.webhooks.deliveries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_for_webhook(self, client: Mobilerun) -> None:
        delivery = client.webhooks.deliveries.list_for_webhook(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(DeliveryListForWebhookResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_for_webhook_with_all_params(self, client: Mobilerun) -> None:
        delivery = client.webhooks.deliveries.list_for_webhook(
            id="550e8400-e29b-41d4-a716-446655440000",
            event_id="x",
            page=1,
            page_size=1,
        )
        assert_matches_type(DeliveryListForWebhookResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_for_webhook(self, client: Mobilerun) -> None:
        response = client.webhooks.deliveries.with_raw_response.list_for_webhook(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryListForWebhookResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_for_webhook(self, client: Mobilerun) -> None:
        with client.webhooks.deliveries.with_streaming_response.list_for_webhook(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryListForWebhookResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_for_webhook(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.deliveries.with_raw_response.list_for_webhook(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_attempts(self, client: Mobilerun) -> None:
        delivery = client.webhooks.deliveries.retrieve_attempts(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(DeliveryRetrieveAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_attempts(self, client: Mobilerun) -> None:
        response = client.webhooks.deliveries.with_raw_response.retrieve_attempts(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryRetrieveAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_attempts(self, client: Mobilerun) -> None:
        with client.webhooks.deliveries.with_streaming_response.retrieve_attempts(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryRetrieveAttemptsResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_attempts(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.deliveries.with_raw_response.retrieve_attempts(
                delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.webhooks.deliveries.with_raw_response.retrieve_attempts(
                delivery_id="",
                id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stats(self, client: Mobilerun) -> None:
        delivery = client.webhooks.deliveries.stats()
        assert_matches_type(DeliveryStatsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stats_with_all_params(self, client: Mobilerun) -> None:
        delivery = client.webhooks.deliveries.stats(
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DeliveryStatsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stats(self, client: Mobilerun) -> None:
        response = client.webhooks.deliveries.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryStatsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stats(self, client: Mobilerun) -> None:
        with client.webhooks.deliveries.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryStatsResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeliveries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        delivery = await async_client.webhooks.deliveries.list()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        delivery = await async_client.webhooks.deliveries.list(
            event_id="x",
            page=1,
            page_size=1,
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="pending",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_for_webhook(self, async_client: AsyncMobilerun) -> None:
        delivery = await async_client.webhooks.deliveries.list_for_webhook(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(DeliveryListForWebhookResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_for_webhook_with_all_params(self, async_client: AsyncMobilerun) -> None:
        delivery = await async_client.webhooks.deliveries.list_for_webhook(
            id="550e8400-e29b-41d4-a716-446655440000",
            event_id="x",
            page=1,
            page_size=1,
        )
        assert_matches_type(DeliveryListForWebhookResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_for_webhook(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.list_for_webhook(
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryListForWebhookResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_for_webhook(self, async_client: AsyncMobilerun) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.list_for_webhook(
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryListForWebhookResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_for_webhook(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.list_for_webhook(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_attempts(self, async_client: AsyncMobilerun) -> None:
        delivery = await async_client.webhooks.deliveries.retrieve_attempts(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(DeliveryRetrieveAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_attempts(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.retrieve_attempts(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryRetrieveAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_attempts(self, async_client: AsyncMobilerun) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.retrieve_attempts(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryRetrieveAttemptsResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_attempts(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.retrieve_attempts(
                delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.retrieve_attempts(
                delivery_id="",
                id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stats(self, async_client: AsyncMobilerun) -> None:
        delivery = await async_client.webhooks.deliveries.stats()
        assert_matches_type(DeliveryStatsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stats_with_all_params(self, async_client: AsyncMobilerun) -> None:
        delivery = await async_client.webhooks.deliveries.stats(
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DeliveryStatsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryStatsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncMobilerun) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryStatsResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True
