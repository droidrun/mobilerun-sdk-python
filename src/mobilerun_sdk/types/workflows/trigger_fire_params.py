# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TriggerFireParams"]


class TriggerFireParams(TypedDict, total=False):
    payload: Required[Dict[str, object]]
    """Arbitrary JSON object forwarded to every flow attached to this trigger.

    Validated against the trigger's customPayloadSchema when one is configured;
    otherwise only "must be a JSON object" is enforced.
    """

    invocation_id: Annotated[str, PropertyInfo(alias="invocationId")]
    """Optional client-supplied idempotency key.

    When provided, a flow that already has an execution for this (flow,
    invocationId) is skipped and `deduplicated` is true. When omitted a fresh
    server-side id is generated (no dedup).
    """
