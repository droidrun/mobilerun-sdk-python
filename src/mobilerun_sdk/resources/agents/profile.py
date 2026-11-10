# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ...types.agents import profile_update_params
from ...types.agents.profile_update_response import ProfileUpdateResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def update(
        self,
        agent_id: str,
        *,
        avatar_config: Optional[profile_update_params.AvatarConfig] | Omit = omit,
        avatar_kind: Optional[Literal["blob"]] | Omit = omit,
        color: Optional[
            Literal[
                "slate", "red", "orange", "amber", "lime", "green", "teal", "cyan", "blue", "indigo", "violet", "pink"
            ]
        ]
        | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        model_profile: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ProfileUpdateResponse:
        """
        Owner-scoped partial update of `displayName`, `instructions`, `modelProfile` and
        the avatar. A null modelProfile uses the environment default; an unknown id
        returns unknown_model_profile with details.validProfiles. Returns the updated
        Agent; an Agent of another owner or an unknown id is a 404.

        Args:
          color: Set the avatar palette color without changing its seed; null removes only the
              color. Omitted color stays unchanged, including during a seed update.

          display_name: Single-line name shown for the Agent; surrounding whitespace is trimmed and it
              needs at least one letter or number.

          instructions: The Agent's individual instructions passage; an empty or whitespace-only text
              clears it. Line breaks count three characters toward the rendered size limit.

          model_profile: Model profile id from GET /agents/model-profiles; null uses the environment
              default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            path_template("/agents/{agent_id}/profile", agent_id=agent_id),
            body=maybe_transform(
                {
                    "avatar_config": avatar_config,
                    "avatar_kind": avatar_kind,
                    "color": color,
                    "display_name": display_name,
                    "instructions": instructions,
                    "model_profile": model_profile,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ProfileUpdateResponse,
        )


class AsyncProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def update(
        self,
        agent_id: str,
        *,
        avatar_config: Optional[profile_update_params.AvatarConfig] | Omit = omit,
        avatar_kind: Optional[Literal["blob"]] | Omit = omit,
        color: Optional[
            Literal[
                "slate", "red", "orange", "amber", "lime", "green", "teal", "cyan", "blue", "indigo", "violet", "pink"
            ]
        ]
        | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        model_profile: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ProfileUpdateResponse:
        """
        Owner-scoped partial update of `displayName`, `instructions`, `modelProfile` and
        the avatar. A null modelProfile uses the environment default; an unknown id
        returns unknown_model_profile with details.validProfiles. Returns the updated
        Agent; an Agent of another owner or an unknown id is a 404.

        Args:
          color: Set the avatar palette color without changing its seed; null removes only the
              color. Omitted color stays unchanged, including during a seed update.

          display_name: Single-line name shown for the Agent; surrounding whitespace is trimmed and it
              needs at least one letter or number.

          instructions: The Agent's individual instructions passage; an empty or whitespace-only text
              clears it. Line breaks count three characters toward the rendered size limit.

          model_profile: Model profile id from GET /agents/model-profiles; null uses the environment
              default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            path_template("/agents/{agent_id}/profile", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "avatar_config": avatar_config,
                    "avatar_kind": avatar_kind,
                    "color": color,
                    "display_name": display_name,
                    "instructions": instructions,
                    "model_profile": model_profile,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ProfileUpdateResponse,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.update = to_raw_response_wrapper(
            profile.update,
        )


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.update = async_to_raw_response_wrapper(
            profile.update,
        )


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.update = to_streamed_response_wrapper(
            profile.update,
        )


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.update = async_to_streamed_response_wrapper(
            profile.update,
        )
