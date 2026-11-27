# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "LinkCreateParams",
    "LinkOnePasswordCredentialBody",
    "LinkOnePasswordCredentialBodyFieldMap",
    "LinkWalletCredentialBody",
]


class LinkOnePasswordCredentialBody(TypedDict, total=False):
    credential_name: Required[Annotated[str, PropertyInfo(alias="credentialName")]]

    field_map: Required[Annotated[Iterable[LinkOnePasswordCredentialBodyFieldMap], PropertyInfo(alias="fieldMap")]]

    item_id: Required[Annotated[str, PropertyInfo(alias="itemId")]]

    vault_id: Required[Annotated[str, PropertyInfo(alias="vaultId")]]

    provider: Literal["onepassword"]


class LinkOnePasswordCredentialBodyFieldMap(TypedDict, total=False):
    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]

    field_type: Required[
        Annotated[
            Literal[
                "email",
                "username",
                "password",
                "api_token",
                "phone_number",
                "two_factor_secret",
                "backup_codes",
                "cc_number",
                "cc_exp",
                "cc_csc",
                "cc_name",
            ],
            PropertyInfo(alias="fieldType"),
        ]
    ]


class LinkWalletCredentialBody(TypedDict, total=False):
    card_id: Required[Annotated[str, PropertyInfo(alias="cardId")]]

    credential_name: Required[Annotated[str, PropertyInfo(alias="credentialName")]]

    provider: Required[Literal["wallet"]]


LinkCreateParams: TypeAlias = Union[LinkOnePasswordCredentialBody, LinkWalletCredentialBody]
