# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .flow_execution import FlowExecution

__all__ = ["ExecutionRetrieveResponse", "Data", "DataFile"]


class DataFile(BaseModel):
    file_id: str = FieldInfo(alias="fileId")

    filename: str

    mime_type: str = FieldInfo(alias="mimeType")

    size_bytes: int = FieldInfo(alias="sizeBytes")


class Data(FlowExecution):
    files: List[DataFile]
    """
    Files produced by files.upload steps, plus files an agent.run step reported on
    its terminal response (agent-created output or a workflow upload minted during
    the turn); derived server-side at read time.
    """


class ExecutionRetrieveResponse(BaseModel):
    data: Data
