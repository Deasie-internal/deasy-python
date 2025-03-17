# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["MetadataCountDistributionsResponse"]


class MetadataCountDistributionsResponse(BaseModel):
    hierarchy: "HierarchyStatsNode"


from .hierarchy_stats_node import HierarchyStatsNode

if PYDANTIC_V2:
    MetadataCountDistributionsResponse.model_rebuild()
else:
    MetadataCountDistributionsResponse.update_forward_refs()  # type: ignore
