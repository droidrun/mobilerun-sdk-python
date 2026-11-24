# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .validations import (
    ValidationsResource,
    AsyncValidationsResource,
    ValidationsResourceWithRawResponse,
    AsyncValidationsResourceWithRawResponse,
    ValidationsResourceWithStreamingResponse,
    AsyncValidationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.compute import (
    function_list_params,
    function_create_params,
    function_source_params,
    function_update_params,
)
from ....types.compute.function_list_response import FunctionListResponse
from ....types.compute.function_create_response import FunctionCreateResponse
from ....types.compute.function_source_response import FunctionSourceResponse
from ....types.compute.function_update_response import FunctionUpdateResponse
from ....types.compute.function_retrieve_response import FunctionRetrieveResponse

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    @cached_property
    def validations(self) -> ValidationsResource:
        return ValidationsResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return FunctionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        source: str,
        api_key: function_create_params.APIKey | Omit = omit,
        description: str | Omit = omit,
        manifest: function_create_params.Manifest | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FunctionCreateResponse:
        """
        Create a function with its first immutable version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/compute/functions",
            body=maybe_transform(
                {
                    "name": name,
                    "source": source,
                    "api_key": api_key,
                    "description": description,
                    "manifest": manifest,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FunctionCreateResponse,
        )

    def retrieve(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionRetrieveResponse:
        """
        Get function metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            path_template("/compute/functions/{function_id}", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionRetrieveResponse,
        )

    def update(
        self,
        function_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FunctionUpdateResponse:
        """
        Rename a function or update its description

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._patch(
            path_template("/compute/functions/{function_id}", function_id=function_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FunctionUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionListResponse:
        """
        List functions owned by this organisation

        Args:
          search: Case-insensitive substring match against the function name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/compute/functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                    },
                    function_list_params.FunctionListParams,
                ),
            ),
            cast_to=FunctionListResponse,
        )

    def delete(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete a function

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/compute/functions/{function_id}", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def source(
        self,
        function_id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionSourceResponse:
        """
        Read verified function source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            path_template("/compute/functions/{function_id}/source", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, function_source_params.FunctionSourceParams),
            ),
            cast_to=FunctionSourceResponse,
        )


class AsyncFunctionsResource(AsyncAPIResource):
    @cached_property
    def validations(self) -> AsyncValidationsResource:
        return AsyncValidationsResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/droidrun/mobilerun-sdk-python#with_streaming_response
        """
        return AsyncFunctionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        source: str,
        api_key: function_create_params.APIKey | Omit = omit,
        description: str | Omit = omit,
        manifest: function_create_params.Manifest | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FunctionCreateResponse:
        """
        Create a function with its first immutable version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/compute/functions",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "source": source,
                    "api_key": api_key,
                    "description": description,
                    "manifest": manifest,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FunctionCreateResponse,
        )

    async def retrieve(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionRetrieveResponse:
        """
        Get function metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            path_template("/compute/functions/{function_id}", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionRetrieveResponse,
        )

    async def update(
        self,
        function_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FunctionUpdateResponse:
        """
        Rename a function or update its description

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._patch(
            path_template("/compute/functions/{function_id}", function_id=function_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FunctionUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionListResponse:
        """
        List functions owned by this organisation

        Args:
          search: Case-insensitive substring match against the function name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/compute/functions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                    },
                    function_list_params.FunctionListParams,
                ),
            ),
            cast_to=FunctionListResponse,
        )

    async def delete(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete a function

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/compute/functions/{function_id}", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def source(
        self,
        function_id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionSourceResponse:
        """
        Read verified function source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            path_template("/compute/functions/{function_id}/source", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"version": version}, function_source_params.FunctionSourceParams),
            ),
            cast_to=FunctionSourceResponse,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            functions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            functions.update,
        )
        self.list = to_raw_response_wrapper(
            functions.list,
        )
        self.delete = to_raw_response_wrapper(
            functions.delete,
        )
        self.source = to_raw_response_wrapper(
            functions.source,
        )

    @cached_property
    def validations(self) -> ValidationsResourceWithRawResponse:
        return ValidationsResourceWithRawResponse(self._functions.validations)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._functions.versions)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._functions.runs)


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            functions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            functions.update,
        )
        self.list = async_to_raw_response_wrapper(
            functions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            functions.delete,
        )
        self.source = async_to_raw_response_wrapper(
            functions.source,
        )

    @cached_property
    def validations(self) -> AsyncValidationsResourceWithRawResponse:
        return AsyncValidationsResourceWithRawResponse(self._functions.validations)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._functions.versions)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._functions.runs)


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            functions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            functions.update,
        )
        self.list = to_streamed_response_wrapper(
            functions.list,
        )
        self.delete = to_streamed_response_wrapper(
            functions.delete,
        )
        self.source = to_streamed_response_wrapper(
            functions.source,
        )

    @cached_property
    def validations(self) -> ValidationsResourceWithStreamingResponse:
        return ValidationsResourceWithStreamingResponse(self._functions.validations)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._functions.versions)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._functions.runs)


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            functions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            functions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            functions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            functions.delete,
        )
        self.source = async_to_streamed_response_wrapper(
            functions.source,
        )

    @cached_property
    def validations(self) -> AsyncValidationsResourceWithStreamingResponse:
        return AsyncValidationsResourceWithStreamingResponse(self._functions.validations)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._functions.versions)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._functions.runs)
