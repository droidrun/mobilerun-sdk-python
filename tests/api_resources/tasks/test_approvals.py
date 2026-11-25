# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types.tasks import ApprovalDecideResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApprovals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_decide(self, client: Mobilerun) -> None:
        approval = client.tasks.approvals.decide(
            approval_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            decision="approve",
        )
        assert_matches_type(ApprovalDecideResponse, approval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_decide(self, client: Mobilerun) -> None:
        response = client.tasks.approvals.with_raw_response.decide(
            approval_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            decision="approve",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        approval = response.parse()
        assert_matches_type(ApprovalDecideResponse, approval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_decide(self, client: Mobilerun) -> None:
        with client.tasks.approvals.with_streaming_response.decide(
            approval_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            decision="approve",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            approval = response.parse()
            assert_matches_type(ApprovalDecideResponse, approval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_decide(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.approvals.with_raw_response.decide(
                approval_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                task_id="",
                decision="approve",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `approval_id` but received ''"):
            client.tasks.approvals.with_raw_response.decide(
                approval_id="",
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                decision="approve",
            )


class TestAsyncApprovals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_decide(self, async_client: AsyncMobilerun) -> None:
        approval = await async_client.tasks.approvals.decide(
            approval_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            decision="approve",
        )
        assert_matches_type(ApprovalDecideResponse, approval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_decide(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.tasks.approvals.with_raw_response.decide(
            approval_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            decision="approve",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        approval = await response.parse()
        assert_matches_type(ApprovalDecideResponse, approval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_decide(self, async_client: AsyncMobilerun) -> None:
        async with async_client.tasks.approvals.with_streaming_response.decide(
            approval_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            decision="approve",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            approval = await response.parse()
            assert_matches_type(ApprovalDecideResponse, approval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_decide(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.approvals.with_raw_response.decide(
                approval_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                task_id="",
                decision="approve",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `approval_id` but received ''"):
            await async_client.tasks.approvals.with_raw_response.decide(
                approval_id="",
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                decision="approve",
            )
