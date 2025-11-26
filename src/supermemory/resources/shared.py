# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.shared import shared_profile_params
from ..types.shared.profile_response import ProfileResponse

__all__ = ["SharedResource", "AsyncSharedResource"]


class SharedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SharedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/supermemoryai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return SharedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SharedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/supermemoryai/python-sdk#with_streaming_response
        """
        return SharedResourceWithStreamingResponse(self)

    def profile(
        self,
        *,
        container_tag: str,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileResponse:
        """
        Get user profile with optional search results

        Args:
          container_tag: Tag to filter the profile by. This can be an ID for your user, a project ID, or
              any other identifier you wish to use to filter memories.

          q: Optional search query to include search results in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v4/profile",
            body=maybe_transform(
                {
                    "container_tag": container_tag,
                    "q": q,
                },
                shared_profile_params.SharedProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileResponse,
        )


class AsyncSharedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSharedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/supermemoryai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSharedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSharedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/supermemoryai/python-sdk#with_streaming_response
        """
        return AsyncSharedResourceWithStreamingResponse(self)

    async def profile(
        self,
        *,
        container_tag: str,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileResponse:
        """
        Get user profile with optional search results

        Args:
          container_tag: Tag to filter the profile by. This can be an ID for your user, a project ID, or
              any other identifier you wish to use to filter memories.

          q: Optional search query to include search results in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v4/profile",
            body=await async_maybe_transform(
                {
                    "container_tag": container_tag,
                    "q": q,
                },
                shared_profile_params.SharedProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileResponse,
        )


class SharedResourceWithRawResponse:
    def __init__(self, shared: SharedResource) -> None:
        self._shared = shared

        self.profile = to_raw_response_wrapper(
            shared.profile,
        )


class AsyncSharedResourceWithRawResponse:
    def __init__(self, shared: AsyncSharedResource) -> None:
        self._shared = shared

        self.profile = async_to_raw_response_wrapper(
            shared.profile,
        )


class SharedResourceWithStreamingResponse:
    def __init__(self, shared: SharedResource) -> None:
        self._shared = shared

        self.profile = to_streamed_response_wrapper(
            shared.profile,
        )


class AsyncSharedResourceWithStreamingResponse:
    def __init__(self, shared: AsyncSharedResource) -> None:
        self._shared = shared

        self.profile = async_to_streamed_response_wrapper(
            shared.profile,
        )
