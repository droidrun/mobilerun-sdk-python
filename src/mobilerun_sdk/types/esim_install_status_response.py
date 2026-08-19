# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from pydantic import Field as FieldInfo

from datetime import datetime

from typing_extensions import Literal

__all__ = ["EsimInstallStatusResponse", "Data", "DataEsim"]

class DataEsim(BaseModel):
    id: str

    carrier_name: Optional[str] = FieldInfo(alias = "carrierName", default = None)

    country_code: Optional[str] = FieldInfo(alias = "countryCode", default = None)

    created_at: Optional[datetime] = FieldInfo(alias = "createdAt", default = None)

    created_by: Optional[str] = FieldInfo(alias = "createdBy", default = None)

    device_id: Optional[str] = FieldInfo(alias = "deviceId", default = None)

    device_uuid: Optional[str] = FieldInfo(alias = "deviceUuid", default = None)

    iccid: Optional[str] = None

    msisdn: Optional[str] = None

    name: Optional[str] = None

    network_status: Optional[Literal["degraded"]] = FieldInfo(alias = "networkStatus", default = None)

    source: Literal["stocked", "byo"]

    status: Literal["in_stock", "owned", "installing", "installed", "install_failed", "retired"]

    subscription_id: Optional[int] = FieldInfo(alias = "subscriptionId", default = None)

    updated_at: Optional[datetime] = FieldInfo(alias = "updatedAt", default = None)

    cancellation_scheduled: Optional[bool] = FieldInfo(alias = "cancellationScheduled", default = None)

    checkout_url: Optional[str] = FieldInfo(alias = "checkoutUrl", default = None)

    current_period_end: Optional[datetime] = FieldInfo(alias = "currentPeriodEnd", default = None)

    exempt: Optional[bool] = None

    rent_status: Optional[Literal["not_applicable", "exempt", "inactive", "awaiting_payment", "active", "cancel_pending", "refund_pending", "retiring", "billing_error"]] = FieldInfo(alias = "rentStatus", default = None)

class Data(BaseModel):
    esim: DataEsim

    operation_id: Optional[str] = FieldInfo(alias = "operationId", default = None)

    status: Optional[Literal["installing", "pending_download", "downloading", "downloaded", "enabling", "configuring_apn", "active", "download_failed", "enable_failed", "download_outcome_unknown", "install_failed", "physical_removal_unconfirmed", "deleted"]] = None

class EsimInstallStatusResponse(BaseModel):
    data: Data