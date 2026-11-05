# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PackageListResponse", "Data", "DataField", "DataLink", "DataLinkFieldMap"]


class DataField(BaseModel):
    field_type: Literal[
        "email", "username", "password", "api_token", "phone_number", "two_factor_secret", "backup_codes"
    ] = FieldInfo(alias="fieldType")

    value: str


class DataLinkFieldMap(BaseModel):
    field_id: str = FieldInfo(alias="fieldId")

    field_type: Literal[
        "email", "username", "password", "api_token", "phone_number", "two_factor_secret", "backup_codes"
    ] = FieldInfo(alias="fieldType")


class DataLink(BaseModel):
    field_map: List[DataLinkFieldMap] = FieldInfo(alias="fieldMap")

    item_id: str = FieldInfo(alias="itemId")

    item_title: str = FieldInfo(alias="itemTitle")

    provider: Literal["onepassword"]

    vault_id: str = FieldInfo(alias="vaultId")

    vault_name: str = FieldInfo(alias="vaultName")


class Data(BaseModel):
    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    credential_name: str = FieldInfo(alias="credentialName")

    fields: List[DataField]

    owner_id: str = FieldInfo(alias="ownerId")

    package_name: str = FieldInfo(alias="packageName")

    secret_path: str = FieldInfo(alias="secretPath")

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Deprecated: use createdBy (same value — the creating actor).

    Null for credentials created before rollout.
    """

    link: Optional[DataLink] = None

    source: Optional[Literal["mobilerun", "onepassword"]] = None


class PackageListResponse(BaseModel):
    data: List[Data]
