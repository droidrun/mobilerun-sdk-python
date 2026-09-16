# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["TaskRunParams", "Credential"]


class TaskRunParams(TypedDict, total=False):
    device_id: Required[Annotated[str, PropertyInfo(alias="deviceId")]]
    """The ID of the device to run the task on."""

    task: Required[str]

    accessibility: bool

    apps: SequenceNotStr[str]

    continue_on_failure: Annotated[bool, PropertyInfo(alias="continueOnFailure")]

    credentials: Iterable[Credential]

    display_id: Annotated[int, PropertyInfo(alias="displayId")]
    """The display ID of the device to run the task on."""

    execution_timeout: Annotated[int, PropertyInfo(alias="executionTimeout")]
    """Maximum agent execution time in seconds (1–2700)."""

    files: SequenceNotStr[str]

    llm_model: Annotated[str, PropertyInfo(alias="llmModel")]
    """The LLM model identifier to use for the task (e.g. 'openai/gpt-5.6-luna')"""

    max_steps: Annotated[int, PropertyInfo(alias="maxSteps")]

    output_schema: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="outputSchema")]

    reasoning: bool

    recording_enabled: Annotated[bool, PropertyInfo(alias="recordingEnabled")]
    """Record device video for the whole task and persist a retrievable reference"""

    stealth: bool

    subagent_model: Annotated[str, PropertyInfo(alias="subagentModel")]
    """LLM model used by sub-agent roles: executor, app_opener, structured_output"""

    system_prompt: Annotated[Optional[str], PropertyInfo(alias="systemPrompt")]
    """
    Optional custom behavioral overlay applied on top of the agent's default system
    prompts. Never echoed back in responses or errors.
    """

    temperature: float
    """Deprecated and ignored. Sampling behavior is controlled by the model provider."""

    vision: bool

    vpn_country: Annotated[
        Optional[Literal["US", "BR", "FR", "DE", "IN", "JP", "KR", "ZA"]], PropertyInfo(alias="vpnCountry")
    ]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Credential(TypedDict, total=False):
    credential_names: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="credentialNames")]]

    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]
