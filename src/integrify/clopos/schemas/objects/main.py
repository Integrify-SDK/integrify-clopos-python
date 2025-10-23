from decimal import Decimal
from typing import Union

from pydantic import BaseModel, Field

from integrify.clopos.schemas.enums import CategoryType, OrderStatus, ProductType
from integrify.clopos.schemas.objects.sub import (
    Balance,
    Image,
    Media,
    ModifierGroup,
    OrderItem,
    Package,
    Payload,
    Price,
    ReceiptPaymentMethod,
    Recipe,
    Tax,
    TimerSetting,
    Timestamp,
    Variant,
)
from integrify.utils import UnsetOrNoneField


class Venue(BaseModel):
    id: int
    """Branch ID"""

    name: str
    """Branch name"""

    address: UnsetOrNoneField[str]
    """Branch address"""

    status: UnsetOrNoneField[int]
    """1 = active, 0 = inactive"""

    phone: UnsetOrNoneField[str]
    """Contact number"""

    email: UnsetOrNoneField[str]
    """Contact email"""

    media: list[str] = []
    """Media URLs"""


class User(Timestamp):
    id: int
    """Unique user identifier"""

    email: UnsetOrNoneField[str]
    """Email address associated with the user"""

    username: str
    """Display name shown in the POS"""

    first_name: UnsetOrNoneField[str]
    """First name of the user"""

    last_name: UnsetOrNoneField[str]
    """last name of the user"""

    pin: str
    """POS PIN code"""

    card: UnsetOrNoneField[str]
    """POS card number"""

    mobile_number: UnsetOrNoneField[str]
    """Mobile number of the user"""

    owner: int
    """1 if the user owns the brand, otherwise 0"""

    hide: int
    """1 if hidden from POS selection, otherwise 0"""

    salary: UnsetOrNoneField[int]
    """Salary of the user"""

    barcode: UnsetOrNoneField[str]
    """POS barcode number"""

    tip_message: UnsetOrNoneField[str]
    """Tip message shown in the POS"""

    can_receive_tips: UnsetOrNoneField[bool]
    """Whether the user can receive tips or not"""

    login_at: UnsetOrNoneField[str]
    """Timestamp when the user logged in"""

    status: bool
    """Indicates whether the user account is active"""

    bonus_balance_id: UnsetOrNoneField[int]
    """Balance ID of the user"""

    properties: UnsetOrNoneField[Union[dict, list]]
    """User properties"""

    image: UnsetOrNoneField[list[str]]
    """User images"""


class Group(Timestamp):
    id: int
    """The unique identifier for the customer group"""

    name: str
    """The name of the customer group"""

    discount_type: UnsetOrNoneField[str]
    """The type of discount applied to the customer group"""

    discount_value: int
    """The discount applied to the customer group"""

    system_type: str
    """The system type of the customer group"""


class Customer(Timestamp):
    id: int
    """The unique identifier for the customer"""

    venue_id: int
    """The ID of the venue the customer belongs to"""

    cid: str
    """The unique identifier for the customer in the POS"""

    group_id: int
    """The ID of the customer group they belong to"""

    group: UnsetOrNoneField[Group]
    """An object containing details of the customer's group"""

    balance_id: int
    """The balance ID of the customer"""

    name: str
    """The name of the customer"""

    discount: int
    """The discount applied to the customer"""

    email: UnsetOrNoneField[str]
    """The email address of the customer"""

    phone: UnsetOrNoneField[str]
    """The primary phone number of the customer"""

    phones: list[str] = []
    """An array of the customer's phone numbers"""

    address: UnsetOrNoneField[str]
    """The address of the customer"""

    addresses: list[str] = []
    """An array of the customer's saved addresses"""

    description: UnsetOrNoneField[str]
    """The description of the customer"""

    address_data: UnsetOrNoneField[list[str]]
    """The customer's address data"""

    bonus_balance_id: UnsetOrNoneField[int]
    """The ID of the customer's bonus balance"""

    balance: UnsetOrNoneField[Balance]
    """Contains details about the customer's store credit balance"""

    cashback_balance_id: UnsetOrNoneField[int]
    """The ID of the customer's cashback balance"""

    cashback_balance: UnsetOrNoneField[Balance]
    """Contains details about the customer's cashback balance"""

    spent: Decimal
    """The total amount spent by the customer"""

    total_discount: Decimal
    """The total discount applied to the customer"""

    total_bonus: Decimal
    """The total amount of bonus points applied to the customer"""

    receipt_count: int
    """The total number of receipts for the customer"""

    gender: UnsetOrNoneField[int]
    """The gender of the customer"""

    date_of_birth: UnsetOrNoneField[str]
    """The date of birth of the customer"""

    code: UnsetOrNoneField[str]
    """The code of the customer"""

    source: UnsetOrNoneField[str]
    """The source of the customer"""

    reference_id: UnsetOrNoneField[str]
    """The reference ID of the customer"""

    phone_verified_at: UnsetOrNoneField[str]
    """The timestamp when the customer's phone number was verified"""

    status: bool
    """The status of the customer account"""

    can_use_loyalty_system: UnsetOrNoneField[bool]
    """Whether the customer can use the loyalty system or not"""

    is_verified: UnsetOrNoneField[bool]
    """Whether the customer is verified or not"""


