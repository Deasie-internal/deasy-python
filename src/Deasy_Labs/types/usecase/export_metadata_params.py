# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExportMetadataParams"]


class ExportMetadataParams(TypedDict, total=False):
    vector_db_config: Required[object]

    export_both_levels: bool

    export_chunk_level: bool

    export_file_level: bool

    export_format: Optional[Literal["json", "csv"]]

    selected_metadata_fields: Optional[List[str]]

    usecase_id: Optional[str]
