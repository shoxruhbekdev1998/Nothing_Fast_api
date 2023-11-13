from pydantic import BaseModel
from typing import Optional, List


class ComfortsBase(BaseModel):
    comfort_name: str
    comfort_description: str


class ComfortsCreate(ComfortsBase):
    pass


class ComfortsUpdate(ComfortsBase):
    id: int
    status: bool
