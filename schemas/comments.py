from pydantic import BaseModel
from typing import Optional, List


class CommentsBase(BaseModel):
    name: str
    last_name: str
    comment: str


class CommentsCreate(CommentsBase):
    pass


class CommentsUpdate(CommentsBase):
    id: int
    status: bool
