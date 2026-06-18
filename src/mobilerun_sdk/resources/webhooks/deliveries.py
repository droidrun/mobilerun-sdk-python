# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.webhooks import delivery_list_params, delivery_stats_params, delivery_list_for_webhook_params
from ...types.webhooks.delivery_list_response import DeliveryListResponse
from ...types.webhooks.delivery_stats_response import DeliveryStatsResponse
from ...types.webhooks.delivery_list_for_webhook_response import DeliveryListForWebhookResponse
from ...types.webhooks.delivery_retrieve_attempts_response import DeliveryRetrieveAttemptsResponse

__all__ = ["DeliveriesResource", "AsyncDeliveriesResource"]


class DeliveriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return DeliveriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        status: Literal["pending", "success", "skipped", "dead"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        """
        List deliveries across all your webhooks

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/webhooks/deliveries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "since": since,
                        "status": status,
                    },
                    delivery_list_params.DeliveryListParams,
                ),
            ),
            cast_to=DeliveryListResponse,
        )

    def list_for_webhook(
        self,
        id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListForWebhookResponse:
        """
        List deliveries for a webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/webhooks/{id}/deliveries", id=id),
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
                    delivery_list_for_webhook_params.DeliveryListForWebhookParams,
                ),
            ),
            cast_to=DeliveryListForWebhookResponse,
        )

    def retrieve_attempts(
        self,
        delivery_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRetrieveAttemptsResponse:
        """
        Get a delivery with its attempts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._get(
            path_template("/webhooks/{id}/deliveries/{delivery_id}", id=id, delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryRetrieveAttemptsResponse,
        )

    def stats(
        self,
        *,
        since: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryStatsResponse:
        """
        Aggregate delivery statistics (excludes test sends)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/webhooks/deliveries/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"since": since}, delivery_stats_params.DeliveryStatsParams),
            ),
            cast_to=DeliveryStatsResponse,
        )


class AsyncDeliveriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncDeliveriesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        status: Literal["pending", "success", "skipped", "dead"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        """
        List deliveries across all your webhooks

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/webhooks/deliveries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "since": since,
                        "status": status,
                    },
                    delivery_list_params.DeliveryListParams,
                ),
            ),
            cast_to=DeliveryListResponse,
        )

    async def list_for_webhook(
        self,
        id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListForWebhookResponse:
        """
        List deliveries for a webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/webhooks/{id}/deliveries", id=id),
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
                    delivery_list_for_webhook_params.DeliveryListForWebhookParams,
                ),
            ),
            cast_to=DeliveryListForWebhookResponse,
        )

    async def retrieve_attempts(
        self,
        delivery_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRetrieveAttemptsResponse:
        """
        Get a delivery with its attempts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._get(
            path_template("/webhooks/{id}/deliveries/{delivery_id}", id=id, delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryRetrieveAttemptsResponse,
        )

    async def stats(
        self,
        *,
        since: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryStatsResponse:
        """
        Aggregate delivery statistics (excludes test sends)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/webhooks/deliveries/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"since": since}, delivery_stats_params.DeliveryStatsParams),
            ),
            cast_to=DeliveryStatsResponse,
        )


class DeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = to_raw_response_wrapper(
            deliveries.list,
        )
        self.list_for_webhook = to_raw_response_wrapper(
            deliveries.list_for_webhook,
        )
        self.retrieve_attempts = to_raw_response_wrapper(
            deliveries.retrieve_attempts,
        )
        self.stats = to_raw_response_wrapper(
            deliveries.stats,
        )


class AsyncDeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = async_to_raw_response_wrapper(
            deliveries.list,
        )
        self.list_for_webhook = async_to_raw_response_wrapper(
            deliveries.list_for_webhook,
        )
        self.retrieve_attempts = async_to_raw_response_wrapper(
            deliveries.retrieve_attempts,
        )
        self.stats = async_to_raw_response_wrapper(
            deliveries.stats,
        )


class DeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = to_streamed_response_wrapper(
            deliveries.list,
        )
        self.list_for_webhook = to_streamed_response_wrapper(
            deliveries.list_for_webhook,
        )
        self.retrieve_attempts = to_streamed_response_wrapper(
            deliveries.retrieve_attempts,
        )
        self.stats = to_streamed_response_wrapper(
            deliveries.stats,
        )


class AsyncDeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = async_to_streamed_response_wrapper(
            deliveries.list,
        )
        self.list_for_webhook = async_to_streamed_response_wrapper(
            deliveries.list_for_webhook,
        )
        self.retrieve_attempts = async_to_streamed_response_wrapper(
            deliveries.retrieve_attempts,
        )
        self.stats = async_to_streamed_response_wrapper(
            deliveries.stats,
        )
