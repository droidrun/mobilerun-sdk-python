# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.agents import (
    RoutineCloneResponse,
    RoutineCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        routine = client.agents.routines.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                }
            ],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RoutineCreateResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        routine = client.agents.routines.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                }
            ],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cooldown_scope="flow",
            cooldown_seconds=0,
            delivery={
                "destination": "one_drive",
                "folder": "x",
                "recording": {"filename": "x"},
                "screenshots": {},
            },
            description="description",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enabled=True,
            health_monitoring_enabled=True,
            notify_on_failure=True,
            notify_on_success=True,
            notify_webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recording_enabled=True,
            recording_policy={"mode": "off"},
            self_healing_enabled=True,
            self_healing_max_attempts=1,
        )
        assert_matches_type(RoutineCreateResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.agents.routines.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                }
            ],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine = response.parse()
        assert_matches_type(RoutineCreateResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.agents.routines.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                }
            ],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine = response.parse()
            assert_matches_type(RoutineCreateResponse, routine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.routines.with_raw_response.create(
                agent_id="",
                actions=[
                    {
                        "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "position": 0,
                    }
                ],
                name="x",
                trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone(self, client: Mobilerun) -> None:
        routine = client.agents.routines.clone(
            routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RoutineCloneResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: Mobilerun) -> None:
        routine = client.agents.routines.clone(
            routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="x",
        )
        assert_matches_type(RoutineCloneResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Mobilerun) -> None:
        response = client.agents.routines.with_raw_response.clone(
            routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine = response.parse()
        assert_matches_type(RoutineCloneResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Mobilerun) -> None:
        with client.agents.routines.with_streaming_response.clone(
            routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine = response.parse()
            assert_matches_type(RoutineCloneResponse, routine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_clone(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.routines.with_raw_response.clone(
                routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `routine_id` but received ''"):
            client.agents.routines.with_raw_response.clone(
                routine_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncRoutines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        routine = await async_client.agents.routines.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                }
            ],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RoutineCreateResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        routine = await async_client.agents.routines.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                }
            ],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cooldown_scope="flow",
            cooldown_seconds=0,
            delivery={
                "destination": "one_drive",
                "folder": "x",
                "recording": {"filename": "x"},
                "screenshots": {},
            },
            description="description",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enabled=True,
            health_monitoring_enabled=True,
            notify_on_failure=True,
            notify_on_success=True,
            notify_webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recording_enabled=True,
            recording_policy={"mode": "off"},
            self_healing_enabled=True,
            self_healing_max_attempts=1,
        )
        assert_matches_type(RoutineCreateResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.routines.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                }
            ],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine = await response.parse()
        assert_matches_type(RoutineCreateResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.routines.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "position": 0,
                }
            ],
            name="x",
            trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine = await response.parse()
            assert_matches_type(RoutineCreateResponse, routine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.routines.with_raw_response.create(
                agent_id="",
                actions=[
                    {
                        "action_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "position": 0,
                    }
                ],
                name="x",
                trigger_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncMobilerun) -> None:
        routine = await async_client.agents.routines.clone(
            routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RoutineCloneResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncMobilerun) -> None:
        routine = await async_client.agents.routines.clone(
            routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            device_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="x",
        )
        assert_matches_type(RoutineCloneResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.agents.routines.with_raw_response.clone(
            routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routine = await response.parse()
        assert_matches_type(RoutineCloneResponse, routine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncMobilerun) -> None:
        async with async_client.agents.routines.with_streaming_response.clone(
            routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routine = await response.parse()
            assert_matches_type(RoutineCloneResponse, routine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_clone(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.routines.with_raw_response.clone(
                routine_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `routine_id` but received ''"):
            await async_client.agents.routines.with_raw_response.clone(
                routine_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
