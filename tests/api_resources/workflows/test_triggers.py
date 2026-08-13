# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.workflows import (
    TriggerFireResponse,
    TriggerListResponse,
    TriggerCreateResponse,
    TriggerDeleteResponse,
    TriggerUpdateResponse,
    TriggerRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTriggers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        trigger = client.workflows.triggers.create(
            activation="event",
            name="x",
        )
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        trigger = client.workflows.triggers.create(
            activation="event",
            name="x",
            conditions={
                "all": [{}],
                "any": [{}],
            },
            custom_payload_schema={"foo": "bar"},
            description="description",
            event_type="eventType",
            schedule_rule={
                "type": "once",
                "date_time": "dateTime",
                "expression": "expression",
                "jitter": {
                    "after_minutes": 0,
                    "before_minutes": 0,
                },
                "rrule": "rrule",
            },
            timezone="timezone",
        )
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.workflows.triggers.with_raw_response.create(
            activation="event",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.workflows.triggers.with_streaming_response.create(
            activation="event",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        trigger = client.workflows.triggers.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TriggerRetrieveResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.workflows.triggers.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerRetrieveResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.workflows.triggers.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerRetrieveResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.workflows.triggers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Mobilerun) -> None:
        trigger = client.workflows.triggers.update(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Mobilerun) -> None:
        trigger = client.workflows.triggers.update(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation="event",
            conditions={
                "all": [{}],
                "any": [{}],
            },
            custom_payload_schema={"foo": "bar"},
            description="description",
            event_type="eventType",
            name="x",
            schedule_rule={
                "type": "once",
                "date_time": "dateTime",
                "expression": "expression",
                "jitter": {
                    "after_minutes": 0,
                    "before_minutes": 0,
                },
                "rrule": "rrule",
            },
            timezone="timezone",
        )
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Mobilerun) -> None:
        response = client.workflows.triggers.with_raw_response.update(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Mobilerun) -> None:
        with client.workflows.triggers.with_streaming_response.update(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.workflows.triggers.with_raw_response.update(
                trigger_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        trigger = client.workflows.triggers.list()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        trigger = client.workflows.triggers.list(
            activation="event",
            event_type="eventType",
            order_by="name",
            order_by_direction="asc",
            page=1,
            page_size=1,
            search="x",
        )
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.workflows.triggers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.workflows.triggers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerListResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        trigger = client.workflows.triggers.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TriggerDeleteResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.workflows.triggers.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerDeleteResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.workflows.triggers.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerDeleteResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.workflows.triggers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fire(self, client: Mobilerun) -> None:
        trigger = client.workflows.triggers.fire(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={"foo": "bar"},
        )
        assert_matches_type(TriggerFireResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fire(self, client: Mobilerun) -> None:
        response = client.workflows.triggers.with_raw_response.fire(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = response.parse()
        assert_matches_type(TriggerFireResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fire(self, client: Mobilerun) -> None:
        with client.workflows.triggers.with_streaming_response.fire(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = response.parse()
            assert_matches_type(TriggerFireResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_fire(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            client.workflows.triggers.with_raw_response.fire(
                trigger_id="",
                payload={"foo": "bar"},
            )


class TestAsyncTriggers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        trigger = await async_client.workflows.triggers.create(
            activation="event",
            name="x",
        )
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        trigger = await async_client.workflows.triggers.create(
            activation="event",
            name="x",
            conditions={
                "all": [{}],
                "any": [{}],
            },
            custom_payload_schema={"foo": "bar"},
            description="description",
            event_type="eventType",
            schedule_rule={
                "type": "once",
                "date_time": "dateTime",
                "expression": "expression",
                "jitter": {
                    "after_minutes": 0,
                    "before_minutes": 0,
                },
                "rrule": "rrule",
            },
            timezone="timezone",
        )
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.triggers.with_raw_response.create(
            activation="event",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.triggers.with_streaming_response.create(
            activation="event",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerCreateResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        trigger = await async_client.workflows.triggers.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TriggerRetrieveResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.triggers.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerRetrieveResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.triggers.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerRetrieveResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.workflows.triggers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMobilerun) -> None:
        trigger = await async_client.workflows.triggers.update(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMobilerun) -> None:
        trigger = await async_client.workflows.triggers.update(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation="event",
            conditions={
                "all": [{}],
                "any": [{}],
            },
            custom_payload_schema={"foo": "bar"},
            description="description",
            event_type="eventType",
            name="x",
            schedule_rule={
                "type": "once",
                "date_time": "dateTime",
                "expression": "expression",
                "jitter": {
                    "after_minutes": 0,
                    "before_minutes": 0,
                },
                "rrule": "rrule",
            },
            timezone="timezone",
        )
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.triggers.with_raw_response.update(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.triggers.with_streaming_response.update(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerUpdateResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.workflows.triggers.with_raw_response.update(
                trigger_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        trigger = await async_client.workflows.triggers.list()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        trigger = await async_client.workflows.triggers.list(
            activation="event",
            event_type="eventType",
            order_by="name",
            order_by_direction="asc",
            page=1,
            page_size=1,
            search="x",
        )
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.triggers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerListResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.triggers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerListResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        trigger = await async_client.workflows.triggers.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TriggerDeleteResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.triggers.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerDeleteResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.triggers.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerDeleteResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.workflows.triggers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fire(self, async_client: AsyncMobilerun) -> None:
        trigger = await async_client.workflows.triggers.fire(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={"foo": "bar"},
        )
        assert_matches_type(TriggerFireResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fire(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.triggers.with_raw_response.fire(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger = await response.parse()
        assert_matches_type(TriggerFireResponse, trigger, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fire(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.triggers.with_streaming_response.fire(
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger = await response.parse()
            assert_matches_type(TriggerFireResponse, trigger, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_fire(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trigger_id` but received ''"):
            await async_client.workflows.triggers.with_raw_response.fire(
                trigger_id="",
                payload={"foo": "bar"},
            )
