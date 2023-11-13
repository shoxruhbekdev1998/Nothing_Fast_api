from pydantic import BaseModel
from typing import Optional,List

class ServicesBase(BaseModel):
    services_names:str


class ServicesCreate(ServicesBase):
    pass

class ServicesUpdate(ServicesBase):
    id:int
    status:bool
