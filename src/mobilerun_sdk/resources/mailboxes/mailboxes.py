# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    mailbox_otp_params,
    mailbox_list_params,
    mailbox_create_params,
    mailbox_update_params,
    mailbox_restart_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.mailbox_otp_response import MailboxOtpResponse
from ...types.mailbox_list_response import MailboxListResponse
from ...types.mailbox_create_response import MailboxCreateResponse
from ...types.mailbox_delete_response import MailboxDeleteResponse
from ...types.mailbox_update_response import MailboxUpdateResponse
from ...types.mailbox_restart_response import MailboxRestartResponse
from ...types.mailbox_capacity_response import MailboxCapacityResponse
from ...types.mailbox_retrieve_response import MailboxRetrieveResponse
from ...types.mailbox_uncancel_response import MailboxUncancelResponse

__all__ = ["MailboxesResource", "AsyncMailboxesResource"]


class MailboxesResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MailboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MailboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MailboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return MailboxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        client_request_id: str,
        billing_preference: Literal["included", "included_only", "rent"] | Omit = omit,
        domain_id: str | Omit = omit,
        label: str | Omit = omit,
        local_part: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxCreateResponse:
        """Creates a mailbox on the default domain or a connected custom domain.

        An
        optional `localPart` selects the address. Replaying the same `clientRequestId`
        and payload returns the original mailbox. Poll the mailbox when a 202 response
        does not yet include a checkout URL.

        Args:
          billing_preference: included uses package capacity when available and otherwise starts paid
              checkout; included_only fails without creating a paid reservation when no
              included slot remains; rent always starts paid checkout.

          domain_id: Optional active custom mailbox domain owned by the caller. Omit to use the
              system domain.

          local_part: Optional mailbox name before the "@". Omit to generate a random address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mailboxes",
            body=maybe_transform(
                {
                    "client_request_id": client_request_id,
                    "billing_preference": billing_preference,
                    "domain_id": domain_id,
                    "label": label,
                    "local_part": local_part,
                },
                mailbox_create_params.MailboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxCreateResponse,
        )

    def retrieve(
        self,
        mailbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxRetrieveResponse:
        """
        Get a mailbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return self._get(
            path_template("/mailboxes/{mailbox_id}", mailbox_id=mailbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxRetrieveResponse,
        )

    def update(
        self,
        mailbox_id: str,
        *,
        label: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxUpdateResponse:
        """
        Updates the label of a mailbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return self._patch(
            path_template("/mailboxes/{mailbox_id}", mailbox_id=mailbox_id),
            body=maybe_transform({"label": label}, mailbox_update_params.MailboxUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxListResponse:
        """
        Lists the caller-owned mailboxes with page-based pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/mailboxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    mailbox_list_params.MailboxListParams,
                ),
            ),
            cast_to=MailboxListResponse,
        )

    def delete(
        self,
        mailbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxDeleteResponse:
        """
        Cancels a pending mailbox or schedules an active paid mailbox for cancellation.
        Existing addresses and messages are retained. Repeating the request is safe.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return self._delete(
            path_template("/mailboxes/{mailbox_id}", mailbox_id=mailbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxDeleteResponse,
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
    ) -> MailboxCapacityResponse:
        """Returns the number of mailboxes currently available through included capacity."""
        return self._get(
            "/mailboxes/capacity",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxCapacityResponse,
        )

    def otp(
        self,
        mailbox_id: str,
        *,
        after: Union[str, datetime] | Omit = omit,
        max_length: int | Omit = omit,
        min_length: int | Omit = omit,
        sender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxOtpResponse:
        """Returns the most likely recent OTP for the mailbox.

        Returns 204 when no matching
        code is available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return self._get(
            path_template("/mailboxes/{mailbox_id}/otp", mailbox_id=mailbox_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "max_length": max_length,
                        "min_length": min_length,
                        "sender": sender,
                    },
                    mailbox_otp_params.MailboxOtpParams,
                ),
            ),
            cast_to=MailboxOtpResponse,
        )

    def restart(
        self,
        mailbox_id: str,
        *,
        billing_preference: Literal["included", "included_only", "rent"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxRestartResponse:
        """Restarts an archived mailbox with the same address.

        Uses included capacity when
        available unless paid service is requested.

        Args:
          billing_preference: included uses package capacity when available and otherwise starts paid
              checkout; included_only fails without creating a paid reservation when no
              included slot remains; rent always starts paid checkout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return self._post(
            path_template("/mailboxes/{mailbox_id}/restart", mailbox_id=mailbox_id),
            body=maybe_transform(
                {"billing_preference": billing_preference}, mailbox_restart_params.MailboxRestartParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxRestartResponse,
        )

    def uncancel(
        self,
        mailbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxUncancelResponse:
        """Withdraws a scheduled cancellation.

        Only available while cancellation is
        pending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return self._post(
            path_template("/mailboxes/{mailbox_id}/uncancel", mailbox_id=mailbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxUncancelResponse,
        )


class AsyncMailboxesResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMailboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMailboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMailboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncMailboxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        client_request_id: str,
        billing_preference: Literal["included", "included_only", "rent"] | Omit = omit,
        domain_id: str | Omit = omit,
        label: str | Omit = omit,
        local_part: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxCreateResponse:
        """Creates a mailbox on the default domain or a connected custom domain.

        An
        optional `localPart` selects the address. Replaying the same `clientRequestId`
        and payload returns the original mailbox. Poll the mailbox when a 202 response
        does not yet include a checkout URL.

        Args:
          billing_preference: included uses package capacity when available and otherwise starts paid
              checkout; included_only fails without creating a paid reservation when no
              included slot remains; rent always starts paid checkout.

          domain_id: Optional active custom mailbox domain owned by the caller. Omit to use the
              system domain.

          local_part: Optional mailbox name before the "@". Omit to generate a random address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mailboxes",
            body=await async_maybe_transform(
                {
                    "client_request_id": client_request_id,
                    "billing_preference": billing_preference,
                    "domain_id": domain_id,
                    "label": label,
                    "local_part": local_part,
                },
                mailbox_create_params.MailboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxCreateResponse,
        )

    async def retrieve(
        self,
        mailbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxRetrieveResponse:
        """
        Get a mailbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return await self._get(
            path_template("/mailboxes/{mailbox_id}", mailbox_id=mailbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxRetrieveResponse,
        )

    async def update(
        self,
        mailbox_id: str,
        *,
        label: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxUpdateResponse:
        """
        Updates the label of a mailbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return await self._patch(
            path_template("/mailboxes/{mailbox_id}", mailbox_id=mailbox_id),
            body=await async_maybe_transform({"label": label}, mailbox_update_params.MailboxUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxListResponse:
        """
        Lists the caller-owned mailboxes with page-based pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/mailboxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    mailbox_list_params.MailboxListParams,
                ),
            ),
            cast_to=MailboxListResponse,
        )

    async def delete(
        self,
        mailbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxDeleteResponse:
        """
        Cancels a pending mailbox or schedules an active paid mailbox for cancellation.
        Existing addresses and messages are retained. Repeating the request is safe.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return await self._delete(
            path_template("/mailboxes/{mailbox_id}", mailbox_id=mailbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxDeleteResponse,
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
    ) -> MailboxCapacityResponse:
        """Returns the number of mailboxes currently available through included capacity."""
        return await self._get(
            "/mailboxes/capacity",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxCapacityResponse,
        )

    async def otp(
        self,
        mailbox_id: str,
        *,
        after: Union[str, datetime] | Omit = omit,
        max_length: int | Omit = omit,
        min_length: int | Omit = omit,
        sender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxOtpResponse:
        """Returns the most likely recent OTP for the mailbox.

        Returns 204 when no matching
        code is available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return await self._get(
            path_template("/mailboxes/{mailbox_id}/otp", mailbox_id=mailbox_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "max_length": max_length,
                        "min_length": min_length,
                        "sender": sender,
                    },
                    mailbox_otp_params.MailboxOtpParams,
                ),
            ),
            cast_to=MailboxOtpResponse,
        )

    async def restart(
        self,
        mailbox_id: str,
        *,
        billing_preference: Literal["included", "included_only", "rent"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxRestartResponse:
        """Restarts an archived mailbox with the same address.

        Uses included capacity when
        available unless paid service is requested.

        Args:
          billing_preference: included uses package capacity when available and otherwise starts paid
              checkout; included_only fails without creating a paid reservation when no
              included slot remains; rent always starts paid checkout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return await self._post(
            path_template("/mailboxes/{mailbox_id}/restart", mailbox_id=mailbox_id),
            body=await async_maybe_transform(
                {"billing_preference": billing_preference}, mailbox_restart_params.MailboxRestartParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxRestartResponse,
        )

    async def uncancel(
        self,
        mailbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailboxUncancelResponse:
        """Withdraws a scheduled cancellation.

        Only available while cancellation is
        pending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mailbox_id:
            raise ValueError(f"Expected a non-empty value for `mailbox_id` but received {mailbox_id!r}")
        return await self._post(
            path_template("/mailboxes/{mailbox_id}/uncancel", mailbox_id=mailbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailboxUncancelResponse,
        )


class MailboxesResourceWithRawResponse:
    def __init__(self, mailboxes: MailboxesResource) -> None:
        self._mailboxes = mailboxes

        self.create = to_raw_response_wrapper(
            mailboxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mailboxes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mailboxes.update,
        )
        self.list = to_raw_response_wrapper(
            mailboxes.list,
        )
        self.delete = to_raw_response_wrapper(
            mailboxes.delete,
        )
        self.capacity = to_raw_response_wrapper(
            mailboxes.capacity,
        )
        self.otp = to_raw_response_wrapper(
            mailboxes.otp,
        )
        self.restart = to_raw_response_wrapper(
            mailboxes.restart,
        )
        self.uncancel = to_raw_response_wrapper(
            mailboxes.uncancel,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._mailboxes.messages)


class AsyncMailboxesResourceWithRawResponse:
    def __init__(self, mailboxes: AsyncMailboxesResource) -> None:
        self._mailboxes = mailboxes

        self.create = async_to_raw_response_wrapper(
            mailboxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mailboxes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mailboxes.update,
        )
        self.list = async_to_raw_response_wrapper(
            mailboxes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mailboxes.delete,
        )
        self.capacity = async_to_raw_response_wrapper(
            mailboxes.capacity,
        )
        self.otp = async_to_raw_response_wrapper(
            mailboxes.otp,
        )
        self.restart = async_to_raw_response_wrapper(
            mailboxes.restart,
        )
        self.uncancel = async_to_raw_response_wrapper(
            mailboxes.uncancel,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._mailboxes.messages)


class MailboxesResourceWithStreamingResponse:
    def __init__(self, mailboxes: MailboxesResource) -> None:
        self._mailboxes = mailboxes

        self.create = to_streamed_response_wrapper(
            mailboxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mailboxes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mailboxes.update,
        )
        self.list = to_streamed_response_wrapper(
            mailboxes.list,
        )
        self.delete = to_streamed_response_wrapper(
            mailboxes.delete,
        )
        self.capacity = to_streamed_response_wrapper(
            mailboxes.capacity,
        )
        self.otp = to_streamed_response_wrapper(
            mailboxes.otp,
        )
        self.restart = to_streamed_response_wrapper(
            mailboxes.restart,
        )
        self.uncancel = to_streamed_response_wrapper(
            mailboxes.uncancel,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._mailboxes.messages)


class AsyncMailboxesResourceWithStreamingResponse:
    def __init__(self, mailboxes: AsyncMailboxesResource) -> None:
        self._mailboxes = mailboxes

        self.create = async_to_streamed_response_wrapper(
            mailboxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mailboxes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mailboxes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mailboxes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mailboxes.delete,
        )
        self.capacity = async_to_streamed_response_wrapper(
            mailboxes.capacity,
        )
        self.otp = async_to_streamed_response_wrapper(
            mailboxes.otp,
        )
        self.restart = async_to_streamed_response_wrapper(
            mailboxes.restart,
        )
        self.uncancel = async_to_streamed_response_wrapper(
            mailboxes.uncancel,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._mailboxes.messages)
