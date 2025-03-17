# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["PsqlConnectorConfigParam", "IndexInfo"]


class IndexInfo(TypedDict, total=False):
    found_indexes: Required[List[str]]

    total_indexes_found: Required[int]


class PsqlConnectorConfigParam(TypedDict, total=False):
    collection_name: Required[str]

    database_name: Required[str]

    db_user: Required[str]

    index_info: Required[IndexInfo]

    name: Required[str]

    password: Required[str]

    port: Required[str]

    url: Required[str]

    filename_key: str

    text_key: str

    type: str
