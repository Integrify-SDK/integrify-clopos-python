from enum import Enum

# import os
# from warnings import warn

VERSION = '{replace}'  # version of client documentation

# ENV VARS HERE
# EXPECTED_KEY: str = os.getenv('EXPECTED_KEY', '')
# EXPECTED_ENV: str = os.getenv('EXPECTED_ENV', Environment.TEST.value)


# if not EXPECTED_KEY:  # pragma: no cover
#     warn(
#         'EXPECTED_KEY mühit dəyişənlərinə dəyər verməsəniz '
#         'sorğular çalışmayacaq!'
#     )


class API(str, Enum):
    """Endpoint constant-ları"""

    # TEST_BASE_URL = '{replace}'
    # PROD_BASE_URL = '{replace}'
    # BASE_URL = PROD_BASE_URL if EXPECTED_ENV == Environment.PROD else TEST_BASE_URL
    # OR
    BASE_URL = '{replace}'  # if test env url = prod url

    API1 = '{replace}'
    # API2 = '{replace}'


__all__ = [
    'VERSION',
    # 'EXPECTED_KEY',
    'API',
]
