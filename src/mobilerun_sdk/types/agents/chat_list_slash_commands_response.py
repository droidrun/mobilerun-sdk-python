# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ChatListSlashCommandsResponse", "Command"]


class Command(BaseModel):
    name: str
    """Including the leading slash (e.g. `/help`)."""

    summary: str

    args: Optional[str] = None
    """Arg signature for the help card (e.g.

    `<task>`, `<deviceId>`). Always angle-bracketed; the summary spells out when an
    arg is optional.
    """


class ChatListSlashCommandsResponse(BaseModel):
    commands: List[Command]
