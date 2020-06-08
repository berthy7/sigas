from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property


class Modelo(Serializable, Base):
    way = {'marca': {}}

    __tablename__ = 'modelo'

    id = Column(Integer, primary_key=True)
    nombre= Column(String(100), nullable=False)
    fkmarca = Column(Integer, ForeignKey('marca.id'), nullable=True)
    estado = Column(Boolean, default=True)

    marca = relationship('Marca')


