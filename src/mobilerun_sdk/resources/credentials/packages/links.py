# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.credentials.packages import link_create_params
from ....types.credentials.packages.link_create_response import LinkCreateResponse

__all__ = ["LinksResource", "AsyncLinksResource"]


class LinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return LinksResourceWithStreamingResponse(self)

    def create(
        self,
        package_name: str,
        *,
        credential_name: str,
        field_map: Iterable[link_create_params.FieldMap],
        item_id: str,
        vault_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LinkCreateResponse:
        """
        Link a 1Password item to a credential

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return self._post(
            path_template("/credentials/packages/{package_name}/links", package_name=package_name),
            body=maybe_transform(
                {
                    "credential_name": credential_name,
                    "field_map": field_map,
                    "item_id": item_id,
                    "vault_id": vault_id,
                },
                link_create_params.LinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LinkCreateResponse,
        )


class AsyncLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        package_name: str,
        *,
        credential_name: str,
        field_map: Iterable[link_create_params.FieldMap],
        item_id: str,
        vault_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LinkCreateResponse:
        """
        Link a 1Password item to a credential

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return await self._post(
            path_template("/credentials/packages/{package_name}/links", package_name=package_name),
            body=await async_maybe_transform(
                {
                    "credential_name": credential_name,
                    "field_map": field_map,
                    "item_id": item_id,
                    "vault_id": vault_id,
                },
                link_create_params.LinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LinkCreateResponse,
        )


class LinksResourceWithRawResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.create = to_raw_response_wrapper(
            links.create,
        )


class AsyncLinksResourceWithRawResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.create = async_to_raw_response_wrapper(
            links.create,
        )


class LinksResourceWithStreamingResponse:
    def __init__(self, links: LinksResource) -> None:
        self._links = links

        self.create = to_streamed_response_wrapper(
            links.create,
        )


class AsyncLinksResourceWithStreamingResponse:
    def __init__(self, links: AsyncLinksResource) -> None:
        self._links = links

        self.create = async_to_streamed_response_wrapper(
            links.create,
        )
