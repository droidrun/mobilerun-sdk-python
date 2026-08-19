# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._resource import SyncAPIResource, AsyncAPIResource

from .services import ServicesResource, AsyncServicesResource, ServicesResourceWithRawResponse, AsyncServicesResourceWithRawResponse, ServicesResourceWithStreamingResponse, AsyncServicesResourceWithStreamingResponse

from ...._compat import cached_property

from ....types.workflows.action_create_response import ActionCreateResponse

from ...._utils import maybe_transform, path_template, async_maybe_transform

from ...._base_client import make_request_options

from ...._types import Omit, omit, NotGiven

from typing import Dict

from ....types.workflows.action_retrieve_response import ActionRetrieveResponse

from ....types.workflows.action_update_response import ActionUpdateResponse

from ....types.workflows.action_list_response import ActionListResponse

from typing_extensions import Literal

from ....types.workflows.action_delete_response import ActionDeleteResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from ...._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body
from ....types.workflows import action_create_params
from ....types.workflows import action_update_params
from ....types.workflows import action_list_params

__all__ = ["ActionsResource", "AsyncActionsResource"]

class ActionsResource(SyncAPIResource):
    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

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

    def create(self,
    *,
    catalog_entry_id: str,
    name: str,
    description: str | Omit = omit,
    params: Dict[str, object] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionCreateResponse:
        """
        Create a reusable action from a catalog entry (`catalogEntryId`), with an
        optional `params` object supplying the values for that entry's service method.
        Returns 400 if the params are invalid for the chosen catalog entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/actions",
            body=maybe_transform({
                "catalog_entry_id": catalog_entry_id,
                "name": name,
                "description": description,
                "params": params,
            }, action_create_params.ActionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionCreateResponse,
        )

    def retrieve(self,
    action_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionRetrieveResponse:
        """
        Fetch a single action by its ID, including its configured service, method, and
        params. Returns 404 if no action matches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
          raise ValueError(
            f'Expected a non-empty value for `action_id` but received {action_id!r}'
          )
        return self._get(
            path_template("/actions/{action_id}", action_id=action_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionRetrieveResponse,
        )

    def update(self,
    action_id: str,
    *,
    description: str | Omit = omit,
    name: str | Omit = omit,
    params: Dict[str, object] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionUpdateResponse:
        """
        Partially update an action's name, description, or params; all fields are
        optional. Returns 404 if the action does not exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
          raise ValueError(
            f'Expected a non-empty value for `action_id` but received {action_id!r}'
          )
        return self._patch(
            path_template("/actions/{action_id}", action_id=action_id),
            body=maybe_transform({
                "description": description,
                "name": name,
                "params": params,
            }, action_update_params.ActionUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionUpdateResponse,
        )

    def list(self,
    *,
    order_by: Literal["name", "createdAt", "updatedAt"] | Omit = omit,
    order_by_direction: Literal["asc", "desc"] | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    search: str | Omit = omit,
    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionListResponse:
        """Return a paginated list of actions.

        Supports filtering by `service`, free-text
        `search`, and ordering by name, createdAt, or updatedAt.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/actions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "order_by": order_by,
                "order_by_direction": order_by_direction,
                "page": page,
                "page_size": page_size,
                "search": search,
                "service": service,
            }, action_list_params.ActionListParams)),
            cast_to=ActionListResponse,
        )

    def delete(self,
    action_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionDeleteResponse:
        """Delete an action by its ID.

        Returns 404 if no action matches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
          raise ValueError(
            f'Expected a non-empty value for `action_id` but received {action_id!r}'
          )
        return self._delete(
            path_template("/actions/{action_id}", action_id=action_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionDeleteResponse,
        )

class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

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

    async def create(self,
    *,
    catalog_entry_id: str,
    name: str,
    description: str | Omit = omit,
    params: Dict[str, object] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionCreateResponse:
        """
        Create a reusable action from a catalog entry (`catalogEntryId`), with an
        optional `params` object supplying the values for that entry's service method.
        Returns 400 if the params are invalid for the chosen catalog entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/actions",
            body=await async_maybe_transform({
                "catalog_entry_id": catalog_entry_id,
                "name": name,
                "description": description,
                "params": params,
            }, action_create_params.ActionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionCreateResponse,
        )

    async def retrieve(self,
    action_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionRetrieveResponse:
        """
        Fetch a single action by its ID, including its configured service, method, and
        params. Returns 404 if no action matches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
          raise ValueError(
            f'Expected a non-empty value for `action_id` but received {action_id!r}'
          )
        return await self._get(
            path_template("/actions/{action_id}", action_id=action_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionRetrieveResponse,
        )

    async def update(self,
    action_id: str,
    *,
    description: str | Omit = omit,
    name: str | Omit = omit,
    params: Dict[str, object] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionUpdateResponse:
        """
        Partially update an action's name, description, or params; all fields are
        optional. Returns 404 if the action does not exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
          raise ValueError(
            f'Expected a non-empty value for `action_id` but received {action_id!r}'
          )
        return await self._patch(
            path_template("/actions/{action_id}", action_id=action_id),
            body=await async_maybe_transform({
                "description": description,
                "name": name,
                "params": params,
            }, action_update_params.ActionUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionUpdateResponse,
        )

    async def list(self,
    *,
    order_by: Literal["name", "createdAt", "updatedAt"] | Omit = omit,
    order_by_direction: Literal["asc", "desc"] | Omit = omit,
    page: int | Omit = omit,
    page_size: int | Omit = omit,
    search: str | Omit = omit,
    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"] | Omit = omit,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionListResponse:
        """Return a paginated list of actions.

        Supports filtering by `service`, free-text
        `search`, and ordering by name, createdAt, or updatedAt.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/actions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "order_by": order_by,
                "order_by_direction": order_by_direction,
                "page": page,
                "page_size": page_size,
                "search": search,
                "service": service,
            }, action_list_params.ActionListParams)),
            cast_to=ActionListResponse,
        )

    async def delete(self,
    action_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> ActionDeleteResponse:
        """Delete an action by its ID.

        Returns 404 if no action matches.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_id:
          raise ValueError(
            f'Expected a non-empty value for `action_id` but received {action_id!r}'
          )
        return await self._delete(
            path_template("/actions/{action_id}", action_id=action_id),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionDeleteResponse,
        )

class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_raw_response_wrapper(
            actions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            actions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            actions.update,
        )
        self.list = to_raw_response_wrapper(
            actions.list,
        )
        self.delete = to_raw_response_wrapper(
            actions.delete,
        )

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._actions.services)

class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_raw_response_wrapper(
            actions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            actions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            actions.update,
        )
        self.list = async_to_raw_response_wrapper(
            actions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            actions.delete,
        )

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._actions.services)

class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_streamed_response_wrapper(
            actions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            actions.update,
        )
        self.list = to_streamed_response_wrapper(
            actions.list,
        )
        self.delete = to_streamed_response_wrapper(
            actions.delete,
        )

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._actions.services)

class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_streamed_response_wrapper(
            actions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            actions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            actions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            actions.delete,
        )

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._actions.services)