# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mobilerun_sdk import Mobilerun, AsyncMobilerun
from mobilerun_sdk.types import (
    MailboxOtpResponse,
    MailboxListResponse,
    MailboxCreateResponse,
    MailboxDeleteResponse,
    MailboxUpdateResponse,
    MailboxRestartResponse,
    MailboxCapacityResponse,
    MailboxRetrieveResponse,
    MailboxUncancelResponse,
)
from mobilerun_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMailboxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.create(
            client_request_id="x",
        )
        assert_matches_type(MailboxCreateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.create(
            client_request_id="x",
            billing_preference="included",
            label="label",
            local_part="jane-doe",
        )
        assert_matches_type(MailboxCreateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mobilerun) -> None:
        response = client.mailboxes.with_raw_response.create(
            client_request_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = response.parse()
        assert_matches_type(MailboxCreateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mobilerun) -> None:
        with client.mailboxes.with_streaming_response.create(
            client_request_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = response.parse()
            assert_matches_type(MailboxCreateResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxRetrieveResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Mobilerun) -> None:
        response = client.mailboxes.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = response.parse()
        assert_matches_type(MailboxRetrieveResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Mobilerun) -> None:
        with client.mailboxes.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = response.parse()
            assert_matches_type(MailboxRetrieveResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            client.mailboxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.update(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
        )
        assert_matches_type(MailboxUpdateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Mobilerun) -> None:
        response = client.mailboxes.with_raw_response.update(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = response.parse()
        assert_matches_type(MailboxUpdateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Mobilerun) -> None:
        with client.mailboxes.with_streaming_response.update(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = response.parse()
            assert_matches_type(MailboxUpdateResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            client.mailboxes.with_raw_response.update(
                mailbox_id="",
                label="label",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.list()
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Mobilerun) -> None:
        response = client.mailboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = response.parse()
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Mobilerun) -> None:
        with client.mailboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = response.parse()
            assert_matches_type(MailboxListResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxDeleteResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Mobilerun) -> None:
        response = client.mailboxes.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = response.parse()
        assert_matches_type(MailboxDeleteResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Mobilerun) -> None:
        with client.mailboxes.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = response.parse()
            assert_matches_type(MailboxDeleteResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            client.mailboxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_capacity(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.capacity()
        assert_matches_type(MailboxCapacityResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_capacity(self, client: Mobilerun) -> None:
        response = client.mailboxes.with_raw_response.capacity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = response.parse()
        assert_matches_type(MailboxCapacityResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_capacity(self, client: Mobilerun) -> None:
        with client.mailboxes.with_streaming_response.capacity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = response.parse()
            assert_matches_type(MailboxCapacityResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_otp(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.otp(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxOtpResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_otp_with_all_params(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.otp(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_length=3,
            min_length=3,
            sender="sender",
        )
        assert_matches_type(MailboxOtpResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_otp(self, client: Mobilerun) -> None:
        response = client.mailboxes.with_raw_response.otp(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = response.parse()
        assert_matches_type(MailboxOtpResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_otp(self, client: Mobilerun) -> None:
        with client.mailboxes.with_streaming_response.otp(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = response.parse()
            assert_matches_type(MailboxOtpResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_otp(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            client.mailboxes.with_raw_response.otp(
                mailbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restart(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.restart(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxRestartResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restart_with_all_params(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.restart(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            billing_preference="included",
        )
        assert_matches_type(MailboxRestartResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restart(self, client: Mobilerun) -> None:
        response = client.mailboxes.with_raw_response.restart(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = response.parse()
        assert_matches_type(MailboxRestartResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restart(self, client: Mobilerun) -> None:
        with client.mailboxes.with_streaming_response.restart(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = response.parse()
            assert_matches_type(MailboxRestartResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restart(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            client.mailboxes.with_raw_response.restart(
                mailbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_uncancel(self, client: Mobilerun) -> None:
        mailbox = client.mailboxes.uncancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxUncancelResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_uncancel(self, client: Mobilerun) -> None:
        response = client.mailboxes.with_raw_response.uncancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = response.parse()
        assert_matches_type(MailboxUncancelResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_uncancel(self, client: Mobilerun) -> None:
        with client.mailboxes.with_streaming_response.uncancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = response.parse()
            assert_matches_type(MailboxUncancelResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_uncancel(self, client: Mobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            client.mailboxes.with_raw_response.uncancel(
                "",
            )


class TestAsyncMailboxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.create(
            client_request_id="x",
        )
        assert_matches_type(MailboxCreateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.create(
            client_request_id="x",
            billing_preference="included",
            label="label",
            local_part="jane-doe",
        )
        assert_matches_type(MailboxCreateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.mailboxes.with_raw_response.create(
            client_request_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = await response.parse()
        assert_matches_type(MailboxCreateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMobilerun) -> None:
        async with async_client.mailboxes.with_streaming_response.create(
            client_request_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = await response.parse()
            assert_matches_type(MailboxCreateResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxRetrieveResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.mailboxes.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = await response.parse()
        assert_matches_type(MailboxRetrieveResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMobilerun) -> None:
        async with async_client.mailboxes.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = await response.parse()
            assert_matches_type(MailboxRetrieveResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            await async_client.mailboxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.update(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
        )
        assert_matches_type(MailboxUpdateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.mailboxes.with_raw_response.update(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = await response.parse()
        assert_matches_type(MailboxUpdateResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMobilerun) -> None:
        async with async_client.mailboxes.with_streaming_response.update(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            label="label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = await response.parse()
            assert_matches_type(MailboxUpdateResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            await async_client.mailboxes.with_raw_response.update(
                mailbox_id="",
                label="label",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.list()
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.mailboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = await response.parse()
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMobilerun) -> None:
        async with async_client.mailboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = await response.parse()
            assert_matches_type(MailboxListResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxDeleteResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.mailboxes.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = await response.parse()
        assert_matches_type(MailboxDeleteResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMobilerun) -> None:
        async with async_client.mailboxes.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = await response.parse()
            assert_matches_type(MailboxDeleteResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            await async_client.mailboxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_capacity(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.capacity()
        assert_matches_type(MailboxCapacityResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_capacity(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.mailboxes.with_raw_response.capacity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = await response.parse()
        assert_matches_type(MailboxCapacityResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_capacity(self, async_client: AsyncMobilerun) -> None:
        async with async_client.mailboxes.with_streaming_response.capacity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = await response.parse()
            assert_matches_type(MailboxCapacityResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_otp(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.otp(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxOtpResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_otp_with_all_params(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.otp(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_length=3,
            min_length=3,
            sender="sender",
        )
        assert_matches_type(MailboxOtpResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_otp(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.mailboxes.with_raw_response.otp(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = await response.parse()
        assert_matches_type(MailboxOtpResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_otp(self, async_client: AsyncMobilerun) -> None:
        async with async_client.mailboxes.with_streaming_response.otp(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = await response.parse()
            assert_matches_type(MailboxOtpResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_otp(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            await async_client.mailboxes.with_raw_response.otp(
                mailbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restart(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.restart(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxRestartResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restart_with_all_params(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.restart(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            billing_preference="included",
        )
        assert_matches_type(MailboxRestartResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restart(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.mailboxes.with_raw_response.restart(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = await response.parse()
        assert_matches_type(MailboxRestartResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restart(self, async_client: AsyncMobilerun) -> None:
        async with async_client.mailboxes.with_streaming_response.restart(
            mailbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = await response.parse()
            assert_matches_type(MailboxRestartResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restart(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            await async_client.mailboxes.with_raw_response.restart(
                mailbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_uncancel(self, async_client: AsyncMobilerun) -> None:
        mailbox = await async_client.mailboxes.uncancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MailboxUncancelResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_uncancel(self, async_client: AsyncMobilerun) -> None:
        response = await async_client.mailboxes.with_raw_response.uncancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailbox = await response.parse()
        assert_matches_type(MailboxUncancelResponse, mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_uncancel(self, async_client: AsyncMobilerun) -> None:
        async with async_client.mailboxes.with_streaming_response.uncancel(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailbox = await response.parse()
            assert_matches_type(MailboxUncancelResponse, mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_uncancel(self, async_client: AsyncMobilerun) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mailbox_id` but received ''"):
            await async_client.mailboxes.with_raw_response.uncancel(
                "",
            )
