from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property
from ...condominios.condominio.models import *


class Huellas(Serializable, Base):
    way = {}

    __tablename__ = 'huellas'

    id = Column(Integer,primary_key=True)
    userid = Column(Integer, nullable=True)
    codigo = Column(Integer, nullable=True)
    nombre = Column(String(100), nullable=True)
    fingerid = Column(Integer, nullable=True)
    valid = Column(Integer, nullable=True)
    fpversion = Column(String(20), nullable=True)
    template = Column(Text, nullable=True)
    template1 = Column(Text, nullable=True)
    template2 = Column(Text, nullable=True)
    template3 = Column(Text, nullable=True)
    template4 = Column(Text, nullable=True)








