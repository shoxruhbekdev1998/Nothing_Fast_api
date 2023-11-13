from pydantic import BaseModel
from typing import Optional, List


class OrdersBase(BaseModel):
    name: str
    email: str
    phone_number: int


class OrdersCreate(OrdersBase):
    pass


class OrdersUpdate(OrdersBase):
    id: int
    status: bool
