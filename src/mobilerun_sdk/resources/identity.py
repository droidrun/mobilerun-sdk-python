# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.identity_me_response import IdentityMeResponse

__all__ = ["IdentityResource", "AsyncIdentityResource"]


class IdentityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return IdentityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return IdentityResourceWithStreamingResponse(self)

    def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityMeResponse:
        """Return the user, owner and authentication method of the calling credential."""
        return self._get(
            "/identity/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityMeResponse,
        )


class AsyncIdentityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncIdentityResourceWithStreamingResponse(self)

    async def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityMeResponse:
        """Return the user, owner and authentication method of the calling credential."""
        return await self._get(
            "/identity/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityMeResponse,
        )


class IdentityResourceWithRawResponse:
    def __init__(self, identity: IdentityResource) -> None:
        self._identity = identity

        self.me = to_raw_response_wrapper(
            identity.me,
        )


class AsyncIdentityResourceWithRawResponse:
    def __init__(self, identity: AsyncIdentityResource) -> None:
        self._identity = identity

        self.me = async_to_raw_response_wrapper(
            identity.me,
        )


class IdentityResourceWithStreamingResponse:
    def __init__(self, identity: IdentityResource) -> None:
        self._identity = identity

        self.me = to_streamed_response_wrapper(
            identity.me,
        )


class AsyncIdentityResourceWithStreamingResponse:
    def __init__(self, identity: AsyncIdentityResource) -> None:
        self._identity = identity

        self.me = async_to_streamed_response_wrapper(
            identity.me,
        )
