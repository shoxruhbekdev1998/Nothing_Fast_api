from sqlalchemy import Column, Integer, String, Boolean, Float, Text, Date, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from db import Base


class About_Services(Base):
    __tablename__ = "About_Services"
    id= Column(Integer, primary_key=True,autoincrement=True)
    services_id=Column(Integer, ForeignKey("Services.id"), nullable=True)
    services = Column(String(30), nullable=True)
    description = Column(Text, nullable=True)
    status = Column(Boolean, nullable = True ,default=True)
    date = Column(Date(),nullable = True,default=func.now())


    servic=relationship("Services", back_populates="about_servic")