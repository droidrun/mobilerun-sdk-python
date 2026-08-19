# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from pydantic import Field as FieldInfo

from datetime import datetime

from typing_extensions import Literal

from typing import Optional

__all__ = ["MediaSessionCreateResponse"]

class MediaSessionCreateResponse(BaseModel):
    camera: bool

    control_token: str = FieldInfo(alias = "controlToken")

    expires_at: datetime = FieldInfo(alias = "expiresAt")

    microphone: bool

    publish_token: str = FieldInfo(alias = "publishToken")

    publish_url: str = FieldInfo(alias = "publishUrl")

    session_id: str = FieldInfo(alias = "sessionId")

    state: Literal["created", "publishing", "active", "stopping", "closed", "failed"]

    schema_: Optional[str] = FieldInfo(alias = "$schema", default = None)
    """A URL to the JSON Schema for this object."""