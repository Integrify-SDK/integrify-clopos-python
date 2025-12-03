import uuid
from functools import partial

import pytest

from integrify.clopos.schemas.common.response import ObjectResponse
from integrify.clopos.schemas.orders.object import Order
from integrify.clopos.schemas.receipts.object import Receipt
from integrify.schemas import APIResponse
from integrify.test import pytest_addoption  # noqa: F401
from integrify.test import requires_env as _requires_env
from tests.client import CloposTestClientClass
from tests.mocks import *  # noqa: F403

requires_env = partial(
    _requires_env,
    'CLOPOS_CLIENT_ID',
    'CLOPOS_CLIENT_SECRET',
    'CLOPOS_BRAND',
    'CLOPOS_VENUE_ID',
)


@pytest.fixture(scope='package')
def client():
    from tests.client import CloposTestClientClass

    yield CloposTestClientClass()


@pytest.fixture(scope='package')
def authed_client(client):
    from tests.client import CloposTestClientClass

    client = CloposTestClientClass()
    client._token = client.auth().body.token
    yield client


@pytest.fixture(scope='package')
def authed_dry_client(client):
    from tests.client import CloposTestClientClass

    client = CloposTestClientClass(dry=True)
    client._token = 'randomtoken'
    yield client


@pytest.fixture(scope='package')
def new_order_resp(authed_client: 'CloposTestClientClass'):
    resp = authed_client.create_order(
        customer_id=1,
        payload={  # type: ignore[arg-type]
            'service': {
                'sale_type_id': 2,
                'sale_type_name': 'Delivery',
                'venue_id': 1,
                'venue_name': 'Main',
            },
            'customer': {
                'id': 9,
                'name': 'Rahid Akhundzada',
                'customer_discount_type': 1,
                'phone': '+994705401040',
            },
            'products': [
                {
                    'product_id': 1,
                    'count': 1,
                    'product_modificators': [
                        {'modificator_id': 187, 'count': 1},
                        {'modificator_id': 201, 'count': 1},
                    ],
                    'meta': {
                        'price': 0,
                        'order_product': {
                            'product': {
                                'id': 1,
                                'name': 'Mega Dürüm Menü Alana Çiğ Köfte Dürüm',
                                'category_id': 1,
                                'station_id': 1,
                                'price': 0,
                            },
                            'count': 1,
                            'status': 'completed',
                            'product_modificators': [
                                {'modificator_id': 187, 'count': 1},
                                {'modificator_id': 201, 'count': 1},
                            ],
                            'product_hash': 'MTExODcsMTEyMDE=',
                        },
                    },
                }
            ],
        },
        meta={
            'comment': '',
            'discount': {'discount_type': 1, 'discount_value': 10},
            'orderTotal': '16.2000',
            'apply_service_charge': True,
            'customer_discount_type': 1,
            'service_charge_value': 0,
        },
    )

    yield resp


@pytest.fixture(scope='package')
def new_order_object(new_order_resp: APIResponse[ObjectResponse[Order]]):
    yield new_order_resp.body.data


@pytest.fixture(scope='package')
def new_receipt_resp(authed_client: 'CloposTestClientClass'):
    cid = uuid.uuid4().hex

    data = {
        'address': '',
        'by_card': 0,
        'by_cash': 30000,
        'cid': cid,
        'closed_at': 1755524813947,
        'created_at': 1755524813947,
        'customer_discount_type': 0,
        'delivery_fee': 0,
        'discount_rate': 0,
        'discount_type': 0,
        'discount_value': 0,
        'gift_total': 0,
        'guests': 1,
        'meta': {
            'preprint_count': 0,
            'sale_type': {'name': 'Satis usulu 1'},
            'user': {'name': 'Clopos'},
            'terminal_updated_at': 1755524813947,
            'availiableDeposit': 30000,
        },
        'original_subtotal': 30000,
        'payment_methods': [{'id': 1, 'name': 'Cash', 'amount': 30000}],
        'printed': False,
        'receipt_products': [
            {
                'cid': 'f5b17d93-5586-411b-9e9d-934d3aa2e2ff',
                'product_id': 31042,
                'portion_size': 1,
                'is_gift': 0,
                'meta': {
                    'product': {
                        'name': 'Апельсинли реване',
                        'giftable': False,
                        'price': 22000,
                        'modifier_name': 'not found',
                        'discountable': True,
                        'sold_by_weight': False,
                        'priceWithoutTaxes': 22000,
                        'barcode': '',
                        'taxes': [],
                        'station': {'id': 57, 'name': 'Отдел Кондитер'},
                    },
                    'originalPrice': 22000,
                    'total_gift': 0,
                    'discountedPrice': 0,
                    'terminal_updated_at': 1755524813946,
                },
                'price': 22000,
                'count': 1,
                'subtotal': 22000,
                'total': 22000,
            },
            {
                'cid': 'c5202cc3-1f03-47b1-9dbc-5f049dabf997',
                'product_id': 31046,
                'portion_size': 1,
                'is_gift': 0,
                'meta': {
                    'product': {
                        'name': 'Ачма узум жевиз',
                        'giftable': False,
                        'price': 8000,
                        'modifier_name': 'not found',
                        'discountable': True,
                        'sold_by_weight': False,
                        'priceWithoutTaxes': 8000,
                        'barcode': '',
                        'taxes': [],
                        'station': {'id': 57, 'name': 'Отдел Кондитер'},
                    },
                    'originalPrice': 8000,
                    'total_gift': 0,
                    'discountedPrice': 0,
                    'terminal_updated_at': 1755524813947,
                },
                'price': 8000,
                'count': 1,
                'subtotal': 8000,
                'total': 8000,
            },
        ],
        'remaining': 0,
        'rps_discount': 0,
        'sale_type_id': 1000,
        'service_charge': 0,
        'service_charge_value': 0,
        'status': 2,
        'subtotal': 30000,
        'terminal_id': 1,
        'total': 30000,
        'total_tax': 0,
        'user_id': 1,
    }

    resp = authed_client.create_receipt(**data)  # type: ignore
    assert resp.ok
    assert resp.body.data.cid == cid

    yield resp


@pytest.fixture(scope='package')
def new_receipt_object(new_receipt_resp: APIResponse[ObjectResponse[Receipt]]):
    yield new_receipt_resp.body.data