class Category(Timestamp):
    id: int
    """Unique identifier"""

    name: str
    """Name of the category"""

    status: int
    """1 = active, 0 = inactive"""

    hidden: bool
    """Whether the category is hidden or not"""

    type: CategoryType
    """product_category, ingredient_category, accounting_category"""

    image: UnsetOrNoneField[Image]
    """Image of the category"""

    position: UnsetOrNoneField[int]
    """The position of the category"""

    emenu_position: UnsetOrNoneField[int]
    """The position of the category in the eMenu"""

    meta: UnsetOrNoneField[dict]
    """Additional settings and visibility info"""

    emenu_hidden: UnsetOrNoneField[bool]
    """Whether the category is hidden in the eMenu or not"""

    code: UnsetOrNoneField[str]
    """The code of the category"""

    lft: int = Field(alias='_lft')
    """Nested set boundaries"""

    rgt: int = Field(alias='_rgt')
    """Nested set boundaries"""

    depth: int
    """Depth of the subcategory"""

    parent_id: UnsetOrNoneField[int]
    """Parent category ID, null for root"""

    slug: UnsetOrNoneField[str]
    """URL-friendly identifier"""

    color: UnsetOrNoneField[str]
    """HEX color"""

    properties: UnsetOrNoneField[Union[dict, list]]
    """Additional settings and visibility info"""

    media: list[Media]
    """Media of the category"""

    children: UnsetOrNoneField[list['Category']]
    """Subcategories"""


class Station(Timestamp):
    id: int
    """Unique identifier"""

    name: str
    """Name of the station"""

    status: int
    """1 = active, 0 = inactive"""

    type: UnsetOrNoneField[int]
    """Type of the station"""

    printable: UnsetOrNoneField[int]
    """Whether the station is printable or not"""

    can_print: UnsetOrNoneField[bool]
    """Can be redirected to a printer"""

    reminder_enabled: UnsetOrNoneField[bool]
    """Is reminder notification on?"""

    meta: UnsetOrNoneField[dict]
    """Additional settings and visibility info"""

    description: UnsetOrNoneField[str]
    """Optional description"""


