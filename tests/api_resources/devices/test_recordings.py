# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.devices import (
    RecordingListResponse,
    RecordingStopResponse,
    RecordingStartResponse,
    RecordingStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecordings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        recording = client.devices.recordings.list(
            device_id="deviceId",
        )
        assert_matches_type(Optional[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        recording = client.devices.recordings.list(
            device_id="deviceId",
            status="status",
            type="type",
        )
        assert_matches_type(Optional[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.devices.recordings.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(Optional[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.devices.recordings.with_streaming_response.list(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(Optional[RecordingListResponse], recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.recordings.with_raw_response.list(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        recording = client.devices.recordings.delete(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.devices.recordings.with_raw_response.delete(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.devices.recordings.with_streaming_response.delete(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.recordings.with_raw_response.delete(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.devices.recordings.with_raw_response.delete(
                recording_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Mobilerun) -> None:
        recording = client.devices.recordings.start(
            device_id="deviceId",
        )
        assert_matches_type(RecordingStartResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: Mobilerun) -> None:
        recording = client.devices.recordings.start(
            device_id="deviceId",
            name="name",
            retention_days=1,
            types=["string"],
        )
        assert_matches_type(RecordingStartResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Mobilerun) -> None:
        response = client.devices.recordings.with_raw_response.start(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingStartResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Mobilerun) -> None:
        with client.devices.recordings.with_streaming_response.start(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingStartResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.recordings.with_raw_response.start(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status(self, client: Mobilerun) -> None:
        recording = client.devices.recordings.status(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert_matches_type(RecordingStatusResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Mobilerun) -> None:
        response = client.devices.recordings.with_raw_response.status(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingStatusResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Mobilerun) -> None:
        with client.devices.recordings.with_streaming_response.status(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingStatusResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.recordings.with_raw_response.status(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.devices.recordings.with_raw_response.status(
                recording_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: Mobilerun) -> None:
        recording = client.devices.recordings.stop(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert_matches_type(RecordingStopResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Mobilerun) -> None:
        response = client.devices.recordings.with_raw_response.stop(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingStopResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Mobilerun) -> None:
        with client.devices.recordings.with_streaming_response.stop(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingStopResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.recordings.with_raw_response.stop(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.devices.recordings.with_raw_response.stop(
                recording_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trajectory(self, client: Mobilerun) -> None:
        recording = client.devices.recordings.trajectory(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trajectory(self, client: Mobilerun) -> None:
        response = client.devices.recordings.with_raw_response.trajectory(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_trajectory(self, client: Mobilerun) -> None:
        with client.devices.recordings.with_streaming_response.trajectory(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_trajectory(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.recordings.with_raw_response.trajectory(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.devices.recordings.with_raw_response.trajectory(
                recording_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_video(self, client: Mobilerun) -> None:
        recording = client.devices.recordings.video(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_video(self, client: Mobilerun) -> None:
        response = client.devices.recordings.with_raw_response.video(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_video(self, client: Mobilerun) -> None:
        with client.devices.recordings.with_streaming_response.video(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_video(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.devices.recordings.with_raw_response.video(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.devices.recordings.with_raw_response.video(
                recording_id="",
                device_id="deviceId",
            )


class TestAsyncRecordings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        recording = await async_client.devices.recordings.list(
            device_id="deviceId",
        )
        assert_matches_type(Optional[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        recording = await async_client.devices.recordings.list(
            device_id="deviceId",
            status="status",
            type="type",
        )
        assert_matches_type(Optional[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.recordings.with_raw_response.list(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(Optional[RecordingListResponse], recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.recordings.with_streaming_response.list(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(Optional[RecordingListResponse], recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.list(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        recording = await async_client.devices.recordings.delete(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.recordings.with_raw_response.delete(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.recordings.with_streaming_response.delete(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.delete(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.delete(
                recording_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncMobilerun) -> None:
        recording = await async_client.devices.recordings.start(
            device_id="deviceId",
        )
        assert_matches_type(RecordingStartResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncMobilerun) -> None:
        recording = await async_client.devices.recordings.start(
            device_id="deviceId",
            name="name",
            retention_days=1,
            types=["string"],
        )
        assert_matches_type(RecordingStartResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.recordings.with_raw_response.start(
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingStartResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.recordings.with_streaming_response.start(
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingStartResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.start(
                device_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncMobilerun) -> None:
        recording = await async_client.devices.recordings.status(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert_matches_type(RecordingStatusResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.recordings.with_raw_response.status(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingStatusResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.recordings.with_streaming_response.status(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingStatusResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.status(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.status(
                recording_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncMobilerun) -> None:
        recording = await async_client.devices.recordings.stop(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert_matches_type(RecordingStopResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.recordings.with_raw_response.stop(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingStopResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.recordings.with_streaming_response.stop(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingStopResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.stop(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.stop(
                recording_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trajectory(self, async_client: AsyncMobilerun) -> None:
        recording = await async_client.devices.recordings.trajectory(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trajectory(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.recordings.with_raw_response.trajectory(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_trajectory(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.recordings.with_streaming_response.trajectory(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_trajectory(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.trajectory(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.trajectory(
                recording_id="",
                device_id="deviceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_video(self, async_client: AsyncMobilerun) -> None:
        recording = await async_client.devices.recordings.video(
            recording_id="recordingId",
            device_id="deviceId",
        )
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_video(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.devices.recordings.with_raw_response.video(
            recording_id="recordingId",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert recording is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_video(self, async_client: AsyncMobilerun) -> None:
        async with async_client.devices.recordings.with_streaming_response.video(
            recording_id="recordingId",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_video(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.video(
                recording_id="recordingId",
                device_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.devices.recordings.with_raw_response.video(
                recording_id="",
                device_id="deviceId",
            )
