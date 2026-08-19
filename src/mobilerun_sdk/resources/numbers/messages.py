# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._resource import SyncAPIResource, AsyncAPIResource

from ..._compat import cached_property

from ..._utils import path_template, maybe_transform, async_maybe_transform

from ...types.numbers.message_list_response import MessageListResponse

from ..._base_client import make_request_options

from typing_extensions import Literal

from ..._types import Omit, omit, NotGiven

from typing import Union

from datetime import datetime

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ...types.numbers import message_list_params

__all__ = ["MessagesResource", "AsyncMessagesResource"]

class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def list(self,
    id: str,
    *,
    direction: Literal["all", "inbound", "outbound"] | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    since: Union[str, datetime] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MessageListResponse:
        """
        Returns SMS messages on the number, inbound and outbound, scoped to the
        authenticated user. Newest first. Messages stay with the number across device
        switches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
          raise ValueError(
            f'Expected a non-empty value for `id` but received {id!r}'
          )
        return self._get(
            path_template("/numbers/phones/{id}/messages", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "direction": direction,
                "page": page,
                "page_size": page_size,
                "since": since,
            }, message_list_params.MessageListParams)),
            cast_to=MessageListResponse,
        )

class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def list(self,
    id: str,
    *,
    direction: Literal["all", "inbound", "outbound"] | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    since: Union[str, datetime] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> MessageListResponse:
        """
        Returns SMS messages on the number, inbound and outbound, scoped to the
        authenticated user. Newest first. Messages stay with the number across device
        switches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
          raise ValueError(
            f'Expected a non-empty value for `id` but received {id!r}'
          )
        return await self._get(
            path_template("/numbers/phones/{id}/messages", id=id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "direction": direction,
                "page": page,
                "page_size": page_size,
                "since": since,
            }, message_list_params.MessageListParams)),
            cast_to=MessageListResponse,
        )

class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )

class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )

class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )

class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )