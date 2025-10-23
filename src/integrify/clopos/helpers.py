from datetime import datetime
from typing import Annotated, Union

from pydantic import BeforeValidator, Field

IsoDateTime = Annotated[
    Union[str, datetime, None],
    Field(BeforeValidator(lambda v: v.isoformat() if isinstance(v, datetime) else v)),
]
