# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.devices import (
    TrafficSessionListResponse,
    TrafficSessionCreateResponse,
    TrafficSessionDeleteResponse,
    TrafficSessionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrafficSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        traffic_session = client.devices.traffic_sessions.create(
            device_id="deviceId",
            idempotency_key="x",
        )
        assert_matches_type(TrafficSessionCreateResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        traffic_session = client.devices.traffic_sessions.create(
            device_id="deviceId",
            idempotency_key="x",
            expires_in_seconds=60,
            max_body_bytes=0,
        )
        assert_matches_type(TrafficSessionCreateResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.devices.traffic_sessions.with_raw_response.create(
            device_id="deviceId",
            idempotency_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_session = response.parse()
        assert_matches_type(TrafficSessionCreateResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.devices.traffic_sessions.with_streaming_response.create(
            device_id="deviceId",
            idempotency_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_session = response.parse()
            assert_matches_type(TrafficSessionCreateResponse, traffic_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.traffic_sessions.with_raw_response.create(
                device_id="",
                idempotency_key="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        traffic_session = client.devices.traffic_sessions.retrieve(
            session_id="sessionId",
            device_id="deviceId",
        )
        assert_matches_type(TrafficSessionRetrieveResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.devices.traffic_sessions.with_raw_response.retrieve(
            session_id="sessionId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_session = response.parse()
        assert_matches_type(TrafficSessionRetrieveResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.devices.traffic_sessions.with_streaming_response.retrieve(
            session_id="sessionId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_session = response.parse()
            assert_matches_type(TrafficSessionRetrieveResponse, traffic_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.traffic_sessions.with_raw_response.retrieve(
                session_id="sessionId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.devices.traffic_sessions.with_raw_response.retrieve(
                session_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        traffic_session = client.devices.traffic_sessions.list(
            device_id="deviceId",
        )
        assert_matches_type(TrafficSessionListResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        traffic_session = client.devices.traffic_sessions.list(
            device_id="deviceId",
            page=1,
            page_size=1,
        )
        assert_matches_type(TrafficSessionListResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.devices.traffic_sessions.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_session = response.parse()
        assert_matches_type(TrafficSessionListResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.devices.traffic_sessions.with_streaming_response.list(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_session = response.parse()
            assert_matches_type(TrafficSessionListResponse, traffic_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.traffic_sessions.with_raw_response.list(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        traffic_session = client.devices.traffic_sessions.delete(
            session_id="sessionId",
            device_id="deviceId",
        )
        assert_matches_type(TrafficSessionDeleteResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.devices.traffic_sessions.with_raw_response.delete(
            session_id="sessionId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_session = response.parse()
        assert_matches_type(TrafficSessionDeleteResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.devices.traffic_sessions.with_streaming_response.delete(
            session_id="sessionId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_session = response.parse()
            assert_matches_type(TrafficSessionDeleteResponse, traffic_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.traffic_sessions.with_raw_response.delete(
                session_id="sessionId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.devices.traffic_sessions.with_raw_response.delete(
                session_id="",
                device_id="deviceId",
            )


class TestAsyncTrafficSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        traffic_session = await async_client.devices.traffic_sessions.create(
            device_id="deviceId",
            idempotency_key="x",
        )
        assert_matches_type(TrafficSessionCreateResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        traffic_session = await async_client.devices.traffic_sessions.create(
            device_id="deviceId",
            idempotency_key="x",
            expires_in_seconds=60,
            max_body_bytes=0,
        )
        assert_matches_type(TrafficSessionCreateResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.traffic_sessions.with_raw_response.create(
            device_id="deviceId",
            idempotency_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_session = await response.parse()
        assert_matches_type(TrafficSessionCreateResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.traffic_sessions.with_streaming_response.create(
            device_id="deviceId",
            idempotency_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_session = await response.parse()
            assert_matches_type(TrafficSessionCreateResponse, traffic_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.traffic_sessions.with_raw_response.create(
                device_id="",
                idempotency_key="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        traffic_session = await async_client.devices.traffic_sessions.retrieve(
            session_id="sessionId",
            device_id="deviceId",
        )
        assert_matches_type(TrafficSessionRetrieveResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.traffic_sessions.with_raw_response.retrieve(
            session_id="sessionId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_session = await response.parse()
        assert_matches_type(TrafficSessionRetrieveResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.traffic_sessions.with_streaming_response.retrieve(
            session_id="sessionId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_session = await response.parse()
            assert_matches_type(TrafficSessionRetrieveResponse, traffic_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.traffic_sessions.with_raw_response.retrieve(
                session_id="sessionId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.devices.traffic_sessions.with_raw_response.retrieve(
                session_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        traffic_session = await async_client.devices.traffic_sessions.list(
            device_id="deviceId",
        )
        assert_matches_type(TrafficSessionListResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        traffic_session = await async_client.devices.traffic_sessions.list(
            device_id="deviceId",
            page=1,
            page_size=1,
        )
        assert_matches_type(TrafficSessionListResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.traffic_sessions.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_session = await response.parse()
        assert_matches_type(TrafficSessionListResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.traffic_sessions.with_streaming_response.list(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_session = await response.parse()
            assert_matches_type(TrafficSessionListResponse, traffic_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.traffic_sessions.with_raw_response.list(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        traffic_session = await async_client.devices.traffic_sessions.delete(
            session_id="sessionId",
            device_id="deviceId",
        )
        assert_matches_type(TrafficSessionDeleteResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.traffic_sessions.with_raw_response.delete(
            session_id="sessionId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_session = await response.parse()
        assert_matches_type(TrafficSessionDeleteResponse, traffic_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.traffic_sessions.with_streaming_response.delete(
            session_id="sessionId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_session = await response.parse()
            assert_matches_type(TrafficSessionDeleteResponse, traffic_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.traffic_sessions.with_raw_response.delete(
                session_id="sessionId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.devices.traffic_sessions.with_raw_response.delete(
                session_id="",
                device_id="deviceId",
            )
