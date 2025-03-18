# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClassifyBulkClassifyParams", "TagDatas"]


class ClassifyBulkClassifyParams(TypedDict, total=False):
    vdb_profile_name: Required[str]

    conditions: Optional["ConditionInputParam"]

    dataslice_id: Optional[str]

    hierarchy_data: Optional[object]

    hierarchy_name: Optional[str]

    job_id: Optional[str]

    llm_profile_name: Optional[str]

    overwrite: bool

    tag_datas: Optional[Dict[str, TagDatas]]

    tag_names: Optional[List[str]]

    total_data_sets: Optional[int]


class TagDatas(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    output_type: Required[str]

    available_values: Optional[List[str]]

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    date_format: Optional[str]

    examples: Optional[List[Union[str, object]]]

    max_values: Annotated[Union[int, str, Iterable[object], None], PropertyInfo(alias="maxValues")]

    neg_examples: Optional[List[str]]

    retry_feedback: Optional[object]

    tag_id: Optional[str]

    tuned: Optional[int]

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    username: Optional[str]


from .condition_input_param import ConditionInputParam
