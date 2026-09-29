# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["TriggerFireParams"]


class TriggerFireParams(TypedDict, total=False):
    payload: Required[Dict[str, object]]
    """Arbitrary JSON object forwarded to every flow attached to this trigger.

    Validated against the trigger's customPayloadSchema when one is configured;
    otherwise only "must be a JSON object" is enforced.
    """
