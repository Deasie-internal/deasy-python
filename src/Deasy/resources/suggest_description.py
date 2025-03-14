# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import suggest_description_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.suggest_description_create_response import SuggestDescriptionCreateResponse

__all__ = ["SuggestDescriptionResource", "AsyncSuggestDescriptionResource"]


class SuggestDescriptionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SuggestDescriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return SuggestDescriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuggestDescriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return SuggestDescriptionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        endpoint_manager_config: object,
        tag_name: str,
        available_values: Optional[List[str]] | NotGiven = NOT_GIVEN,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        current_description: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuggestDescriptionCreateResponse:
        """
        Suggest a description for a tag based on context and vector DB content

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/suggest_description",
            body=maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "tag_name": tag_name,
                    "available_values": available_values,
                    "context": context,
                    "current_description": current_description,
                    "vector_db_config": vector_db_config,
                },
                suggest_description_create_params.SuggestDescriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuggestDescriptionCreateResponse,
        )


class AsyncSuggestDescriptionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSuggestDescriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSuggestDescriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuggestDescriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Deasie-internal/deasy-sdk#with_streaming_response
        """
        return AsyncSuggestDescriptionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        endpoint_manager_config: object,
        tag_name: str,
        available_values: Optional[List[str]] | NotGiven = NOT_GIVEN,
        context: Optional[str] | NotGiven = NOT_GIVEN,
        current_description: Optional[str] | NotGiven = NOT_GIVEN,
        vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SuggestDescriptionCreateResponse:
        """
        Suggest a description for a tag based on context and vector DB content

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/suggest_description",
            body=await async_maybe_transform(
                {
                    "endpoint_manager_config": endpoint_manager_config,
                    "tag_name": tag_name,
                    "available_values": available_values,
                    "context": context,
                    "current_description": current_description,
                    "vector_db_config": vector_db_config,
                },
                suggest_description_create_params.SuggestDescriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuggestDescriptionCreateResponse,
        )


class SuggestDescriptionResourceWithRawResponse:
    def __init__(self, suggest_description: SuggestDescriptionResource) -> None:
        self._suggest_description = suggest_description

        self.create = to_raw_response_wrapper(
            suggest_description.create,
        )


class AsyncSuggestDescriptionResourceWithRawResponse:
    def __init__(self, suggest_description: AsyncSuggestDescriptionResource) -> None:
        self._suggest_description = suggest_description

        self.create = async_to_raw_response_wrapper(
            suggest_description.create,
        )


class SuggestDescriptionResourceWithStreamingResponse:
    def __init__(self, suggest_description: SuggestDescriptionResource) -> None:
        self._suggest_description = suggest_description

        self.create = to_streamed_response_wrapper(
            suggest_description.create,
        )


class AsyncSuggestDescriptionResourceWithStreamingResponse:
    def __init__(self, suggest_description: AsyncSuggestDescriptionResource) -> None:
        self._suggest_description = suggest_description

        self.create = async_to_streamed_response_wrapper(
            suggest_description.create,
        )
