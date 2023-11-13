from sqlalchemy import Column, Integer, String, Boolean, Float, Text, Date, func
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from db import Base


class Services(Base):
    __tablename__ = "Services"
    id = Column(Integer, primary_key=True, autoincrement=True)
    services_names=Column(String(30), nullable=True)
    status = Column(Boolean, nullable=True, default=True)
    date = Column(Date(), nullable=True, default=func.now())

    about_servic=relationship("About_Services", back_populates="servic")