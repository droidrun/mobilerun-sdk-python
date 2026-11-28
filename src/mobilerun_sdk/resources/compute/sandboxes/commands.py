# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.compute.sandboxes import command_retrieve_params
from ....types.compute.sandboxes.command_list_response import CommandListResponse
from ....types.compute.sandboxes.command_retrieve_response import CommandRetrieveResponse

__all__ = ["CommandsResource", "AsyncCommandsResource"]


class CommandsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CommandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return CommandsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        command_id: str,
        *,
        sandbox_id: str,
        wait_s: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandRetrieveResponse:
        """
        Get a command result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        if not command_id:
            raise ValueError(f"Expected a non-empty value for `command_id` but received {command_id!r}")
        return self._get(
            path_template(
                "/compute/sandboxes/{sandbox_id}/commands/{command_id}", sandbox_id=sandbox_id, command_id=command_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"wait_s": wait_s}, command_retrieve_params.CommandRetrieveParams),
            ),
            cast_to=CommandRetrieveResponse,
        )

    def list(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandListResponse:
        """
        List the newest commands

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._get(
            path_template("/compute/sandboxes/{sandbox_id}/commands", sandbox_id=sandbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandListResponse,
        )


class AsyncCommandsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncCommandsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        command_id: str,
        *,
        sandbox_id: str,
        wait_s: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandRetrieveResponse:
        """
        Get a command result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        if not command_id:
            raise ValueError(f"Expected a non-empty value for `command_id` but received {command_id!r}")
        return await self._get(
            path_template(
                "/compute/sandboxes/{sandbox_id}/commands/{command_id}", sandbox_id=sandbox_id, command_id=command_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"wait_s": wait_s}, command_retrieve_params.CommandRetrieveParams),
            ),
            cast_to=CommandRetrieveResponse,
        )

    async def list(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandListResponse:
        """
        List the newest commands

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._get(
            path_template("/compute/sandboxes/{sandbox_id}/commands", sandbox_id=sandbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandListResponse,
        )


class CommandsResourceWithRawResponse:
    def __init__(self, commands: CommandsResource) -> None:
        self._commands = commands

        self.retrieve = to_raw_response_wrapper(
            commands.retrieve,
        )
        self.list = to_raw_response_wrapper(
            commands.list,
        )


class AsyncCommandsResourceWithRawResponse:
    def __init__(self, commands: AsyncCommandsResource) -> None:
        self._commands = commands

        self.retrieve = async_to_raw_response_wrapper(
            commands.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            commands.list,
        )


class CommandsResourceWithStreamingResponse:
    def __init__(self, commands: CommandsResource) -> None:
        self._commands = commands

        self.retrieve = to_streamed_response_wrapper(
            commands.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            commands.list,
        )


class AsyncCommandsResourceWithStreamingResponse:
    def __init__(self, commands: AsyncCommandsResource) -> None:
        self._commands = commands

        self.retrieve = async_to_streamed_response_wrapper(
            commands.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            commands.list,
        )
