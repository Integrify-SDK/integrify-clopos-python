from decimal import Decimal

from pydantic import Field, model_serializer

from integrify.api import PayloadBaseModel
from integrify.clopos import env
from integrify.clopos.helpers import IsoDateTime
from integrify.clopos.schemas.enums import CategoryType, DiscountType, OrderStatus, ProductType
from integrify.clopos.schemas.objects.input import PaymentMethodIn
from integrify.clopos.schemas.objects.sub import LineItem
from integrify.utils import UnsetField, UnsetOrNoneField


class AuthRequest(PayloadBaseModel):
    client_id: str = Field(default=env.CLOPOS_CLIENT_ID, min_length=1, validate_default=True)
    client_secret: str = Field(
        default=env.CLOPOS_CLIENT_SECRET,
        min_length=1,
        validate_default=True,
    )
    brand: str = Field(default=env.CLOPOS_BRAND, min_length=1, validate_default=True)
    venue_id: str = Field(default=env.CLOPOS_VENUE_ID, min_length=1, validate_default=True)


class GetByIDRequest(PayloadBaseModel):
    URL_PARAM_FIELDS = {'id'}
    id: int


class GetPaginatedDataRequest(PayloadBaseModel):
    page: UnsetField[int]
    limit: UnsetField[int]


class GetCustomersRequest(GetPaginatedDataRequest):
    search: UnsetField[str]


class GetCategoriesRequest(GetPaginatedDataRequest):
    parent_id: UnsetField[int]
    type: UnsetField[CategoryType]
    include_children: UnsetField[bool]
    include_inactive: UnsetField[bool]


class GetCategoryByIDRequest(GetByIDRequest):
    include_children: UnsetField[bool]


class GetStationsRequest(GetPaginatedDataRequest):
    status: UnsetField[int]
    can_print: UnsetField[bool]


class GetProductsRequest(GetPaginatedDataRequest):
    type: UnsetField[list[ProductType]]
    """Filters by product type. Possible values: GOODS, DISH, TIMER, PREPARATION, INGREDIENT"""

    category_id: UnsetField[list[int]]
    """Lists products belonging to the specified category IDs"""

    station_id: UnsetField[list[int]]
    """Retrieves products assigned to the specified station IDs"""

    tags: UnsetField[list[int]]
    """Filters for products with the specified tag IDs"""

    giftable: UnsetField[str]
    """Filters for products that are ("1") or are not giftable"""

    discountable: UnsetField[str]
    """Filters for products that are ("1") or are not discountable"""

    inventory_behavior: UnsetField[str]
    """Filters by inventory behavior mode (e.g., "3")"""

    have_ingredients: UnsetField[str]
    """Retrieves products that have a recipe/ingredients ("1")"""

    sold_by_portion: UnsetField[str]
    """Lists products sold by portion ("1")"""

    has_variants: UnsetField[str]
    """Lists products that have variants (`modifications`) ("1")"""

    has_modifiers: UnsetField[str]
    """Lists products that have modifier group (`modificator_groups`) ("1")"""

    has_barcode: UnsetField[str]
    """Retrieves products that have a barcode ("1")"""

    has_service_charge: UnsetField[str]
    """Lists products to which a service charge applies ("1")"""

    @model_serializer(mode='wrap')
    def serialize_model(self, serializer) -> dict:
        """Model serializer"""

        data = serializer(self)

        # Transform to [field_name, value] format
        result = {}
        for key, value in data.items():
            if value is not None:  # Only include non-None values
                result[key] = [key, value]

        return {'filters': result}


class GetOrdersRequest(GetPaginatedDataRequest):
    status: UnsetField[OrderStatus]


class CreateOrderRequest(PayloadBaseModel):
    customer_id: str
    """Customer identifier"""

    line_items: list[LineItem]
    """List of order items"""


class UpdateOrderRequest(GetByIDRequest):
    status: OrderStatus


class GetReceiptsRequest(GetPaginatedDataRequest):
    sort_by: UnsetField[str]
    sort_order: UnsetField[int]
    date_from: UnsetField[IsoDateTime]
    date_to: UnsetField[IsoDateTime]


class CreateReceiptRequest(PayloadBaseModel):
    cid: str
    payment_methods: list[PaymentMethodIn]
    user_id: int
    by_cash: UnsetField[Decimal]
    by_card: UnsetField[Decimal]
    customer_discount_type: UnsetField[DiscountType]
    discount_rate: UnsetField[Decimal]
    discount_value: UnsetField[Decimal]
    delivery_fee: UnsetField[Decimal]
    created_at: UnsetField[int]
    closed_at: UnsetField[int]
    address: UnsetField[str]
    courier_id: UnsetOrNoneField[int]
