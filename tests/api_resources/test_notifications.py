# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from mobilerun_sdk.types import NotificationCatalogResponse, NotificationGetPreferencesResponse, NotificationUpdatePreferencesResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types import notification_update_preferences_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_catalog(self, client: Mobilerun) -> None:
        notification = client.notifications.catalog()
        assert_matches_type(NotificationCatalogResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_catalog(self, client: Mobilerun) -> None:

        response = client.notifications.with_raw_response.catalog()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        notification = response.parse()
        assert_matches_type(NotificationCatalogResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_catalog(self, client: Mobilerun) -> None:
        with client.notifications.with_streaming_response.catalog() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            notification = response.parse()
            assert_matches_type(NotificationCatalogResponse, notification, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_preferences(self, client: Mobilerun) -> None:
        notification = client.notifications.get_preferences()
        assert_matches_type(NotificationGetPreferencesResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_preferences(self, client: Mobilerun) -> None:

        response = client.notifications.with_raw_response.get_preferences()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        notification = response.parse()
        assert_matches_type(NotificationGetPreferencesResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_preferences(self, client: Mobilerun) -> None:
        with client.notifications.with_streaming_response.get_preferences() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            notification = response.parse()
            assert_matches_type(NotificationGetPreferencesResponse, notification, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_preferences(self, client: Mobilerun) -> None:
        notification = client.notifications.update_preferences(
            muted_types=["workflow.run.running", "task.run.running"],
        )
        assert_matches_type(NotificationUpdatePreferencesResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_preferences(self, client: Mobilerun) -> None:

        response = client.notifications.with_raw_response.update_preferences(
            muted_types=["workflow.run.running", "task.run.running"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        notification = response.parse()
        assert_matches_type(NotificationUpdatePreferencesResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_preferences(self, client: Mobilerun) -> None:
        with client.notifications.with_streaming_response.update_preferences(
            muted_types=["workflow.run.running", "task.run.running"],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            notification = response.parse()
            assert_matches_type(NotificationUpdatePreferencesResponse, notification, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_catalog(self, async_client: AsyncMobilerun) -> None:
        notification = await async_client.notifications.catalog()
        assert_matches_type(NotificationCatalogResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_catalog(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.notifications.with_raw_response.catalog()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        notification = await response.parse()
        assert_matches_type(NotificationCatalogResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_catalog(self, async_client: AsyncMobilerun) -> None:
        async with async_client.notifications.with_streaming_response.catalog() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            notification = await response.parse()
            assert_matches_type(NotificationCatalogResponse, notification, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_preferences(self, async_client: AsyncMobilerun) -> None:
        notification = await async_client.notifications.get_preferences()
        assert_matches_type(NotificationGetPreferencesResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_preferences(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.notifications.with_raw_response.get_preferences()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        notification = await response.parse()
        assert_matches_type(NotificationGetPreferencesResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_preferences(self, async_client: AsyncMobilerun) -> None:
        async with async_client.notifications.with_streaming_response.get_preferences() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            notification = await response.parse()
            assert_matches_type(NotificationGetPreferencesResponse, notification, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_preferences(self, async_client: AsyncMobilerun) -> None:
        notification = await async_client.notifications.update_preferences(
            muted_types=["workflow.run.running", "task.run.running"],
        )
        assert_matches_type(NotificationUpdatePreferencesResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_preferences(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.notifications.with_raw_response.update_preferences(
            muted_types=["workflow.run.running", "task.run.running"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        notification = await response.parse()
        assert_matches_type(NotificationUpdatePreferencesResponse, notification, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_preferences(self, async_client: AsyncMobilerun) -> None:
        async with async_client.notifications.with_streaming_response.update_preferences(
            muted_types=["workflow.run.running", "task.run.running"],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            notification = await response.parse()
            assert_matches_type(NotificationUpdatePreferencesResponse, notification, path=['response'])

        assert cast(Any, response.is_closed) is True