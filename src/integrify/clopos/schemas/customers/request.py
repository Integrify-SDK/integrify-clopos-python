from typing import Literal

from pydantic import Field, model_serializer

from integrify.clopos.helpers import IsoDate
from integrify.clopos.schemas.common.request import PaginatedDataRequest
from integrify.clopos.schemas.enums import Gender
from integrify.schemas import PayloadBaseModel
from integrify.utils import UnsetField, UnsetOrNoneField


class GetCustomersRequest(PaginatedDataRequest):
    with_: UnsetField[list[Literal['group', 'balance', 'cashback_balance']]] = Field(alias='with[]')
    filter_bys: UnsetField[list[str]] = Field(exclude=True)
    filter_values: UnsetField[list[str]] = Field(exclude=True)

    @model_serializer(mode='wrap')
    def serialize_model(self, serializer) -> dict:
        """Model serializer"""
        data = serializer(self)

        filter_bys = data.pop('filter_bys', [])
        filter_values = data.pop('filter_values', [])

        for i, (filter_by, filter_value) in enumerate(zip(filter_bys, filter_values)):
            data[f'filters[{i}][0]'] = filter_by
            data[f'filter[{i}][1]'] = filter_value

        return data


class CreateCustomerRequest(PayloadBaseModel):
    name: str
    email: UnsetField[str]
    phone: UnsetField[str]
    code: UnsetField[str]
    cid: UnsetField[str]
    description: UnsetField[str]
    group_id: UnsetField[int]
    gender: UnsetOrNoneField[Gender]
    date_of_birth: UnsetField[IsoDate]
