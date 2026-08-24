# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailboxOtpParams"]


class MailboxOtpParams(TypedDict, total=False):
    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    max_length: Annotated[int, PropertyInfo(alias="maxLength")]

    min_length: Annotated[int, PropertyInfo(alias="minLength")]

    sender: str