class Product(Timestamp):
    id: int
    """Unique identifier"""

    cid: UnsetOrNoneField[str]
    """Unique identifier"""

    parent_id: UnsetOrNoneField[int]
    """Parent product ID, null for root"""

    station_id: UnsetOrNoneField[int]
    """The ID of the station the product belongs to"""

    category_id: UnsetOrNoneField[int]
    """The ID of the category the product belongs to"""

    unit_id: UnsetOrNoneField[int]
    """The ID of the unit the product belongs to"""

    net_output: UnsetOrNoneField[int]
    """Net output of the product"""

    type: ProductType
    """product, ingredient, accounting"""

    name: str
    """The main name of the product"""

    parent_name: UnsetOrNoneField[str]
    """The name of the parent product"""

    image: UnsetOrNoneField[Image]
    """Image of the product"""

    position: UnsetOrNoneField[int]
    """The position of the product in the menu"""

    description: UnsetOrNoneField[str]
    """Description of the product"""

    barcode: UnsetOrNoneField[str]
    """The barcode of the product"""

    gov_code: UnsetOrNoneField[str]
    """The government code of the product"""

    cost: UnsetOrNoneField[Decimal]
    """The cost of the product"""

    status: int
    """1 = active, 0 = inactive"""

    hidden: UnsetOrNoneField[bool]
    """Whether the product is hidden or not"""

    sold_by_weight: UnsetOrNoneField[bool]
    """Whether the product is sold by weight or not"""

    max_age: UnsetOrNoneField[int]
    """The maximum age of the product"""

    discountable: UnsetOrNoneField[bool]
    """Whether the product is discountable or not"""

    giftable: UnsetOrNoneField[bool]
    """Whether the product is giftable or not"""

    has_modifications: UnsetOrNoneField[bool]
    """If true, the product has variants in the modifications array"""

    meta: UnsetOrNoneField[dict]
    """Additional settings and visibility info"""

    setting: UnsetOrNoneField[TimerSetting]
    """Pricing rules for TIMER type products. See Timer Settings"""

    modifications: UnsetOrNoneField[list[Variant]]
    """List of variants for GOODS type products. See Variant Object"""

    modificator_groups: UnsetOrNoneField[list[ModifierGroup]]
    """List of modificator groups for GOODS type products. See Modificator Group Object"""

    recipe: UnsetOrNoneField[Recipe]
    """Recipe for DISH or PREPARATION type products. See Recipe Item."""

    packages: UnsetOrNoneField[list[Package]]
    """Packages for INGREDIENT type products. See Package Object."""

    variants: list['Product'] = []
    """Variants of the product"""

    e_menu_id: UnsetOrNoneField[int]
    """The ID of the eMenu the product belongs to"""

    emenu_category_id: UnsetOrNoneField[int]
    """The ID of the category the product belongs to in eMenu"""

    emenu_position: UnsetOrNoneField[int]
    """The position of the product in eMenu"""

    emenu_hidden: UnsetOrNoneField[bool]
    """Whether the product is hidden in eMenu or not"""

    accounting_category_id: UnsetOrNoneField[int]
    """The ID of the category the product belongs to in accounting"""

    price: Decimal
    """The base price of the product (variants may have their own prices)"""

    prices: UnsetOrNoneField[list[Price]]
    """The prices of the product"""

    cost_price: UnsetOrNoneField[Decimal]
    """The cost price of the product"""

    markup_rate: UnsetOrNoneField[Decimal]
    """The markup rate of the product"""

    taxes: UnsetOrNoneField[list[Tax]]
    """Taxes applied to the product"""

    cooking_time: UnsetOrNoneField[int]
    """The cooking time of the product"""

    ignore_service_charge: UnsetOrNoneField[bool]
    """Whether the product should ignore the service charge or not"""

    inventory_behavior: UnsetOrNoneField[int]
    """The inventory behavior of the product"""

    low_stock: UnsetOrNoneField[int]
    """Low stock count"""

    unit_weight: UnsetOrNoneField[int]
    """The weight of the product in grams"""

    name_slug: UnsetOrNoneField[str]
    """The slug of the product name"""

    full_name: UnsetOrNoneField[str]
    """The full product name, including variant information"""

    gross_margin: UnsetOrNoneField[Decimal]
    """The gross margin of the product"""

    slug: UnsetOrNoneField[str]
    """The slug of the product"""

    color: UnsetOrNoneField[str]
    """The color of the product"""

    venues: UnsetOrNoneField[list[Venue]]
    """The venues the product is available in"""

    properties: UnsetOrNoneField[list[dict]]
    """The properties of the product"""

    media: list[Media]
    """Media of the product"""

    tags: UnsetOrNoneField[list[dict]]
    """Tags of the product"""

    total_quantity: UnsetOrNoneField[int]
    """The total quantity of the product"""

    total_cost: UnsetOrNoneField[Decimal]
    """The total cost of the product"""

    average_cost: UnsetOrNoneField[Decimal]
    """The average cost of the product"""

    open_receipts_count: UnsetOrNoneField[int]
    """The number of open receipts for the product"""


