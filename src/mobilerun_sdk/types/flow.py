# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Flow"]


class Flow(BaseModel):
    id: str

    blocked_at: Optional[str] = FieldInfo(alias="blockedAt", default=None)

    consecutive_failures: int = FieldInfo(alias="consecutiveFailures")

    cooldown_scope: Literal["flow", "device"] = FieldInfo(alias="cooldownScope")

    cooldown_seconds: Optional[int] = FieldInfo(alias="cooldownSeconds", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    description: Optional[str] = None

    device_ids: List[str] = FieldInfo(alias="deviceIds")

    enabled: bool

    health_monitoring_enabled: bool = FieldInfo(alias="healthMonitoringEnabled")

    last_failure_at: Optional[str] = FieldInfo(alias="lastFailureAt", default=None)

    last_failure_code: Optional[
        Literal["device_not_found", "permission_denied", "client_error", "transient", "logic", "invalid_config"]
    ] = FieldInfo(alias="lastFailureCode", default=None)

    last_triggered_at: Optional[str] = FieldInfo(alias="lastTriggeredAt", default=None)

    name: str

    notify_on_failure: bool = FieldInfo(alias="notifyOnFailure")

    notify_on_success: bool = FieldInfo(alias="notifyOnSuccess")

    notify_webhook_id: Optional[str] = FieldInfo(alias="notifyWebhookId", default=None)

    owner_id: str = FieldInfo(alias="ownerId")

    self_healing_enabled: bool = FieldInfo(alias="selfHealingEnabled")

    self_healing_max_attempts: int = FieldInfo(alias="selfHealingMaxAttempts")

    status: Literal["healthy", "failing", "blocked"]

    template_resolution_version: int = FieldInfo(alias="templateResolutionVersion")
    """Template-resolver semantics this flow runs under (MVA-23).

    1 = legacy (missing/forbidden/null all resolve to ''). 2 = typed
    (missing/forbidden throw, a whole-token null stays JSON null). Existing flows
    stay 1; new flows default to 2.
    """

    trigger_id: str = FieldInfo(alias="triggerId")

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")
    """Deprecated: use ownerId (tenancy) / createdBy (actor)."""
