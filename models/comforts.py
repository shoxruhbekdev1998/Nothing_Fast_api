from sqlalchemy import Column, Integer, String, Boolean, Float, Text, Date, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from db import Base


class Comforts(Base):
    __tablename__ = "Comforts"
    id = Column(Integer, primary_key=True,autoincrement=True)
    comfort_name = Column(String(30), nullable=True)
    comfort_description = Column(Text, nullable=True)
    status = Column(Boolean, nullable = True ,default=True)
    date = Column(Date(),nullable = True,default=func.now())


