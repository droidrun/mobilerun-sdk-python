# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["RecordingStartParams"]


class RecordingStartParams(TypedDict, total=False):
    name: str

    quality: int
    """Capture quality from 1 (lowest) to 10 (full stream quality).

    Defaults to the device's full quality. Honored by devices recording through the
    portal stream bridge.
    """

    retention_days: Annotated[int, PropertyInfo(alias="retentionDays")]

    types: Optional[SequenceNotStr[str]]
    """
    Artifacts to capture: trajectory (input actions; on portal stream-bridge devices
    only when the handset announces trajectory capture), video, and audio (captured
    into the video artifact, so it requires video; honored by portal stream-bridge
    recorders). Defaults to trajectory and video, narrowed to what the device
    produces.
    """
