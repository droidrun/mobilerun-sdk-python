# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from pydantic import Field as FieldInfo

from typing_extensions import Literal

from typing import Optional

__all__ = ["MediaSessionActivateResponse"]

class MediaSessionActivateResponse(BaseModel):
    camera: bool

    expires_at: datetime = FieldInfo(alias = "expiresAt")

    microphone: bool

    session_id: str = FieldInfo(alias = "sessionId")

    state: Literal["created", "publishing", "active", "stopping", "closed", "failed"]

    schema_: Optional[str] = FieldInfo(alias = "$schema", default = None)
    """A URL to the JSON Schema for this object."""