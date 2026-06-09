# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents.telegram.bot_list_response import BotListResponse
from ....types.agents.telegram.bot_revoke_link_response import BotRevokeLinkResponse
from ....types.agents.telegram.bot_request_link_response import BotRequestLinkResponse

__all__ = ["BotsResource", "AsyncBotsResource"]


class BotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return BotsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotListResponse:
        """List the current user's Telegram link rows"""
        return self._get(
            "/agents/telegram/bots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotListResponse,
        )

    def request_link(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotRequestLinkResponse:
        """
        Issues a one-shot deeplink (`t.me/<sharedBot>?start=<code>`) for the
        operator-owned shared bot. The user opens the link, taps `Start`, and the
        webhook binds their Telegram account to this droidrun user. No bot token is
        needed from the user — the operator owns the bot.
        """
        return self._post(
            "/agents/telegram/bots/connect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotRequestLinkResponse,
        )

    def revoke_link(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotRevokeLinkResponse:
        """Disables the link.

        Future inbound messages from this Telegram account get the
        welcome reply. The existing chat history is NOT wiped — start a fresh chat from
        the UI if you suspect compromise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/agents/telegram/bots/{id}/revoke", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotRevokeLinkResponse,
        )


class AsyncBotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncBotsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotListResponse:
        """List the current user's Telegram link rows"""
        return await self._get(
            "/agents/telegram/bots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotListResponse,
        )

    async def request_link(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotRequestLinkResponse:
        """
        Issues a one-shot deeplink (`t.me/<sharedBot>?start=<code>`) for the
        operator-owned shared bot. The user opens the link, taps `Start`, and the
        webhook binds their Telegram account to this droidrun user. No bot token is
        needed from the user — the operator owns the bot.
        """
        return await self._post(
            "/agents/telegram/bots/connect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotRequestLinkResponse,
        )

    async def revoke_link(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotRevokeLinkResponse:
        """Disables the link.

        Future inbound messages from this Telegram account get the
        welcome reply. The existing chat history is NOT wiped — start a fresh chat from
        the UI if you suspect compromise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/agents/telegram/bots/{id}/revoke", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotRevokeLinkResponse,
        )


class BotsResourceWithRawResponse:
    def __init__(self, bots: BotsResource) -> None:
        self._bots = bots

        self.list = to_raw_response_wrapper(
            bots.list,
        )
        self.request_link = to_raw_response_wrapper(
            bots.request_link,
        )
        self.revoke_link = to_raw_response_wrapper(
            bots.revoke_link,
        )


class AsyncBotsResourceWithRawResponse:
    def __init__(self, bots: AsyncBotsResource) -> None:
        self._bots = bots

        self.list = async_to_raw_response_wrapper(
            bots.list,
        )
        self.request_link = async_to_raw_response_wrapper(
            bots.request_link,
        )
        self.revoke_link = async_to_raw_response_wrapper(
            bots.revoke_link,
        )


class BotsResourceWithStreamingResponse:
    def __init__(self, bots: BotsResource) -> None:
        self._bots = bots

        self.list = to_streamed_response_wrapper(
            bots.list,
        )
        self.request_link = to_streamed_response_wrapper(
            bots.request_link,
        )
        self.revoke_link = to_streamed_response_wrapper(
            bots.revoke_link,
        )


class AsyncBotsResourceWithStreamingResponse:
    def __init__(self, bots: AsyncBotsResource) -> None:
        self._bots = bots

        self.list = async_to_streamed_response_wrapper(
            bots.list,
        )
        self.request_link = async_to_streamed_response_wrapper(
            bots.request_link,
        )
        self.revoke_link = async_to_streamed_response_wrapper(
            bots.revoke_link,
        )
