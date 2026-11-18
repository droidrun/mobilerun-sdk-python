# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.functions import (
    ValidationCreateResponse,
    ValidationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        validation = client.functions.validations.create(
            source="x",
        )
        assert_matches_type(ValidationCreateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        validation = client.functions.validations.create(
            source="x",
            wait_s=0,
            manifest={
                "credentials": [
                    {
                        "name": "x",
                        "package_name": "x",
                    }
                ],
                "hosts": ["string"],
                "scopes": ["_lk___klzn__.____uu"],
            },
        )
        assert_matches_type(ValidationCreateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.functions.validations.with_raw_response.create(
            source="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validation = response.parse()
        assert_matches_type(ValidationCreateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.functions.validations.with_streaming_response.create(
            source="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validation = response.parse()
            assert_matches_type(ValidationCreateResponse, validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        validation = client.functions.validations.retrieve(
            validation_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ValidationRetrieveResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Mobilerun) -> None:
        validation = client.functions.validations.retrieve(
            validation_id="550e8400-e29b-41d4-a716-446655440000",
            wait_s=0,
        )
        assert_matches_type(ValidationRetrieveResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.functions.validations.with_raw_response.retrieve(
            validation_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validation = response.parse()
        assert_matches_type(ValidationRetrieveResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.functions.validations.with_streaming_response.retrieve(
            validation_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validation = response.parse()
            assert_matches_type(ValidationRetrieveResponse, validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `validation_id` but received ''"):
            client.functions.validations.with_raw_response.retrieve(
                validation_id="",
            )


class TestAsyncValidations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        validation = await async_client.functions.validations.create(
            source="x",
        )
        assert_matches_type(ValidationCreateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        validation = await async_client.functions.validations.create(
            source="x",
            wait_s=0,
            manifest={
                "credentials": [
                    {
                        "name": "x",
                        "package_name": "x",
                    }
                ],
                "hosts": ["string"],
                "scopes": ["_lk___klzn__.____uu"],
            },
        )
        assert_matches_type(ValidationCreateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.functions.validations.with_raw_response.create(
            source="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validation = await response.parse()
        assert_matches_type(ValidationCreateResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.functions.validations.with_streaming_response.create(
            source="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validation = await response.parse()
            assert_matches_type(ValidationCreateResponse, validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        validation = await async_client.functions.validations.retrieve(
            validation_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ValidationRetrieveResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMobilerun) -> None:
        validation = await async_client.functions.validations.retrieve(
            validation_id="550e8400-e29b-41d4-a716-446655440000",
            wait_s=0,
        )
        assert_matches_type(ValidationRetrieveResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.functions.validations.with_raw_response.retrieve(
            validation_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validation = await response.parse()
        assert_matches_type(ValidationRetrieveResponse, validation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.functions.validations.with_streaming_response.retrieve(
            validation_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validation = await response.parse()
            assert_matches_type(ValidationRetrieveResponse, validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `validation_id` but received ''"):
            await async_client.functions.validations.with_raw_response.retrieve(
                validation_id="",
            )
