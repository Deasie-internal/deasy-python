# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["GraphListParams"]


class GraphListParams(TypedDict, total=False):
    graph_names: Optional[List[str]]
