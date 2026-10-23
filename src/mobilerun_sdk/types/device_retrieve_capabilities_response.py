# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DeviceRetrieveCapabilitiesResponse", "Capabilities"]


class Capabilities(BaseModel):
    accessibility: bool

    agent: bool

    apps: bool

    browser: bool

    camera_injection: bool = FieldInfo(alias="cameraInjection")

    clipboard: bool

    esim: bool

    factory_reset: bool = FieldInfo(alias="factoryReset")

    files: bool

    fingerprint: bool

    frida: bool

    geo: bool

    human_touch: bool = FieldInfo(alias="humanTouch")

    identity_reset: bool = FieldInfo(alias="identityReset")

    language: bool

    logcat: bool

    microphone_injection: bool = FieldInfo(alias="microphoneInjection")

    proxy: bool

    recording: bool

    reset: bool

    shell: bool

    spoofing: bool

    stop: bool

    stream: bool

    time: bool

    traffic_inspection: bool = FieldInfo(alias="trafficInspection")

    media_injection_transport: Optional[Literal["direct"]] = FieldInfo(alias="mediaInjectionTransport", default=None)


class DeviceRetrieveCapabilitiesResponse(BaseModel):
    capabilities: Capabilities

    device_type: str = FieldInfo(alias="deviceType")

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
