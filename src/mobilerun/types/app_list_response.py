# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AppListResponse", "Count", "Item", "Pagination"]


class Count(BaseModel):
    available_count: float = FieldInfo(alias="availableCount")

    queued_count: float = FieldInfo(alias="queuedCount")

    store_count: float = FieldInfo(alias="storeCount")

    total_count: float = FieldInfo(alias="totalCount")

    upload_count: float = FieldInfo(alias="uploadCount")


class Item(BaseModel):
    id: str

    category_name: Optional[str] = FieldInfo(alias="categoryName", default=None)

    country: Literal[
        "AF",
        "AL",
        "DZ",
        "AS",
        "AD",
        "AO",
        "AI",
        "AQ",
        "AG",
        "AR",
        "AM",
        "AW",
        "AP",
        "AU",
        "AT",
        "AZ",
        "BS",
        "BH",
        "BD",
        "BB",
        "BY",
        "BE",
        "BZ",
        "BJ",
        "BM",
        "BT",
        "BO",
        "BQ",
        "BA",
        "BW",
        "BV",
        "BR",
        "IO",
        "BN",
        "BG",
        "BF",
        "BI",
        "KH",
        "CM",
        "CA",
        "CV",
        "KY",
        "CF",
        "TD",
        "CL",
        "CN",
        "CX",
        "CC",
        "CO",
        "KM",
        "CG",
        "CD",
        "CK",
        "CR",
        "HR",
        "CU",
        "CW",
        "CY",
        "CZ",
        "CI",
        "DK",
        "DJ",
        "DM",
        "DO",
        "EC",
        "EG",
        "SV",
        "GQ",
        "ER",
        "EE",
        "ET",
        "FK",
        "FO",
        "FJ",
        "FI",
        "FR",
        "GF",
        "PF",
        "TF",
        "GA",
        "GM",
        "GE",
        "DE",
        "GH",
        "GI",
        "GR",
        "GL",
        "GD",
        "GP",
        "GU",
        "GT",
        "GG",
        "GN",
        "GW",
        "GY",
        "HT",
        "HM",
        "VA",
        "HN",
        "HK",
        "HU",
        "IS",
        "IN",
        "ID",
        "IR",
        "IQ",
        "IE",
        "IM",
        "IL",
        "IT",
        "JM",
        "JP",
        "JE",
        "JO",
        "KZ",
        "KE",
        "KI",
        "KR",
        "KW",
        "KG",
        "LA",
        "LV",
        "LB",
        "LS",
        "LR",
        "LY",
        "LI",
        "LT",
        "LU",
        "MO",
        "MG",
        "MW",
        "MY",
        "MV",
        "ML",
        "MT",
        "MH",
        "MQ",
        "MR",
        "MU",
        "YT",
        "MX",
        "FM",
        "MD",
        "MC",
        "MN",
        "ME",
        "MS",
        "MA",
        "MZ",
        "MM",
        "NA",
        "NR",
        "NP",
        "NL",
        "AN",
        "NC",
        "NZ",
        "NI",
        "NE",
        "NG",
        "NU",
        "NF",
        "KP",
        "MK",
        "MP",
        "NO",
        "OM",
        "PK",
        "PW",
        "PS",
        "PA",
        "PG",
        "PY",
        "PE",
        "PH",
        "PN",
        "PL",
        "PT",
        "PR",
        "QA",
        "RE",
        "RO",
        "RU",
        "RW",
        "BL",
        "SH",
        "KN",
        "LC",
        "MF",
        "PM",
        "VC",
        "WS",
        "SM",
        "ST",
        "SA",
        "SN",
        "RS",
        "CS",
        "SC",
        "SL",
        "SG",
        "SX",
        "SK",
        "SI",
        "SB",
        "SO",
        "ZA",
        "GS",
        "SS",
        "ES",
        "LK",
        "SD",
        "SR",
        "SJ",
        "SZ",
        "SE",
        "CH",
        "SY",
        "TW",
        "TJ",
        "TZ",
        "TH",
        "TL",
        "TG",
        "TK",
        "TO",
        "TT",
        "TN",
        "TR",
        "TM",
        "TC",
        "TV",
        "UG",
        "UA",
        "AE",
        "GB",
        "US",
        "UM",
        "UY",
        "UZ",
        "VU",
        "VE",
        "VN",
        "VG",
        "VI",
        "WF",
        "EH",
        "YE",
        "ZM",
        "ZW",
        "AX",
    ]

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    developer_name: Optional[str] = FieldInfo(alias="developerName", default=None)

    display_name: str = FieldInfo(alias="displayName")

    expected_files: Union[str, float, bool, Dict[str, Optional[object]], List[Optional[object]], None] = FieldInfo(
        alias="expectedFiles", default=None
    )

    icon_url: str = FieldInfo(alias="iconURL")

    package_name: str = FieldInfo(alias="packageName")

    privacy_policy_url: Optional[str] = FieldInfo(alias="privacyPolicyUrl", default=None)

    queued_at: Optional[datetime] = FieldInfo(alias="queuedAt", default=None)

    rating_count: Optional[int] = FieldInfo(alias="ratingCount", default=None)

    rating_score: Optional[str] = FieldInfo(alias="ratingScore", default=None)

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)

    source: Literal["uploaded", "store"]

    status: Literal["queued", "available", "failed"]

    stealth_tier: Optional[Literal["tier1", "tier2", "tier3"]] = FieldInfo(alias="stealthTier", default=None)

    target_sdk: Optional[int] = FieldInfo(alias="targetSdk", default=None)

    type: Literal["android", "ios"]

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    version_code: int = FieldInfo(alias="versionCode")

    version_name: str = FieldInfo(alias="versionName")


class Pagination(BaseModel):
    has_next: bool = FieldInfo(alias="hasNext")

    has_prev: bool = FieldInfo(alias="hasPrev")

    page: int

    pages: int

    page_size: int = FieldInfo(alias="pageSize")

    total: int


class AppListResponse(BaseModel):
    count: Count

    items: List[Item]

    pagination: Pagination
