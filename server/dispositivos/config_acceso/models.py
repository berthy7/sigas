from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property
from ...condominios.condominio.models import *


class Configacceso(Serializable, Base):
    way = {'condominio': {},'configcerraduras': {'cerraduras': {'entrada': {},'dispositivo': {}}},'configtarjetas': {'tarjetas': {}}}

    __tablename__ = 'configuracionacceso'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=True, default="")
    codigoacceso = Column(String(100), nullable=True, default="")

    fkcondominio = Column(Integer, ForeignKey('condominio.id'), nullable=True)
    estado = Column(Boolean,  default=True)

    condominio = relationship('Condominio')
    configcerraduras = relationship('Configaccesocerraduras', cascade="save-update, merge, delete, delete-orphan")
    configtarjetas = relationship('Configaccesotarjetas', cascade="save-update, merge, delete, delete-orphan")

class Configaccesocerraduras(Serializable, Base):
    way = {'configacceso': {},'cerraduras': {}}

    __tablename__ = 'accesocerraduras'

    id = Column(Integer, primary_key=True)
    fkconfigacceso = Column(Integer, ForeignKey('configuracionacceso.id'), nullable=True)
    fkcerraduras = Column(Integer, ForeignKey('cerraduras.id'), nullable=True)
    estado = Column(Boolean, default=True)

    configacceso = relationship('Configacceso')
    cerraduras = relationship('Cerraduras')


class Configaccesotarjetas(Serializable, Base):
    way = {'configacceso': {},'tarjetas': {}}

    __tablename__ = 'accesotarjetas'

    id = Column(Integer, primary_key=True)
    fkconfigacceso = Column(Integer, ForeignKey('configuracionacceso.id'), nullable=True)
    fknropase = Column(Integer, ForeignKey('nropase.id'), nullable=True)
    estado = Column(Boolean, default=True)

    configacceso = relationship('Configacceso')
    tarjetas = relationship('Nropase')







