from pydantic import BaseModel
from typing import Optional,List

class UserBase(BaseModel):
    roll: str
    name:str
    last_name: Optional[str]=None
    username: str
    phone_number:str
    password:str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    id:int
    status:bool



class Token(BaseModel):
    access_token=str
    token=str

class TokenData(BaseModel):
    id: Optional[str] = None

class UserCurrent(BaseModel):
    roll: str
    name: str
    last_name: str
    username:str
    phone_number: str
    region: str
    password: str
    status: bool