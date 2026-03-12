# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .package_credentials_param import PackageCredentialsParam

__all__ = ["TaskRunParams"]


class TaskRunParams(TypedDict, total=False):
    device_id: Required[Annotated[str, PropertyInfo(alias="deviceId")]]
    """The ID of the device to run the task on."""

    task: Required[str]

    agent_id: Annotated[int, PropertyInfo(alias="agentId")]

    apps: SequenceNotStr[str]

    credentials: Iterable[PackageCredentialsParam]

    display_id: Annotated[int, PropertyInfo(alias="displayId")]
    """The display ID of the device to run the task on."""

    execution_timeout: Annotated[int, PropertyInfo(alias="executionTimeout")]

    files: SequenceNotStr[str]

    llm_model: Annotated[str, PropertyInfo(alias="llmModel")]
    """The LLM model identifier to use for the task (e.g.

    'google/gemini-3.1-flash-lite-preview')
    """

    max_steps: Annotated[int, PropertyInfo(alias="maxSteps")]

    output_schema: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="outputSchema")]

    reasoning: bool

    stealth: bool

    temperature: float

    vision: bool

    vpn_country: Annotated[
        Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]], PropertyInfo(alias="vpnCountry")
    ]
