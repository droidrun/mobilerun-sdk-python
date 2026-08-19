# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required, Literal

from .._utils import PropertyInfo

from .._types import SequenceNotStr

from typing import Iterable, Optional, Dict

__all__ = ["TaskRunStreamedParams", "Credential"]

class TaskRunStreamedParams(TypedDict, total=False):
    device_id: Required[Annotated[str, PropertyInfo(alias="deviceId")]]
    """The ID of the device to run the task on."""

    task: Required[str]

    accessibility: bool

    agent_id: Annotated[int, PropertyInfo(alias="agentId")]

    apps: SequenceNotStr[str]

    continue_on_failure: Annotated[bool, PropertyInfo(alias="continueOnFailure")]

    credentials: Iterable[Credential]

    display_id: Annotated[int, PropertyInfo(alias="displayId")]
    """The display ID of the device to run the task on."""

    execution_timeout: Annotated[int, PropertyInfo(alias="executionTimeout")]

    files: SequenceNotStr[str]

    llm_model: Annotated[str, PropertyInfo(alias="llmModel")]
    """The LLM model identifier to use for the task (e.g. 'google/gemini-3.5-flash')"""

    max_steps: Annotated[int, PropertyInfo(alias="maxSteps")]

    memory_namespace: Annotated[str, PropertyInfo(alias="memoryNamespace")]
    """Memory namespace for cross-task personalization"""

    output_schema: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="outputSchema")]

    reasoning: bool

    stealth: bool

    subagent_model: Annotated[str, PropertyInfo(alias="subagentModel")]
    """LLM model used by sub-agent roles: executor, app_opener, structured_output"""

    temperature: float

    vision: bool

    vpn_country: Annotated[Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]], PropertyInfo(alias="vpnCountry")]

class Credential(TypedDict, total=False):
    credential_names: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="credentialNames")]]

    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]