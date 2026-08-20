# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["CredentialListResponse", "Item", "ItemField"]


class ItemField(BaseModel):
    field_type: Literal[
        "email", "username", "password", "api_token", "phone_number", "two_factor_secret", "backup_codes"
    ] = FieldInfo(alias="fieldType")

    value: str


class Item(BaseModel):
    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    credential_name: str = FieldInfo(alias="credentialName")

    fields: List[ItemField]

    owner_id: str = FieldInfo(alias="ownerId")

    package_name: str = FieldInfo(alias="packageName")

    secret_path: str = FieldInfo(alias="secretPath")

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Deprecated: use createdBy (same value — the creating actor).

    Null for credentials created before rollout.
    """


class CredentialListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
