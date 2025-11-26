# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import profile_property_params
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
from ..types.profile_property_response import ProfilePropertyResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/supermemoryai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/supermemoryai/python-sdk#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def property(
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
    ) -> ProfilePropertyResponse:
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
                profile_property_params.ProfilePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePropertyResponse,
        )


class AsyncProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/supermemoryai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/supermemoryai/python-sdk#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def property(
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
    ) -> ProfilePropertyResponse:
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
                profile_property_params.ProfilePropertyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePropertyResponse,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.property = to_raw_response_wrapper(
            profile.property,
        )


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.property = async_to_raw_response_wrapper(
            profile.property,
        )


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.property = to_streamed_response_wrapper(
            profile.property,
        )


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.property = async_to_streamed_response_wrapper(
            profile.property,
        )
