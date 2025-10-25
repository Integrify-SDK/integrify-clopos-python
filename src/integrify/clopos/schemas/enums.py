from enum import Enum


class CategoryType(str, Enum):
    PRODUCT = 'PRODUCT'
    INGREDIENT = 'INGREDIENT'
    ACCOUNTING = 'ACCOUNTING'


class ProductType(str, Enum):
    GOODS = 'GOODS'
    DISH = 'DISH'
    TIMER = 'TIMER'
    PREPARATION = 'PREPARATION'
    INGREDIENT = 'INGREDIENT'
    MODIFICATION = 'MODIFICATION '


class OrderStatus(str, Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'
    IGNORE = 'IGNORE'


class DiscountType(int, Enum):
    NONE = 0
    PERCENTAGE = 1
    FIXED = 2
