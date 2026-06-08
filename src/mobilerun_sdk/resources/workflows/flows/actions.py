# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ....types.workflows.flows import action_add_params, action_replace_params
from ....types.workflows.flows.action_add_response import ActionAddResponse
from ....types.workflows.flows.action_list_response import ActionListResponse
from ....types.workflows.flow_action_overrides_param import FlowActionOverridesParam
from ....types.workflows.flows.action_remove_response import ActionRemoveResponse
from ....types.workflows.flow_child_action_input_param import FlowChildActionInputParam
from ....types.workflows.flows.action_replace_response import ActionReplaceResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def list(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionListResponse:
        """
        List actions for a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._get(
            path_template("/flows/{flow_id}/actions", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionListResponse,
        )

    def add(
        self,
        flow_id: str,
        *,
        action_id: str,
        position: int,
        children: Iterable[FlowChildActionInputParam] | Omit = omit,
        continue_on_error: bool | Omit = omit,
        device_id: str | Omit = omit,
        name_override: str | Omit = omit,
        overrides: Optional[FlowActionOverridesParam] | Omit = omit,
        parent_flow_action_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAddResponse:
        """
        Add an action to a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._post(
            path_template("/flows/{flow_id}/actions", flow_id=flow_id),
            body=maybe_transform(
                {
                    "action_id": action_id,
                    "position": position,
                    "children": children,
                    "continue_on_error": continue_on_error,
                    "device_id": device_id,
                    "name_override": name_override,
                    "overrides": overrides,
                    "parent_flow_action_id": parent_flow_action_id,
                },
                action_add_params.ActionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddResponse,
        )

    def remove(
        self,
        flow_action_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRemoveResponse:
        """
        Remove an action from a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not flow_action_id:
            raise ValueError(f"Expected a non-empty value for `flow_action_id` but received {flow_action_id!r}")
        return self._delete(
            path_template("/flows/{flow_id}/actions/{flow_action_id}", flow_id=flow_id, flow_action_id=flow_action_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveResponse,
        )

    def replace(
        self,
        flow_id: str,
        *,
        actions: Iterable[action_replace_params.Action],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionReplaceResponse:
        """
        Replace all actions for a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._put(
            path_template("/flows/{flow_id}/actions", flow_id=flow_id),
            body=maybe_transform({"actions": actions}, action_replace_params.ActionReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionReplaceResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def list(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionListResponse:
        """
        List actions for a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._get(
            path_template("/flows/{flow_id}/actions", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionListResponse,
        )

    async def add(
        self,
        flow_id: str,
        *,
        action_id: str,
        position: int,
        children: Iterable[FlowChildActionInputParam] | Omit = omit,
        continue_on_error: bool | Omit = omit,
        device_id: str | Omit = omit,
        name_override: str | Omit = omit,
        overrides: Optional[FlowActionOverridesParam] | Omit = omit,
        parent_flow_action_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionAddResponse:
        """
        Add an action to a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._post(
            path_template("/flows/{flow_id}/actions", flow_id=flow_id),
            body=await async_maybe_transform(
                {
                    "action_id": action_id,
                    "position": position,
                    "children": children,
                    "continue_on_error": continue_on_error,
                    "device_id": device_id,
                    "name_override": name_override,
                    "overrides": overrides,
                    "parent_flow_action_id": parent_flow_action_id,
                },
                action_add_params.ActionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddResponse,
        )

    async def remove(
        self,
        flow_action_id: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRemoveResponse:
        """
        Remove an action from a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not flow_action_id:
            raise ValueError(f"Expected a non-empty value for `flow_action_id` but received {flow_action_id!r}")
        return await self._delete(
            path_template("/flows/{flow_id}/actions/{flow_action_id}", flow_id=flow_id, flow_action_id=flow_action_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveResponse,
        )

    async def replace(
        self,
        flow_id: str,
        *,
        actions: Iterable[action_replace_params.Action],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionReplaceResponse:
        """
        Replace all actions for a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._put(
            path_template("/flows/{flow_id}/actions", flow_id=flow_id),
            body=await async_maybe_transform({"actions": actions}, action_replace_params.ActionReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionReplaceResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.list = to_raw_response_wrapper(
            actions.list,
        )
        self.add = to_raw_response_wrapper(
            actions.add,
        )
        self.remove = to_raw_response_wrapper(
            actions.remove,
        )
        self.replace = to_raw_response_wrapper(
            actions.replace,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.list = async_to_raw_response_wrapper(
            actions.list,
        )
        self.add = async_to_raw_response_wrapper(
            actions.add,
        )
        self.remove = async_to_raw_response_wrapper(
            actions.remove,
        )
        self.replace = async_to_raw_response_wrapper(
            actions.replace,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.list = to_streamed_response_wrapper(
            actions.list,
        )
        self.add = to_streamed_response_wrapper(
            actions.add,
        )
        self.remove = to_streamed_response_wrapper(
            actions.remove,
        )
        self.replace = to_streamed_response_wrapper(
            actions.replace,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.list = async_to_streamed_response_wrapper(
            actions.list,
        )
        self.add = async_to_streamed_response_wrapper(
            actions.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            actions.remove,
        )
        self.replace = async_to_streamed_response_wrapper(
            actions.replace,
        )
