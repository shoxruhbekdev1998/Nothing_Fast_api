import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True,autoincrement=True)
    roll = Column(String(20), nullable=True)
    name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    phone_number = Column(String(30), nullable=True)
    username = Column(String(50), unique=True, nullable=True)
    password = Column(String(200),nullable=True)
    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)
    token = Column(String(400),default = '',nullable=True)
