# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ModelListResponse", "Data"]


class Data(BaseModel):
    id: str

    created: int

    object: Literal["model"]

    owned_by: str

    group: Optional[Literal["recommended", "fast", "more"]] = None

    label: Optional[str] = None

    order: Optional[int] = None

    surfaces: Optional[List[Literal["assistant", "tasks"]]] = None
    """Model pickers this model is offered in, from LiteLLM model_info.ui_surfaces.

    Omitted when unset, which means every picker.
    """


class ModelListResponse(BaseModel):
    data: List[Data]

    object: Literal["list"]
