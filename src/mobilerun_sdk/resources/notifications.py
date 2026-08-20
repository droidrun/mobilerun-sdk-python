# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import notification_update_preferences_params
from .._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.notification_catalog_response import NotificationCatalogResponse
from ..types.notification_get_preferences_response import NotificationGetPreferencesResponse
from ..types.notification_update_preferences_response import NotificationUpdatePreferencesResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def catalog(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCatalogResponse:
        """Returns the catalog of notifiable event types grouped by source category.

        Each
        event lists its type identifier, label, and description, which can be referenced
        when muting event types in notification preferences.
        """
        return self._get(
            "/notifications/catalog",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationCatalogResponse,
        )

    def get_preferences(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationGetPreferencesResponse:
        """
        Returns your current notification preferences, expressed as the list of event
        types you have muted. An empty list means notifications are enabled for all
        notifiable event types.
        """
        return self._get(
            "/notifications/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationGetPreferencesResponse,
        )

    def update_preferences(
        self,
        *,
        muted_types: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationUpdatePreferencesResponse:
        """Replaces your set of muted event types with the supplied list.

        Any unknown or
        non-notifiable types are dropped, and the response returns the muted types that
        were actually stored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/notifications/preferences",
            body=maybe_transform(
                {"muted_types": muted_types}, notification_update_preferences_params.NotificationUpdatePreferencesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationUpdatePreferencesResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def catalog(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCatalogResponse:
        """Returns the catalog of notifiable event types grouped by source category.

        Each
        event lists its type identifier, label, and description, which can be referenced
        when muting event types in notification preferences.
        """
        return await self._get(
            "/notifications/catalog",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationCatalogResponse,
        )

    async def get_preferences(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationGetPreferencesResponse:
        """
        Returns your current notification preferences, expressed as the list of event
        types you have muted. An empty list means notifications are enabled for all
        notifiable event types.
        """
        return await self._get(
            "/notifications/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationGetPreferencesResponse,
        )

    async def update_preferences(
        self,
        *,
        muted_types: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationUpdatePreferencesResponse:
        """Replaces your set of muted event types with the supplied list.

        Any unknown or
        non-notifiable types are dropped, and the response returns the muted types that
        were actually stored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/notifications/preferences",
            body=await async_maybe_transform(
                {"muted_types": muted_types}, notification_update_preferences_params.NotificationUpdatePreferencesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationUpdatePreferencesResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.catalog = to_raw_response_wrapper(
            notifications.catalog,
        )
        self.get_preferences = to_raw_response_wrapper(
            notifications.get_preferences,
        )
        self.update_preferences = to_raw_response_wrapper(
            notifications.update_preferences,
        )


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.catalog = async_to_raw_response_wrapper(
            notifications.catalog,
        )
        self.get_preferences = async_to_raw_response_wrapper(
            notifications.get_preferences,
        )
        self.update_preferences = async_to_raw_response_wrapper(
            notifications.update_preferences,
        )


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.catalog = to_streamed_response_wrapper(
            notifications.catalog,
        )
        self.get_preferences = to_streamed_response_wrapper(
            notifications.get_preferences,
        )
        self.update_preferences = to_streamed_response_wrapper(
            notifications.update_preferences,
        )


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.catalog = async_to_streamed_response_wrapper(
            notifications.catalog,
        )
        self.get_preferences = async_to_streamed_response_wrapper(
            notifications.get_preferences,
        )
        self.update_preferences = async_to_streamed_response_wrapper(
            notifications.update_preferences,
        )
