# Base parts of Clopos: Auth, Venues, Users/Customers, Categories and Station

from typing import TYPE_CHECKING

from integrify.clopos.schemas.objects.main import (
    Category,
    Customer,
    Group,
    SaleType,
    Station,
    User,
    Venue,
)
from integrify.clopos.schemas.response import ErrorResponse
from tests.conftest import requires_env

if TYPE_CHECKING:
    from tests.client import CloposTestClientClass


@requires_env()
def test_auth(client: 'CloposTestClientClass'):
    resp = client.auth()

    assert resp.ok
    assert resp.body.success
    assert resp.body.token.startswith('oauth_')


@requires_env()
def test_wrong_auth(client: 'CloposTestClientClass'):
    resp = client.auth(brand='wrong_brand')

    assert not resp.ok
    assert isinstance(resp.body, ErrorResponse)
    assert not resp.body.success


@requires_env()
def test_get_venues(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_venues()

    assert resp.ok
    assert resp.body.success
    assert isinstance(resp.body.data, list)
    assert isinstance(resp.body.data[0], Venue)


@requires_env()
def test_get_users(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_users()

    assert resp.ok
    assert resp.body.success
    assert isinstance(resp.body.data, list)
    assert isinstance(resp.body.data[0], User)


@requires_env()
def test_get_user_by_id(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_user_by_id(1)

    assert resp.ok
    assert resp.body.success
    assert isinstance(resp.body.data, User)

    assert resp.body.data.id == 1


@requires_env()
def test_get_user_by_id_wrong_id(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_user_by_id(1000)

    assert not resp.ok
    assert isinstance(resp.body, ErrorResponse)
    assert not resp.body.success

    assert resp.body.error == 'No query results for model [App\\Models\\Auth\\User] 1000'


@requires_env()
def test_get_customers(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_customers()

    assert resp.ok
    assert resp.body.success
    assert isinstance(resp.body.data, list)
    assert isinstance(resp.body.data[0], Customer)


@requires_env()
def test_get_customer_by_id(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_customer_by_id(1)

    # assert resp.ok
    # assert resp.body.success
    # assert isinstance(resp.body.data, Customer)

    # assert resp.body.data.id == 1

    assert not resp.ok
    assert isinstance(resp.body, ErrorResponse)
    assert not resp.body.success

    # assert resp.body.error == 'No query results for model [App\\Models\\Customer] 1000'
    assert resp.body.error == 'Not found!'


@requires_env()
def test_get_customer_by_id_wrong_id(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_customer_by_id(1000)

    assert not resp.ok
    assert isinstance(resp.body, ErrorResponse)
    assert not resp.body.success

    # assert resp.body.error == 'No query results for model [App\\Models\\Customer] 1000'
    assert resp.body.error == 'Not found!'


@requires_env()
def test_get_customer_groups(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_customer_groups()

    assert resp.ok
    assert resp.body.success
    assert isinstance(resp.body.data, list)
    assert isinstance(resp.body.data[0], Group)


@requires_env()
def test_get_categories(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_categories()

    assert resp.ok
    assert resp.body.success
    assert isinstance(resp.body.data, list)
    assert isinstance(resp.body.data[0], Category)


@requires_env()
def test_get_category_by_id(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_category_by_id(1)

    # assert resp.ok
    # assert resp.body.success
    # assert isinstance(resp.body.data, Category)

    # assert resp.body.data.id == 1

    assert not resp.ok
    assert isinstance(resp.body, ErrorResponse)
    assert not resp.body.success

    # assert resp.body.error == 'No query results for model [App\\Models\\Customer] 1000'
    assert resp.body.error == 'Not found!'


@requires_env()
def test_get_category_by_id_wrong_id(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_category_by_id(1000)

    assert not resp.ok
    assert isinstance(resp.body, ErrorResponse)
    assert not resp.body.success

    # assert resp.body.error == 'No query results for model [App\\Models\\Category] 1000'
    assert resp.body.error == 'Not found!'


@requires_env()
def test_get_stations(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_stations()

    assert resp.ok
    assert resp.body.success
    assert isinstance(resp.body.data, list)
    assert isinstance(resp.body.data[0], Station)


@requires_env()
def test_get_station_by_id(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_station_by_id(1)

    # assert resp.ok
    # assert resp.body.success
    # assert isinstance(resp.body.data, Station)

    # assert resp.body.data.id == 1

    assert not resp.ok
    assert isinstance(resp.body, ErrorResponse)
    assert not resp.body.success

    assert resp.body.error == 'Not found!'


@requires_env()
def test_get_station_by_id_wrong_id(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_station_by_id(1000)

    assert not resp.ok
    assert isinstance(resp.body, ErrorResponse)
    assert not resp.body.success

    # assert resp.body.error == 'No query results for model [App\\Models\\Station] 1000'
    assert resp.body.error == 'Not found!'


@requires_env()
def test_get_sale_types(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_sale_types()

    assert resp.ok
    assert resp.body.success
    assert isinstance(resp.body.data, list)
    assert isinstance(resp.body.data[0], SaleType)


@requires_env()
def test_get_payment_methods(authed_client: 'CloposTestClientClass'):
    resp = authed_client.get_payment_methods()

    # assert resp.ok
    # assert resp.body.success
    # assert isinstance(resp.body.data, list)
    # assert isinstance(resp.body.data[0], PaymentMethod)

    assert not resp.ok
    assert isinstance(resp.body, ErrorResponse)
    assert not resp.body.success

    assert resp.body.error == 'Not found!'
