from pydantic import BaseModel
from typing import Optional,List

class PartnersBase(BaseModel):
    partner_name:str
    partner_description:str
    partner_link:str




class PartnersCreate(PartnersBase):
    pass

class PartnersUpdate(PartnersBase):
    id:int
    status:bool
