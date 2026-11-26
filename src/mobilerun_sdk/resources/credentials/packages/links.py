# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, required_args, maybe_transform, async_maybe_transform
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

    @overload
    def create(
        self,
        package_name: str,
        *,
        credential_name: str,
        field_map: Iterable[link_create_params.LinkOnePasswordCredentialBodyFieldMap],
        item_id: str,
        vault_id: str,
        provider: Literal["onepassword"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LinkCreateResponse:
        """
        Creates a read-only credential that resolves its values live from the provider.
        `provider` defaults to `onepassword` (vaultId, itemId, fieldMap). `wallet` takes
        a cardId, is only allowed in the reserved payment_cards package, and only the
        cardholder may link the card (404 otherwise). Never replaces an existing
        credential of the same name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        package_name: str,
        *,
        card_id: str,
        credential_name: str,
        provider: Literal["wallet"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LinkCreateResponse:
        """
        Creates a read-only credential that resolves its values live from the provider.
        `provider` defaults to `onepassword` (vaultId, itemId, fieldMap). `wallet` takes
        a cardId, is only allowed in the reserved payment_cards package, and only the
        cardholder may link the card (404 otherwise). Never replaces an existing
        credential of the same name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["credential_name", "field_map", "item_id", "vault_id"], ["card_id", "credential_name", "provider"])
    def create(
        self,
        package_name: str,
        *,
        credential_name: str,
        field_map: Iterable[link_create_params.LinkOnePasswordCredentialBodyFieldMap] | Omit = omit,
        item_id: str | Omit = omit,
        vault_id: str | Omit = omit,
        provider: Literal["onepassword"] | Literal["wallet"] | Omit = omit,
        card_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LinkCreateResponse:
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
                    "provider": provider,
                    "card_id": card_id,
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

    @overload
    async def create(
        self,
        package_name: str,
        *,
        credential_name: str,
        field_map: Iterable[link_create_params.LinkOnePasswordCredentialBodyFieldMap],
        item_id: str,
        vault_id: str,
        provider: Literal["onepassword"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LinkCreateResponse:
        """
        Creates a read-only credential that resolves its values live from the provider.
        `provider` defaults to `onepassword` (vaultId, itemId, fieldMap). `wallet` takes
        a cardId, is only allowed in the reserved payment_cards package, and only the
        cardholder may link the card (404 otherwise). Never replaces an existing
        credential of the same name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        package_name: str,
        *,
        card_id: str,
        credential_name: str,
        provider: Literal["wallet"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LinkCreateResponse:
        """
        Creates a read-only credential that resolves its values live from the provider.
        `provider` defaults to `onepassword` (vaultId, itemId, fieldMap). `wallet` takes
        a cardId, is only allowed in the reserved payment_cards package, and only the
        cardholder may link the card (404 otherwise). Never replaces an existing
        credential of the same name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["credential_name", "field_map", "item_id", "vault_id"], ["card_id", "credential_name", "provider"])
    async def create(
        self,
        package_name: str,
        *,
        credential_name: str,
        field_map: Iterable[link_create_params.LinkOnePasswordCredentialBodyFieldMap] | Omit = omit,
        item_id: str | Omit = omit,
        vault_id: str | Omit = omit,
        provider: Literal["onepassword"] | Literal["wallet"] | Omit = omit,
        card_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LinkCreateResponse:
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
                    "provider": provider,
                    "card_id": card_id,
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
