# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["MetadataListResponse"]


class MetadataListResponse(BaseModel):
    metadata: Dict[str, object]
