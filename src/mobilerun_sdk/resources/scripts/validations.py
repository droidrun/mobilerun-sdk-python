# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.scripts import validation_create_params, validation_retrieve_params
from ...types.scripts.validation_create_response import ValidationCreateResponse
from ...types.scripts.validation_retrieve_response import ValidationRetrieveResponse

__all__ = ["ValidationsResource", "AsyncValidationsResource"]


class ValidationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return ValidationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        source: str,
        wait_s: Optional[int] | Omit = omit,
        manifest: validation_create_params.Manifest | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ValidationCreateResponse:
        """
        Validate Python script source without uploading it

        Args:
          wait_s: Wait up to 25 seconds for validation to finish. Excess waiters return
              immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/sandbox/scripts/validations",
            body=maybe_transform(
                {
                    "source": source,
                    "manifest": manifest,
                },
                validation_create_params.ValidationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform({"wait_s": wait_s}, validation_create_params.ValidationCreateParams),
            ),
            cast_to=ValidationCreateResponse,
        )

    def retrieve(
        self,
        validation_id: str,
        *,
        wait_s: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidationRetrieveResponse:
        """
        Retrieve a script validation owned by this organisation

        Args:
          wait_s: Wait up to 25 seconds for validation to finish. Excess waiters return
              immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not validation_id:
            raise ValueError(f"Expected a non-empty value for `validation_id` but received {validation_id!r}")
        return self._get(
            path_template("/sandbox/scripts/validations/{validation_id}", validation_id=validation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"wait_s": wait_s}, validation_retrieve_params.ValidationRetrieveParams),
            ),
            cast_to=ValidationRetrieveResponse,
        )


class AsyncValidationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncValidationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        source: str,
        wait_s: Optional[int] | Omit = omit,
        manifest: validation_create_params.Manifest | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ValidationCreateResponse:
        """
        Validate Python script source without uploading it

        Args:
          wait_s: Wait up to 25 seconds for validation to finish. Excess waiters return
              immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/sandbox/scripts/validations",
            body=await async_maybe_transform(
                {
                    "source": source,
                    "manifest": manifest,
                },
                validation_create_params.ValidationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=await async_maybe_transform({"wait_s": wait_s}, validation_create_params.ValidationCreateParams),
            ),
            cast_to=ValidationCreateResponse,
        )

    async def retrieve(
        self,
        validation_id: str,
        *,
        wait_s: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidationRetrieveResponse:
        """
        Retrieve a script validation owned by this organisation

        Args:
          wait_s: Wait up to 25 seconds for validation to finish. Excess waiters return
              immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not validation_id:
            raise ValueError(f"Expected a non-empty value for `validation_id` but received {validation_id!r}")
        return await self._get(
            path_template("/sandbox/scripts/validations/{validation_id}", validation_id=validation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"wait_s": wait_s}, validation_retrieve_params.ValidationRetrieveParams
                ),
            ),
            cast_to=ValidationRetrieveResponse,
        )


class ValidationsResourceWithRawResponse:
    def __init__(self, validations: ValidationsResource) -> None:
        self._validations = validations

        self.create = to_raw_response_wrapper(
            validations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            validations.retrieve,
        )


class AsyncValidationsResourceWithRawResponse:
    def __init__(self, validations: AsyncValidationsResource) -> None:
        self._validations = validations

        self.create = async_to_raw_response_wrapper(
            validations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            validations.retrieve,
        )


class ValidationsResourceWithStreamingResponse:
    def __init__(self, validations: ValidationsResource) -> None:
        self._validations = validations

        self.create = to_streamed_response_wrapper(
            validations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            validations.retrieve,
        )


class AsyncValidationsResourceWithStreamingResponse:
    def __init__(self, validations: AsyncValidationsResource) -> None:
        self._validations = validations

        self.create = async_to_streamed_response_wrapper(
            validations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            validations.retrieve,
        )
