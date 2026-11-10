# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.devices.number_binding_list_response import NumberBindingListResponse
from ...types.devices.number_binding_list_candidates_response import NumberBindingListCandidatesResponse

__all__ = ["NumberBindingsResource", "AsyncNumberBindingsResource"]


class NumberBindingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NumberBindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NumberBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberBindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return NumberBindingsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberBindingListResponse:
        return self._get(
            "/devices/number-bindings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberBindingListResponse,
        )

    def list_candidates(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberBindingListCandidatesResponse:
        return self._get(
            "/devices/number-bindings/candidates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberBindingListCandidatesResponse,
        )


class AsyncNumberBindingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNumberBindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberBindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncNumberBindingsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberBindingListResponse:
        return await self._get(
            "/devices/number-bindings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberBindingListResponse,
        )

    async def list_candidates(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberBindingListCandidatesResponse:
        return await self._get(
            "/devices/number-bindings/candidates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberBindingListCandidatesResponse,
        )


class NumberBindingsResourceWithRawResponse:
    def __init__(self, number_bindings: NumberBindingsResource) -> None:
        self._number_bindings = number_bindings

        self.list = to_raw_response_wrapper(
            number_bindings.list,
        )
        self.list_candidates = to_raw_response_wrapper(
            number_bindings.list_candidates,
        )


class AsyncNumberBindingsResourceWithRawResponse:
    def __init__(self, number_bindings: AsyncNumberBindingsResource) -> None:
        self._number_bindings = number_bindings

        self.list = async_to_raw_response_wrapper(
            number_bindings.list,
        )
        self.list_candidates = async_to_raw_response_wrapper(
            number_bindings.list_candidates,
        )


class NumberBindingsResourceWithStreamingResponse:
    def __init__(self, number_bindings: NumberBindingsResource) -> None:
        self._number_bindings = number_bindings

        self.list = to_streamed_response_wrapper(
            number_bindings.list,
        )
        self.list_candidates = to_streamed_response_wrapper(
            number_bindings.list_candidates,
        )


class AsyncNumberBindingsResourceWithStreamingResponse:
    def __init__(self, number_bindings: AsyncNumberBindingsResource) -> None:
        self._number_bindings = number_bindings

        self.list = async_to_streamed_response_wrapper(
            number_bindings.list,
        )
        self.list_candidates = async_to_streamed_response_wrapper(
            number_bindings.list_candidates,
        )
