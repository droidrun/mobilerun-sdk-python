# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from pydantic import Field as FieldInfo

from typing import Optional

__all__ = ["DeviceRetrieveCapabilitiesResponse", "Capabilities"]

class Capabilities(BaseModel):
    accessibility: bool

    agent: bool

    apps: bool

    browser: bool

    camera_injection: bool = FieldInfo(alias = "cameraInjection")

    esim: bool

    files: bool

    fingerprint: bool

    frida: bool

    geo: bool

    human_touch: bool = FieldInfo(alias = "humanTouch")

    language: bool

    logcat: bool

    microphone_injection: bool = FieldInfo(alias = "microphoneInjection")

    proxy: bool

    reset: bool

    shell: bool

    spoofing: bool

    stop: bool

    stream: bool

    time: bool

class DeviceRetrieveCapabilitiesResponse(BaseModel):
    capabilities: Capabilities

    device_type: str = FieldInfo(alias = "deviceType")

    schema_: Optional[str] = FieldInfo(alias = "$schema", default = None)
    """A URL to the JSON Schema for this object."""