# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .shared_params.or_ import Or
from .shared_params.and_ import And

__all__ = ["QueryParam"]

QueryParam: TypeAlias = Union[Or, And]