class PaymentMethod(Timestamp):
    id: int
    """The unique identifier for the payment method"""

    name: str
    """The name of the payment method (e.g., "Cash", "Card")"""

    customer_required: int
    """Whether a customer must be attached to the transaction (1 for yes, 0 for no)"""

    is_system: int
    """Indicates if it’s a system-default payment method"""

    balance_id: UnsetOrNoneField[int]
    """The ID of the balance associated with the payment method"""

    balance: UnsetOrNoneField[Balance]
    """An object containing details of the associated balance account"""

    service: dict
    """Details of any external service integrated with this payment method"""

    split: UnsetOrNoneField[int]
    """Indicates if this payment method can be used for split payments"""

    status: dict[str, int]
    """Map of venue_id -> 0/1 availability for this method"""


class SaleType(Timestamp):
    id: int
    """The unique identifier for the sale type"""

    name: str
    """The name of the sale type (e.g., "In-store", "Delivery")"""

    system_type: UnsetOrNoneField[str]
    """A system-defined type identifier (e.g., "IN", "DELIVERY")"""

    status: dict[str, int]
    """Map of venue_id -> 0/1 availability for this method"""

    channel: UnsetOrNoneField[str]
    """The channel the sale type belongs to"""

    service_charge_rate: UnsetOrNoneField[Decimal]
    """The service charge rate associated with this sale type"""

    payment_method_id: UnsetOrNoneField[int]
    """The ID of the default payment method for this sale type, if any"""

    position: UnsetOrNoneField[int]
    """The position of the sale type in the list of sale types"""

    payment_method: UnsetOrNoneField[PaymentMethod]
    """An object containing details of the associated payment method"""

    media: list[Media]
    """Media of the sale type"""


class Order(Timestamp):
    id: int
    """The unique identifier for the order"""

    venue_id: UnsetOrNoneField[int]
    """The ID of the venue associated with the order"""

    type: UnsetOrNoneField[str]
    """The ID of the sale type associated with the order"""

    integration: UnsetOrNoneField[str]
    """The integration channel associated with the order"""

    integration_uuid: UnsetOrNoneField[str]
    """The UUID of the integration associated with the order"""

    integration_id: UnsetOrNoneField[int]
    """The ID of the integration associated with the order"""

    customer_ref_id: UnsetOrNoneField[str]
    """The reference ID of the customer associated with the order"""

    integration_status: UnsetOrNoneField[str]
    """The status of the integration associated with the order"""

    integration_response: UnsetOrNoneField[str]
    """The response from the integration associated with the order"""

    customer_id: UnsetOrNoneField[int]
    """The ID of the customer associated with the order"""

    receive_user_id: UnsetOrNoneField[int]
    """The ID of the user who received the order"""

    receive_terminal_id: UnsetOrNoneField[int]
    """The ID of the terminal where the order was received"""

    status: OrderStatus
    """Current lifecycle state. accepted orders are sent to the POS"""

    payload: Payload
    """ Payload of the order"""

    receipt_id: UnsetOrNoneField[int]
    """Linked open receipt ID once the POS accepts the order"""

    payment_status: UnsetOrNoneField[str]
    """	Payment state (e.g., pending, paid)"""

    total_amount: UnsetOrNoneField[Decimal]
    """Order grand total"""

    line_items: UnsetOrNoneField[list[OrderItem]]
    """Line items of the order"""

    sale_type: UnsetOrNoneField[SaleType]
    """An object containing details of the associated sale type"""

    payment_method_id: UnsetOrNoneField[int]
    """The ID of the payment method associated with the order"""

    payment_method: UnsetOrNoneField[PaymentMethod]
    """An object containing details of the associated payment method"""

    properties: UnsetOrNoneField[dict]
    """Additional properties of the order"""


