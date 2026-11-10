# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentListResponse", "Agent", "AgentProfile", "AgentProfileAvatarConfig", "AgentThreadPreview"]


class AgentProfileAvatarConfig(BaseModel):
    """
    Configuration of a `blob` avatar: its seed and optional user-chosen palette color. A color-only config retains the default seed fallback.
    """

    color: Optional[
        Literal["slate", "red", "orange", "amber", "lime", "green", "teal", "cyan", "blue", "indigo", "violet", "pink"]
    ] = None

    seed: Union[str, int, None] = None


class AgentProfile(BaseModel):
    """
    Persona of the Agent plus its individual instructions passage; `instructions` is null when none is set.
    """

    avatar_config: Optional[AgentProfileAvatarConfig] = FieldInfo(alias="avatarConfig", default=None)
    """
    Configuration of a `blob` avatar: its seed and optional user-chosen palette
    color. A color-only config retains the default seed fallback.
    """

    avatar_kind: Optional[Literal["blob"]] = FieldInfo(alias="avatarKind", default=None)

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    instructions: Optional[str] = None

    api_model_profile: Optional[str] = FieldInfo(alias="modelProfile", default=None)


class AgentThreadPreview(BaseModel):
    """
    Newest thread excerpt (90 characters), awaits-input and timestamp, from at most 20 newest rows. Null when the thread has no rows.
    """

    awaits_input: bool = FieldInfo(alias="awaitsInput")

    excerpt: Optional[str] = None

    timestamp: Optional[datetime] = None


class Agent(BaseModel):
    """An Agent of the owner: its lifecycle state, profile and runtime."""

    id: str

    archived_at: Optional[str] = FieldInfo(alias="archivedAt", default=None)

    created_at: str = FieldInfo(alias="createdAt")

    disabled_reason: Optional[Literal["owner", "over-limit"]] = FieldInfo(alias="disabledReason", default=None)
    """
    Why a `disabled` Agent is disabled: `owner` chose it, `over-limit` the plan
    grants fewer Agent slots than the owner had enabled. Null while the Agent is not
    disabled.
    """

    error_code: Optional[str] = FieldInfo(alias="errorCode", default=None)
    """Why provisioning failed, null otherwise.

    An open set: new codes can appear. Codes written today: `provision_timeout`,
    `agent_limit_reached`, `provision_failed`; a code the harness reports for a
    failed start is passed through.
    """

    primary: bool
    """
    Whether this is the owner's primary Agent, the one a chat session uses when it
    names no `agentId`.
    """

    profile: AgentProfile
    """
    Persona of the Agent plus its individual instructions passage; `instructions` is
    null when none is set.
    """

    provisioned_at: Optional[str] = FieldInfo(alias="provisionedAt", default=None)
    """
    When provisioning of the Agent completed (ISO 8601); null while a newly created
    Agent is still pending and after its provisioning failed.
    """

    status: Literal["active", "pending", "failed", "archived", "disabled"]
    """`pending`: created but not provisioned yet, it takes no turns.

    `active`: ready for turns. `failed`: provisioning gave up (see `errorCode`); the
    Agent is archived. `archived`: read-only. `disabled`: switched off by the owner
    or because the plan grants fewer Agent slots; it takes no turns and holds no
    slot, and the owner can enable it again while a slot is free.
    """

    thread_preview: Optional[AgentThreadPreview] = FieldInfo(alias="threadPreview", default=None)
    """
    Newest thread excerpt (90 characters), awaits-input and timestamp, from at most
    20 newest rows. Null when the thread has no rows.
    """

    thread_session_id: Optional[str] = FieldInfo(alias="threadSessionId", default=None)
    """
    Active chat on the active machine, pinned first, then session lastActiveAt DESC,
    id DESC. Null for pending/archived Agents or no thread.
    """

    welcome_pending: bool = FieldInfo(alias="welcomePending")
    """
    Whether this active primary Agent is still due its one-time greeting: the
    welcome-back for an adopted primary, or the onboarding greeting for a primary
    whose chat never had a message.
    """

    last_active_at: Optional[str] = FieldInfo(alias="lastActiveAt", default=None)
    """
    Latest activity of the Agent (newest chat session activity or live turn
    heartbeat), ISO 8601; null when it has never been active.
    """

    runtime: Optional[Literal["awake", "sleeping", "waking"]] = None
    """Whether the Agent is running right now, derived from stored state only.

    `waking`: an active start, its machine is provisioning or a restart/rehydrate is
    pending and changed within the last 10 minutes (a timed-out or stalled start
    reads `sleeping`). `awake`: the machine is running and this Agent has been
    started in the current run. `sleeping`: everything else (stopped or parked
    machine, an Agent the running harness has not started yet, or an Agent that is
    not active). `awake` can lag a machine stop until the reconciler converges.
    """


class AgentListResponse(BaseModel):
    agents: List[Agent]
