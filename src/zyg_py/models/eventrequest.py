"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from zyg_py.types import BaseModel


class CustomerTypedDict(TypedDict):
    customer_id: str
    r"""Internal customer ID"""
    external_id: NotRequired[str]
    r"""External system ID, if applicable"""
    email: NotRequired[str]
    r"""Email address of the customer"""


class Customer(BaseModel):
    customer_id: Annotated[str, pydantic.Field(alias="customerId")]
    r"""Internal customer ID"""

    external_id: Annotated[Optional[str], pydantic.Field(alias="externalId")] = None
    r"""External system ID, if applicable"""

    email: Optional[str] = None
    r"""Email address of the customer"""


class Severity(str, Enum):
    r"""The severity of the event"""

    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class EventRequestTypedDict(TypedDict):
    event: str
    r"""The type of the event, e.g., 'Billing Issue'"""
    body: str
    r"""Detailed information about the event."""
    customer: CustomerTypedDict
    notify: bool
    r"""Whether or not to notify the customer or support team"""
    severity: NotRequired[Severity]
    r"""The severity of the event"""
    timestamp: NotRequired[datetime]
    r"""Optional timestamp of when the event occurred. If not provided, the server will generate one."""


class EventRequest(BaseModel):
    event: str
    r"""The type of the event, e.g., 'Billing Issue'"""

    body: str
    r"""Detailed information about the event."""

    customer: Customer

    notify: bool
    r"""Whether or not to notify the customer or support team"""

    severity: Optional[Severity] = Severity.INFO
    r"""The severity of the event"""

    timestamp: Optional[datetime] = None
    r"""Optional timestamp of when the event occurred. If not provided, the server will generate one."""
