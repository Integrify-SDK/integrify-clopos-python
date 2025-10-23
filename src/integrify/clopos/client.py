from typing import TYPE_CHECKING, Optional

from integrify.api import APIClient
from integrify.clopos import env
from integrify.clopos.handlers import (
    AuthHandler,
    CreateOrderHandler,
    CreateReceiptHandler,
    DeleteReceiptHandler,
    GetByIDHandler,
    GetCategoriesHandler,
    GetCategoryByIDHandler,
    GetOrderByIDHandler,
    GetOrdersHandler,
    GetPaginatedDataHandler,
    GetProductsHandler,
    GetStationsHandler,
)
from integrify.clopos.schemas.objects.main import (
    Category,
    Customer,
    Group,
    Order,
    PaymentMethod,
    Product,
    Receipt,
    SaleType,
    Station,
    User,
    Venue,
)
from integrify.clopos.schemas.response import (
    AuthResponse,
    BaseResponse,
    ObjectListResponse,
    ObjectResponse,
)
from integrify.schemas import APIResponse
from integrify.utils import UNSET, Unset

__all__ = ['CloposClientClass', 'CloposRequest', 'CloposAsyncRequest']


class CloposClientClass(APIClient):
    """Base class for CloposClient"""

    def __init__(
        self,
        name='Clopos',
        base_url: Optional[str] = env.API.BASE_URL,
        default_handler=None,
        sync: bool = True,
        dry: bool = False,
    ):
        super().__init__(name, base_url, default_handler, sync, dry)

        self.add_url('auth', env.API.AUTH, verb='POST')
        self.add_handler('auth', AuthHandler)

        self.add_url('get_venues', env.API.VENUES, verb='GET')
        self.add_handler('get_venues', GetPaginatedDataHandler(Venue))

        self.add_url('get_users', env.API.USERS, verb='GET')
        self.add_handler('get_users', GetPaginatedDataHandler(User))
        self.add_url('get_user_by_id', env.API.USER_BY_ID, verb='GET')
        self.add_handler('get_user_by_id', GetByIDHandler(User))

        self.add_url('get_customers', env.API.CUSTOMERS, verb='GET')
        self.add_handler('get_customers', GetPaginatedDataHandler(Customer))
        self.add_url('get_customer_by_id', env.API.CUSTOMER_BY_ID, verb='GET')
        self.add_handler('get_customer_by_id', GetByIDHandler(Customer))
        self.add_url('get_customer_groups', env.API.CUSTOMER_GROUPS, verb='GET')
        self.add_handler('get_customer_groups', GetPaginatedDataHandler(Group))

        self.add_url('get_categories', env.API.CATEGORIES, verb='GET')
        self.add_handler('get_categories', GetCategoriesHandler)
        self.add_url('get_category_by_id', env.API.CATEGORY_BY_ID, verb='GET')
        self.add_handler('get_category_by_id', GetCategoryByIDHandler)

        self.add_url('get_stations', env.API.STATIONS, verb='GET')
        self.add_handler('get_stations', GetStationsHandler)
        self.add_url('get_station_by_id', env.API.STATION_BY_ID, verb='GET')
        self.add_handler('get_station_by_id', GetByIDHandler(Station))

        self.add_url('get_products', env.API.PRODUCTS, verb='GET')
        self.add_handler('get_products', GetProductsHandler)
        self.add_url('get_product_by_id', env.API.PRODUCT_BY_ID, verb='GET')
        self.add_handler('get_product_by_id', GetByIDHandler(Product))

        self.add_url('get_sale_types', env.API.SALE_TYPES, verb='GET')
        self.add_handler('get_sale_types', GetPaginatedDataHandler(SaleType))
        self.add_url('get_payment_methods', env.API.PAYMENT_METHODS, verb='GET')
        self.add_handler('get_payment_methods', GetPaginatedDataHandler(PaymentMethod))

        self.add_url('get_orders', env.API.ORDERS, verb='GET')
        self.add_handler('get_orders', GetOrdersHandler)
        self.add_url('get_order_by_id', env.API.ORDER_BY_ID, verb='GET')
        self.add_handler('get_order_by_id', GetOrderByIDHandler)
        self.add_url('create_order', env.API.ORDERS, verb='POST')
        self.add_handler('create_order', CreateOrderHandler)

        self.add_url('get_receipts', env.API.RECEIPTS, verb='GET')
        self.add_handler('get_receipts', GetPaginatedDataHandler(Receipt))
        self.add_url('get_receipt_by_id', env.API.RECEIPT_BY_ID, verb='GET')
        self.add_handler('get_receipt_by_id', GetByIDHandler(Receipt))
        self.add_url('create_receipt', env.API.RECEIPTS, verb='POST')
        self.add_handler('create_receipt', CreateReceiptHandler)
        self.add_url('delete_receipt', env.API.RECEIPT_BY_ID, verb='DELETE')
        self.add_handler('delete_receipt', DeleteReceiptHandler)

    if TYPE_CHECKING:
        # pylint: disable=all
        def auth(
            self,
            client_id: Unset[str] = UNSET,
            client_secret: Unset[str] = UNSET,
            brand: Unset[str] = UNSET,
            venue_id: Unset[str] = UNSET,
        ) -> APIResponse[AuthResponse]: ...

        def get_venues(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[Venue]]: ...

        def get_users(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[User]]: ...

        def get_user_by_id(
            self,
            id: int,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectResponse[User]]: ...

        def get_customers(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[Customer]]: ...

        def get_customer_by_id(
            self,
            id: int,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectResponse[Customer]]: ...

        def get_customer_groups(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[Group]]: ...

        def get_categories(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[Category]]: ...

        def get_category_by_id(
            self,
            id: int,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectResponse[Category]]: ...

        def get_stations(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[Station]]: ...

        def get_station_by_id(
            self,
            id: int,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectResponse[Station]]: ...

        def get_products(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[Product]]: ...

        def get_product_by_id(
            self,
            id: int,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectResponse[Product]]: ...

        def get_sale_types(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[SaleType]]: ...

        def get_payment_methods(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[PaymentMethod]]: ...

        def get_orders(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[Order]]: ...

        def get_order_by_id(
            self,
            id: int,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectResponse[Order]]: ...

        def create_order(
            self,
            # order: Order,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectResponse[Order]]: ...

        def get_receipts(
            self,
            page: Unset[int] = UNSET,
            limit: Unset[int] = UNSET,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectListResponse[Receipt]]: ...

        def get_receipt_by_id(
            self,
            id: int,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectResponse[Receipt]]: ...

        def create_receipt(
            self,
            # receipt: Receipt,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[ObjectResponse[Receipt]]: ...

        def delete_receipt(
            self,
            id: int,
            headers: Unset[dict[str, str]] = UNSET,
        ) -> APIResponse[BaseResponse]: ...


CloposRequest = CloposClientClass(sync=True)
CloposAsyncRequest = CloposClientClass(sync=False)
