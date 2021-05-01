from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from ...database.models import Base
from server.database.serializable import Serializable



class Ajuste(Serializable, Base):
    way = {}

    __tablename__ = 'ajuste'

    id = Column( Integer, primary_key=True)
    claveSecreta = Column( String(150), nullable=False)
    app_id = Column(String(150), nullable=False)
    rest_api_key = Column(String(150), nullable=False)
    channel_id = Column(String(150), nullable=False)

    enabled = Column(Boolean, default=True)





