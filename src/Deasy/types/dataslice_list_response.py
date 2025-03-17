# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["DatasliceListResponse", "Dataslice"]


class Dataslice(BaseModel):
    data_points: int

    dataslice_id: str

    dataslice_name: str

    last_updated: datetime

    status: str

    condition: Optional[List[object]] = None

    condition_new: Optional["ConditionOutput"] = None

    description: Optional[str] = None

    export_collection_name: Optional[str] = None

    graph_id: Optional[str] = None

    latest_graph: Optional[object] = None

    vector_db_config: Optional[object] = None


class DatasliceListResponse(BaseModel):
    dataslices: List[Dataslice]


from .condition_output import ConditionOutput

if PYDANTIC_V2:
    DatasliceListResponse.model_rebuild()
    Dataslice.model_rebuild()
else:
    DatasliceListResponse.update_forward_refs()  # type: ignore
    Dataslice.update_forward_refs()  # type: ignore
