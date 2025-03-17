# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from Deasy import Deasy, AsyncDeasy
from Deasy.types import ClassifyClassifyFilesResponse
from tests.utils import assert_matches_type
from Deasy._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassify:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_files(self, client: Deasy) -> None:
        classify = client.classify.classify_files(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_files_with_all_params(self, client: Deasy) -> None:
        classify = client.classify.classify_files(
            vdb_profile_name="vdb_profile_name",
            dataslice_id="dataslice_id",
            file_names=["string"],
            hierarchy_data={},
            hierarchy_name="hierarchy_name",
            job_id="job_id",
            llm_profile_name="llm_profile_name",
            overwrite=True,
            soft_run=True,
            tag_datas={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                    "available_values": ["string"],
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "date_format": "date_format",
                    "examples": ["string"],
                    "max_values": 0,
                    "neg_examples": ["string"],
                    "retry_feedback": {},
                    "tag_id": "tag_id",
                    "tuned": 0,
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "username": "username",
                }
            },
            tag_names=["string"],
        )
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_classify_files(self, client: Deasy) -> None:
        response = client.classify.with_raw_response.classify_files(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = response.parse()
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_classify_files(self, client: Deasy) -> None:
        with client.classify.with_streaming_response.classify_files(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = response.parse()
            assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassify:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_files(self, async_client: AsyncDeasy) -> None:
        classify = await async_client.classify.classify_files(
            vdb_profile_name="vdb_profile_name",
        )
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_files_with_all_params(self, async_client: AsyncDeasy) -> None:
        classify = await async_client.classify.classify_files(
            vdb_profile_name="vdb_profile_name",
            dataslice_id="dataslice_id",
            file_names=["string"],
            hierarchy_data={},
            hierarchy_name="hierarchy_name",
            job_id="job_id",
            llm_profile_name="llm_profile_name",
            overwrite=True,
            soft_run=True,
            tag_datas={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "output_type": "output_type",
                    "available_values": ["string"],
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "date_format": "date_format",
                    "examples": ["string"],
                    "max_values": 0,
                    "neg_examples": ["string"],
                    "retry_feedback": {},
                    "tag_id": "tag_id",
                    "tuned": 0,
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "username": "username",
                }
            },
            tag_names=["string"],
        )
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_classify_files(self, async_client: AsyncDeasy) -> None:
        response = await async_client.classify.with_raw_response.classify_files(
            vdb_profile_name="vdb_profile_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = await response.parse()
        assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_classify_files(self, async_client: AsyncDeasy) -> None:
        async with async_client.classify.with_streaming_response.classify_files(
            vdb_profile_name="vdb_profile_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = await response.parse()
            assert_matches_type(ClassifyClassifyFilesResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True
