# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .commands import (
    CommandsResource,
    AsyncCommandsResource,
    CommandsResourceWithRawResponse,
    AsyncCommandsResourceWithRawResponse,
    CommandsResourceWithStreamingResponse,
    AsyncCommandsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.compute import sandbox_exec_params, sandbox_list_params, sandbox_create_params
from ....types.compute.sandbox_exec_response import SandboxExecResponse
from ....types.compute.sandbox_list_response import SandboxListResponse
from ....types.compute.sandbox_create_response import SandboxCreateResponse
from ....types.compute.sandbox_delete_response import SandboxDeleteResponse
from ....types.compute.sandbox_retrieve_response import SandboxRetrieveResponse

__all__ = ["SandboxesResource", "AsyncSandboxesResource"]


class SandboxesResource(SyncAPIResource):
    @cached_property
    def commands(self) -> CommandsResource:
        return CommandsResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SandboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SandboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return SandboxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allowed_hosts: SequenceNotStr[str] | Omit = omit,
        api_key: sandbox_create_params.APIKey | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        idle_timeout_s: int | Omit = omit,
        name: str | Omit = omit,
        timeout_s: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SandboxCreateResponse:
        """
        Create a sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/compute/sandboxes",
            body=maybe_transform(
                {
                    "allowed_hosts": allowed_hosts,
                    "api_key": api_key,
                    "env": env,
                    "idle_timeout_s": idle_timeout_s,
                    "name": name,
                    "timeout_s": timeout_s,
                },
                sandbox_create_params.SandboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SandboxCreateResponse,
        )

    def retrieve(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxRetrieveResponse:
        """
        Get a sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._get(
            path_template("/compute/sandboxes/{sandbox_id}", sandbox_id=sandbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxRetrieveResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["starting", "running", "stopped"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxListResponse:
        """
        List sandboxes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/compute/sandboxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                    },
                    sandbox_list_params.SandboxListParams,
                ),
            ),
            cast_to=SandboxListResponse,
        )

    def delete(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SandboxDeleteResponse:
        """
        Stop a sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._delete(
            path_template("/compute/sandboxes/{sandbox_id}", sandbox_id=sandbox_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SandboxDeleteResponse,
        )

    def exec(
        self,
        sandbox_id: str,
        *,
        command: str,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        timeout_s: int | Omit = omit,
        wait_s: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SandboxExecResponse:
        """
        Execute a shell command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._post(
            path_template("/compute/sandboxes/{sandbox_id}/exec", sandbox_id=sandbox_id),
            body=maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_s": timeout_s,
                    "wait_s": wait_s,
                },
                sandbox_exec_params.SandboxExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SandboxExecResponse,
        )


class AsyncSandboxesResource(AsyncAPIResource):
    @cached_property
    def commands(self) -> AsyncCommandsResource:
        return AsyncCommandsResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSandboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSandboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncSandboxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allowed_hosts: SequenceNotStr[str] | Omit = omit,
        api_key: sandbox_create_params.APIKey | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        idle_timeout_s: int | Omit = omit,
        name: str | Omit = omit,
        timeout_s: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SandboxCreateResponse:
        """
        Create a sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/compute/sandboxes",
            body=await async_maybe_transform(
                {
                    "allowed_hosts": allowed_hosts,
                    "api_key": api_key,
                    "env": env,
                    "idle_timeout_s": idle_timeout_s,
                    "name": name,
                    "timeout_s": timeout_s,
                },
                sandbox_create_params.SandboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SandboxCreateResponse,
        )

    async def retrieve(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxRetrieveResponse:
        """
        Get a sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._get(
            path_template("/compute/sandboxes/{sandbox_id}", sandbox_id=sandbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["starting", "running", "stopped"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxListResponse:
        """
        List sandboxes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/compute/sandboxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                    },
                    sandbox_list_params.SandboxListParams,
                ),
            ),
            cast_to=SandboxListResponse,
        )

    async def delete(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SandboxDeleteResponse:
        """
        Stop a sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._delete(
            path_template("/compute/sandboxes/{sandbox_id}", sandbox_id=sandbox_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SandboxDeleteResponse,
        )

    async def exec(
        self,
        sandbox_id: str,
        *,
        command: str,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        timeout_s: int | Omit = omit,
        wait_s: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SandboxExecResponse:
        """
        Execute a shell command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._post(
            path_template("/compute/sandboxes/{sandbox_id}/exec", sandbox_id=sandbox_id),
            body=await async_maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "timeout_s": timeout_s,
                    "wait_s": wait_s,
                },
                sandbox_exec_params.SandboxExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SandboxExecResponse,
        )


class SandboxesResourceWithRawResponse:
    def __init__(self, sandboxes: SandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = to_raw_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sandboxes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            sandboxes.list,
        )
        self.delete = to_raw_response_wrapper(
            sandboxes.delete,
        )
        self.exec = to_raw_response_wrapper(
            sandboxes.exec,
        )

    @cached_property
    def commands(self) -> CommandsResourceWithRawResponse:
        return CommandsResourceWithRawResponse(self._sandboxes.commands)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._sandboxes.files)


class AsyncSandboxesResourceWithRawResponse:
    def __init__(self, sandboxes: AsyncSandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = async_to_raw_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sandboxes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sandboxes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sandboxes.delete,
        )
        self.exec = async_to_raw_response_wrapper(
            sandboxes.exec,
        )

    @cached_property
    def commands(self) -> AsyncCommandsResourceWithRawResponse:
        return AsyncCommandsResourceWithRawResponse(self._sandboxes.commands)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._sandboxes.files)


class SandboxesResourceWithStreamingResponse:
    def __init__(self, sandboxes: SandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = to_streamed_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sandboxes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sandboxes.list,
        )
        self.delete = to_streamed_response_wrapper(
            sandboxes.delete,
        )
        self.exec = to_streamed_response_wrapper(
            sandboxes.exec,
        )

    @cached_property
    def commands(self) -> CommandsResourceWithStreamingResponse:
        return CommandsResourceWithStreamingResponse(self._sandboxes.commands)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._sandboxes.files)


class AsyncSandboxesResourceWithStreamingResponse:
    def __init__(self, sandboxes: AsyncSandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = async_to_streamed_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sandboxes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sandboxes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sandboxes.delete,
        )
        self.exec = async_to_streamed_response_wrapper(
            sandboxes.exec,
        )

    @cached_property
    def commands(self) -> AsyncCommandsResourceWithStreamingResponse:
        return AsyncCommandsResourceWithStreamingResponse(self._sandboxes.commands)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._sandboxes.files)
