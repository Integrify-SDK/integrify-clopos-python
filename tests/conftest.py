from functools import partial

import pytest

from integrify.test import pytest_addoption  # noqa: F401
from integrify.test import requires_env as _requires_env
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
