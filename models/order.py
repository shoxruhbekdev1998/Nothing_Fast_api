import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(30), nullable=True)
    email = Column(String(30), nullable=True)
    phone_number = Column(String(30), nullable=True)
    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)

