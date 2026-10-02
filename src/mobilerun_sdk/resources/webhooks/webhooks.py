# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, overload

import httpx

from ...types import webhook_list_params, webhook_create_params, webhook_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .deliveries import (
    DeliveriesResource,
    AsyncDeliveriesResource,
    DeliveriesResourceWithRawResponse,
    AsyncDeliveriesResourceWithRawResponse,
    DeliveriesResourceWithStreamingResponse,
    AsyncDeliveriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .integrations import (
    IntegrationsResource,
    AsyncIntegrationsResource,
    IntegrationsResourceWithRawResponse,
    AsyncIntegrationsResourceWithRawResponse,
    IntegrationsResourceWithStreamingResponse,
    AsyncIntegrationsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.webhook_list_response import WebhookListResponse
from ...types.webhook_create_response import WebhookCreateResponse
from ...types.webhook_update_response import WebhookUpdateResponse
from ...types.webhook_retrieve_response import WebhookRetrieveResponse
from ...types.webhook_rotate_secret_response import WebhookRotateSecretResponse
from ...types.webhook_test_delivery_response import WebhookTestDeliveryResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def integrations(self) -> IntegrationsResource:
        return IntegrationsResource(self._client)

    @cached_property
    def deliveries(self) -> DeliveriesResource:
        return DeliveriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        url: str,
        description: str | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        kind: Literal["http"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookCreateResponse:
        """
        Creates a webhook subscription and an optional list of event types to subscribe
        to (defaults to all when omitted). `kind: "http"` (the default) delivers signed
        JSON to a URL; the response includes the generated signing secret, which is
        returned only once at creation time and cannot be retrieved later.
        `kind: "integration"` posts each event as a message into a connected integration
        target (e.g. a Slack channel): pick the `capability` from
        `GET /webhooks/integrations` and the `args` from
        `GET /webhooks/integrations/{capabilityId}/targets`. Integration webhooks have
        no signing secret.

        Args:
          kind: Delivery transport. Omitted ⇒ `http`.

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
        *,
        args: Dict[str, object],
        capability: webhook_create_params.Variant1Capability,
        kind: Literal["integration"],
        description: str | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookCreateResponse:
        """
        Creates a webhook subscription and an optional list of event types to subscribe
        to (defaults to all when omitted). `kind: "http"` (the default) delivers signed
        JSON to a URL; the response includes the generated signing secret, which is
        returned only once at creation time and cannot be retrieved later.
        `kind: "integration"` posts each event as a message into a connected integration
        target (e.g. a Slack channel): pick the `capability` from
        `GET /webhooks/integrations` and the `args` from
        `GET /webhooks/integrations/{capabilityId}/targets`. Integration webhooks have
        no signing secret.

        Args:
          args: Target args exactly as returned by
              `GET /webhooks/integrations/{capabilityId}/targets`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["url"], ["args", "capability", "kind"])
    def create(
        self,
        *,
        url: str | Omit = omit,
        description: str | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        kind: Literal["http"] | Literal["integration"] | Omit = omit,
        args: Dict[str, object] | Omit = omit,
        capability: webhook_create_params.Variant1Capability | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookCreateResponse:
        return self._post(
            "/webhooks",
            body=maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "event_types": event_types,
                    "kind": kind,
                    "args": args,
                    "capability": capability,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveResponse:
        """
        Returns a single webhook subscription by id, including its URL (or integration
        target), subscribed event types, state, and system-observed delivery health. The
        signing secret is never included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        state: Literal["ACTIVE", "DISABLED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookUpdateResponse:
        """Updates a webhook subscription.

        Any combination of the subscribed event types,
        state (ACTIVE or DISABLED), and description may be changed, and at least one
        field must be supplied. Setting state to ACTIVE re-enables a subscription that
        was auto-blocked after sustained delivery failures. The URL or integration
        target cannot be changed; delete and recreate the webhook instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/webhooks/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "event_types": event_types,
                    "state": state,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookUpdateResponse,
        )

    def list(
        self,
        *,
        created_by: str | Omit = omit,
        kind: Literal["http", "integration"] | Omit = omit,
        mine: Literal["true", "false"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["active", "failing", "blocked", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """
        Returns a paginated list of your webhook subscriptions, optionally filtered by
        status (active, failing, blocked, or disabled), by `search` (a case-insensitive
        substring match against the URL or description), and/or by delivery `kind`. The
        response also includes per-status counts across all of your subscriptions (of
        the requested `kind`, if given; the other filters do not apply to the counts).

        Args:
          created_by: Only include webhooks created by this actor id. Mutually exclusive with `mine`.

          kind: Only include webhooks of this delivery kind.

          mine: When true, only include webhooks created by you (not just owned by your org).

          search: Case-insensitive substring match against the URL or description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/webhooks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_by": created_by,
                        "kind": kind,
                        "mine": mine,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                    },
                    webhook_list_params.WebhookListParams,
                ),
            ),
            cast_to=WebhookListResponse,
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
        """Deletes a webhook subscription so it stops receiving deliveries.

        Returns 204 No
        Content on success.

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
            path_template("/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def rotate_secret(
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
    ) -> WebhookRotateSecretResponse:
        """
        Generates a new signing secret for the webhook subscription and returns it once
        in the response. The previous secret is replaced immediately, so any signature
        verification on your endpoint must be updated to use the new value. Only `http`
        webhooks have a signing secret; for `integration` webhooks this returns 400.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/webhooks/{id}/rotate-secret", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookRotateSecretResponse,
        )

    def test_delivery(
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
    ) -> WebhookTestDeliveryResponse:
        """
        Sends a single test payload to the webhook subscription URL (or a test message
        to its integration target) to verify connectivity. The response reports whether
        the attempt succeeded along with the returned HTTP status code or error, if any.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/webhooks/{id}/test", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookTestDeliveryResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        return AsyncIntegrationsResource(self._client)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResource:
        return AsyncDeliveriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        url: str,
        description: str | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        kind: Literal["http"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookCreateResponse:
        """
        Creates a webhook subscription and an optional list of event types to subscribe
        to (defaults to all when omitted). `kind: "http"` (the default) delivers signed
        JSON to a URL; the response includes the generated signing secret, which is
        returned only once at creation time and cannot be retrieved later.
        `kind: "integration"` posts each event as a message into a connected integration
        target (e.g. a Slack channel): pick the `capability` from
        `GET /webhooks/integrations` and the `args` from
        `GET /webhooks/integrations/{capabilityId}/targets`. Integration webhooks have
        no signing secret.

        Args:
          kind: Delivery transport. Omitted ⇒ `http`.

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
        *,
        args: Dict[str, object],
        capability: webhook_create_params.Variant1Capability,
        kind: Literal["integration"],
        description: str | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookCreateResponse:
        """
        Creates a webhook subscription and an optional list of event types to subscribe
        to (defaults to all when omitted). `kind: "http"` (the default) delivers signed
        JSON to a URL; the response includes the generated signing secret, which is
        returned only once at creation time and cannot be retrieved later.
        `kind: "integration"` posts each event as a message into a connected integration
        target (e.g. a Slack channel): pick the `capability` from
        `GET /webhooks/integrations` and the `args` from
        `GET /webhooks/integrations/{capabilityId}/targets`. Integration webhooks have
        no signing secret.

        Args:
          args: Target args exactly as returned by
              `GET /webhooks/integrations/{capabilityId}/targets`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["url"], ["args", "capability", "kind"])
    async def create(
        self,
        *,
        url: str | Omit = omit,
        description: str | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        kind: Literal["http"] | Literal["integration"] | Omit = omit,
        args: Dict[str, object] | Omit = omit,
        capability: webhook_create_params.Variant1Capability | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookCreateResponse:
        return await self._post(
            "/webhooks",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "event_types": event_types,
                    "kind": kind,
                    "args": args,
                    "capability": capability,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveResponse:
        """
        Returns a single webhook subscription by id, including its URL (or integration
        target), subscribed event types, state, and system-observed delivery health. The
        signing secret is never included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        event_types: SequenceNotStr[str] | Omit = omit,
        state: Literal["ACTIVE", "DISABLED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookUpdateResponse:
        """Updates a webhook subscription.

        Any combination of the subscribed event types,
        state (ACTIVE or DISABLED), and description may be changed, and at least one
        field must be supplied. Setting state to ACTIVE re-enables a subscription that
        was auto-blocked after sustained delivery failures. The URL or integration
        target cannot be changed; delete and recreate the webhook instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/webhooks/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "event_types": event_types,
                    "state": state,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookUpdateResponse,
        )

    async def list(
        self,
        *,
        created_by: str | Omit = omit,
        kind: Literal["http", "integration"] | Omit = omit,
        mine: Literal["true", "false"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["active", "failing", "blocked", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """
        Returns a paginated list of your webhook subscriptions, optionally filtered by
        status (active, failing, blocked, or disabled), by `search` (a case-insensitive
        substring match against the URL or description), and/or by delivery `kind`. The
        response also includes per-status counts across all of your subscriptions (of
        the requested `kind`, if given; the other filters do not apply to the counts).

        Args:
          created_by: Only include webhooks created by this actor id. Mutually exclusive with `mine`.

          kind: Only include webhooks of this delivery kind.

          mine: When true, only include webhooks created by you (not just owned by your org).

          search: Case-insensitive substring match against the URL or description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/webhooks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_by": created_by,
                        "kind": kind,
                        "mine": mine,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                    },
                    webhook_list_params.WebhookListParams,
                ),
            ),
            cast_to=WebhookListResponse,
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
        """Deletes a webhook subscription so it stops receiving deliveries.

        Returns 204 No
        Content on success.

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
            path_template("/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def rotate_secret(
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
    ) -> WebhookRotateSecretResponse:
        """
        Generates a new signing secret for the webhook subscription and returns it once
        in the response. The previous secret is replaced immediately, so any signature
        verification on your endpoint must be updated to use the new value. Only `http`
        webhooks have a signing secret; for `integration` webhooks this returns 400.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/webhooks/{id}/rotate-secret", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookRotateSecretResponse,
        )

    async def test_delivery(
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
    ) -> WebhookTestDeliveryResponse:
        """
        Sends a single test payload to the webhook subscription URL (or a test message
        to its integration target) to verify connectivity. The response reports whether
        the attempt succeeded along with the returned HTTP status code or error, if any.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/webhooks/{id}/test", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookTestDeliveryResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.rotate_secret = to_raw_response_wrapper(
            webhooks.rotate_secret,
        )
        self.test_delivery = to_raw_response_wrapper(
            webhooks.test_delivery,
        )

    @cached_property
    def integrations(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self._webhooks.integrations)

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithRawResponse:
        return DeliveriesResourceWithRawResponse(self._webhooks.deliveries)


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            webhooks.rotate_secret,
        )
        self.test_delivery = async_to_raw_response_wrapper(
            webhooks.test_delivery,
        )

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self._webhooks.integrations)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithRawResponse:
        return AsyncDeliveriesResourceWithRawResponse(self._webhooks.deliveries)


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            webhooks.rotate_secret,
        )
        self.test_delivery = to_streamed_response_wrapper(
            webhooks.test_delivery,
        )

    @cached_property
    def integrations(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self._webhooks.integrations)

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithStreamingResponse:
        return DeliveriesResourceWithStreamingResponse(self._webhooks.deliveries)


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            webhooks.rotate_secret,
        )
        self.test_delivery = async_to_streamed_response_wrapper(
            webhooks.test_delivery,
        )

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self._webhooks.integrations)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        return AsyncDeliveriesResourceWithStreamingResponse(self._webhooks.deliveries)
