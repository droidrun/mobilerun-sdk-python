# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import stream_token_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.stream_token_create_response import StreamTokenCreateResponse

__all__ = ["StreamTokensResource", "AsyncStreamTokensResource"]


class StreamTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StreamTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StreamTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return StreamTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        device_id: str,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> StreamTokenCreateResponse:
        """Mint a short-lived, single-use stream token for a device.

        The token permits
        streaming and control.

        Args:
          allowed_origins: Exact `https://host[:port]` origins (and `http://localhost[:port]`) allowed to
              connect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/identity/stream-keys",
            body=maybe_transform(
                {
                    "device_id": device_id,
                    "allowed_origins": allowed_origins,
                    "ttl_seconds": ttl_seconds,
                },
                stream_token_create_params.StreamTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=StreamTokenCreateResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Revoke a stream token by its id.

        The token can no longer be used to start a
        stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/identity/stream-keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncStreamTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStreamTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStreamTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncStreamTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        device_id: str,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        ttl_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> StreamTokenCreateResponse:
        """Mint a short-lived, single-use stream token for a device.

        The token permits
        streaming and control.

        Args:
          allowed_origins: Exact `https://host[:port]` origins (and `http://localhost[:port]`) allowed to
              connect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/identity/stream-keys",
            body=await async_maybe_transform(
                {
                    "device_id": device_id,
                    "allowed_origins": allowed_origins,
                    "ttl_seconds": ttl_seconds,
                },
                stream_token_create_params.StreamTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=StreamTokenCreateResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Revoke a stream token by its id.

        The token can no longer be used to start a
        stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/identity/stream-keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class StreamTokensResourceWithRawResponse:
    def __init__(self, stream_tokens: StreamTokensResource) -> None:
        self._stream_tokens = stream_tokens

        self.create = to_raw_response_wrapper(
            stream_tokens.create,
        )
        self.delete = to_raw_response_wrapper(
            stream_tokens.delete,
        )


class AsyncStreamTokensResourceWithRawResponse:
    def __init__(self, stream_tokens: AsyncStreamTokensResource) -> None:
        self._stream_tokens = stream_tokens

        self.create = async_to_raw_response_wrapper(
            stream_tokens.create,
        )
        self.delete = async_to_raw_response_wrapper(
            stream_tokens.delete,
        )


class StreamTokensResourceWithStreamingResponse:
    def __init__(self, stream_tokens: StreamTokensResource) -> None:
        self._stream_tokens = stream_tokens

        self.create = to_streamed_response_wrapper(
            stream_tokens.create,
        )
        self.delete = to_streamed_response_wrapper(
            stream_tokens.delete,
        )


class AsyncStreamTokensResourceWithStreamingResponse:
    def __init__(self, stream_tokens: AsyncStreamTokensResource) -> None:
        self._stream_tokens = stream_tokens

        self.create = async_to_streamed_response_wrapper(
            stream_tokens.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            stream_tokens.delete,
        )
