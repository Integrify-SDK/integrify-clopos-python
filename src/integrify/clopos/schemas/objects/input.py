from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from integrify.clopos.helpers import IsoDateTime


class PaymentMethodIn(BaseModel):
    id: int
    """The unique identifier for the payment method"""

    name: str
    """The name of the payment method (e.g., "Cash", "Card")"""

    amount: Decimal
    """The amount of the payment method"""


class ReceiptProductIn(BaseModel):
    id: int
    """The unique identifier for the receipt product"""

    cid: str
    """The CID of the receipt product"""

    product_id: int
    """The ID of the product associated with the receipt product"""

    receipt_id: int
    """The ID of the receipt associated with the receipt product"""

    product_hash: str
    """The hash of the product associated with the receipt product"""

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

    cost: Decimal
    """The cost of the receipt product"""

    is_gift: bool
    """Whether the receipt product is a gift"""

    preprint_count: int
    """The preprint count of the receipt product"""

    station_printed_count: int
    """The station printed count of the receipt product"""

    station_aborted_count: int
    """The station aborted count of the receipt product"""

    seller_id: int
    """The ID of the seller associated with the receipt product"""

    loyalty_type: Optional[str]
    """The loyalty type of the receipt product"""

    loyalty_value: Optional[Decimal]
    """The loyalty value of the receipt product"""

    discount_rate: Decimal
    """The discount rate of the receipt product"""

    discount_value: Decimal
    """The discount value of the receipt product"""

    discount_type: Decimal
    """The discount type of the receipt product"""

    total_discount: Decimal
    """The total discount of the receipt product"""

    subtotal: Decimal
    """The subtotal of the receipt product"""

    receipt_discount: Decimal
    """The receipt discount of the receipt product"""

    created_at: IsoDateTime
    """The created at of the receipt product"""

    updated_at: IsoDateTime
    """The updated at of the receipt product"""

    terminal_updated_at: IsoDateTime
    """The terminal updated at of the receipt product"""

    deleted_at: IsoDateTime
    """The deleted at of the receipt product"""

    receipt_product_modificators: list
    """The receipt product modificators of the receipt product"""

    taxes: list
    """The taxes of the receipt product"""
