# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

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
from ...types.workflows import trigger_fire_params, trigger_list_params, trigger_create_params, trigger_update_params
from ...types.workflows.trigger_fire_response import TriggerFireResponse
from ...types.workflows.trigger_list_response import TriggerListResponse
from ...types.workflows.trigger_create_response import TriggerCreateResponse
from ...types.workflows.trigger_delete_response import TriggerDeleteResponse
from ...types.workflows.trigger_update_response import TriggerUpdateResponse
from ...types.workflows.trigger_retrieve_response import TriggerRetrieveResponse

__all__ = ["TriggersResource", "AsyncTriggersResource"]


class TriggersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TriggersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TriggersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return TriggersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        activation: Literal["event", "schedule", "custom"],
        name: str,
        conditions: trigger_create_params.Conditions | Omit = omit,
        custom_payload_schema: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        event_type: str | Omit = omit,
        schedule_rule: trigger_create_params.ScheduleRule | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerCreateResponse:
        """
        Create a trigger

        Args:
          custom_payload_schema: Optional JSON Schema for validating payloads sent to this custom trigger

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/triggers",
            body=maybe_transform(
                {
                    "activation": activation,
                    "name": name,
                    "conditions": conditions,
                    "custom_payload_schema": custom_payload_schema,
                    "description": description,
                    "event_type": event_type,
                    "schedule_rule": schedule_rule,
                    "timezone": timezone,
                },
                trigger_create_params.TriggerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerCreateResponse,
        )

    def retrieve(
        self,
        trigger_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerRetrieveResponse:
        """
        Get a trigger

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._get(
            path_template("/triggers/{trigger_id}", trigger_id=trigger_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerRetrieveResponse,
        )

    def update(
        self,
        trigger_id: str,
        *,
        activation: Literal["event", "schedule", "custom"] | Omit = omit,
        conditions: trigger_update_params.Conditions | Omit = omit,
        custom_payload_schema: Optional[Dict[str, object]] | Omit = omit,
        description: str | Omit = omit,
        event_type: str | Omit = omit,
        name: str | Omit = omit,
        schedule_rule: trigger_update_params.ScheduleRule | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerUpdateResponse:
        """
        Update a trigger

        Args:
          custom_payload_schema: Optional JSON Schema for validating payloads sent to this custom trigger

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._patch(
            path_template("/triggers/{trigger_id}", trigger_id=trigger_id),
            body=maybe_transform(
                {
                    "activation": activation,
                    "conditions": conditions,
                    "custom_payload_schema": custom_payload_schema,
                    "description": description,
                    "event_type": event_type,
                    "name": name,
                    "schedule_rule": schedule_rule,
                    "timezone": timezone,
                },
                trigger_update_params.TriggerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerUpdateResponse,
        )

    def list(
        self,
        *,
        activation: Literal["event", "schedule", "custom"] | Omit = omit,
        event_type: str | Omit = omit,
        order_by: Literal["name", "createdAt", "updatedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerListResponse:
        """
        List triggers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/triggers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "activation": activation,
                        "event_type": event_type,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                    },
                    trigger_list_params.TriggerListParams,
                ),
            ),
            cast_to=TriggerListResponse,
        )

    def delete(
        self,
        trigger_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerDeleteResponse:
        """
        Delete a trigger

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._delete(
            path_template("/triggers/{trigger_id}", trigger_id=trigger_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerDeleteResponse,
        )

    def fire(
        self,
        trigger_id: str,
        *,
        payload: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerFireResponse:
        """
        Invoke a custom trigger directly with an arbitrary JSON payload.

        Fan-out: a trigger may be referenced by multiple flows (workflows). Firing it
        enqueues one execution per enabled, non-deleted flow attached to this trigger,
        each receiving the same payload. The `enqueuedCount` in the response reports how
        many were enqueued (0 if no flows are attached, or if all matching flows are
        gated by a cooldown).

        Payload validation:

        - If the trigger has a `customPayloadSchema`, the payload is validated against
          it (JSON Schema via AJV).
        - If no schema is configured, the payload only needs to be a JSON object — any
          keys and values are accepted.

        Only triggers with `activation = "custom"` can be fired through this endpoint;
        event and schedule triggers return 409.

        Args:
          payload: Arbitrary JSON object forwarded to every flow attached to this trigger.
              Validated against the trigger's customPayloadSchema when one is configured;
              otherwise only "must be a JSON object" is enforced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return self._post(
            path_template("/triggers/{trigger_id}/fire", trigger_id=trigger_id),
            body=maybe_transform({"payload": payload}, trigger_fire_params.TriggerFireParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerFireResponse,
        )


class AsyncTriggersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTriggersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTriggersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTriggersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncTriggersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        activation: Literal["event", "schedule", "custom"],
        name: str,
        conditions: trigger_create_params.Conditions | Omit = omit,
        custom_payload_schema: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        event_type: str | Omit = omit,
        schedule_rule: trigger_create_params.ScheduleRule | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerCreateResponse:
        """
        Create a trigger

        Args:
          custom_payload_schema: Optional JSON Schema for validating payloads sent to this custom trigger

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/triggers",
            body=await async_maybe_transform(
                {
                    "activation": activation,
                    "name": name,
                    "conditions": conditions,
                    "custom_payload_schema": custom_payload_schema,
                    "description": description,
                    "event_type": event_type,
                    "schedule_rule": schedule_rule,
                    "timezone": timezone,
                },
                trigger_create_params.TriggerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerCreateResponse,
        )

    async def retrieve(
        self,
        trigger_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerRetrieveResponse:
        """
        Get a trigger

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._get(
            path_template("/triggers/{trigger_id}", trigger_id=trigger_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerRetrieveResponse,
        )

    async def update(
        self,
        trigger_id: str,
        *,
        activation: Literal["event", "schedule", "custom"] | Omit = omit,
        conditions: trigger_update_params.Conditions | Omit = omit,
        custom_payload_schema: Optional[Dict[str, object]] | Omit = omit,
        description: str | Omit = omit,
        event_type: str | Omit = omit,
        name: str | Omit = omit,
        schedule_rule: trigger_update_params.ScheduleRule | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerUpdateResponse:
        """
        Update a trigger

        Args:
          custom_payload_schema: Optional JSON Schema for validating payloads sent to this custom trigger

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._patch(
            path_template("/triggers/{trigger_id}", trigger_id=trigger_id),
            body=await async_maybe_transform(
                {
                    "activation": activation,
                    "conditions": conditions,
                    "custom_payload_schema": custom_payload_schema,
                    "description": description,
                    "event_type": event_type,
                    "name": name,
                    "schedule_rule": schedule_rule,
                    "timezone": timezone,
                },
                trigger_update_params.TriggerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerUpdateResponse,
        )

    async def list(
        self,
        *,
        activation: Literal["event", "schedule", "custom"] | Omit = omit,
        event_type: str | Omit = omit,
        order_by: Literal["name", "createdAt", "updatedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerListResponse:
        """
        List triggers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/triggers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "activation": activation,
                        "event_type": event_type,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                    },
                    trigger_list_params.TriggerListParams,
                ),
            ),
            cast_to=TriggerListResponse,
        )

    async def delete(
        self,
        trigger_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerDeleteResponse:
        """
        Delete a trigger

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._delete(
            path_template("/triggers/{trigger_id}", trigger_id=trigger_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerDeleteResponse,
        )

    async def fire(
        self,
        trigger_id: str,
        *,
        payload: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggerFireResponse:
        """
        Invoke a custom trigger directly with an arbitrary JSON payload.

        Fan-out: a trigger may be referenced by multiple flows (workflows). Firing it
        enqueues one execution per enabled, non-deleted flow attached to this trigger,
        each receiving the same payload. The `enqueuedCount` in the response reports how
        many were enqueued (0 if no flows are attached, or if all matching flows are
        gated by a cooldown).

        Payload validation:

        - If the trigger has a `customPayloadSchema`, the payload is validated against
          it (JSON Schema via AJV).
        - If no schema is configured, the payload only needs to be a JSON object — any
          keys and values are accepted.

        Only triggers with `activation = "custom"` can be fired through this endpoint;
        event and schedule triggers return 409.

        Args:
          payload: Arbitrary JSON object forwarded to every flow attached to this trigger.
              Validated against the trigger's customPayloadSchema when one is configured;
              otherwise only "must be a JSON object" is enforced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trigger_id:
            raise ValueError(f"Expected a non-empty value for `trigger_id` but received {trigger_id!r}")
        return await self._post(
            path_template("/triggers/{trigger_id}/fire", trigger_id=trigger_id),
            body=await async_maybe_transform({"payload": payload}, trigger_fire_params.TriggerFireParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggerFireResponse,
        )


class TriggersResourceWithRawResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.create = to_raw_response_wrapper(
            triggers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            triggers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            triggers.update,
        )
        self.list = to_raw_response_wrapper(
            triggers.list,
        )
        self.delete = to_raw_response_wrapper(
            triggers.delete,
        )
        self.fire = to_raw_response_wrapper(
            triggers.fire,
        )


class AsyncTriggersResourceWithRawResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.create = async_to_raw_response_wrapper(
            triggers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            triggers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            triggers.update,
        )
        self.list = async_to_raw_response_wrapper(
            triggers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            triggers.delete,
        )
        self.fire = async_to_raw_response_wrapper(
            triggers.fire,
        )


class TriggersResourceWithStreamingResponse:
    def __init__(self, triggers: TriggersResource) -> None:
        self._triggers = triggers

        self.create = to_streamed_response_wrapper(
            triggers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            triggers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            triggers.update,
        )
        self.list = to_streamed_response_wrapper(
            triggers.list,
        )
        self.delete = to_streamed_response_wrapper(
            triggers.delete,
        )
        self.fire = to_streamed_response_wrapper(
            triggers.fire,
        )


class AsyncTriggersResourceWithStreamingResponse:
    def __init__(self, triggers: AsyncTriggersResource) -> None:
        self._triggers = triggers

        self.create = async_to_streamed_response_wrapper(
            triggers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            triggers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            triggers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            triggers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            triggers.delete,
        )
        self.fire = async_to_streamed_response_wrapper(
            triggers.fire,
        )
