# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import esim_list_params, esim_create_params, esim_import_params, esim_update_params, esim_install_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.esim_list_response import EsimListResponse
from ...types.esim_create_response import EsimCreateResponse
from ...types.esim_import_response import EsimImportResponse
from ...types.esim_update_response import EsimUpdateResponse
from ...types.esim_install_response import EsimInstallResponse
from ...types.esim_capacity_response import EsimCapacityResponse
from ...types.esim_retrieve_response import EsimRetrieveResponse
from ...types.esim_selector_response import EsimSelectorResponse
from ...types.esim_install_status_response import EsimInstallStatusResponse
from ...types.esim_confirm_payment_response import EsimConfirmPaymentResponse

__all__ = ["EsimsResource", "AsyncEsimsResource"]


class EsimsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EsimsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EsimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EsimsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return EsimsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimCreateResponse:
        """
        Purchases a physical eSIM from available inventory for the authenticated owner.
        Returns 409 when no stock is available, or 402 with a billing checkout URL when
        billing capacity is exhausted.

        Args:
          idempotency_key: Client-supplied key; replaying the same key returns the original purchase
              instead of buying again

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/numbers/esims",
            body=maybe_transform({"idempotency_key": idempotency_key}, esim_create_params.EsimCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimCreateResponse,
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
    ) -> EsimRetrieveResponse:
        """
        Retrieves a single physical eSIM.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/numbers/esims/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        msisdn: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimUpdateResponse:
        """Updates the eSIM's self-reported msisdn and/or display name.

        Both fields are
        optional, but the request body itself is required. Omitting a field leaves it
        unchanged; setting it to null or an empty string clears it. `name` is capped at
        15 characters. Available regardless of the eSIM's current status.

        Args:
          msisdn: Self-reported E.164 MSISDN for this eSIM's line. Omit to leave unchanged;
              null/empty clears it. An unverified label — never used for routing.

          name: User-defined display label — NFC-normalized, up to 15 GRAPHEMES (not UTF-16 code
              units; an emoji/flag may span several). Omit to leave unchanged;
              null/empty/whitespace-only clears it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/numbers/esims/{id}", id=id),
            body=maybe_transform(
                {
                    "msisdn": msisdn,
                    "name": name,
                },
                esim_update_params.EsimUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimUpdateResponse,
        )

    def list(
        self,
        *,
        mine: Literal["true", "false"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["all", "in_stock", "owned", "installing", "installed", "install_failed", "retired"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimListResponse:
        """
        Lists physical eSIMs owned by the authenticated owner.

        Args:
          mine: Only include eSIMs created by the calling actor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/numbers/esims",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "mine": mine,
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                    },
                    esim_list_params.EsimListParams,
                ),
            ),
            cast_to=EsimListResponse,
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
    ) -> None:
        """Removes a physical eSIM.

        Idempotent — returns 204 for a fresh removal or a
        replay of an already-removed eSIM. An eSIM currently installed on a device is
        uninstalled first, then removed. An eSIM in an intermediate install state
        returns 409 `operator_resolution_required` and requires manual resolution.
        Returns 404 if the eSIM doesn't exist or isn't owned by the caller.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/numbers/esims/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def capacity(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimCapacityResponse:
        """
        Reports whether a free device is currently available, for pre-checking the
        import flow before upload. This is a hint only, not a reservation —
        `POST /esims/import` re-checks availability at submit time.
        """
        return self._get(
            "/numbers/esims/capacity",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimCapacityResponse,
        )

    def confirm_payment(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimConfirmPaymentResponse:
        """
        Checks for proof of payment for this eSIM's current rent and confirms it if
        found. If no proof is available yet, returns 200 with the eSIM unchanged rather
        than an error. Always returns the current eSIM state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/numbers/esims/{id}/confirm-payment", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimConfirmPaymentResponse,
        )

    def import_(
        self,
        *,
        auto_install: bool | Omit = omit,
        carrier_name: str | Omit = omit,
        confirmation_code: str | Omit = omit,
        country_code: str | Omit = omit,
        device_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        lpa_code: str | Omit = omit,
        matching_id: str | Omit = omit,
        msisdn: str | Omit = omit,
        name: Optional[str] | Omit = omit,
        notes: str | Omit = omit,
        smdp_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimImportResponse:
        """
        Registers a bring-your-own (BYO) eSIM activation code as owned inventory.
        Provide either `{ smdpAddress, matchingId?, confirmationCode? }` or
        `{ lpaCode }` — supplying both, or neither, returns 400. An optional `name` sets
        a display label on the created eSIM (up to 15 characters).

        Subject to per-owner and daily import limits, and disabled entirely unless BYO
        imports are enabled for this deployment (409 `byo_disabled`). Idempotent via
        `idempotencyKey`: replaying the same key with an identical request returns the
        original response; the same key with a different request returns 409
        `idempotency_conflict`.

        When rent-first billing is off (default), the import is free — 201 with the
        eSIM. Setting `autoInstall: true` additionally dispatches an install immediately
        after import (`deviceId` may only be set together with `autoInstall`): this
        returns 202 with `{esim, operationId, statusUrl}` when the install claim
        succeeds (poll `GET /esims/{id}/install-status`), or 201 with the eSIM plus
        `installDispatch: {ok: false, reason}` when the install could not be dispatched
        — the import itself still succeeds either way.

        When rent-first billing is on, import additionally requires available device
        capacity (409 `device_pool_empty`) and is subject to a per-owner
        awaiting-payment cap (409 `byo_awaiting_payment_cap`). On success the eSIM is
        created `awaiting_payment` and a checkout is started: 201 with
        `{esim, rentStatus, checkoutUrl}` when the checkout URL is ready immediately, or
        202 with `checkoutUrl: null` otherwise — poll `GET /esims/{id}` until it's
        populated. Once payment is confirmed, install is triggered automatically.

        Args:
          auto_install: Rent OFF only: dispatch install-on-device immediately after a successful import.
              No-op when ESIM_BYO_RENT_ENABLED=true.

          device_id: physedge device id to auto-install onto; requires autoInstall:true and rent OFF.
              Omit for a random pool device.

          idempotency_key: Client-supplied key; replaying the same key+request returns the original import
              instead of importing again

          lpa_code: Full LPA activation code

          msisdn: Self-reported E.164 MSISDN for this eSIM's line — an unverified label, never
              used for routing

          name: User-defined display label — NFC-normalized, up to 15 GRAPHEMES (not UTF-16 code
              units; an emoji/flag may span several). Omit/null/empty/whitespace-only leaves
              it unset.

          smdp_address: SM-DP+ activation host — bare hostname ONLY, no port/scheme/path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/numbers/esims/import",
            body=maybe_transform(
                {
                    "auto_install": auto_install,
                    "carrier_name": carrier_name,
                    "confirmation_code": confirmation_code,
                    "country_code": country_code,
                    "device_id": device_id,
                    "idempotency_key": idempotency_key,
                    "lpa_code": lpa_code,
                    "matching_id": matching_id,
                    "msisdn": msisdn,
                    "name": name,
                    "notes": notes,
                    "smdp_address": smdp_address,
                },
                esim_import_params.EsimImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimImportResponse,
        )

    def install(
        self,
        id: str,
        *,
        device_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimInstallResponse:
        """Installs the eSIM's activation code onto a device.

        `deviceId` is optional — omit
        it to use an available device from the pool. This call is asynchronous: it
        returns 202 with `{esim, operationId, statusUrl}` immediately, and the result is
        available by polling `GET /esims/{id}/install-status`. Retrying with the same
        request is safe if a response is lost.

        Returns 409 when the eSIM is not in the `owned` state, or when no device is
        currently available (see `reason`). When rent-first billing is enabled, a BYO
        eSIM whose rent isn't active returns 402 with `{esim, rentStatus, checkoutUrl}`
        instead.

        Args:
          device_id: physedge device id to install the eSIM onto; omit for a random pool device

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/numbers/esims/{id}/install", id=id),
            body=maybe_transform({"device_id": device_id}, esim_install_params.EsimInstallParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimInstallResponse,
        )

    def install_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimInstallStatusResponse:
        """
        Returns the eSIM's current install status, checking for a terminal outcome if an
        install is still in progress.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/numbers/esims/{id}/install-status", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimInstallStatusResponse,
        )

    def selector(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimSelectorResponse:
        """
        Returns a lightweight list (id, msisdn, carrierName, status, masked iccid) for
        use in a message filter dropdown. Unlike `GET /esims`, this includes all
        statuses, including retired eSIMs, and is not paginated.
        """
        return self._get(
            "/numbers/esims/selector",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimSelectorResponse,
        )


class AsyncEsimsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEsimsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEsimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEsimsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncEsimsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimCreateResponse:
        """
        Purchases a physical eSIM from available inventory for the authenticated owner.
        Returns 409 when no stock is available, or 402 with a billing checkout URL when
        billing capacity is exhausted.

        Args:
          idempotency_key: Client-supplied key; replaying the same key returns the original purchase
              instead of buying again

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/numbers/esims",
            body=await async_maybe_transform({"idempotency_key": idempotency_key}, esim_create_params.EsimCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimCreateResponse,
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
    ) -> EsimRetrieveResponse:
        """
        Retrieves a single physical eSIM.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/numbers/esims/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        msisdn: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimUpdateResponse:
        """Updates the eSIM's self-reported msisdn and/or display name.

        Both fields are
        optional, but the request body itself is required. Omitting a field leaves it
        unchanged; setting it to null or an empty string clears it. `name` is capped at
        15 characters. Available regardless of the eSIM's current status.

        Args:
          msisdn: Self-reported E.164 MSISDN for this eSIM's line. Omit to leave unchanged;
              null/empty clears it. An unverified label — never used for routing.

          name: User-defined display label — NFC-normalized, up to 15 GRAPHEMES (not UTF-16 code
              units; an emoji/flag may span several). Omit to leave unchanged;
              null/empty/whitespace-only clears it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/numbers/esims/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "msisdn": msisdn,
                    "name": name,
                },
                esim_update_params.EsimUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimUpdateResponse,
        )

    async def list(
        self,
        *,
        mine: Literal["true", "false"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal["all", "in_stock", "owned", "installing", "installed", "install_failed", "retired"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimListResponse:
        """
        Lists physical eSIMs owned by the authenticated owner.

        Args:
          mine: Only include eSIMs created by the calling actor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/numbers/esims",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "mine": mine,
                        "page": page,
                        "page_size": page_size,
                        "status": status,
                    },
                    esim_list_params.EsimListParams,
                ),
            ),
            cast_to=EsimListResponse,
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
    ) -> None:
        """Removes a physical eSIM.

        Idempotent — returns 204 for a fresh removal or a
        replay of an already-removed eSIM. An eSIM currently installed on a device is
        uninstalled first, then removed. An eSIM in an intermediate install state
        returns 409 `operator_resolution_required` and requires manual resolution.
        Returns 404 if the eSIM doesn't exist or isn't owned by the caller.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/numbers/esims/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def capacity(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimCapacityResponse:
        """
        Reports whether a free device is currently available, for pre-checking the
        import flow before upload. This is a hint only, not a reservation —
        `POST /esims/import` re-checks availability at submit time.
        """
        return await self._get(
            "/numbers/esims/capacity",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimCapacityResponse,
        )

    async def confirm_payment(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimConfirmPaymentResponse:
        """
        Checks for proof of payment for this eSIM's current rent and confirms it if
        found. If no proof is available yet, returns 200 with the eSIM unchanged rather
        than an error. Always returns the current eSIM state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/numbers/esims/{id}/confirm-payment", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimConfirmPaymentResponse,
        )

    async def import_(
        self,
        *,
        auto_install: bool | Omit = omit,
        carrier_name: str | Omit = omit,
        confirmation_code: str | Omit = omit,
        country_code: str | Omit = omit,
        device_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        lpa_code: str | Omit = omit,
        matching_id: str | Omit = omit,
        msisdn: str | Omit = omit,
        name: Optional[str] | Omit = omit,
        notes: str | Omit = omit,
        smdp_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimImportResponse:
        """
        Registers a bring-your-own (BYO) eSIM activation code as owned inventory.
        Provide either `{ smdpAddress, matchingId?, confirmationCode? }` or
        `{ lpaCode }` — supplying both, or neither, returns 400. An optional `name` sets
        a display label on the created eSIM (up to 15 characters).

        Subject to per-owner and daily import limits, and disabled entirely unless BYO
        imports are enabled for this deployment (409 `byo_disabled`). Idempotent via
        `idempotencyKey`: replaying the same key with an identical request returns the
        original response; the same key with a different request returns 409
        `idempotency_conflict`.

        When rent-first billing is off (default), the import is free — 201 with the
        eSIM. Setting `autoInstall: true` additionally dispatches an install immediately
        after import (`deviceId` may only be set together with `autoInstall`): this
        returns 202 with `{esim, operationId, statusUrl}` when the install claim
        succeeds (poll `GET /esims/{id}/install-status`), or 201 with the eSIM plus
        `installDispatch: {ok: false, reason}` when the install could not be dispatched
        — the import itself still succeeds either way.

        When rent-first billing is on, import additionally requires available device
        capacity (409 `device_pool_empty`) and is subject to a per-owner
        awaiting-payment cap (409 `byo_awaiting_payment_cap`). On success the eSIM is
        created `awaiting_payment` and a checkout is started: 201 with
        `{esim, rentStatus, checkoutUrl}` when the checkout URL is ready immediately, or
        202 with `checkoutUrl: null` otherwise — poll `GET /esims/{id}` until it's
        populated. Once payment is confirmed, install is triggered automatically.

        Args:
          auto_install: Rent OFF only: dispatch install-on-device immediately after a successful import.
              No-op when ESIM_BYO_RENT_ENABLED=true.

          device_id: physedge device id to auto-install onto; requires autoInstall:true and rent OFF.
              Omit for a random pool device.

          idempotency_key: Client-supplied key; replaying the same key+request returns the original import
              instead of importing again

          lpa_code: Full LPA activation code

          msisdn: Self-reported E.164 MSISDN for this eSIM's line — an unverified label, never
              used for routing

          name: User-defined display label — NFC-normalized, up to 15 GRAPHEMES (not UTF-16 code
              units; an emoji/flag may span several). Omit/null/empty/whitespace-only leaves
              it unset.

          smdp_address: SM-DP+ activation host — bare hostname ONLY, no port/scheme/path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/numbers/esims/import",
            body=await async_maybe_transform(
                {
                    "auto_install": auto_install,
                    "carrier_name": carrier_name,
                    "confirmation_code": confirmation_code,
                    "country_code": country_code,
                    "device_id": device_id,
                    "idempotency_key": idempotency_key,
                    "lpa_code": lpa_code,
                    "matching_id": matching_id,
                    "msisdn": msisdn,
                    "name": name,
                    "notes": notes,
                    "smdp_address": smdp_address,
                },
                esim_import_params.EsimImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimImportResponse,
        )

    async def install(
        self,
        id: str,
        *,
        device_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimInstallResponse:
        """Installs the eSIM's activation code onto a device.

        `deviceId` is optional — omit
        it to use an available device from the pool. This call is asynchronous: it
        returns 202 with `{esim, operationId, statusUrl}` immediately, and the result is
        available by polling `GET /esims/{id}/install-status`. Retrying with the same
        request is safe if a response is lost.

        Returns 409 when the eSIM is not in the `owned` state, or when no device is
        currently available (see `reason`). When rent-first billing is enabled, a BYO
        eSIM whose rent isn't active returns 402 with `{esim, rentStatus, checkoutUrl}`
        instead.

        Args:
          device_id: physedge device id to install the eSIM onto; omit for a random pool device

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/numbers/esims/{id}/install", id=id),
            body=await async_maybe_transform({"device_id": device_id}, esim_install_params.EsimInstallParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimInstallResponse,
        )

    async def install_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimInstallStatusResponse:
        """
        Returns the eSIM's current install status, checking for a terminal outcome if an
        install is still in progress.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/numbers/esims/{id}/install-status", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimInstallStatusResponse,
        )

    async def selector(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EsimSelectorResponse:
        """
        Returns a lightweight list (id, msisdn, carrierName, status, masked iccid) for
        use in a message filter dropdown. Unlike `GET /esims`, this includes all
        statuses, including retired eSIMs, and is not paginated.
        """
        return await self._get(
            "/numbers/esims/selector",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EsimSelectorResponse,
        )


class EsimsResourceWithRawResponse:
    def __init__(self, esims: EsimsResource) -> None:
        self._esims = esims

        self.create = to_raw_response_wrapper(
            esims.create,
        )
        self.retrieve = to_raw_response_wrapper(
            esims.retrieve,
        )
        self.update = to_raw_response_wrapper(
            esims.update,
        )
        self.list = to_raw_response_wrapper(
            esims.list,
        )
        self.delete = to_raw_response_wrapper(
            esims.delete,
        )
        self.capacity = to_raw_response_wrapper(
            esims.capacity,
        )
        self.confirm_payment = to_raw_response_wrapper(
            esims.confirm_payment,
        )
        self.import_ = to_raw_response_wrapper(
            esims.import_,
        )
        self.install = to_raw_response_wrapper(
            esims.install,
        )
        self.install_status = to_raw_response_wrapper(
            esims.install_status,
        )
        self.selector = to_raw_response_wrapper(
            esims.selector,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._esims.messages)


class AsyncEsimsResourceWithRawResponse:
    def __init__(self, esims: AsyncEsimsResource) -> None:
        self._esims = esims

        self.create = async_to_raw_response_wrapper(
            esims.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            esims.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            esims.update,
        )
        self.list = async_to_raw_response_wrapper(
            esims.list,
        )
        self.delete = async_to_raw_response_wrapper(
            esims.delete,
        )
        self.capacity = async_to_raw_response_wrapper(
            esims.capacity,
        )
        self.confirm_payment = async_to_raw_response_wrapper(
            esims.confirm_payment,
        )
        self.import_ = async_to_raw_response_wrapper(
            esims.import_,
        )
        self.install = async_to_raw_response_wrapper(
            esims.install,
        )
        self.install_status = async_to_raw_response_wrapper(
            esims.install_status,
        )
        self.selector = async_to_raw_response_wrapper(
            esims.selector,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._esims.messages)


class EsimsResourceWithStreamingResponse:
    def __init__(self, esims: EsimsResource) -> None:
        self._esims = esims

        self.create = to_streamed_response_wrapper(
            esims.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            esims.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            esims.update,
        )
        self.list = to_streamed_response_wrapper(
            esims.list,
        )
        self.delete = to_streamed_response_wrapper(
            esims.delete,
        )
        self.capacity = to_streamed_response_wrapper(
            esims.capacity,
        )
        self.confirm_payment = to_streamed_response_wrapper(
            esims.confirm_payment,
        )
        self.import_ = to_streamed_response_wrapper(
            esims.import_,
        )
        self.install = to_streamed_response_wrapper(
            esims.install,
        )
        self.install_status = to_streamed_response_wrapper(
            esims.install_status,
        )
        self.selector = to_streamed_response_wrapper(
            esims.selector,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._esims.messages)


class AsyncEsimsResourceWithStreamingResponse:
    def __init__(self, esims: AsyncEsimsResource) -> None:
        self._esims = esims

        self.create = async_to_streamed_response_wrapper(
            esims.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            esims.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            esims.update,
        )
        self.list = async_to_streamed_response_wrapper(
            esims.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            esims.delete,
        )
        self.capacity = async_to_streamed_response_wrapper(
            esims.capacity,
        )
        self.confirm_payment = async_to_streamed_response_wrapper(
            esims.confirm_payment,
        )
        self.import_ = async_to_streamed_response_wrapper(
            esims.import_,
        )
        self.install = async_to_streamed_response_wrapper(
            esims.install,
        )
        self.install_status = async_to_streamed_response_wrapper(
            esims.install_status,
        )
        self.selector = async_to_streamed_response_wrapper(
            esims.selector,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._esims.messages)
