# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import TaskStatus, task_run_params, task_list_params, task_run_streamed_params, task_send_message_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .ui_states import (
    UiStatesResource,
    AsyncUiStatesResource,
    UiStatesResourceWithRawResponse,
    AsyncUiStatesResourceWithRawResponse,
    UiStatesResourceWithStreamingResponse,
    AsyncUiStatesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .screenshots import (
    ScreenshotsResource,
    AsyncScreenshotsResource,
    ScreenshotsResourceWithRawResponse,
    AsyncScreenshotsResourceWithRawResponse,
    ScreenshotsResourceWithStreamingResponse,
    AsyncScreenshotsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.task_status import TaskStatus
from ...types.task_run_response import TaskRunResponse
from ...types.task_list_response import TaskListResponse
from ...types.task_stop_response import TaskStopResponse
from ...types.task_retrieve_response import TaskRetrieveResponse
from ...types.task_get_status_response import TaskGetStatusResponse
from ...types.package_credentials_param import PackageCredentialsParam
from ...types.task_send_message_response import TaskSendMessageResponse
from ...types.task_get_trajectory_response import TaskGetTrajectoryResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    """Tasks API"""

    @cached_property
    def screenshots(self) -> ScreenshotsResource:
        """Tasks API"""
        return ScreenshotsResource(self._client)

    @cached_property
    def ui_states(self) -> UiStatesResource:
        """Tasks API"""
        return UiStatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRetrieveResponse:
        """
        Get full details of a task by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    def list(
        self,
        *,
        order_by: Optional[Literal["id", "createdAt", "finishedAt", "status"]] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        status: Optional[TaskStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskListResponse:
        """
        List tasks with optional filtering, sorting, and pagination.

        Args:
          query: Search in task description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "query": query,
                        "status": status,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )

    def attach(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach to a running task and receive its events as an SSE stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/tasks/{task_id}/attach", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGetStatusResponse:
        """
        Get the status of a task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetStatusResponse,
        )

    def get_trajectory(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGetTrajectoryResponse:
        """
        Get the trajectory of a task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/tasks/{task_id}/trajectory", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetTrajectoryResponse,
        )

    def run(
        self,
        *,
        device_id: str,
        task: str,
        agent_id: int | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        credentials: Iterable[PackageCredentialsParam] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reasoning: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRunResponse:
        """Create and dispatch a new agent task.

        Returns the task ID and device stream
        details.

        Args:
          device_id: The ID of the device to run the task on.

          display_id: The display ID of the device to run the task on.

          llm_model: The LLM model identifier to use for the task (e.g.
              'google/gemini-3.1-flash-lite-preview')

          subagent_model: LLM model used by sub-agent roles: executor, app_opener, structured_output

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tasks",
            body=maybe_transform(
                {
                    "device_id": device_id,
                    "task": task,
                    "agent_id": agent_id,
                    "apps": apps,
                    "credentials": credentials,
                    "display_id": display_id,
                    "execution_timeout": execution_timeout,
                    "files": files,
                    "llm_model": llm_model,
                    "max_steps": max_steps,
                    "output_schema": output_schema,
                    "reasoning": reasoning,
                    "stealth": stealth,
                    "subagent_model": subagent_model,
                    "temperature": temperature,
                    "vision": vision,
                    "vpn_country": vpn_country,
                },
                task_run_params.TaskRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRunResponse,
        )

    def run_streamed(
        self,
        *,
        device_id: str,
        task: str,
        agent_id: int | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        credentials: Iterable[PackageCredentialsParam] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reasoning: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create and dispatch a new agent task, returning an SSE stream of task events.
        Cancels the task if the client disconnects.

        Args:
          device_id: The ID of the device to run the task on.

          display_id: The display ID of the device to run the task on.

          llm_model: The LLM model identifier to use for the task (e.g.
              'google/gemini-3.1-flash-lite-preview')

          subagent_model: LLM model used by sub-agent roles: executor, app_opener, structured_output

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tasks/stream",
            body=maybe_transform(
                {
                    "device_id": device_id,
                    "task": task,
                    "agent_id": agent_id,
                    "apps": apps,
                    "credentials": credentials,
                    "display_id": display_id,
                    "execution_timeout": execution_timeout,
                    "files": files,
                    "llm_model": llm_model,
                    "max_steps": max_steps,
                    "output_schema": output_schema,
                    "reasoning": reasoning,
                    "stealth": stealth,
                    "subagent_model": subagent_model,
                    "temperature": temperature,
                    "vision": vision,
                    "vpn_country": vpn_country,
                },
                task_run_streamed_params.TaskRunStreamedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def send_message(
        self,
        task_id: str,
        *,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskSendMessageResponse:
        """Send a message to a running agent task.

        The message ID is delivered via SSE
        (UserMessageEvent with action=queued).

        Args:
          message: Message to send to the running agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._post(
            path_template("/tasks/{task_id}/message", task_id=task_id),
            body=maybe_transform({"message": message}, task_send_message_params.TaskSendMessageParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskSendMessageResponse,
        )

    def stop(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskStopResponse:
        """Cancel a running task.

        Returns an error if the task is already in a terminal
        state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._post(
            path_template("/tasks/{task_id}/cancel", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskStopResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    """Tasks API"""

    @cached_property
    def screenshots(self) -> AsyncScreenshotsResource:
        """Tasks API"""
        return AsyncScreenshotsResource(self._client)

    @cached_property
    def ui_states(self) -> AsyncUiStatesResource:
        """Tasks API"""
        return AsyncUiStatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRetrieveResponse:
        """
        Get full details of a task by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    async def list(
        self,
        *,
        order_by: Optional[Literal["id", "createdAt", "finishedAt", "status"]] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        status: Optional[TaskStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskListResponse:
        """
        List tasks with optional filtering, sorting, and pagination.

        Args:
          query: Search in task description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "query": query,
                        "status": status,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )

    async def attach(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach to a running task and receive its events as an SSE stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/tasks/{task_id}/attach", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGetStatusResponse:
        """
        Get the status of a task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/tasks/{task_id}/status", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetStatusResponse,
        )

    async def get_trajectory(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGetTrajectoryResponse:
        """
        Get the trajectory of a task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/tasks/{task_id}/trajectory", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetTrajectoryResponse,
        )

    async def run(
        self,
        *,
        device_id: str,
        task: str,
        agent_id: int | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        credentials: Iterable[PackageCredentialsParam] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reasoning: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRunResponse:
        """Create and dispatch a new agent task.

        Returns the task ID and device stream
        details.

        Args:
          device_id: The ID of the device to run the task on.

          display_id: The display ID of the device to run the task on.

          llm_model: The LLM model identifier to use for the task (e.g.
              'google/gemini-3.1-flash-lite-preview')

          subagent_model: LLM model used by sub-agent roles: executor, app_opener, structured_output

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tasks",
            body=await async_maybe_transform(
                {
                    "device_id": device_id,
                    "task": task,
                    "agent_id": agent_id,
                    "apps": apps,
                    "credentials": credentials,
                    "display_id": display_id,
                    "execution_timeout": execution_timeout,
                    "files": files,
                    "llm_model": llm_model,
                    "max_steps": max_steps,
                    "output_schema": output_schema,
                    "reasoning": reasoning,
                    "stealth": stealth,
                    "subagent_model": subagent_model,
                    "temperature": temperature,
                    "vision": vision,
                    "vpn_country": vpn_country,
                },
                task_run_params.TaskRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRunResponse,
        )

    async def run_streamed(
        self,
        *,
        device_id: str,
        task: str,
        agent_id: int | Omit = omit,
        apps: SequenceNotStr[str] | Omit = omit,
        credentials: Iterable[PackageCredentialsParam] | Omit = omit,
        display_id: int | Omit = omit,
        execution_timeout: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        llm_model: str | Omit = omit,
        max_steps: int | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        reasoning: bool | Omit = omit,
        stealth: bool | Omit = omit,
        subagent_model: str | Omit = omit,
        temperature: float | Omit = omit,
        vision: bool | Omit = omit,
        vpn_country: Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create and dispatch a new agent task, returning an SSE stream of task events.
        Cancels the task if the client disconnects.

        Args:
          device_id: The ID of the device to run the task on.

          display_id: The display ID of the device to run the task on.

          llm_model: The LLM model identifier to use for the task (e.g.
              'google/gemini-3.1-flash-lite-preview')

          subagent_model: LLM model used by sub-agent roles: executor, app_opener, structured_output

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tasks/stream",
            body=await async_maybe_transform(
                {
                    "device_id": device_id,
                    "task": task,
                    "agent_id": agent_id,
                    "apps": apps,
                    "credentials": credentials,
                    "display_id": display_id,
                    "execution_timeout": execution_timeout,
                    "files": files,
                    "llm_model": llm_model,
                    "max_steps": max_steps,
                    "output_schema": output_schema,
                    "reasoning": reasoning,
                    "stealth": stealth,
                    "subagent_model": subagent_model,
                    "temperature": temperature,
                    "vision": vision,
                    "vpn_country": vpn_country,
                },
                task_run_streamed_params.TaskRunStreamedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def send_message(
        self,
        task_id: str,
        *,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskSendMessageResponse:
        """Send a message to a running agent task.

        The message ID is delivered via SSE
        (UserMessageEvent with action=queued).

        Args:
          message: Message to send to the running agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._post(
            path_template("/tasks/{task_id}/message", task_id=task_id),
            body=await async_maybe_transform({"message": message}, task_send_message_params.TaskSendMessageParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskSendMessageResponse,
        )

    async def stop(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskStopResponse:
        """Cancel a running task.

        Returns an error if the task is already in a terminal
        state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._post(
            path_template("/tasks/{task_id}/cancel", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskStopResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.attach = to_raw_response_wrapper(
            tasks.attach,
        )
        self.get_status = to_raw_response_wrapper(
            tasks.get_status,
        )
        self.get_trajectory = to_raw_response_wrapper(
            tasks.get_trajectory,
        )
        self.run = to_raw_response_wrapper(
            tasks.run,
        )
        self.run_streamed = to_raw_response_wrapper(
            tasks.run_streamed,
        )
        self.send_message = to_raw_response_wrapper(
            tasks.send_message,
        )
        self.stop = to_raw_response_wrapper(
            tasks.stop,
        )

    @cached_property
    def screenshots(self) -> ScreenshotsResourceWithRawResponse:
        """Tasks API"""
        return ScreenshotsResourceWithRawResponse(self._tasks.screenshots)

    @cached_property
    def ui_states(self) -> UiStatesResourceWithRawResponse:
        """Tasks API"""
        return UiStatesResourceWithRawResponse(self._tasks.ui_states)


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.attach = async_to_raw_response_wrapper(
            tasks.attach,
        )
        self.get_status = async_to_raw_response_wrapper(
            tasks.get_status,
        )
        self.get_trajectory = async_to_raw_response_wrapper(
            tasks.get_trajectory,
        )
        self.run = async_to_raw_response_wrapper(
            tasks.run,
        )
        self.run_streamed = async_to_raw_response_wrapper(
            tasks.run_streamed,
        )
        self.send_message = async_to_raw_response_wrapper(
            tasks.send_message,
        )
        self.stop = async_to_raw_response_wrapper(
            tasks.stop,
        )

    @cached_property
    def screenshots(self) -> AsyncScreenshotsResourceWithRawResponse:
        """Tasks API"""
        return AsyncScreenshotsResourceWithRawResponse(self._tasks.screenshots)

    @cached_property
    def ui_states(self) -> AsyncUiStatesResourceWithRawResponse:
        """Tasks API"""
        return AsyncUiStatesResourceWithRawResponse(self._tasks.ui_states)


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.attach = to_streamed_response_wrapper(
            tasks.attach,
        )
        self.get_status = to_streamed_response_wrapper(
            tasks.get_status,
        )
        self.get_trajectory = to_streamed_response_wrapper(
            tasks.get_trajectory,
        )
        self.run = to_streamed_response_wrapper(
            tasks.run,
        )
        self.run_streamed = to_streamed_response_wrapper(
            tasks.run_streamed,
        )
        self.send_message = to_streamed_response_wrapper(
            tasks.send_message,
        )
        self.stop = to_streamed_response_wrapper(
            tasks.stop,
        )

    @cached_property
    def screenshots(self) -> ScreenshotsResourceWithStreamingResponse:
        """Tasks API"""
        return ScreenshotsResourceWithStreamingResponse(self._tasks.screenshots)

    @cached_property
    def ui_states(self) -> UiStatesResourceWithStreamingResponse:
        """Tasks API"""
        return UiStatesResourceWithStreamingResponse(self._tasks.ui_states)


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.attach = async_to_streamed_response_wrapper(
            tasks.attach,
        )
        self.get_status = async_to_streamed_response_wrapper(
            tasks.get_status,
        )
        self.get_trajectory = async_to_streamed_response_wrapper(
            tasks.get_trajectory,
        )
        self.run = async_to_streamed_response_wrapper(
            tasks.run,
        )
        self.run_streamed = async_to_streamed_response_wrapper(
            tasks.run_streamed,
        )
        self.send_message = async_to_streamed_response_wrapper(
            tasks.send_message,
        )
        self.stop = async_to_streamed_response_wrapper(
            tasks.stop,
        )

    @cached_property
    def screenshots(self) -> AsyncScreenshotsResourceWithStreamingResponse:
        """Tasks API"""
        return AsyncScreenshotsResourceWithStreamingResponse(self._tasks.screenshots)

    @cached_property
    def ui_states(self) -> AsyncUiStatesResourceWithStreamingResponse:
        """Tasks API"""
        return AsyncUiStatesResourceWithStreamingResponse(self._tasks.ui_states)
