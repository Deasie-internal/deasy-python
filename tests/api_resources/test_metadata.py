# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from Deasy.types import (
    MetadataDeleteResponse,
    MetadataGetEvidenceResponse,
    MetadataGetUniqueTagsResponse,
    MetadataGetBasicMetadataResponse,
    MetadataGetDistributionsResponse,
    MetadataGetTagStatisticsResponse,
    MetadataGetDistinctValuesResponse,
    MetadataCountDistributionsResponse,
    MetadataFilterByConditionsResponse,
    MetadataGetFilteredMetadataResponse,
    MetadataGetOobTaggedFileCountResponse,
    MetadataApplyStandardizationDBResponse,
    MetadataSuggestStandardizationResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Deasy) -> None:
        metadata = client.metadata.delete(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.delete(
            vector_db_config={},
            x_user="x-user",
            conditions=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
            file_names=["string"],
            tags=["string"],
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.delete(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.delete(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_apply_standardization_db(self, client: Deasy) -> None:
        metadata = client.metadata.apply_standardization_db(
            endpoint_manager_config={},
            standard_mapping={"foo": [{}]},
            tag_name="tag_name",
            vector_db_config={},
        )
        assert_matches_type(MetadataApplyStandardizationDBResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_apply_standardization_db(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.apply_standardization_db(
            endpoint_manager_config={},
            standard_mapping={"foo": [{}]},
            tag_name="tag_name",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataApplyStandardizationDBResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_apply_standardization_db(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.apply_standardization_db(
            endpoint_manager_config={},
            standard_mapping={"foo": [{}]},
            tag_name="tag_name",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataApplyStandardizationDBResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_count_distributions(self, client: Deasy) -> None:
        metadata = client.metadata.count_distributions(
            current_tree="current_tree",
            vector_db_config={},
        )
        assert_matches_type(MetadataCountDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_count_distributions_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.count_distributions(
            current_tree="current_tree",
            vector_db_config={},
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            endpoint_manager_config={},
            x_token="x-token",
        )
        assert_matches_type(MetadataCountDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_count_distributions(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.count_distributions(
            current_tree="current_tree",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataCountDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_count_distributions(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.count_distributions(
            current_tree="current_tree",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataCountDistributionsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_filter_by_conditions(self, client: Deasy) -> None:
        metadata = client.metadata.filter_by_conditions(
            conditions=[{"tag_id": "tag_id"}],
            vector_db_config={},
        )
        assert_matches_type(MetadataFilterByConditionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_filter_by_conditions_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.filter_by_conditions(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
            analyze_remaining_tags=["string"],
        )
        assert_matches_type(MetadataFilterByConditionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_filter_by_conditions(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.filter_by_conditions(
            conditions=[{"tag_id": "tag_id"}],
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataFilterByConditionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_filter_by_conditions(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.filter_by_conditions(
            conditions=[{"tag_id": "tag_id"}],
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataFilterByConditionsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_basic_metadata(self, client: Deasy) -> None:
        metadata = client.metadata.get_basic_metadata(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetBasicMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_basic_metadata(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.get_basic_metadata(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataGetBasicMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_basic_metadata(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.get_basic_metadata(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataGetBasicMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_distinct_values(self, client: Deasy) -> None:
        metadata = client.metadata.get_distinct_values(
            page=0,
            tag_id="tag_id",
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataGetDistinctValuesResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_distinct_values_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.get_distinct_values(
            page=0,
            tag_id="tag_id",
            vector_db_config={},
            x_user="x-user",
            conditions=[{}],
            per_page=0,
            search_query="search_query",
        )
        assert_matches_type(MetadataGetDistinctValuesResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_distinct_values(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.get_distinct_values(
            page=0,
            tag_id="tag_id",
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataGetDistinctValuesResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_distinct_values(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.get_distinct_values(
            page=0,
            tag_id="tag_id",
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataGetDistinctValuesResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_distributions(self, client: Deasy) -> None:
        metadata = client.metadata.get_distributions(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_distributions_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.get_distributions(
            vector_db_config={},
            columns=["string"],
            conditions_new={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            dataslice_id="dataslice_id",
            max_val_per_tag=0,
            node_condition=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
        )
        assert_matches_type(MetadataGetDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_distributions(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.get_distributions(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataGetDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_distributions(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.get_distributions(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataGetDistributionsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_evidence(self, client: Deasy) -> None:
        metadata = client.metadata.get_evidence(
            filename="filename",
            tag_id="tag_id",
            tag_value="tag_value",
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataGetEvidenceResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_evidence(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.get_evidence(
            filename="filename",
            tag_id="tag_id",
            tag_value="tag_value",
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataGetEvidenceResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_evidence(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.get_evidence(
            filename="filename",
            tag_id="tag_id",
            tag_value="tag_value",
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataGetEvidenceResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_filtered_metadata(self, client: Deasy) -> None:
        metadata = client.metadata.get_filtered_metadata(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
        )
        assert_matches_type(MetadataGetFilteredMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_filtered_metadata_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.get_filtered_metadata(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
            conditions_new={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            dataslice_id="dataslice_id",
            limit=0,
            node_condition=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
            offset=0,
            search_query="search_query",
            sort_by="sort_by",
            sort_order="sort_order",
        )
        assert_matches_type(MetadataGetFilteredMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_filtered_metadata(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.get_filtered_metadata(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataGetFilteredMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_filtered_metadata(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.get_filtered_metadata(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataGetFilteredMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_oob_tagged_file_count(self, client: Deasy) -> None:
        metadata = client.metadata.get_oob_tagged_file_count(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetOobTaggedFileCountResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_oob_tagged_file_count_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.get_oob_tagged_file_count(
            vector_db_config={},
            conditions=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
        )
        assert_matches_type(MetadataGetOobTaggedFileCountResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_oob_tagged_file_count(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.get_oob_tagged_file_count(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataGetOobTaggedFileCountResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_oob_tagged_file_count(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.get_oob_tagged_file_count(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataGetOobTaggedFileCountResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_tag_statistics(self, client: Deasy) -> None:
        metadata = client.metadata.get_tag_statistics(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetTagStatisticsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_tag_statistics_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.get_tag_statistics(
            vector_db_config={},
            conditions=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
            tag_ids=["string"],
        )
        assert_matches_type(MetadataGetTagStatisticsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_tag_statistics(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.get_tag_statistics(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataGetTagStatisticsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_tag_statistics(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.get_tag_statistics(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataGetTagStatisticsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_unique_tags(self, client: Deasy) -> None:
        metadata = client.metadata.get_unique_tags(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetUniqueTagsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_unique_tags_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.get_unique_tags(
            vector_db_config={},
            dataslice_id="dataslice_id",
            file_names=["string"],
            node_condition=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
        )
        assert_matches_type(MetadataGetUniqueTagsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_unique_tags(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.get_unique_tags(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataGetUniqueTagsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_unique_tags(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.get_unique_tags(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataGetUniqueTagsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_suggest_standardization(self, client: Deasy) -> None:
        metadata = client.metadata.suggest_standardization(
            description="description",
            endpoint_manager_config={},
            output_type="output_type",
            tag_name="tag_name",
            value_distribution={"foo": 0},
            vector_db_config={},
        )
        assert_matches_type(MetadataSuggestStandardizationResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_suggest_standardization_with_all_params(self, client: Deasy) -> None:
        metadata = client.metadata.suggest_standardization(
            description="description",
            endpoint_manager_config={},
            output_type="output_type",
            tag_name="tag_name",
            value_distribution={"foo": 0},
            vector_db_config={},
            context="context",
            existing_categories={},
        )
        assert_matches_type(MetadataSuggestStandardizationResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_suggest_standardization(self, client: Deasy) -> None:
        response = client.metadata.with_raw_response.suggest_standardization(
            description="description",
            endpoint_manager_config={},
            output_type="output_type",
            tag_name="tag_name",
            value_distribution={"foo": 0},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataSuggestStandardizationResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_suggest_standardization(self, client: Deasy) -> None:
        with client.metadata.with_streaming_response.suggest_standardization(
            description="description",
            endpoint_manager_config={},
            output_type="output_type",
            tag_name="tag_name",
            value_distribution={"foo": 0},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataSuggestStandardizationResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.delete(
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.delete(
            vector_db_config={},
            x_user="x-user",
            conditions=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
            file_names=["string"],
            tags=["string"],
        )
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.delete(
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.delete(
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataDeleteResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_apply_standardization_db(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.apply_standardization_db(
            endpoint_manager_config={},
            standard_mapping={"foo": [{}]},
            tag_name="tag_name",
            vector_db_config={},
        )
        assert_matches_type(MetadataApplyStandardizationDBResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_apply_standardization_db(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.apply_standardization_db(
            endpoint_manager_config={},
            standard_mapping={"foo": [{}]},
            tag_name="tag_name",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataApplyStandardizationDBResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_apply_standardization_db(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.apply_standardization_db(
            endpoint_manager_config={},
            standard_mapping={"foo": [{}]},
            tag_name="tag_name",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataApplyStandardizationDBResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_count_distributions(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.count_distributions(
            current_tree="current_tree",
            vector_db_config={},
        )
        assert_matches_type(MetadataCountDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_count_distributions_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.count_distributions(
            current_tree="current_tree",
            vector_db_config={},
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            endpoint_manager_config={},
            x_token="x-token",
        )
        assert_matches_type(MetadataCountDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_count_distributions(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.count_distributions(
            current_tree="current_tree",
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataCountDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_count_distributions(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.count_distributions(
            current_tree="current_tree",
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataCountDistributionsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_filter_by_conditions(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.filter_by_conditions(
            conditions=[{"tag_id": "tag_id"}],
            vector_db_config={},
        )
        assert_matches_type(MetadataFilterByConditionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_filter_by_conditions_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.filter_by_conditions(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
            analyze_remaining_tags=["string"],
        )
        assert_matches_type(MetadataFilterByConditionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_filter_by_conditions(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.filter_by_conditions(
            conditions=[{"tag_id": "tag_id"}],
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataFilterByConditionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_filter_by_conditions(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.filter_by_conditions(
            conditions=[{"tag_id": "tag_id"}],
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataFilterByConditionsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_basic_metadata(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_basic_metadata(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetBasicMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_basic_metadata(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.get_basic_metadata(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataGetBasicMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_basic_metadata(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.get_basic_metadata(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataGetBasicMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_distinct_values(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_distinct_values(
            page=0,
            tag_id="tag_id",
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataGetDistinctValuesResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_distinct_values_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_distinct_values(
            page=0,
            tag_id="tag_id",
            vector_db_config={},
            x_user="x-user",
            conditions=[{}],
            per_page=0,
            search_query="search_query",
        )
        assert_matches_type(MetadataGetDistinctValuesResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_distinct_values(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.get_distinct_values(
            page=0,
            tag_id="tag_id",
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataGetDistinctValuesResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_distinct_values(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.get_distinct_values(
            page=0,
            tag_id="tag_id",
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataGetDistinctValuesResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_distributions(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_distributions(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_distributions_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_distributions(
            vector_db_config={},
            columns=["string"],
            conditions_new={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            dataslice_id="dataslice_id",
            max_val_per_tag=0,
            node_condition=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
        )
        assert_matches_type(MetadataGetDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_distributions(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.get_distributions(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataGetDistributionsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_distributions(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.get_distributions(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataGetDistributionsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_evidence(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_evidence(
            filename="filename",
            tag_id="tag_id",
            tag_value="tag_value",
            vector_db_config={},
            x_user="x-user",
        )
        assert_matches_type(MetadataGetEvidenceResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_evidence(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.get_evidence(
            filename="filename",
            tag_id="tag_id",
            tag_value="tag_value",
            vector_db_config={},
            x_user="x-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataGetEvidenceResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_evidence(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.get_evidence(
            filename="filename",
            tag_id="tag_id",
            tag_value="tag_value",
            vector_db_config={},
            x_user="x-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataGetEvidenceResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_filtered_metadata(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_filtered_metadata(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
        )
        assert_matches_type(MetadataGetFilteredMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_filtered_metadata_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_filtered_metadata(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
            conditions_new={
                "children": [],
                "condition": "AND",
                "tag": {
                    "name": "name",
                    "values": ["string"],
                },
            },
            dataslice_id="dataslice_id",
            limit=0,
            node_condition=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
            offset=0,
            search_query="search_query",
            sort_by="sort_by",
            sort_order="sort_order",
        )
        assert_matches_type(MetadataGetFilteredMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_filtered_metadata(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.get_filtered_metadata(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataGetFilteredMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_filtered_metadata(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.get_filtered_metadata(
            conditions=[
                {
                    "tag_id": "tag_id",
                    "values": ["string"],
                }
            ],
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataGetFilteredMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_oob_tagged_file_count(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_oob_tagged_file_count(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetOobTaggedFileCountResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_oob_tagged_file_count_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_oob_tagged_file_count(
            vector_db_config={},
            conditions=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
        )
        assert_matches_type(MetadataGetOobTaggedFileCountResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_oob_tagged_file_count(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.get_oob_tagged_file_count(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataGetOobTaggedFileCountResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_oob_tagged_file_count(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.get_oob_tagged_file_count(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataGetOobTaggedFileCountResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_tag_statistics(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_tag_statistics(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetTagStatisticsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_tag_statistics_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_tag_statistics(
            vector_db_config={},
            conditions=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
            tag_ids=["string"],
        )
        assert_matches_type(MetadataGetTagStatisticsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_tag_statistics(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.get_tag_statistics(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataGetTagStatisticsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_tag_statistics(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.get_tag_statistics(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataGetTagStatisticsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_unique_tags(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_unique_tags(
            vector_db_config={},
        )
        assert_matches_type(MetadataGetUniqueTagsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_unique_tags_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.get_unique_tags(
            vector_db_config={},
            dataslice_id="dataslice_id",
            file_names=["string"],
            node_condition=[
                {
                    "tag_id": "tag_id",
                    "operator": "in",
                    "values": ["string"],
                }
            ],
        )
        assert_matches_type(MetadataGetUniqueTagsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_unique_tags(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.get_unique_tags(
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataGetUniqueTagsResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_unique_tags(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.get_unique_tags(
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataGetUniqueTagsResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_suggest_standardization(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.suggest_standardization(
            description="description",
            endpoint_manager_config={},
            output_type="output_type",
            tag_name="tag_name",
            value_distribution={"foo": 0},
            vector_db_config={},
        )
        assert_matches_type(MetadataSuggestStandardizationResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_suggest_standardization_with_all_params(self, async_client: AsyncDeasy) -> None:
        metadata = await async_client.metadata.suggest_standardization(
            description="description",
            endpoint_manager_config={},
            output_type="output_type",
            tag_name="tag_name",
            value_distribution={"foo": 0},
            vector_db_config={},
            context="context",
            existing_categories={},
        )
        assert_matches_type(MetadataSuggestStandardizationResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_suggest_standardization(self, async_client: AsyncDeasy) -> None:
        response = await async_client.metadata.with_raw_response.suggest_standardization(
            description="description",
            endpoint_manager_config={},
            output_type="output_type",
            tag_name="tag_name",
            value_distribution={"foo": 0},
            vector_db_config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataSuggestStandardizationResponse, metadata, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_suggest_standardization(self, async_client: AsyncDeasy) -> None:
        async with async_client.metadata.with_streaming_response.suggest_standardization(
            description="description",
            endpoint_manager_config={},
            output_type="output_type",
            tag_name="tag_name",
            value_distribution={"foo": 0},
            vector_db_config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataSuggestStandardizationResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True
