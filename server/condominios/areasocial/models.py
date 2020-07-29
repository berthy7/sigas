from sqlalchemy import Column, Integer, String, Boolean, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from ..condominio.models import *

from ...database.models import Base
from ...database.serializable import Serializable


class Areasocial(Serializable, Base):
    way = {'condominio': {}}

    __tablename__ = 'areasocial'

    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=True)
    nombre = Column(String(100), nullable=True)
    ubicacion = Column(String(100), nullable=True)
    fkcondominio = Column(Integer, ForeignKey('condominio.id'), nullable=True)
    estado = Column(Boolean, default=True)

    condominio = relationship('Condominio')
