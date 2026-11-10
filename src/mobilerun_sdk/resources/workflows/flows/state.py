# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.workflows.flows.state_list_response import StateListResponse
from ....types.workflows.flows.state_delete_response import StateDeleteResponse
from ....types.workflows.flows.state_list_versions_response import StateListVersionsResponse

__all__ = ["StateResource", "AsyncStateResource"]


class StateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return StateResourceWithStreamingResponse(self)

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
    ) -> StateListResponse:
        """
        List the keys a routine has saved with `state.save`, with the metadata of each
        key's newest version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return self._get(
            path_template("/flows/{flow_id}/state", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateListResponse,
        )

    def delete(
        self,
        key: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> StateDeleteResponse:
        """Delete every version of one state key.

        The next `state.load` of the key reports
        `found: false`. Deleting an unknown key succeeds.

        Args:
          key: State key: 1–128 characters of letters, digits, ".", "\\__" or "-".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._delete(
            path_template("/flows/{flow_id}/state/{key}", flow_id=flow_id, key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=StateDeleteResponse,
        )

    def list_versions(
        self,
        key: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StateListVersionsResponse:
        """
        Return the retained versions of one state key, newest first, including each
        saved value. An unknown key returns an empty list.

        Args:
          key: State key: 1–128 characters of letters, digits, ".", "\\__" or "-".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            path_template("/flows/{flow_id}/state/{key}/versions", flow_id=flow_id, key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateListVersionsResponse,
        )


class AsyncStateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncStateResourceWithStreamingResponse(self)

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
    ) -> StateListResponse:
        """
        List the keys a routine has saved with `state.save`, with the metadata of each
        key's newest version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return await self._get(
            path_template("/flows/{flow_id}/state", flow_id=flow_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateListResponse,
        )

    async def delete(
        self,
        key: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> StateDeleteResponse:
        """Delete every version of one state key.

        The next `state.load` of the key reports
        `found: false`. Deleting an unknown key succeeds.

        Args:
          key: State key: 1–128 characters of letters, digits, ".", "\\__" or "-".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._delete(
            path_template("/flows/{flow_id}/state/{key}", flow_id=flow_id, key=key),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=StateDeleteResponse,
        )

    async def list_versions(
        self,
        key: str,
        *,
        flow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StateListVersionsResponse:
        """
        Return the retained versions of one state key, newest first, including each
        saved value. An unknown key returns an empty list.

        Args:
          key: State key: 1–128 characters of letters, digits, ".", "\\__" or "-".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            path_template("/flows/{flow_id}/state/{key}/versions", flow_id=flow_id, key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateListVersionsResponse,
        )


class StateResourceWithRawResponse:
    def __init__(self, state: StateResource) -> None:
        self._state = state

        self.list = to_raw_response_wrapper(
            state.list,
        )
        self.delete = to_raw_response_wrapper(
            state.delete,
        )
        self.list_versions = to_raw_response_wrapper(
            state.list_versions,
        )


class AsyncStateResourceWithRawResponse:
    def __init__(self, state: AsyncStateResource) -> None:
        self._state = state

        self.list = async_to_raw_response_wrapper(
            state.list,
        )
        self.delete = async_to_raw_response_wrapper(
            state.delete,
        )
        self.list_versions = async_to_raw_response_wrapper(
            state.list_versions,
        )


class StateResourceWithStreamingResponse:
    def __init__(self, state: StateResource) -> None:
        self._state = state

        self.list = to_streamed_response_wrapper(
            state.list,
        )
        self.delete = to_streamed_response_wrapper(
            state.delete,
        )
        self.list_versions = to_streamed_response_wrapper(
            state.list_versions,
        )


class AsyncStateResourceWithStreamingResponse:
    def __init__(self, state: AsyncStateResource) -> None:
        self._state = state

        self.list = async_to_streamed_response_wrapper(
            state.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            state.delete,
        )
        self.list_versions = async_to_streamed_response_wrapper(
            state.list_versions,
        )
