# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_add_params, client_profile_params
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    SequenceNotStr,
    omit,
    not_given,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import search, memories, settings, documents, connections
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, SupermemoryError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.add_response import AddResponse
from .types.profile_response import ProfileResponse

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Supermemory",
    "AsyncSupermemory",
    "Client",
    "AsyncClient",
]


class Supermemory(SyncAPIClient):
    memories: memories.MemoriesResource
    documents: documents.DocumentsResource
    search: search.SearchResource
    settings: settings.SettingsResource
    connections: connections.ConnectionsResource
    with_raw_response: SupermemoryWithRawResponse
    with_streaming_response: SupermemoryWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Supermemory client instance.

        This automatically infers the `api_key` argument from the `SUPERMEMORY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SUPERMEMORY_API_KEY")
        if api_key is None:
            raise SupermemoryError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SUPERMEMORY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("SUPERMEMORY_BASE_URL")
        if base_url is None:
            base_url = f"https://api.supermemory.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.memories = memories.MemoriesResource(self)
        self.documents = documents.DocumentsResource(self)
        self.search = search.SearchResource(self)
        self.settings = settings.SettingsResource(self)
        self.connections = connections.ConnectionsResource(self)
        self.with_raw_response = SupermemoryWithRawResponse(self)
        self.with_streaming_response = SupermemoryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def add(
        self,
        *,
        content: str,
        container_tag: str | Omit = omit,
        container_tags: SequenceNotStr[str] | Omit = omit,
        custom_id: str | Omit = omit,
        metadata: Dict[str, Union[str, float, bool, SequenceNotStr[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddResponse:
        """
        Add a document with any content type (text, url, file, etc.) and metadata

        Args:
          content: The content to extract and process into a document. This can be a URL to a
              website, a PDF, an image, or a video.

          container_tag: Optional tag this document should be containerized by. Max 100 characters,
              alphanumeric with hyphens and underscores only.

          custom_id: Optional custom ID of the document. Max 100 characters, alphanumeric with
              hyphens and underscores only.

          metadata: Optional metadata for the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v3/documents",
            body=maybe_transform(
                {
                    "content": content,
                    "container_tag": container_tag,
                    "container_tags": container_tags,
                    "custom_id": custom_id,
                    "metadata": metadata,
                },
                client_add_params.ClientAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddResponse,
        )

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
        return self.post(
            "/v4/profile",
            body=maybe_transform(
                {
                    "container_tag": container_tag,
                    "q": q,
                },
                client_profile_params.ClientProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSupermemory(AsyncAPIClient):
    memories: memories.AsyncMemoriesResource
    documents: documents.AsyncDocumentsResource
    search: search.AsyncSearchResource
    settings: settings.AsyncSettingsResource
    connections: connections.AsyncConnectionsResource
    with_raw_response: AsyncSupermemoryWithRawResponse
    with_streaming_response: AsyncSupermemoryWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncSupermemory client instance.

        This automatically infers the `api_key` argument from the `SUPERMEMORY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SUPERMEMORY_API_KEY")
        if api_key is None:
            raise SupermemoryError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SUPERMEMORY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("SUPERMEMORY_BASE_URL")
        if base_url is None:
            base_url = f"https://api.supermemory.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.memories = memories.AsyncMemoriesResource(self)
        self.documents = documents.AsyncDocumentsResource(self)
        self.search = search.AsyncSearchResource(self)
        self.settings = settings.AsyncSettingsResource(self)
        self.connections = connections.AsyncConnectionsResource(self)
        self.with_raw_response = AsyncSupermemoryWithRawResponse(self)
        self.with_streaming_response = AsyncSupermemoryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def add(
        self,
        *,
        content: str,
        container_tag: str | Omit = omit,
        container_tags: SequenceNotStr[str] | Omit = omit,
        custom_id: str | Omit = omit,
        metadata: Dict[str, Union[str, float, bool, SequenceNotStr[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddResponse:
        """
        Add a document with any content type (text, url, file, etc.) and metadata

        Args:
          content: The content to extract and process into a document. This can be a URL to a
              website, a PDF, an image, or a video.

          container_tag: Optional tag this document should be containerized by. Max 100 characters,
              alphanumeric with hyphens and underscores only.

          custom_id: Optional custom ID of the document. Max 100 characters, alphanumeric with
              hyphens and underscores only.

          metadata: Optional metadata for the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v3/documents",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "container_tag": container_tag,
                    "container_tags": container_tags,
                    "custom_id": custom_id,
                    "metadata": metadata,
                },
                client_add_params.ClientAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddResponse,
        )

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
        return await self.post(
            "/v4/profile",
            body=await async_maybe_transform(
                {
                    "container_tag": container_tag,
                    "q": q,
                },
                client_profile_params.ClientProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SupermemoryWithRawResponse:
    def __init__(self, client: Supermemory) -> None:
        self.memories = memories.MemoriesResourceWithRawResponse(client.memories)
        self.documents = documents.DocumentsResourceWithRawResponse(client.documents)
        self.search = search.SearchResourceWithRawResponse(client.search)
        self.settings = settings.SettingsResourceWithRawResponse(client.settings)
        self.connections = connections.ConnectionsResourceWithRawResponse(client.connections)

        self.add = to_raw_response_wrapper(
            client.add,
        )
        self.profile = to_raw_response_wrapper(
            client.profile,
        )


class AsyncSupermemoryWithRawResponse:
    def __init__(self, client: AsyncSupermemory) -> None:
        self.memories = memories.AsyncMemoriesResourceWithRawResponse(client.memories)
        self.documents = documents.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.search = search.AsyncSearchResourceWithRawResponse(client.search)
        self.settings = settings.AsyncSettingsResourceWithRawResponse(client.settings)
        self.connections = connections.AsyncConnectionsResourceWithRawResponse(client.connections)

        self.add = async_to_raw_response_wrapper(
            client.add,
        )
        self.profile = async_to_raw_response_wrapper(
            client.profile,
        )


class SupermemoryWithStreamedResponse:
    def __init__(self, client: Supermemory) -> None:
        self.memories = memories.MemoriesResourceWithStreamingResponse(client.memories)
        self.documents = documents.DocumentsResourceWithStreamingResponse(client.documents)
        self.search = search.SearchResourceWithStreamingResponse(client.search)
        self.settings = settings.SettingsResourceWithStreamingResponse(client.settings)
        self.connections = connections.ConnectionsResourceWithStreamingResponse(client.connections)

        self.add = to_streamed_response_wrapper(
            client.add,
        )
        self.profile = to_streamed_response_wrapper(
            client.profile,
        )


class AsyncSupermemoryWithStreamedResponse:
    def __init__(self, client: AsyncSupermemory) -> None:
        self.memories = memories.AsyncMemoriesResourceWithStreamingResponse(client.memories)
        self.documents = documents.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.search = search.AsyncSearchResourceWithStreamingResponse(client.search)
        self.settings = settings.AsyncSettingsResourceWithStreamingResponse(client.settings)
        self.connections = connections.AsyncConnectionsResourceWithStreamingResponse(client.connections)

        self.add = async_to_streamed_response_wrapper(
            client.add,
        )
        self.profile = async_to_streamed_response_wrapper(
            client.profile,
        )


Client = Supermemory

AsyncClient = AsyncSupermemory
