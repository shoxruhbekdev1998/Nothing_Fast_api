import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Comments(Base):
    __tablename__ = "Comments"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    comment = Column(Text,nullable=True)
    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)



