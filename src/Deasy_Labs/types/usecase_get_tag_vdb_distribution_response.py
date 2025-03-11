# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["UsecaseGetTagVdbDistributionResponse"]


class UsecaseGetTagVdbDistributionResponse(BaseModel):
    tag_distribution: Dict[str, int]
