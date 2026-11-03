# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OnepasswordConnectResponse", "Data", "DataVault"]


class DataVault(BaseModel):
    id: str

    title: str


class Data(BaseModel):
    connected: bool

    connected_at: Optional[str] = FieldInfo(alias="connectedAt", default=None)

    connected_by: Optional[str] = FieldInfo(alias="connectedBy", default=None)

    vaults: Optional[List[DataVault]] = None


class OnepasswordConnectResponse(BaseModel):
    data: Data
