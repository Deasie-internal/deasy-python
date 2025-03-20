# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    tags,
    graph,
    classify,
    metadata,
    prepare_data,
    classify_bulk,
    llm_connector,
    vdb_connector,
    suggest_hierarchy,
    suggest_description,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import DeasyError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.dataslice import dataslice

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Deasy", "AsyncDeasy", "Client", "AsyncClient"]


class Deasy(SyncAPIClient):
    classify_bulk: classify_bulk.ClassifyBulkResource
    classify: classify.ClassifyResource
    prepare_data: prepare_data.PrepareDataResource
    suggest_hierarchy: suggest_hierarchy.SuggestHierarchyResource
    suggest_description: suggest_description.SuggestDescriptionResource
    tags: tags.TagsResource
    metadata: metadata.MetadataResource
    vdb_connector: vdb_connector.VdbConnectorResource
    llm_connector: llm_connector.LlmConnectorResource
    dataslice: dataslice.DatasliceResource
    graph: graph.GraphResource
    with_raw_response: DeasyWithRawResponse
    with_streaming_response: DeasyWithStreamedResponse

    # client options
    x_token: str
    x_user: str

    def __init__(
        self,
        *,
        x_token: str | None = None,
        x_user: str,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new synchronous Deasy client instance.

        This automatically infers the `x_token` argument from the `DEASY_API_KEY` environment variable if it is not provided.
        """
        if x_token is None:
            x_token = os.environ.get("DEASY_API_KEY")
        if x_token is None:
            raise DeasyError(
                "The x_token client option must be set either by passing x_token to the client or by setting the DEASY_API_KEY environment variable"
            )
        self.x_token = x_token

        self.x_user = x_user

        if base_url is None:
            base_url = os.environ.get("DEASY_BASE_URL")
        if base_url is None:
            base_url = f"https://prod-deasy-api-service-660949837227.us-east1.run.app/"

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

        self.classify_bulk = classify_bulk.ClassifyBulkResource(self)
        self.classify = classify.ClassifyResource(self)
        self.prepare_data = prepare_data.PrepareDataResource(self)
        self.suggest_hierarchy = suggest_hierarchy.SuggestHierarchyResource(self)
        self.suggest_description = suggest_description.SuggestDescriptionResource(self)
        self.tags = tags.TagsResource(self)
        self.metadata = metadata.MetadataResource(self)
        self.vdb_connector = vdb_connector.VdbConnectorResource(self)
        self.llm_connector = llm_connector.LlmConnectorResource(self)
        self.dataslice = dataslice.DatasliceResource(self)
        self.graph = graph.GraphResource(self)
        self.with_raw_response = DeasyWithRawResponse(self)
        self.with_streaming_response = DeasyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Token": self.x_token,
            "X-User": self.x_user,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_token: str | None = None,
        x_user: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
            x_token=x_token or self.x_token,
            x_user=x_user or self.x_user,
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


class AsyncDeasy(AsyncAPIClient):
    classify_bulk: classify_bulk.AsyncClassifyBulkResource
    classify: classify.AsyncClassifyResource
    prepare_data: prepare_data.AsyncPrepareDataResource
    suggest_hierarchy: suggest_hierarchy.AsyncSuggestHierarchyResource
    suggest_description: suggest_description.AsyncSuggestDescriptionResource
    tags: tags.AsyncTagsResource
    metadata: metadata.AsyncMetadataResource
    vdb_connector: vdb_connector.AsyncVdbConnectorResource
    llm_connector: llm_connector.AsyncLlmConnectorResource
    dataslice: dataslice.AsyncDatasliceResource
    graph: graph.AsyncGraphResource
    with_raw_response: AsyncDeasyWithRawResponse
    with_streaming_response: AsyncDeasyWithStreamedResponse

    # client options
    x_token: str
    x_user: str

    def __init__(
        self,
        *,
        x_token: str | None = None,
        x_user: str,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new async AsyncDeasy client instance.

        This automatically infers the `x_token` argument from the `DEASY_API_KEY` environment variable if it is not provided.
        """
        if x_token is None:
            x_token = os.environ.get("DEASY_API_KEY")
        if x_token is None:
            raise DeasyError(
                "The x_token client option must be set either by passing x_token to the client or by setting the DEASY_API_KEY environment variable"
            )
        self.x_token = x_token

        self.x_user = x_user

        if base_url is None:
            base_url = os.environ.get("DEASY_BASE_URL")
        if base_url is None:
            base_url = f"https://prod-deasy-api-service-660949837227.us-east1.run.app/"

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

        self.classify_bulk = classify_bulk.AsyncClassifyBulkResource(self)
        self.classify = classify.AsyncClassifyResource(self)
        self.prepare_data = prepare_data.AsyncPrepareDataResource(self)
        self.suggest_hierarchy = suggest_hierarchy.AsyncSuggestHierarchyResource(self)
        self.suggest_description = suggest_description.AsyncSuggestDescriptionResource(self)
        self.tags = tags.AsyncTagsResource(self)
        self.metadata = metadata.AsyncMetadataResource(self)
        self.vdb_connector = vdb_connector.AsyncVdbConnectorResource(self)
        self.llm_connector = llm_connector.AsyncLlmConnectorResource(self)
        self.dataslice = dataslice.AsyncDatasliceResource(self)
        self.graph = graph.AsyncGraphResource(self)
        self.with_raw_response = AsyncDeasyWithRawResponse(self)
        self.with_streaming_response = AsyncDeasyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Token": self.x_token,
            "X-User": self.x_user,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_token: str | None = None,
        x_user: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
            x_token=x_token or self.x_token,
            x_user=x_user or self.x_user,
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


class DeasyWithRawResponse:
    def __init__(self, client: Deasy) -> None:
        self.classify_bulk = classify_bulk.ClassifyBulkResourceWithRawResponse(client.classify_bulk)
        self.classify = classify.ClassifyResourceWithRawResponse(client.classify)
        self.prepare_data = prepare_data.PrepareDataResourceWithRawResponse(client.prepare_data)
        self.suggest_hierarchy = suggest_hierarchy.SuggestHierarchyResourceWithRawResponse(client.suggest_hierarchy)
        self.suggest_description = suggest_description.SuggestDescriptionResourceWithRawResponse(
            client.suggest_description
        )
        self.tags = tags.TagsResourceWithRawResponse(client.tags)
        self.metadata = metadata.MetadataResourceWithRawResponse(client.metadata)
        self.vdb_connector = vdb_connector.VdbConnectorResourceWithRawResponse(client.vdb_connector)
        self.llm_connector = llm_connector.LlmConnectorResourceWithRawResponse(client.llm_connector)
        self.dataslice = dataslice.DatasliceResourceWithRawResponse(client.dataslice)
        self.graph = graph.GraphResourceWithRawResponse(client.graph)


class AsyncDeasyWithRawResponse:
    def __init__(self, client: AsyncDeasy) -> None:
        self.classify_bulk = classify_bulk.AsyncClassifyBulkResourceWithRawResponse(client.classify_bulk)
        self.classify = classify.AsyncClassifyResourceWithRawResponse(client.classify)
        self.prepare_data = prepare_data.AsyncPrepareDataResourceWithRawResponse(client.prepare_data)
        self.suggest_hierarchy = suggest_hierarchy.AsyncSuggestHierarchyResourceWithRawResponse(
            client.suggest_hierarchy
        )
        self.suggest_description = suggest_description.AsyncSuggestDescriptionResourceWithRawResponse(
            client.suggest_description
        )
        self.tags = tags.AsyncTagsResourceWithRawResponse(client.tags)
        self.metadata = metadata.AsyncMetadataResourceWithRawResponse(client.metadata)
        self.vdb_connector = vdb_connector.AsyncVdbConnectorResourceWithRawResponse(client.vdb_connector)
        self.llm_connector = llm_connector.AsyncLlmConnectorResourceWithRawResponse(client.llm_connector)
        self.dataslice = dataslice.AsyncDatasliceResourceWithRawResponse(client.dataslice)
        self.graph = graph.AsyncGraphResourceWithRawResponse(client.graph)


class DeasyWithStreamedResponse:
    def __init__(self, client: Deasy) -> None:
        self.classify_bulk = classify_bulk.ClassifyBulkResourceWithStreamingResponse(client.classify_bulk)
        self.classify = classify.ClassifyResourceWithStreamingResponse(client.classify)
        self.prepare_data = prepare_data.PrepareDataResourceWithStreamingResponse(client.prepare_data)
        self.suggest_hierarchy = suggest_hierarchy.SuggestHierarchyResourceWithStreamingResponse(
            client.suggest_hierarchy
        )
        self.suggest_description = suggest_description.SuggestDescriptionResourceWithStreamingResponse(
            client.suggest_description
        )
        self.tags = tags.TagsResourceWithStreamingResponse(client.tags)
        self.metadata = metadata.MetadataResourceWithStreamingResponse(client.metadata)
        self.vdb_connector = vdb_connector.VdbConnectorResourceWithStreamingResponse(client.vdb_connector)
        self.llm_connector = llm_connector.LlmConnectorResourceWithStreamingResponse(client.llm_connector)
        self.dataslice = dataslice.DatasliceResourceWithStreamingResponse(client.dataslice)
        self.graph = graph.GraphResourceWithStreamingResponse(client.graph)


class AsyncDeasyWithStreamedResponse:
    def __init__(self, client: AsyncDeasy) -> None:
        self.classify_bulk = classify_bulk.AsyncClassifyBulkResourceWithStreamingResponse(client.classify_bulk)
        self.classify = classify.AsyncClassifyResourceWithStreamingResponse(client.classify)
        self.prepare_data = prepare_data.AsyncPrepareDataResourceWithStreamingResponse(client.prepare_data)
        self.suggest_hierarchy = suggest_hierarchy.AsyncSuggestHierarchyResourceWithStreamingResponse(
            client.suggest_hierarchy
        )
        self.suggest_description = suggest_description.AsyncSuggestDescriptionResourceWithStreamingResponse(
            client.suggest_description
        )
        self.tags = tags.AsyncTagsResourceWithStreamingResponse(client.tags)
        self.metadata = metadata.AsyncMetadataResourceWithStreamingResponse(client.metadata)
        self.vdb_connector = vdb_connector.AsyncVdbConnectorResourceWithStreamingResponse(client.vdb_connector)
        self.llm_connector = llm_connector.AsyncLlmConnectorResourceWithStreamingResponse(client.llm_connector)
        self.dataslice = dataslice.AsyncDatasliceResourceWithStreamingResponse(client.dataslice)
        self.graph = graph.AsyncGraphResourceWithStreamingResponse(client.graph)


Client = Deasy

AsyncClient = AsyncDeasy
