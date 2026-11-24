# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk._utils import parse_datetime
from mobilerun_sdk.types.workflows.flows import (
    ScheduledRunListResponse,
    ScheduledRunCancelResponse,
    ScheduledRunCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScheduledRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        scheduled_run = client.workflows.flows.scheduled_runs.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ScheduledRunCreateResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        scheduled_run = client.workflows.flows.scheduled_runs.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            payload={"foo": "bar"},
        )
        assert_matches_type(ScheduledRunCreateResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.workflows.flows.scheduled_runs.with_raw_response.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_run = response.parse()
        assert_matches_type(ScheduledRunCreateResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.workflows.flows.scheduled_runs.with_streaming_response.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_run = response.parse()
            assert_matches_type(ScheduledRunCreateResponse, scheduled_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.workflows.flows.scheduled_runs.with_raw_response.create(
                flow_id="",
                run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        scheduled_run = client.workflows.flows.scheduled_runs.list(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScheduledRunListResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        scheduled_run = client.workflows.flows.scheduled_runs.list(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=1,
            page_size=1,
            status="scheduled",
        )
        assert_matches_type(ScheduledRunListResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.workflows.flows.scheduled_runs.with_raw_response.list(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_run = response.parse()
        assert_matches_type(ScheduledRunListResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.workflows.flows.scheduled_runs.with_streaming_response.list(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_run = response.parse()
            assert_matches_type(ScheduledRunListResponse, scheduled_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.workflows.flows.scheduled_runs.with_raw_response.list(
                flow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Mobilerun) -> None:
        scheduled_run = client.workflows.flows.scheduled_runs.cancel(
            scheduled_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScheduledRunCancelResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Mobilerun) -> None:
        response = client.workflows.flows.scheduled_runs.with_raw_response.cancel(
            scheduled_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_run = response.parse()
        assert_matches_type(ScheduledRunCancelResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Mobilerun) -> None:
        with client.workflows.flows.scheduled_runs.with_streaming_response.cancel(
            scheduled_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_run = response.parse()
            assert_matches_type(ScheduledRunCancelResponse, scheduled_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.workflows.flows.scheduled_runs.with_raw_response.cancel(
                scheduled_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_run_id` but received ''"):
            client.workflows.flows.scheduled_runs.with_raw_response.cancel(
                scheduled_run_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncScheduledRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        scheduled_run = await async_client.workflows.flows.scheduled_runs.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ScheduledRunCreateResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        scheduled_run = await async_client.workflows.flows.scheduled_runs.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            payload={"foo": "bar"},
        )
        assert_matches_type(ScheduledRunCreateResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.flows.scheduled_runs.with_raw_response.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_run = await response.parse()
        assert_matches_type(ScheduledRunCreateResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.scheduled_runs.with_streaming_response.create(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_run = await response.parse()
            assert_matches_type(ScheduledRunCreateResponse, scheduled_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.workflows.flows.scheduled_runs.with_raw_response.create(
                flow_id="",
                run_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        scheduled_run = await async_client.workflows.flows.scheduled_runs.list(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScheduledRunListResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        scheduled_run = await async_client.workflows.flows.scheduled_runs.list(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=1,
            page_size=1,
            status="scheduled",
        )
        assert_matches_type(ScheduledRunListResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.flows.scheduled_runs.with_raw_response.list(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_run = await response.parse()
        assert_matches_type(ScheduledRunListResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.scheduled_runs.with_streaming_response.list(
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_run = await response.parse()
            assert_matches_type(ScheduledRunListResponse, scheduled_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.workflows.flows.scheduled_runs.with_raw_response.list(
                flow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncMobilerun) -> None:
        scheduled_run = await async_client.workflows.flows.scheduled_runs.cancel(
            scheduled_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScheduledRunCancelResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.workflows.flows.scheduled_runs.with_raw_response.cancel(
            scheduled_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_run = await response.parse()
        assert_matches_type(ScheduledRunCancelResponse, scheduled_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.flows.scheduled_runs.with_streaming_response.cancel(
            scheduled_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_run = await response.parse()
            assert_matches_type(ScheduledRunCancelResponse, scheduled_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.workflows.flows.scheduled_runs.with_raw_response.cancel(
                scheduled_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                flow_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scheduled_run_id` but received ''"):
            await async_client.workflows.flows.scheduled_runs.with_raw_response.cancel(
                scheduled_run_id="",
                flow_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
