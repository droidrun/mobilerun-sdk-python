# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from pydantic import Field as FieldInfo

__all__ = ["WebhookTestDeliveryResponse", "Data"]

class Data(BaseModel):
    error: Optional[str] = None

    status_code: Optional[float] = FieldInfo(alias = "statusCode", default = None)

    success: bool

class WebhookTestDeliveryResponse(BaseModel):
    data: Data