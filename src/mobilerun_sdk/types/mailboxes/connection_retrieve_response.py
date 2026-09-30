# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConnectionRetrieveResponse"]


class ConnectionRetrieveResponse(BaseModel):
    address: Optional[str] = None

    connection_id: str = FieldInfo(alias="connectionId")

    mailbox_id: str = FieldInfo(alias="mailboxId")

    redirect_url: Optional[str] = FieldInfo(alias="redirectUrl", default=None)

    status: Literal["pending", "active", "expired", "removed"]
