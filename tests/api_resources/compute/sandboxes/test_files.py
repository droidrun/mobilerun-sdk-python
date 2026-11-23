# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Mobilerun, respx_mock: MockRouter) -> None:
        respx_mock.get("/compute/sandboxes/550e8400-e29b-41d4-a716-446655440000/files").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        file = client.compute.sandboxes.files.download(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            path="x",
        )
        assert file.is_closed
        assert file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Mobilerun, respx_mock: MockRouter) -> None:
        respx_mock.get("/compute/sandboxes/550e8400-e29b-41d4-a716-446655440000/files").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        file = client.compute.sandboxes.files.with_raw_response.download(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            path="x",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert file.json() == {"foo": "bar"}
        assert isinstance(file, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Mobilerun, respx_mock: MockRouter) -> None:
        respx_mock.get("/compute/sandboxes/550e8400-e29b-41d4-a716-446655440000/files").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.compute.sandboxes.files.with_streaming_response.download(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            path="x",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, StreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.compute.sandboxes.files.with_raw_response.download(
                sandbox_id="",
                path="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Mobilerun) -> None:
        file = client.compute.sandboxes.files.upload(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            body=b"Example data",
            path="x",
        )
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Mobilerun) -> None:
        response = client.compute.sandboxes.files.with_raw_response.upload(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            body=b"Example data",
            path="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Mobilerun) -> None:
        with client.compute.sandboxes.files.with_streaming_response.upload(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            body=b"Example data",
            path="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.compute.sandboxes.files.with_raw_response.upload(
                sandbox_id="",
                body=b"Example data",
                path="x",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncMobilerun, respx_mock: MockRouter) -> None:
        respx_mock.get("/compute/sandboxes/550e8400-e29b-41d4-a716-446655440000/files").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        file = await async_client.compute.sandboxes.files.download(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            path="x",
        )
        assert file.is_closed
        assert await file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncMobilerun, respx_mock: MockRouter) -> None:
        respx_mock.get("/compute/sandboxes/550e8400-e29b-41d4-a716-446655440000/files").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        file = await async_client.compute.sandboxes.files.with_raw_response.download(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            path="x",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await file.json() == {"foo": "bar"}
        assert isinstance(file, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncMobilerun, respx_mock: MockRouter) -> None:
        respx_mock.get("/compute/sandboxes/550e8400-e29b-41d4-a716-446655440000/files").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.compute.sandboxes.files.with_streaming_response.download(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            path="x",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.compute.sandboxes.files.with_raw_response.download(
                sandbox_id="",
                path="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncMobilerun) -> None:
        file = await async_client.compute.sandboxes.files.upload(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            body=b"Example data",
            path="x",
        )
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.compute.sandboxes.files.with_raw_response.upload(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            body=b"Example data",
            path="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncMobilerun) -> None:
        async with async_client.compute.sandboxes.files.with_streaming_response.upload(
            sandbox_id="550e8400-e29b-41d4-a716-446655440000",
            body=b"Example data",
            path="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.compute.sandboxes.files.with_raw_response.upload(
                sandbox_id="",
                body=b"Example data",
                path="x",
            )
