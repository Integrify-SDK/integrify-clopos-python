from typing import TYPE_CHECKING, Optional

from integrify.api import APIClient
from integrify.integration_name import env

__all__ = ['ClientClass', 'ClientClass', 'Request']


class ClientClass(APIClient):
    """{replace} sorğular üçün baza class"""

    def __init__(
        self,
        name='{replace}',
        base_url: Optional[str] = env.API.BASE_URL,
        default_handler=None,
        sync: bool = True,
        dry: bool = False,
    ):
        super().__init__(name, base_url, default_handler, sync, dry)

        # {REPLACE}
        # self.add_url('api1', env.API.API1, verb='{replace}')
        # self.add_handler('{replace}', {replace})

    if TYPE_CHECKING:
        '''
        def api1(
            self,
            arg1: Numeric,
            arg2: str,
        ) -> APIResponse[{replace}]:
            """{SHORT EXPLANATION HERE}

            **Endpoint:** *{RELATIVE PATH ENDPOINT HERE}*

            Example:
                ```python
                {EXAMPLE HERE}
                ```

            **Cavab formatı**: {LINK TO DOCUMENT OF SCHEMA HERE}

            {OPTIONAL: LONG DESCRIPTION HERE}

            Args:
                arg1: {EXPLANATION OF ARG1}
                arg2: {EXPLANATION OF ARG2}
            """  # noqa: E501
        '''


Request = ClientClass(sync=True)
AsyncRequest = ClientClass(sync=False)
