from typing import Optional

from pydantic import Field, model_serializer

from integrify.api import PayloadBaseModel
from integrify.clopos import env
from integrify.clopos.schemas.enums import CategoryType, ProductType
from integrify.clopos.schemas.objects.sub import LineItem


class AuthRequest(PayloadBaseModel):
    client_id: str = Field(default=env.CLOPOS_CLIENT_ID, min_length=1, validate_default=True)
    client_secret: str = Field(
        default=env.CLOPOS_CLIENT_SECRET,
        min_length=1,
        validate_default=True,
    )
    brand: str = Field(default=env.CLOPOS_BRAND, validate_default=True)
    venue_id: str = Field(default=env.CLOPOS_VENUE_ID, validate_default=True)


class GetByIDRequest(PayloadBaseModel):
    URL_PARAM_FIELDS = {'id'}
    id: int


class GetPaginatedDataRequest(PayloadBaseModel):
    page: Optional[int] = None
    limit: Optional[int] = None
    search: Optional[str] = None


class GetCategoriesRequest(PayloadBaseModel):
    page: Optional[int] = None
    limit: Optional[int] = None
    parent_id: Optional[int] = None
    type: Optional[CategoryType] = None
    include_children: Optional[bool] = True
    include_inactive: Optional[bool] = False


class GetCategoryByIDRequest(GetByIDRequest):
    include_children: Optional[bool] = True


class GetStationsRequest(GetPaginatedDataRequest):
    status: Optional[int] = None
    can_print: Optional[bool] = None


class GetProductsRequest(GetPaginatedDataRequest):
    type: Optional[list[ProductType]] = None
    """Filters by product type. Possible values: GOODS, DISH, TIMER, PREPARATION, INGREDIENT"""

    category_id: Optional[list[int]] = None
    """Lists products belonging to the specified category IDs"""

    station_id: Optional[list[int]] = None
    """Retrieves products assigned to the specified station IDs"""

    tags: Optional[list[int]] = None
    """Filters for products with the specified tag IDs"""

    giftable: Optional[str] = None
    """Filters for products that are ("1") or are not giftable"""

    discountable: Optional[str] = None
    """Filters for products that are ("1") or are not discountable"""

    inventory_behavior: Optional[str] = None
    """Filters by inventory behavior mode (e.g., "3")"""

    have_ingredients: Optional[str] = Field(None, serialization_alias='haveIngredients')
    """Retrieves products that have a recipe/ingredients ("1")"""

    sold_by_portion: Optional[str] = None
    """Lists products sold by portion ("1")"""

    has_variants: Optional[str] = None
    """Lists products that have variants (`modifications`) ("1")"""

    has_modifiers: Optional[str] = None
    """Lists products that have modifier group (`modificator_groups`) ("1")"""

    has_barcode: Optional[str] = None
    """Retrieves products that have a barcode ("1")"""

    has_service_charge: Optional[str] = None
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


class CreateOrderRequest(PayloadBaseModel):
    customer_id: str
    """Customer identifier"""

    line_items: list[LineItem]
    """List of order items"""
