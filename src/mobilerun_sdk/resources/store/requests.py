# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.store import request_create_params
from ..._base_client import make_request_options
from ...types.store.request_create_response import RequestCreateResponse

__all__ = ["RequestsResource", "AsyncRequestsResource"]


class RequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return RequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        platform: Literal["android", "ios"],
        requested: str,
        surface: Literal["store", "mcp", "api"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RequestCreateResponse:
        """
        Request a missing store app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/store/requests",
            body=maybe_transform(
                {
                    "platform": platform,
                    "requested": requested,
                    "surface": surface,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RequestCreateResponse,
        )


class AsyncRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        platform: Literal["android", "ios"],
        requested: str,
        surface: Literal["store", "mcp", "api"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RequestCreateResponse:
        """
        Request a missing store app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/store/requests",
            body=await async_maybe_transform(
                {
                    "platform": platform,
                    "requested": requested,
                    "surface": surface,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RequestCreateResponse,
        )


class RequestsResourceWithRawResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_raw_response_wrapper(
            requests.create,
        )


class AsyncRequestsResourceWithRawResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_raw_response_wrapper(
            requests.create,
        )


class RequestsResourceWithStreamingResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_streamed_response_wrapper(
            requests.create,
        )


class AsyncRequestsResourceWithStreamingResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_streamed_response_wrapper(
            requests.create,
        )