class Receipt(Timestamp):
    id: int
    """Unique receipt identifier"""

    venue_id: UnsetOrNoneField[int]
    """The ID of the venue associated with the receipt"""

    cash_shift_cid: UnsetOrNoneField[str]
    """The UUID of the cash shift associated with the receipt"""

    cid: UnsetOrNoneField[str]
    """Transaction UUID"""

    user_id: UnsetOrNoneField[int]
    """The ID of the user associated with the receipt"""

    open_by_user_id: UnsetOrNoneField[int]
    """The ID of the user who opened the receipt"""

    close_by_user_id: UnsetOrNoneField[int]
    """The ID of the user who closed the receipt"""

    courier_id: UnsetOrNoneField[int]
    """The ID of the courier associated with the receipt"""

    seller_id: UnsetOrNoneField[int]
    """The ID of the seller associated with the receipt"""

    terminal_id: UnsetOrNoneField[int]
    """The ID of the terminal associated with the receipt"""

    source: UnsetOrNoneField[str]
    """The source of the receipt"""

    closed_terminal_id: UnsetOrNoneField[int]
    """The ID of the terminal where the receipt was closed"""

    service_notification_id: UnsetOrNoneField[int]
    """The ID of the service notification associated with the receipt"""

    table_id: UnsetOrNoneField[int]
    """The ID of the table associated with the receipt"""

    hall_id: UnsetOrNoneField[int]
    """The ID of the hall associated with the receipt"""

    customer_id: UnsetOrNoneField[int]
    """The ID of the customer associated with the receipt"""

    sale_type_id: UnsetOrNoneField[int]
    """Sale type identifier"""

    is_returns: UnsetOrNoneField[bool]
    """Whether the receipt is a return"""

    guests: UnsetOrNoneField[int]
    """The number of guests associated with the receipt"""

    status: UnsetOrNoneField[int]
    """Receipt status code"""

    lock: UnsetOrNoneField[bool]
    """Lock identifier"""

    inventory_status: UnsetOrNoneField[int]
    """Inventory status code"""

    report_status: UnsetOrNoneField[int]
    """Report status code"""

    meta: UnsetOrNoneField[dict]
    """Receipt meta data"""

    suspicion: UnsetOrNoneField[int]
    """Suspicion level code"""

    printed: UnsetOrNoneField[bool]
    """Whether the receipt has been printed"""

    total: UnsetOrNoneField[Decimal]
    """Total amount collected"""

    subtotal: UnsetOrNoneField[Decimal]
    """Subtotal before adjustments"""

    original_subtotal: UnsetOrNoneField[Decimal]
    """Receipt original subtotal"""

    gift_total: UnsetOrNoneField[Decimal]
    """Receipt gift total"""

    total_cost: UnsetOrNoneField[Decimal] = Field(alias='totalCost')
    """Receipt total cost"""

    payment_methods: UnsetOrNoneField[list[ReceiptPaymentMethod]]
    """Payment methods associated with the receipt"""

    fiscal_id: UnsetOrNoneField[str]
    """Receipt fiscal ID"""

    by_cash: UnsetOrNoneField[Decimal]
    """Amount collected by cash"""

    by_card: UnsetOrNoneField[Decimal]
    """Amount collected by card"""

    remaining: UnsetOrNoneField[Decimal]
    """Remaining amount"""

    discount_type: UnsetOrNoneField[int]
    """Discount type"""

    discount_value: UnsetOrNoneField[Decimal]
    """Discount value"""

    discount_rate: UnsetOrNoneField[Decimal]
    """Discount rate"""

    rps_discount: UnsetOrNoneField[Decimal]
    """RPS discount"""

    service_charge: UnsetOrNoneField[Decimal]
    """Service charge"""

    service_charge_value: UnsetOrNoneField[Decimal]
    """Service charge value"""

    i_tax: UnsetOrNoneField[Decimal]
    """I tax"""

    delivery_fee: UnsetOrNoneField[Decimal]
    """Delivery fee"""

    e_tax: UnsetOrNoneField[Decimal]
    """E tax"""

    total_tax: UnsetOrNoneField[Decimal]
    """Total tax"""

    description: UnsetOrNoneField[str]
    """Receipt description"""

    address: UnsetOrNoneField[str]
    """Receipt address"""

    terminal_version: UnsetOrNoneField[str]
    """Receipt terminal version"""

    loyalty_type: UnsetOrNoneField[int]
    """Loyalty type"""

    loyalty_value: UnsetOrNoneField[Decimal]
    """Loyalty value"""

    order_status: UnsetOrNoneField[OrderStatus]
    """Order status code"""

    order_number: UnsetOrNoneField[str]
    """Order number"""

    terminal_updated_at: UnsetOrNoneField[str]
    """Receipt terminal updated at"""

    closed_at: UnsetOrNoneField[str]
    """Receipt closed at"""

    shift_date: UnsetOrNoneField[str]
    """Shift date associated with the receipt"""

    gift_count: UnsetOrNoneField[int]
    """Receipt gift count"""

    total_discount: UnsetOrNoneField[Decimal]
    """Receipt total discount"""

    properties: UnsetOrNoneField[dict]
    """Receipt properties"""


Payload.model_rebuild()
