import json
from functools import cached_property
from typing import Annotated, Union

from pydantic import Field

from integrify.api import APIPayloadHandler
from integrify.clopos import env
from integrify.clopos.schemas.common import CreateReceiptReqResp
from integrify.clopos.schemas.objects import Category, Station
from integrify.clopos.schemas.objects.main import Order, Product
from integrify.clopos.schemas.request import (
    AuthRequest,
    CreateOrderRequest,
    GetByIDRequest,
    GetCategoriesRequest,
    GetCategoryByIDRequest,
    GetPaginatedDataRequest,
    GetProductsRequest,
    GetStationsRequest,
)
from integrify.clopos.schemas.response import (
    AuthResponse,
    BaseResponse,
    ErrorResponse,
    ObjectListResponse,
    ObjectResponse,
)


class AuthHandler(APIPayloadHandler):
    def __init__(
        self,
        req_model=AuthRequest,
        resp_model=Annotated[Union[AuthResponse, ErrorResponse], Field(discriminator='success')],
        dry=False,
    ):
        super().__init__(req_model, resp_model, dry)


class AuthedAPIPayloadHandler(APIPayloadHandler):
    def __init__(self, req_model=None, resp_model=None, dry=False):
        super().__init__(
            req_model,
            Annotated[Union[resp_model, ErrorResponse], Field(discriminator='success')],
            dry,
        )

    @cached_property
    def headers(self):
        default = super().headers

        if env.CLOPOS_BRAND:
            default['x-brand'] = env.CLOPOS_BRAND

        if env.CLOPOS_VENUE_ID:
            default['x-venue'] = env.CLOPOS_VENUE_ID

        return default


def GetPaginatedDataHandler(object_type, req_model=GetPaginatedDataRequest):  # pylint: disable=invalid-name
    """Function to dynamically create ObjectListResponse[object_type]"""

    class _GetPaginatedDataHandler(AuthedAPIPayloadHandler):
        def __init__(self, dry=False):
            super().__init__(
                req_model=req_model,
                resp_model=ObjectListResponse[object_type],
                dry=dry,
            )

    return _GetPaginatedDataHandler


def GetByIDHandler(object_type, req_model=GetByIDRequest):  # pylint: disable=invalid-name
    """Function to dynamically create ObjectResponse[object_type]"""

    class _GetByIDHandler(AuthedAPIPayloadHandler):
        def __init__(self, dry=False):
            super().__init__(
                req_model=req_model,
                resp_model=ObjectResponse[object_type],
                dry=dry,
            )

    return _GetByIDHandler


###################################################################################################


class GetCategoriesHandler(AuthedAPIPayloadHandler):
    def __init__(
        self,
        req_model=GetCategoriesRequest,
        resp_model=ObjectListResponse[Category],
        dry=False,
    ):
        super().__init__(req_model, resp_model, dry)


class GetCategoryByIDHandler(AuthedAPIPayloadHandler):
    def __init__(
        self,
        req_model=GetCategoryByIDRequest,
        resp_model=ObjectResponse[Category],
        dry=False,
    ):
        super().__init__(req_model, resp_model, dry)


class GetStationsHandler(AuthedAPIPayloadHandler):
    def __init__(
        self,
        req_model=GetStationsRequest,
        resp_model=ObjectListResponse[Station],
        dry=False,
    ):
        super().__init__(req_model, resp_model, dry)


class GetProductsHandler(AuthedAPIPayloadHandler):
    def __init__(
        self,
        req_model=GetProductsRequest,
        resp_model=ObjectListResponse[Product],
        dry=False,
    ):
        super().__init__(req_model, resp_model, dry)

    def post_handle_payload(self, data):
        return json.dumps(data)  # for urlencoding


class GetOrdersHandler(AuthedAPIPayloadHandler):
    def __init__(
        self,
        req_model=GetPaginatedDataRequest,
        resp_model=ObjectListResponse[Order],
        dry=False,
    ):
        super().__init__(req_model, resp_model, dry)


class GetOrderByIDHandler(AuthedAPIPayloadHandler):
    def __init__(self, req_model=GetByIDRequest, resp_model=ObjectResponse[Order], dry=False):
        super().__init__(req_model, resp_model, dry)


class CreateOrderHandler(AuthedAPIPayloadHandler):
    def __init__(self, req_model=CreateOrderRequest, resp_model=ObjectResponse[Order], dry=False):
        super().__init__(req_model, resp_model, dry)


class CreateReceiptHandler(AuthedAPIPayloadHandler):
    def __init__(
        self,
        req_model=CreateReceiptReqResp,
        resp_model=ObjectResponse[CreateReceiptReqResp],
        dry=False,
    ):
        super().__init__(req_model, resp_model, dry)


class DeleteReceiptHandler(AuthedAPIPayloadHandler):
    def __init__(self, req_model=GetByIDRequest, resp_model=BaseResponse, dry=False):
        super().__init__(req_model, resp_model, dry)
