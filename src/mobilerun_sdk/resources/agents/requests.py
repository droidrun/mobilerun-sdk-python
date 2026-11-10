# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents import request_list_params, request_list_for_agent_params
from ...types.agents.request_list_response import RequestListResponse
from ...types.agents.request_retrieve_response import RequestRetrieveResponse
from ...types.agents.request_list_for_agent_response import RequestListForAgentResponse
from ...types.agents.request_retrieve_by_session_response import RequestRetrieveBySessionResponse

__all__ = ["RequestsResource", "AsyncRequestsResource"]


class RequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return RequestsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestRetrieveResponse:
        """Owner-scoped.

        Returns the request with its payloads and event timeline; an
        unknown id or another owner's request is a 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            path_template("/agents/requests/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestRetrieveResponse,
        )

    def list(
        self,
        *,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestListResponse:
        """Owner-scoped.

        Returns newest requests first, ordered by creation time and id.
        Use nextCursor as before to read older pages. Invalid cursors return 400
        invalid_cursor. Use the single read for payloads and events.

        Args:
          before: Opaque nextCursor from the previous page.

          limit: Maximum number of requests to return (1–100; default 50).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/agents/requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "limit": limit,
                    },
                    request_list_params.RequestListParams,
                ),
            ),
            cast_to=RequestListResponse,
        )

    def list_for_agent(
        self,
        agent_id: str,
        *,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestListForAgentResponse:
        """Owner-scoped.

        Returns newest requests where the Agent is source or target. Use
        nextCursor as before to read older pages. Invalid cursors return 400
        invalid_cursor.

        Args:
          before: Opaque nextCursor from the previous page.

          limit: Maximum number of requests to return (1–100; default 50).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/agents/{agent_id}/requests", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "limit": limit,
                    },
                    request_list_for_agent_params.RequestListForAgentParams,
                ),
            ),
            cast_to=RequestListForAgentResponse,
        )

    def retrieve_by_session(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestRetrieveBySessionResponse:
        """Owner-scoped.

        Returns the Agent-to-Agent request whose target session is
        {sessionId}, including its payloads and event timeline. Unknown sessions,
        source-only sessions, sessions without a request, and another owner's sessions
        return 404 agent_request_not_found.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/agents/sessions/{session_id}/request", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestRetrieveBySessionResponse,
        )


class AsyncRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncRequestsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestRetrieveResponse:
        """Owner-scoped.

        Returns the request with its payloads and event timeline; an
        unknown id or another owner's request is a 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            path_template("/agents/requests/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestRetrieveResponse,
        )

    async def list(
        self,
        *,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestListResponse:
        """Owner-scoped.

        Returns newest requests first, ordered by creation time and id.
        Use nextCursor as before to read older pages. Invalid cursors return 400
        invalid_cursor. Use the single read for payloads and events.

        Args:
          before: Opaque nextCursor from the previous page.

          limit: Maximum number of requests to return (1–100; default 50).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/agents/requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "before": before,
                        "limit": limit,
                    },
                    request_list_params.RequestListParams,
                ),
            ),
            cast_to=RequestListResponse,
        )

    async def list_for_agent(
        self,
        agent_id: str,
        *,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestListForAgentResponse:
        """Owner-scoped.

        Returns newest requests where the Agent is source or target. Use
        nextCursor as before to read older pages. Invalid cursors return 400
        invalid_cursor.

        Args:
          before: Opaque nextCursor from the previous page.

          limit: Maximum number of requests to return (1–100; default 50).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/agents/{agent_id}/requests", agent_id=agent_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "before": before,
                        "limit": limit,
                    },
                    request_list_for_agent_params.RequestListForAgentParams,
                ),
            ),
            cast_to=RequestListForAgentResponse,
        )

    async def retrieve_by_session(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestRetrieveBySessionResponse:
        """Owner-scoped.

        Returns the Agent-to-Agent request whose target session is
        {sessionId}, including its payloads and event timeline. Unknown sessions,
        source-only sessions, sessions without a request, and another owner's sessions
        return 404 agent_request_not_found.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/agents/sessions/{session_id}/request", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestRetrieveBySessionResponse,
        )


class RequestsResourceWithRawResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.retrieve = to_raw_response_wrapper(
            requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            requests.list,
        )
        self.list_for_agent = to_raw_response_wrapper(
            requests.list_for_agent,
        )
        self.retrieve_by_session = to_raw_response_wrapper(
            requests.retrieve_by_session,
        )


class AsyncRequestsResourceWithRawResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.retrieve = async_to_raw_response_wrapper(
            requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            requests.list,
        )
        self.list_for_agent = async_to_raw_response_wrapper(
            requests.list_for_agent,
        )
        self.retrieve_by_session = async_to_raw_response_wrapper(
            requests.retrieve_by_session,
        )


class RequestsResourceWithStreamingResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.retrieve = to_streamed_response_wrapper(
            requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            requests.list,
        )
        self.list_for_agent = to_streamed_response_wrapper(
            requests.list_for_agent,
        )
        self.retrieve_by_session = to_streamed_response_wrapper(
            requests.retrieve_by_session,
        )


class AsyncRequestsResourceWithStreamingResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.retrieve = async_to_streamed_response_wrapper(
            requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            requests.list,
        )
        self.list_for_agent = async_to_streamed_response_wrapper(
            requests.list_for_agent,
        )
        self.retrieve_by_session = async_to_streamed_response_wrapper(
            requests.retrieve_by_session,
        )
