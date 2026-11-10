# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentModelProfilesResponse", "Profile"]


class Profile(BaseModel):
    id: str

    cost_hint: str = FieldInfo(alias="costHint")

    description: str

    label: str


class AgentModelProfilesResponse(BaseModel):
    default_profile_id: str = FieldInfo(alias="defaultProfileId")

    profiles: List[Profile]
