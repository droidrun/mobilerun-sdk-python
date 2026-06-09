# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .bots import (
    BotsResource,
    AsyncBotsResource,
    BotsResourceWithRawResponse,
    AsyncBotsResourceWithRawResponse,
    BotsResourceWithStreamingResponse,
    AsyncBotsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents import telegram_receive_update_params

__all__ = ["TelegramResource", "AsyncTelegramResource"]


class TelegramResource(SyncAPIResource):
    @cached_property
    def bots(self) -> BotsResource:
        return BotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TelegramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TelegramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelegramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return TelegramResourceWithStreamingResponse(self)

    def receive_update(
        self,
        *,
        update_id: float,
        message: telegram_receive_update_params.Message | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Public endpoint called by Telegram's servers for the operator-owned shared bot.
        One fixed URL, one fixed secret: the orchestrator compares
        `X-Telegram-Bot-Api-Secret-Token` against `env.TELEGRAM_WEBHOOK_SECRET` with a
        constant-time check. Inbound routing keys on `message.from.id` (Telegram user
        id) → active link row → droidrun user. Returns 200 for ignorable events (group
        chats, dedup hits, unrecognized senders) to avoid Telegram retry storms; 401
        only for missing/wrong secret; 400 for malformed bodies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/agents/telegram/webhook",
            body=maybe_transform(
                {
                    "update_id": update_id,
                    "message": message,
                },
                telegram_receive_update_params.TelegramReceiveUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTelegramResource(AsyncAPIResource):
    @cached_property
    def bots(self) -> AsyncBotsResource:
        return AsyncBotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTelegramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTelegramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelegramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncTelegramResourceWithStreamingResponse(self)

    async def receive_update(
        self,
        *,
        update_id: float,
        message: telegram_receive_update_params.Message | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Public endpoint called by Telegram's servers for the operator-owned shared bot.
        One fixed URL, one fixed secret: the orchestrator compares
        `X-Telegram-Bot-Api-Secret-Token` against `env.TELEGRAM_WEBHOOK_SECRET` with a
        constant-time check. Inbound routing keys on `message.from.id` (Telegram user
        id) → active link row → droidrun user. Returns 200 for ignorable events (group
        chats, dedup hits, unrecognized senders) to avoid Telegram retry storms; 401
        only for missing/wrong secret; 400 for malformed bodies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/agents/telegram/webhook",
            body=await async_maybe_transform(
                {
                    "update_id": update_id,
                    "message": message,
                },
                telegram_receive_update_params.TelegramReceiveUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TelegramResourceWithRawResponse:
    def __init__(self, telegram: TelegramResource) -> None:
        self._telegram = telegram

        self.receive_update = to_raw_response_wrapper(
            telegram.receive_update,
        )

    @cached_property
    def bots(self) -> BotsResourceWithRawResponse:
        return BotsResourceWithRawResponse(self._telegram.bots)


class AsyncTelegramResourceWithRawResponse:
    def __init__(self, telegram: AsyncTelegramResource) -> None:
        self._telegram = telegram

        self.receive_update = async_to_raw_response_wrapper(
            telegram.receive_update,
        )

    @cached_property
    def bots(self) -> AsyncBotsResourceWithRawResponse:
        return AsyncBotsResourceWithRawResponse(self._telegram.bots)


class TelegramResourceWithStreamingResponse:
    def __init__(self, telegram: TelegramResource) -> None:
        self._telegram = telegram

        self.receive_update = to_streamed_response_wrapper(
            telegram.receive_update,
        )

    @cached_property
    def bots(self) -> BotsResourceWithStreamingResponse:
        return BotsResourceWithStreamingResponse(self._telegram.bots)


class AsyncTelegramResourceWithStreamingResponse:
    def __init__(self, telegram: AsyncTelegramResource) -> None:
        self._telegram = telegram

        self.receive_update = async_to_streamed_response_wrapper(
            telegram.receive_update,
        )

    @cached_property
    def bots(self) -> AsyncBotsResourceWithStreamingResponse:
        return AsyncBotsResourceWithStreamingResponse(self._telegram.bots)
