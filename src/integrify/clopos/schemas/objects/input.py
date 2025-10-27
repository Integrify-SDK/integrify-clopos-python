from decimal import Decimal

from pydantic import BaseModel

from integrify.clopos.helpers import IsoDateTime
from integrify.utils import UnsetField, UnsetOrNoneField


class PaymentMethodIn(BaseModel):
    id: int
    """The unique identifier for the payment method"""

    name: str
    """The name of the payment method (e.g., "Cash", "Card")"""

    amount: Decimal
    """The amount of the payment method"""


class ServiceIn(BaseModel):
    sale_type_id: int
    sale_type_name: str
    venue_id: int
    venue_name: str


class CustomerIn(BaseModel):
    id: int
    name: str
    customer_discount_type: UnsetField[int] = None
    phone: UnsetField[str] = None
    address: UnsetOrNoneField[str]


class ProductIn(BaseModel):
    product_id: int
    count: int
    product_modificators: UnsetOrNoneField[list[dict]]
    meta: UnsetOrNoneField[dict]


class OrderPayloadIn(BaseModel):
    service: ServiceIn
    customer: CustomerIn
    products: list[ProductIn]
    meta: UnsetOrNoneField[dict]


class ReceiptProductIn(BaseModel):
    model_config = {'extra': 'allow'}

    id: UnsetField[int]
    """The unique identifier for the receipt product"""

    cid: str
    """The CID of the receipt product"""

    product_id: int
    """The ID of the product associated with the receipt product"""

    meta: dict
    """The meta data of the receipt product"""

    count: int
    """The count of the receipt product"""

    portion_size: Decimal
    """The portion size of the receipt product"""

    total: Decimal
    """The total of the receipt product"""

    price: Decimal
    """The price of the receipt product"""

    cost: UnsetField[Decimal]
    """The cost of the receipt product"""

    is_gift: bool
    """Whether the receipt product is a gift"""

    created_at: UnsetField[IsoDateTime]
    """The created at of the receipt product"""

    updated_at: UnsetField[IsoDateTime]
    """The updated at of the receipt product"""

    terminal_updated_at: UnsetField[IsoDateTime]
    """The terminal updated at of the receipt product"""

    deleted_at: UnsetField[IsoDateTime]
    """The deleted at of the receipt product"""
