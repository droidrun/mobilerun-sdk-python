# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LinkCreateParams", "FieldMap"]


class LinkCreateParams(TypedDict, total=False):
    credential_name: Required[Annotated[str, PropertyInfo(alias="credentialName")]]

    field_map: Required[Annotated[Iterable[FieldMap], PropertyInfo(alias="fieldMap")]]

    item_id: Required[Annotated[str, PropertyInfo(alias="itemId")]]

    vault_id: Required[Annotated[str, PropertyInfo(alias="vaultId")]]


class FieldMap(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]

    field_type: Required[
        Annotated[
            Literal["email", "username", "password", "api_token", "phone_number", "two_factor_secret", "backup_codes"],
            PropertyInfo(alias="fieldType"),
        ]
    ]
