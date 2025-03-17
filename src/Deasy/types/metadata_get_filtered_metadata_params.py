# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .tag_condition_param import TagConditionParam

__all__ = ["MetadataGetFilteredMetadataParams", "Condition"]


class MetadataGetFilteredMetadataParams(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]

    vector_db_config: Required[object]

    conditions_new: Optional["ConditionInputParam"]

    dataslice_id: Optional[str]

    limit: Optional[int]

    node_condition: Optional[Iterable[TagConditionParam]]

    offset: Optional[int]

    search_query: Optional[str]


class Condition(TypedDict, total=False):
    tag_id: Required[str]

    values: Required[List[str]]


from .condition_input_param import ConditionInputParam
