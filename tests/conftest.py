# from functools import partial

import pytest

from integrify.test import pytest_addoption  # noqa: F401

# from integrify.test import requires_env as _requires_env
from tests.mocks import *  # noqa: F403

# requires_env = partial(_requires_env, 'EXPECTED_KEY')


@pytest.fixture(scope='package')
def client():
    from integrify.clopos.client import CloposClientClass

    yield CloposClientClass()
