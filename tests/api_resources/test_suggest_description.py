# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy_Labs import DeasyLabs, AsyncDeasyLabs
from tests.utils import assert_matches_type
from Deasy_Labs.types import SuggestDescriptionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuggestDescription:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DeasyLabs) -> None:
        suggest_description = client.suggest_description.create(
            endpoint_manager_config={},
            tag_name="tag_name",
        )
        assert_matches_type(SuggestDescriptionCreateResponse, suggest_description, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: DeasyLabs) -> None:
        suggest_description = client.suggest_description.create(
            endpoint_manager_config={},
            tag_name="tag_name",
            available_values=["string"],
            context="context",
            current_description="current_description",
            vector_db_config={},
        )
        assert_matches_type(SuggestDescriptionCreateResponse, suggest_description, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DeasyLabs) -> None:
        response = client.suggest_description.with_raw_response.create(
            endpoint_manager_config={},
            tag_name="tag_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suggest_description = response.parse()
        assert_matches_type(SuggestDescriptionCreateResponse, suggest_description, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DeasyLabs) -> None:
        with client.suggest_description.with_streaming_response.create(
            endpoint_manager_config={},
            tag_name="tag_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suggest_description = response.parse()
            assert_matches_type(SuggestDescriptionCreateResponse, suggest_description, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSuggestDescription:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDeasyLabs) -> None:
        suggest_description = await async_client.suggest_description.create(
            endpoint_manager_config={},
            tag_name="tag_name",
        )
        assert_matches_type(SuggestDescriptionCreateResponse, suggest_description, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDeasyLabs) -> None:
        suggest_description = await async_client.suggest_description.create(
            endpoint_manager_config={},
            tag_name="tag_name",
            available_values=["string"],
            context="context",
            current_description="current_description",
            vector_db_config={},
        )
        assert_matches_type(SuggestDescriptionCreateResponse, suggest_description, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDeasyLabs) -> None:
        response = await async_client.suggest_description.with_raw_response.create(
            endpoint_manager_config={},
            tag_name="tag_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suggest_description = await response.parse()
        assert_matches_type(SuggestDescriptionCreateResponse, suggest_description, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDeasyLabs) -> None:
        async with async_client.suggest_description.with_streaming_response.create(
            endpoint_manager_config={},
            tag_name="tag_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suggest_description = await response.parse()
            assert_matches_type(SuggestDescriptionCreateResponse, suggest_description, path=["response"])

        assert cast(Any, response.is_closed) is True
