# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
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
from ....types.workflows import flow_list_params, flow_clone_params, flow_create_params, flow_update_params
from ....types.workflows.flow_list_response import FlowListResponse
from ....types.workflows.flow_clone_response import FlowCloneResponse
from ....types.workflows.flow_create_response import FlowCreateResponse
from ....types.workflows.flow_delete_response import FlowDeleteResponse
from ....types.workflows.flow_update_response import FlowUpdateResponse
from ....types.workflows.flow_unblock_response import FlowUnblockResponse
from ....types.workflows.flow_retrieve_response import FlowRetrieveResponse

__all__ = ["FlowsResource", "AsyncFlowsResource"]


class FlowsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return FlowsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        actions: Iterable[flow_create_params.Action],
        name: str,
        trigger_id: str,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowCreateResponse:
        """
        Create a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/flows",
            body=maybe_transform(
                {
                    "actions": actions,
                    "name": name,
                    "trigger_id": trigger_id,
                    "cooldown_scope": cooldown_scope,
                    "cooldown_seconds": cooldown_seconds,
                    "description": description,
                    "enabled": enabled,
                },
                flow_create_params.FlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowCreateResponse,
        )

    def retrieve(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowRetrieveResponse:
        """
        Get a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._get(
            path_template("/flows/{flow_id}", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowRetrieveResponse,
        )

    def update(
        self,
        flow_id: str,
        *,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        trigger_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowUpdateResponse:
        """
        Update a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._patch(
            path_template("/flows/{flow_id}", flow_id=flow_id),
            body=maybe_transform(
                {
                    "cooldown_scope": cooldown_scope,
                    "cooldown_seconds": cooldown_seconds,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "trigger_id": trigger_id,
                },
                flow_update_params.FlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowUpdateResponse,
        )

    def list(
        self,
        *,
        enabled: Optional[bool] | Omit = omit,
        order_by: Literal["name", "createdAt", "updatedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: List[Literal["healthy", "failing", "blocked"]] | Omit = omit,
        trigger_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowListResponse:
        """
        List flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/flows",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                        "trigger_id": trigger_id,
                    },
                    flow_list_params.FlowListParams,
                ),
            ),
            cast_to=FlowListResponse,
        )

    def delete(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowDeleteResponse:
        """
        Delete a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._delete(
            path_template("/flows/{flow_id}", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowDeleteResponse,
        )

    def clone(
        self,
        flow_id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowCloneResponse:
        """
        Clone a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._post(
            path_template("/flows/{flow_id}/clone", flow_id=flow_id),
            body=maybe_transform({"name": name}, flow_clone_params.FlowCloneParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowCloneResponse,
        )

    def unblock(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowUnblockResponse:
        """Clear a flow's blocked status after fixing the underlying issue.

        Idempotent —
        safe to call on already-healthy flows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._post(
            path_template("/flows/{flow_id}/unblock", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowUnblockResponse,
        )


class AsyncFlowsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncFlowsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        actions: Iterable[flow_create_params.Action],
        name: str,
        trigger_id: str,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowCreateResponse:
        """
        Create a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/flows",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "name": name,
                    "trigger_id": trigger_id,
                    "cooldown_scope": cooldown_scope,
                    "cooldown_seconds": cooldown_seconds,
                    "description": description,
                    "enabled": enabled,
                },
                flow_create_params.FlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowCreateResponse,
        )

    async def retrieve(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowRetrieveResponse:
        """
        Get a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._get(
            path_template("/flows/{flow_id}", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowRetrieveResponse,
        )

    async def update(
        self,
        flow_id: str,
        *,
        cooldown_scope: Literal["flow", "device"] | Omit = omit,
        cooldown_seconds: Optional[int] | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        trigger_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowUpdateResponse:
        """
        Update a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._patch(
            path_template("/flows/{flow_id}", flow_id=flow_id),
            body=await async_maybe_transform(
                {
                    "cooldown_scope": cooldown_scope,
                    "cooldown_seconds": cooldown_seconds,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "trigger_id": trigger_id,
                },
                flow_update_params.FlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowUpdateResponse,
        )

    async def list(
        self,
        *,
        enabled: Optional[bool] | Omit = omit,
        order_by: Literal["name", "createdAt", "updatedAt"] | Omit = omit,
        order_by_direction: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: List[Literal["healthy", "failing", "blocked"]] | Omit = omit,
        trigger_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowListResponse:
        """
        List flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/flows",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "enabled": enabled,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                        "trigger_id": trigger_id,
                    },
                    flow_list_params.FlowListParams,
                ),
            ),
            cast_to=FlowListResponse,
        )

    async def delete(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowDeleteResponse:
        """
        Delete a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._delete(
            path_template("/flows/{flow_id}", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowDeleteResponse,
        )

    async def clone(
        self,
        flow_id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowCloneResponse:
        """
        Clone a flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._post(
            path_template("/flows/{flow_id}/clone", flow_id=flow_id),
            body=await async_maybe_transform({"name": name}, flow_clone_params.FlowCloneParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowCloneResponse,
        )

    async def unblock(
        self,
        flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FlowUnblockResponse:
        """Clear a flow's blocked status after fixing the underlying issue.

        Idempotent —
        safe to call on already-healthy flows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._post(
            path_template("/flows/{flow_id}/unblock", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FlowUnblockResponse,
        )


class FlowsResourceWithRawResponse:
    def __init__(self, flows: FlowsResource) -> None:
        self._flows = flows

        self.create = to_raw_response_wrapper(
            flows.create,
        )
        self.retrieve = to_raw_response_wrapper(
            flows.retrieve,
        )
        self.update = to_raw_response_wrapper(
            flows.update,
        )
        self.list = to_raw_response_wrapper(
            flows.list,
        )
        self.delete = to_raw_response_wrapper(
            flows.delete,
        )
        self.clone = to_raw_response_wrapper(
            flows.clone,
        )
        self.unblock = to_raw_response_wrapper(
            flows.unblock,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._flows.actions)


class AsyncFlowsResourceWithRawResponse:
    def __init__(self, flows: AsyncFlowsResource) -> None:
        self._flows = flows

        self.create = async_to_raw_response_wrapper(
            flows.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            flows.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            flows.update,
        )
        self.list = async_to_raw_response_wrapper(
            flows.list,
        )
        self.delete = async_to_raw_response_wrapper(
            flows.delete,
        )
        self.clone = async_to_raw_response_wrapper(
            flows.clone,
        )
        self.unblock = async_to_raw_response_wrapper(
            flows.unblock,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._flows.actions)


class FlowsResourceWithStreamingResponse:
    def __init__(self, flows: FlowsResource) -> None:
        self._flows = flows

        self.create = to_streamed_response_wrapper(
            flows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            flows.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            flows.update,
        )
        self.list = to_streamed_response_wrapper(
            flows.list,
        )
        self.delete = to_streamed_response_wrapper(
            flows.delete,
        )
        self.clone = to_streamed_response_wrapper(
            flows.clone,
        )
        self.unblock = to_streamed_response_wrapper(
            flows.unblock,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._flows.actions)


class AsyncFlowsResourceWithStreamingResponse:
    def __init__(self, flows: AsyncFlowsResource) -> None:
        self._flows = flows

        self.create = async_to_streamed_response_wrapper(
            flows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            flows.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            flows.update,
        )
        self.list = async_to_streamed_response_wrapper(
            flows.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            flows.delete,
        )
        self.clone = async_to_streamed_response_wrapper(
            flows.clone,
        )
        self.unblock = async_to_streamed_response_wrapper(
            flows.unblock,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._flows.actions)
