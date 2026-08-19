# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from typing import Optional, List

__all__ = ["CredentialCreateResponse", "Data", "DataField"]

class DataField(BaseModel):
    field_type: Literal["email", "username", "password", "api_token", "phone_number", "two_factor_secret", "backup_codes"] = FieldInfo(alias = "fieldType")

    value: str

class Data(BaseModel):
    created_by: Optional[str] = FieldInfo(alias = "createdBy", default = None)

    credential_name: str = FieldInfo(alias = "credentialName")

    fields: List[DataField]

    owner_id: str = FieldInfo(alias = "ownerId")

    package_name: str = FieldInfo(alias = "packageName")

    secret_path: str = FieldInfo(alias = "secretPath")

    user_id: Optional[str] = FieldInfo(alias = "userId", default = None)
    """Deprecated: use createdBy (same value — the creating actor).

    Null for credentials created before rollout.
    """

class CredentialCreateResponse(BaseModel):
    data: Data

    message: str

    success: Literal[True]