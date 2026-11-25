# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.tasks import approval_decide_params
from ..._base_client import make_request_options
from ...types.tasks.approval_decide_response import ApprovalDecideResponse

__all__ = ["ApprovalsResource", "AsyncApprovalsResource"]


class ApprovalsResource(SyncAPIResource):
    """Tasks API"""

    @cached_property
    def with_raw_response(self) -> ApprovalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ApprovalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApprovalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ApprovalsResourceWithStreamingResponse(self)

    def decide(
        self,
        approval_id: str,
        *,
        task_id: str,
        decision: Literal["approve", "deny"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ApprovalDecideResponse:
        """
        Approve or deny the approval a running task is waiting for (see
        `pendingApproval` on the task). Deny ends the task as failed.

        Args:
          decision: Approve lets the task continue; deny ends it as failed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        if not approval_id:
            raise ValueError(f"Expected a non-empty value for `approval_id` but received {approval_id!r}")
        return self._post(
            path_template("/tasks/{task_id}/approvals/{approval_id}", task_id=task_id, approval_id=approval_id),
            body=maybe_transform({"decision": decision}, approval_decide_params.ApprovalDecideParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ApprovalDecideResponse,
        )


class AsyncApprovalsResource(AsyncAPIResource):
    """Tasks API"""

    @cached_property
    def with_raw_response(self) -> AsyncApprovalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApprovalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApprovalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncApprovalsResourceWithStreamingResponse(self)

    async def decide(
        self,
        approval_id: str,
        *,
        task_id: str,
        decision: Literal["approve", "deny"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ApprovalDecideResponse:
        """
        Approve or deny the approval a running task is waiting for (see
        `pendingApproval` on the task). Deny ends the task as failed.

        Args:
          decision: Approve lets the task continue; deny ends it as failed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        if not approval_id:
            raise ValueError(f"Expected a non-empty value for `approval_id` but received {approval_id!r}")
        return await self._post(
            path_template("/tasks/{task_id}/approvals/{approval_id}", task_id=task_id, approval_id=approval_id),
            body=await async_maybe_transform({"decision": decision}, approval_decide_params.ApprovalDecideParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ApprovalDecideResponse,
        )


class ApprovalsResourceWithRawResponse:
    def __init__(self, approvals: ApprovalsResource) -> None:
        self._approvals = approvals

        self.decide = to_raw_response_wrapper(
            approvals.decide,
        )


class AsyncApprovalsResourceWithRawResponse:
    def __init__(self, approvals: AsyncApprovalsResource) -> None:
        self._approvals = approvals

        self.decide = async_to_raw_response_wrapper(
            approvals.decide,
        )


class ApprovalsResourceWithStreamingResponse:
    def __init__(self, approvals: ApprovalsResource) -> None:
        self._approvals = approvals

        self.decide = to_streamed_response_wrapper(
            approvals.decide,
        )


class AsyncApprovalsResourceWithStreamingResponse:
    def __init__(self, approvals: AsyncApprovalsResource) -> None:
        self._approvals = approvals

        self.decide = async_to_streamed_response_wrapper(
            approvals.decide,
        )
