import datetime

from sqlalchemy import Column, Integer, String, Boolean, Float, Text, ForeignKey, Date, DateTime, func, and_

from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import URLType
from sqlalchemy_utils.functions import foreign_keys

from db import Base
from models.about_services import About_Services
from models.comforts import Comforts
from models.comments import Comments
from models.partners import Partners


class Files(Base):
    __tablename__ = "Files"
    id = Column(Integer, primary_key=True, autoincrement=True)
    file = Column(URLType, nullable=True)
    source = Column(String(30), nullable=False)
    source_id = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=True, default=True)
    date = Column(DateTime, default=func.now(), nullable=False)

    tests = relationship('About_Services', foreign_keys=[source_id],
                         primaryjoin=lambda: and_(About_Services.id == Files.source_id, Files.source == "about_servic"),
                         backref=backref('uploaded_files'))

    tests1 = relationship('Comforts', foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Comforts.id == Files.source_id, Files.source == "comfort"),
                          backref=backref('comfort_files'))

    tests2 = relationship('Comments', foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Comments.id == Files.source_id, Files.source == "comment"),
                          backref=backref('comment_files'))

    tests3 = relationship('Partners', foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Partners.id == Files.source_id, Files.source == "partner"),
                          backref=backref('partner_files'))
