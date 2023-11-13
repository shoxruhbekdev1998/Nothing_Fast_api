from sqlalchemy import Column, Integer, String, Boolean, Float, Text, Date, func
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from db import Base


class Partners(Base):
    __tablename__ = "Partners"
    id = Column(Integer, primary_key=True,autoincrement=True)
    partner_name = Column(String(30), nullable=True)
    partner_description = Column(Text, nullable=True)
    partner_link = Column(String(500), nullable=True)
    status = Column(Boolean, nullable = True ,default=True)
    date = Column(Date(),nullable = True,default=func.now())
