# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from deasy_python import DeasyLabs, AsyncDeasyLabs
from deasy_python.types import (
    TagResponse,
    TagListResponse,
    TagCreateResponse,
    TagUpsertResponse,
    TagGetDeleteStatsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DeasyLabs) -> None:
        tag = client.tags.create(
            tag_data={},
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DeasyLabs) -> None:
        response = client.tags.with_raw_response.create(
            tag_data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DeasyLabs) -> None:
        with client.tags.with_streaming_response.create(
            tag_data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: DeasyLabs) -> None:
        tag = client.tags.update(
            tag_data={},
        )
        assert_matches_type(TagResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: DeasyLabs) -> None:
        response = client.tags.with_raw_response.update(
            tag_data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: DeasyLabs) -> None:
        with client.tags.with_streaming_response.update(
            tag_data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: DeasyLabs) -> None:
        tag = client.tags.list()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: DeasyLabs) -> None:
        response = client.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: DeasyLabs) -> None:
        with client.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: DeasyLabs) -> None:
        tag = client.tags.delete(
            tag_name="tag_name",
        )
        assert_matches_type(TagResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: DeasyLabs) -> None:
        response = client.tags.with_raw_response.delete(
            tag_name="tag_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: DeasyLabs) -> None:
        with client.tags.with_streaming_response.delete(
            tag_name="tag_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_delete_stats(self, client: DeasyLabs) -> None:
        tag = client.tags.get_delete_stats(
            tag_name="tag_name",
        )
        assert_matches_type(TagGetDeleteStatsResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_delete_stats(self, client: DeasyLabs) -> None:
        response = client.tags.with_raw_response.get_delete_stats(
            tag_name="tag_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagGetDeleteStatsResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_delete_stats(self, client: DeasyLabs) -> None:
        with client.tags.with_streaming_response.get_delete_stats(
            tag_name="tag_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagGetDeleteStatsResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_upsert(self, client: DeasyLabs) -> None:
        tag = client.tags.upsert(
            tag_data={},
        )
        assert_matches_type(TagUpsertResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upsert(self, client: DeasyLabs) -> None:
        response = client.tags.with_raw_response.upsert(
            tag_data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagUpsertResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upsert(self, client: DeasyLabs) -> None:
        with client.tags.with_streaming_response.upsert(
            tag_data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagUpsertResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDeasyLabs) -> None:
        tag = await async_client.tags.create(
            tag_data={},
        )
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.tags.with_raw_response.create(
            tag_data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagCreateResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.tags.with_streaming_response.create(
            tag_data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagCreateResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncDeasyLabs) -> None:
        tag = await async_client.tags.update(
            tag_data={},
        )
        assert_matches_type(TagResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.tags.with_raw_response.update(
            tag_data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.tags.with_streaming_response.update(
            tag_data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDeasyLabs) -> None:
        tag = await async_client.tags.list()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasyLabs) -> None:
        tag = await async_client.tags.delete(
            tag_name="tag_name",
        )
        assert_matches_type(TagResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.tags.with_raw_response.delete(
            tag_name="tag_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.tags.with_streaming_response.delete(
            tag_name="tag_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_delete_stats(self, async_client: AsyncDeasyLabs) -> None:
        tag = await async_client.tags.get_delete_stats(
            tag_name="tag_name",
        )
        assert_matches_type(TagGetDeleteStatsResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_delete_stats(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.tags.with_raw_response.get_delete_stats(
            tag_name="tag_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagGetDeleteStatsResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_delete_stats(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.tags.with_streaming_response.get_delete_stats(
            tag_name="tag_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagGetDeleteStatsResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_upsert(self, async_client: AsyncDeasyLabs) -> None:
        tag = await async_client.tags.upsert(
            tag_data={},
        )
        assert_matches_type(TagUpsertResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.tags.with_raw_response.upsert(
            tag_data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagUpsertResponse, tag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.tags.with_streaming_response.upsert(
            tag_data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagUpsertResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True
