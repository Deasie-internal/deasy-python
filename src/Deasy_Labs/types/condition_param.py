# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConditionParam", "Tag"]


class Tag(TypedDict, total=False):
    name: Required[str]

    values: Required[List[str]]


class ConditionParam(TypedDict, total=False):
    children: Optional[Iterable["ConditionParam"]]

    condition: Optional[Literal["AND", "OR"]]

    tag: Optional[Tag]
