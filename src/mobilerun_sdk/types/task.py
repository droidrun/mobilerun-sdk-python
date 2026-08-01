# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Task"]


class Task(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    task_id: str = FieldInfo(alias="taskId")

    updated_at: datetime = FieldInfo(alias="updatedAt")
