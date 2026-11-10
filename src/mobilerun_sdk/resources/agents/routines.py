# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.agents import routine_clone_params, routine_create_params
from ...types.agents.routine_clone_response import RoutineCloneResponse
from ...types.agents.routine_create_response import RoutineCreateResponse

__all__ = ["RoutinesResource", "AsyncRoutinesResource"]


class RoutinesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RoutinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return RoutinesResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        actions: Iterable[routine_create_params.Action],
        name: str,
        trigger_id: str,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        delivery: routine_create_params.Delivery | Omit = omit,
        description: str | Omit = omit,
        device_ids: SequenceNotStr[str] | Omit = omit,
        enabled: bool | Omit = omit,
        health_monitoring_enabled: bool | Omit = omit,
        notify_on_failure: bool | Omit = omit,
        notify_on_success: bool | Omit = omit,
        notify_webhook_id: Optional[str] | Omit = omit,
        recording_enabled: bool | Omit = omit,
        recording_policy: routine_create_params.RecordingPolicy | Omit = omit,
        self_healing_enabled: bool | Omit = omit,
        self_healing_max_attempts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RoutineCreateResponse:
        """
        Forwards the scheduler CreateFlowBody unchanged and assigns the Agent selected
        in the path. Requires Idempotency-Key; reuse it after a transient failure.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/agents/{agent_id}/routines", agent_id=agent_id),
            body=maybe_transform(
                {
                    "actions": actions,
                    "name": name,
                    "trigger_id": trigger_id,
                    "cooldown_scope": cooldown_scope,
                    "cooldown_seconds": cooldown_seconds,
                    "delivery": delivery,
                    "description": description,
                    "device_ids": device_ids,
                    "enabled": enabled,
                    "health_monitoring_enabled": health_monitoring_enabled,
                    "notify_on_failure": notify_on_failure,
                    "notify_on_success": notify_on_success,
                    "notify_webhook_id": notify_webhook_id,
                    "recording_enabled": recording_enabled,
                    "recording_policy": recording_policy,
                    "self_healing_enabled": self_healing_enabled,
                    "self_healing_max_attempts": self_healing_max_attempts,
                },
                routine_create_params.RoutineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RoutineCreateResponse,
        )

    def clone(
        self,
        routine_id: str,
        *,
        agent_id: str,
        device_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RoutineCloneResponse:
        """
        The source must belong to the authenticated owner and be assigned to the same
        Agent or unassigned. The target is the Agent in the path. Requires
        Idempotency-Key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not routine_id:
            raise ValueError(f"Expected a non-empty value for `routine_id` but received {routine_id!r}")
        return self._post(
            path_template("/agents/{agent_id}/routines/{routine_id}/clone", agent_id=agent_id, routine_id=routine_id),
            body=maybe_transform(
                {
                    "device_ids": device_ids,
                    "name": name,
                },
                routine_clone_params.RoutineCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RoutineCloneResponse,
        )


class AsyncRoutinesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncRoutinesResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        actions: Iterable[routine_create_params.Action],
        name: str,
        trigger_id: str,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        delivery: routine_create_params.Delivery | Omit = omit,
        description: str | Omit = omit,
        device_ids: SequenceNotStr[str] | Omit = omit,
        enabled: bool | Omit = omit,
        health_monitoring_enabled: bool | Omit = omit,
        notify_on_failure: bool | Omit = omit,
        notify_on_success: bool | Omit = omit,
        notify_webhook_id: Optional[str] | Omit = omit,
        recording_enabled: bool | Omit = omit,
        recording_policy: routine_create_params.RecordingPolicy | Omit = omit,
        self_healing_enabled: bool | Omit = omit,
        self_healing_max_attempts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RoutineCreateResponse:
        """
        Forwards the scheduler CreateFlowBody unchanged and assigns the Agent selected
        in the path. Requires Idempotency-Key; reuse it after a transient failure.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/agents/{agent_id}/routines", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "name": name,
                    "trigger_id": trigger_id,
                    "cooldown_scope": cooldown_scope,
                    "cooldown_seconds": cooldown_seconds,
                    "delivery": delivery,
                    "description": description,
                    "device_ids": device_ids,
                    "enabled": enabled,
                    "health_monitoring_enabled": health_monitoring_enabled,
                    "notify_on_failure": notify_on_failure,
                    "notify_on_success": notify_on_success,
                    "notify_webhook_id": notify_webhook_id,
                    "recording_enabled": recording_enabled,
                    "recording_policy": recording_policy,
                    "self_healing_enabled": self_healing_enabled,
                    "self_healing_max_attempts": self_healing_max_attempts,
                },
                routine_create_params.RoutineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RoutineCreateResponse,
        )

    async def clone(
        self,
        routine_id: str,
        *,
        agent_id: str,
        device_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RoutineCloneResponse:
        """
        The source must belong to the authenticated owner and be assigned to the same
        Agent or unassigned. The target is the Agent in the path. Requires
        Idempotency-Key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not routine_id:
            raise ValueError(f"Expected a non-empty value for `routine_id` but received {routine_id!r}")
        return await self._post(
            path_template("/agents/{agent_id}/routines/{routine_id}/clone", agent_id=agent_id, routine_id=routine_id),
            body=await async_maybe_transform(
                {
                    "device_ids": device_ids,
                    "name": name,
                },
                routine_clone_params.RoutineCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RoutineCloneResponse,
        )


class RoutinesResourceWithRawResponse:
    def __init__(self, routines: RoutinesResource) -> None:
        self._routines = routines

        self.create = to_raw_response_wrapper(
            routines.create,
        )
        self.clone = to_raw_response_wrapper(
            routines.clone,
        )


class AsyncRoutinesResourceWithRawResponse:
    def __init__(self, routines: AsyncRoutinesResource) -> None:
        self._routines = routines

        self.create = async_to_raw_response_wrapper(
            routines.create,
        )
        self.clone = async_to_raw_response_wrapper(
            routines.clone,
        )


class RoutinesResourceWithStreamingResponse:
    def __init__(self, routines: RoutinesResource) -> None:
        self._routines = routines

        self.create = to_streamed_response_wrapper(
            routines.create,
        )
        self.clone = to_streamed_response_wrapper(
            routines.clone,
        )


class AsyncRoutinesResourceWithStreamingResponse:
    def __init__(self, routines: AsyncRoutinesResource) -> None:
        self._routines = routines

        self.create = async_to_streamed_response_wrapper(
            routines.create,
        )
        self.clone = async_to_streamed_response_wrapper(
            routines.clone,
        )
