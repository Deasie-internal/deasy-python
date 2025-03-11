# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .deasy_tag import DeasyTag

__all__ = ["TagCreateResponse"]


class TagCreateResponse(BaseModel):
    available_values_added: List[str]

    tag: DeasyTag

    tag_id: str
