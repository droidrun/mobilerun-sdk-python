# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from mobilerun_sdk.types.workflows import EventDryRunResponse, EventIngestResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types.workflows import event_dry_run_params
from mobilerun_sdk.types.workflows import event_ingest_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_dry_run(self, client: Mobilerun) -> None:
        event = client.workflows.events.dry_run(
            event_type="x",
        )
        assert_matches_type(EventDryRunResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_dry_run_with_all_params(self, client: Mobilerun) -> None:
        event = client.workflows.events.dry_run(
            event_type="x",
            device_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={
                "foo": "bar"
            },
        )
        assert_matches_type(EventDryRunResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_dry_run(self, client: Mobilerun) -> None:

        response = client.workflows.events.with_raw_response.dry_run(
            event_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        event = response.parse()
        assert_matches_type(EventDryRunResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_dry_run(self, client: Mobilerun) -> None:
        with client.workflows.events.with_streaming_response.dry_run(
            event_type="x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            event = response.parse()
            assert_matches_type(EventDryRunResponse, event, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest(self, client: Mobilerun) -> None:
        event = client.workflows.events.ingest(
            event_type="x",
        )
        assert_matches_type(EventIngestResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_with_all_params(self, client: Mobilerun) -> None:
        event = client.workflows.events.ingest(
            event_type="x",
            device_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={
                "foo": "bar"
            },
        )
        assert_matches_type(EventIngestResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest(self, client: Mobilerun) -> None:

        response = client.workflows.events.with_raw_response.ingest(
            event_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        event = response.parse()
        assert_matches_type(EventIngestResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest(self, client: Mobilerun) -> None:
        with client.workflows.events.with_streaming_response.ingest(
            event_type="x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            event = response.parse()
            assert_matches_type(EventIngestResponse, event, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_dry_run(self, async_client: AsyncMobilerun) -> None:
        event = await async_client.workflows.events.dry_run(
            event_type="x",
        )
        assert_matches_type(EventDryRunResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_dry_run_with_all_params(self, async_client: AsyncMobilerun) -> None:
        event = await async_client.workflows.events.dry_run(
            event_type="x",
            device_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={
                "foo": "bar"
            },
        )
        assert_matches_type(EventDryRunResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_dry_run(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.events.with_raw_response.dry_run(
            event_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        event = await response.parse()
        assert_matches_type(EventDryRunResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_dry_run(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.events.with_streaming_response.dry_run(
            event_type="x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            event = await response.parse()
            assert_matches_type(EventDryRunResponse, event, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest(self, async_client: AsyncMobilerun) -> None:
        event = await async_client.workflows.events.ingest(
            event_type="x",
        )
        assert_matches_type(EventIngestResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_with_all_params(self, async_client: AsyncMobilerun) -> None:
        event = await async_client.workflows.events.ingest(
            event_type="x",
            device_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payload={
                "foo": "bar"
            },
        )
        assert_matches_type(EventIngestResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.workflows.events.with_raw_response.ingest(
            event_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        event = await response.parse()
        assert_matches_type(EventIngestResponse, event, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest(self, async_client: AsyncMobilerun) -> None:
        async with async_client.workflows.events.with_streaming_response.ingest(
            event_type="x",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            event = await response.parse()
            assert_matches_type(EventIngestResponse, event, path=['response'])

        assert cast(Any, response.is_closed) is True