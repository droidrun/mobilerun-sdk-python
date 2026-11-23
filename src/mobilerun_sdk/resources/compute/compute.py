# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .sandboxes.sandboxes import (
    SandboxesResource,
    AsyncSandboxesResource,
    SandboxesResourceWithRawResponse,
    AsyncSandboxesResourceWithRawResponse,
    SandboxesResourceWithStreamingResponse,
    AsyncSandboxesResourceWithStreamingResponse,
)

__all__ = ["ComputeResource", "AsyncComputeResource"]


class ComputeResource(SyncAPIResource):
    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def sandboxes(self) -> SandboxesResource:
        return SandboxesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ComputeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ComputeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComputeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ComputeResourceWithStreamingResponse(self)


class AsyncComputeResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def sandboxes(self) -> AsyncSandboxesResource:
        return AsyncSandboxesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncComputeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncComputeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComputeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncComputeResourceWithStreamingResponse(self)


class ComputeResourceWithRawResponse:
    def __init__(self, compute: ComputeResource) -> None:
        self._compute = compute

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._compute.runs)

    @cached_property
    def sandboxes(self) -> SandboxesResourceWithRawResponse:
        return SandboxesResourceWithRawResponse(self._compute.sandboxes)


class AsyncComputeResourceWithRawResponse:
    def __init__(self, compute: AsyncComputeResource) -> None:
        self._compute = compute

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._compute.runs)

    @cached_property
    def sandboxes(self) -> AsyncSandboxesResourceWithRawResponse:
        return AsyncSandboxesResourceWithRawResponse(self._compute.sandboxes)


class ComputeResourceWithStreamingResponse:
    def __init__(self, compute: ComputeResource) -> None:
        self._compute = compute

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._compute.runs)

    @cached_property
    def sandboxes(self) -> SandboxesResourceWithStreamingResponse:
        return SandboxesResourceWithStreamingResponse(self._compute.sandboxes)


class AsyncComputeResourceWithStreamingResponse:
    def __init__(self, compute: AsyncComputeResource) -> None:
        self._compute = compute

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._compute.runs)

    @cached_property
    def sandboxes(self) -> AsyncSandboxesResourceWithStreamingResponse:
        return AsyncSandboxesResourceWithStreamingResponse(self._compute.sandboxes)
