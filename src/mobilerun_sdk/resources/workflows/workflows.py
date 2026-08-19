# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._resource import SyncAPIResource, AsyncAPIResource

from .triggers import TriggersResource, AsyncTriggersResource, TriggersResourceWithRawResponse, AsyncTriggersResourceWithRawResponse, TriggersResourceWithStreamingResponse, AsyncTriggersResourceWithStreamingResponse

from ..._compat import cached_property

from .action_catalog import ActionCatalogResource, AsyncActionCatalogResource, ActionCatalogResourceWithRawResponse, AsyncActionCatalogResourceWithRawResponse, ActionCatalogResourceWithStreamingResponse, AsyncActionCatalogResourceWithStreamingResponse

from .actions.actions import ActionsResource, AsyncActionsResource, ActionsResourceWithRawResponse, AsyncActionsResourceWithRawResponse, ActionsResourceWithStreamingResponse, AsyncActionsResourceWithStreamingResponse

from .flows.flows import FlowsResource, AsyncFlowsResource, FlowsResourceWithRawResponse, AsyncFlowsResourceWithRawResponse, FlowsResourceWithStreamingResponse, AsyncFlowsResourceWithStreamingResponse

from .events import EventsResource, AsyncEventsResource, EventsResourceWithRawResponse, AsyncEventsResourceWithRawResponse, EventsResourceWithStreamingResponse, AsyncEventsResourceWithStreamingResponse

from .executions import ExecutionsResource, AsyncExecutionsResource, ExecutionsResourceWithRawResponse, AsyncExecutionsResourceWithRawResponse, ExecutionsResourceWithStreamingResponse, AsyncExecutionsResourceWithStreamingResponse

from .timezones import TimezonesResource, AsyncTimezonesResource, TimezonesResourceWithRawResponse, AsyncTimezonesResourceWithRawResponse, TimezonesResourceWithStreamingResponse, AsyncTimezonesResourceWithStreamingResponse

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]

class WorkflowsResource(SyncAPIResource):
    @cached_property
    def triggers(self) -> TriggersResource:
        return TriggersResource(self._client)

    @cached_property
    def action_catalog(self) -> ActionCatalogResource:
        return ActionCatalogResource(self._client)

    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def flows(self) -> FlowsResource:
        return FlowsResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def executions(self) -> ExecutionsResource:
        return ExecutionsResource(self._client)

    @cached_property
    def timezones(self) -> TimezonesResource:
        return TimezonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return WorkflowsResourceWithStreamingResponse(self)

class AsyncWorkflowsResource(AsyncAPIResource):
    @cached_property
    def triggers(self) -> AsyncTriggersResource:
        return AsyncTriggersResource(self._client)

    @cached_property
    def action_catalog(self) -> AsyncActionCatalogResource:
        return AsyncActionCatalogResource(self._client)

    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def flows(self) -> AsyncFlowsResource:
        return AsyncFlowsResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def executions(self) -> AsyncExecutionsResource:
        return AsyncExecutionsResource(self._client)

    @cached_property
    def timezones(self) -> AsyncTimezonesResource:
        return AsyncTimezonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncWorkflowsResourceWithStreamingResponse(self)

class WorkflowsResourceWithRawResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

    @cached_property
    def triggers(self) -> TriggersResourceWithRawResponse:
        return TriggersResourceWithRawResponse(self._workflows.triggers)

    @cached_property
    def action_catalog(self) -> ActionCatalogResourceWithRawResponse:
        return ActionCatalogResourceWithRawResponse(self._workflows.action_catalog)

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._workflows.actions)

    @cached_property
    def flows(self) -> FlowsResourceWithRawResponse:
        return FlowsResourceWithRawResponse(self._workflows.flows)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._workflows.events)

    @cached_property
    def executions(self) -> ExecutionsResourceWithRawResponse:
        return ExecutionsResourceWithRawResponse(self._workflows.executions)

    @cached_property
    def timezones(self) -> TimezonesResourceWithRawResponse:
        return TimezonesResourceWithRawResponse(self._workflows.timezones)

class AsyncWorkflowsResourceWithRawResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

    @cached_property
    def triggers(self) -> AsyncTriggersResourceWithRawResponse:
        return AsyncTriggersResourceWithRawResponse(self._workflows.triggers)

    @cached_property
    def action_catalog(self) -> AsyncActionCatalogResourceWithRawResponse:
        return AsyncActionCatalogResourceWithRawResponse(self._workflows.action_catalog)

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._workflows.actions)

    @cached_property
    def flows(self) -> AsyncFlowsResourceWithRawResponse:
        return AsyncFlowsResourceWithRawResponse(self._workflows.flows)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._workflows.events)

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithRawResponse:
        return AsyncExecutionsResourceWithRawResponse(self._workflows.executions)

    @cached_property
    def timezones(self) -> AsyncTimezonesResourceWithRawResponse:
        return AsyncTimezonesResourceWithRawResponse(self._workflows.timezones)

class WorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

    @cached_property
    def triggers(self) -> TriggersResourceWithStreamingResponse:
        return TriggersResourceWithStreamingResponse(self._workflows.triggers)

    @cached_property
    def action_catalog(self) -> ActionCatalogResourceWithStreamingResponse:
        return ActionCatalogResourceWithStreamingResponse(self._workflows.action_catalog)

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._workflows.actions)

    @cached_property
    def flows(self) -> FlowsResourceWithStreamingResponse:
        return FlowsResourceWithStreamingResponse(self._workflows.flows)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._workflows.events)

    @cached_property
    def executions(self) -> ExecutionsResourceWithStreamingResponse:
        return ExecutionsResourceWithStreamingResponse(self._workflows.executions)

    @cached_property
    def timezones(self) -> TimezonesResourceWithStreamingResponse:
        return TimezonesResourceWithStreamingResponse(self._workflows.timezones)

class AsyncWorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

    @cached_property
    def triggers(self) -> AsyncTriggersResourceWithStreamingResponse:
        return AsyncTriggersResourceWithStreamingResponse(self._workflows.triggers)

    @cached_property
    def action_catalog(self) -> AsyncActionCatalogResourceWithStreamingResponse:
        return AsyncActionCatalogResourceWithStreamingResponse(self._workflows.action_catalog)

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._workflows.actions)

    @cached_property
    def flows(self) -> AsyncFlowsResourceWithStreamingResponse:
        return AsyncFlowsResourceWithStreamingResponse(self._workflows.flows)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._workflows.events)

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithStreamingResponse:
        return AsyncExecutionsResourceWithStreamingResponse(self._workflows.executions)

    @cached_property
    def timezones(self) -> AsyncTimezonesResourceWithStreamingResponse:
        return AsyncTimezonesResourceWithStreamingResponse(self._workflows.timezones)