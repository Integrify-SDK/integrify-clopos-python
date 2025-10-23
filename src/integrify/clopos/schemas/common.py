from decimal import Decimal
from typing import Union

from integrify.api import PayloadBaseModel
from integrify.clopos.helpers import IsoDateTime
from integrify.clopos.schemas.objects.input import PaymentMethodIn, ReceiptProductIn
from integrify.utils import UnsetOrNoneField


class CreateReceiptReqResp(PayloadBaseModel):
    cid: str
    payment_methods: list[PaymentMethodIn]
    subtotal: Decimal
    total: Decimal
    user_id: int
    closed_at: IsoDateTime = None
    created_at: IsoDateTime = None
    customer_discount_type: UnsetOrNoneField[int] = None
    delivery_fee: UnsetOrNoneField[Decimal] = None
    description: UnsetOrNoneField[str] = None
    discount_rate: UnsetOrNoneField[Decimal] = None
    discount_type: UnsetOrNoneField[int] = None
    discount_value: UnsetOrNoneField[Decimal] = None
    e_tax: UnsetOrNoneField[Decimal] = None
    gif_total: UnsetOrNoneField[Decimal] = None
    guests: UnsetOrNoneField[int] = None
    i_tax: UnsetOrNoneField[Decimal] = None
    local_status: UnsetOrNoneField[int] = None
    meta: UnsetOrNoneField[dict] = None
    original_subtotal: UnsetOrNoneField[Decimal] = None
    printed: UnsetOrNoneField[bool] = None
    receipt_products: UnsetOrNoneField[list[ReceiptProductIn]] = None
    remaining: UnsetOrNoneField[Union[Decimal, str]] = None
    rps_discount: UnsetOrNoneField[Decimal] = None
    sale_type_id: UnsetOrNoneField[int] = None
    service_charge: UnsetOrNoneField[Decimal] = None
    service_charge_value: UnsetOrNoneField[Decimal] = None
    service_notification_id: UnsetOrNoneField[int] = None
    status: UnsetOrNoneField[int] = None
    terminal_id: UnsetOrNoneField[int] = None
    total_tax: UnsetOrNoneField[Decimal] = None
    deleted_at: IsoDateTime = None
    updated_at: IsoDateTime = None
