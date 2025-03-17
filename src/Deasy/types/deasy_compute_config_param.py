# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeasyComputeConfigParam"]


class DeasyComputeConfigParam(TypedDict, total=False):
    llm_type: Annotated[str, PropertyInfo(alias="llmType")]
