from pydantic import BaseModel
from typing import Optional, List


class About_ServicesBase(BaseModel):
    services_id:int
    services: str
    description: str


class About_ServicesCreate(About_ServicesBase):
    pass


class About_ServicesUpdate(About_ServicesBase):
    id: int
    status: bool
