# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from mobilerun_sdk import Mobilerun, AsyncMobilerun

from mobilerun_sdk.types.devices import MediaSessionCreateResponse, MediaSessionActivateResponse, MediaSessionRetrieveCurrentResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from tests.utils import assert_matches_type
from mobilerun_sdk.types.devices import media_session_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestMediaSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        media_session = client.devices.media_sessions.create(
            device_id="deviceId",
            camera=True,
            microphone=True,
        )
        assert_matches_type(MediaSessionCreateResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:

        response = client.devices.media_sessions.with_raw_response.create(
            device_id="deviceId",
            camera=True,
            microphone=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        media_session = response.parse()
        assert_matches_type(MediaSessionCreateResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.devices.media_sessions.with_streaming_response.create(
            device_id="deviceId",
            camera=True,
            microphone=True,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            media_session = response.parse()
            assert_matches_type(MediaSessionCreateResponse, media_session, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.media_sessions.with_raw_response.create(
              device_id="",
              camera=True,
              microphone=True,
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        media_session = client.devices.media_sessions.delete(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        )
        assert media_session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:

        response = client.devices.media_sessions.with_raw_response.delete(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        media_session = response.parse()
        assert media_session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.devices.media_sessions.with_streaming_response.delete(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            media_session = response.parse()
            assert media_session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.media_sessions.with_raw_response.delete(
              session_id="sessionId",
              device_id="",
              x_media_control_token="X-Media-Control-Token",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
          client.devices.media_sessions.with_raw_response.delete(
              session_id="",
              device_id="deviceId",
              x_media_control_token="X-Media-Control-Token",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activate(self, client: Mobilerun) -> None:
        media_session = client.devices.media_sessions.activate(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        )
        assert_matches_type(MediaSessionActivateResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_activate(self, client: Mobilerun) -> None:

        response = client.devices.media_sessions.with_raw_response.activate(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        media_session = response.parse()
        assert_matches_type(MediaSessionActivateResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_activate(self, client: Mobilerun) -> None:
        with client.devices.media_sessions.with_streaming_response.activate(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            media_session = response.parse()
            assert_matches_type(MediaSessionActivateResponse, media_session, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_activate(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.media_sessions.with_raw_response.activate(
              session_id="sessionId",
              device_id="",
              x_media_control_token="X-Media-Control-Token",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
          client.devices.media_sessions.with_raw_response.activate(
              session_id="",
              device_id="deviceId",
              x_media_control_token="X-Media-Control-Token",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_current(self, client: Mobilerun) -> None:
        media_session = client.devices.media_sessions.retrieve_current(
            "deviceId",
        )
        assert_matches_type(MediaSessionRetrieveCurrentResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_current(self, client: Mobilerun) -> None:

        response = client.devices.media_sessions.with_raw_response.retrieve_current(
            "deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        media_session = response.parse()
        assert_matches_type(MediaSessionRetrieveCurrentResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_current(self, client: Mobilerun) -> None:
        with client.devices.media_sessions.with_streaming_response.retrieve_current(
            "deviceId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            media_session = response.parse()
            assert_matches_type(MediaSessionRetrieveCurrentResponse, media_session, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_current(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          client.devices.media_sessions.with_raw_response.retrieve_current(
              "",
          )
class TestAsyncMediaSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        media_session = await async_client.devices.media_sessions.create(
            device_id="deviceId",
            camera=True,
            microphone=True,
        )
        assert_matches_type(MediaSessionCreateResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.media_sessions.with_raw_response.create(
            device_id="deviceId",
            camera=True,
            microphone=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        media_session = await response.parse()
        assert_matches_type(MediaSessionCreateResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.media_sessions.with_streaming_response.create(
            device_id="deviceId",
            camera=True,
            microphone=True,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            media_session = await response.parse()
            assert_matches_type(MediaSessionCreateResponse, media_session, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.media_sessions.with_raw_response.create(
              device_id="",
              camera=True,
              microphone=True,
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        media_session = await async_client.devices.media_sessions.delete(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        )
        assert media_session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.media_sessions.with_raw_response.delete(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        media_session = await response.parse()
        assert media_session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.media_sessions.with_streaming_response.delete(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            media_session = await response.parse()
            assert media_session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.media_sessions.with_raw_response.delete(
              session_id="sessionId",
              device_id="",
              x_media_control_token="X-Media-Control-Token",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
          await async_client.devices.media_sessions.with_raw_response.delete(
              session_id="",
              device_id="deviceId",
              x_media_control_token="X-Media-Control-Token",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activate(self, async_client: AsyncMobilerun) -> None:
        media_session = await async_client.devices.media_sessions.activate(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        )
        assert_matches_type(MediaSessionActivateResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.media_sessions.with_raw_response.activate(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        media_session = await response.parse()
        assert_matches_type(MediaSessionActivateResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.media_sessions.with_streaming_response.activate(
            session_id="sessionId",
            device_id="deviceId",
            x_media_control_token="X-Media-Control-Token",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            media_session = await response.parse()
            assert_matches_type(MediaSessionActivateResponse, media_session, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_activate(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.media_sessions.with_raw_response.activate(
              session_id="sessionId",
              device_id="",
              x_media_control_token="X-Media-Control-Token",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
          await async_client.devices.media_sessions.with_raw_response.activate(
              session_id="",
              device_id="deviceId",
              x_media_control_token="X-Media-Control-Token",
          )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_current(self, async_client: AsyncMobilerun) -> None:
        media_session = await async_client.devices.media_sessions.retrieve_current(
            "deviceId",
        )
        assert_matches_type(MediaSessionRetrieveCurrentResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_current(self, async_client: AsyncMobilerun) -> None:

        response = await async_client.devices.media_sessions.with_raw_response.retrieve_current(
            "deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        media_session = await response.parse()
        assert_matches_type(MediaSessionRetrieveCurrentResponse, media_session, path=['response'])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_current(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.media_sessions.with_streaming_response.retrieve_current(
            "deviceId",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            media_session = await response.parse()
            assert_matches_type(MediaSessionRetrieveCurrentResponse, media_session, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_current(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
          await async_client.devices.media_sessions.with_raw_response.retrieve_current(
              "",
          )