from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property

class Vehiculo(Serializable, Base):
    way = {'residente': {},'invitado': {},'tipo': {},'color': {},'marca': {},'modelo': {},'nropase': {}}

    __tablename__ = 'vehiculo'

    id = Column(Integer, primary_key=True)
    placa = Column(String(100), nullable=False)
    fktipo = Column(Integer, ForeignKey('tipo_vehiculo.id'), nullable=True)
    fkcolor = Column(Integer, ForeignKey('color.id'), nullable=True)
    fkmarca = Column(Integer, ForeignKey('marca.id'), nullable=True)
    fkmodelo = Column(Integer, ForeignKey('modelo.id'), nullable=True)
    fkresidente = Column(Integer, ForeignKey('residente.id'), nullable=True)
    fkinvitado = Column(Integer, ForeignKey('invitado.id'), nullable=True)
    fknropase = Column(Integer, ForeignKey('nropase.id'), nullable=True)
    estado = Column(Boolean, default=True)

    residente = relationship('Residente')
    invitado = relationship('Invitado')
    tipo = relationship('Tipovehiculo')
    color = relationship('Color')
    marca = relationship('Marca')
    modelo = relationship('Modelo')
    nropase = relationship('Nropase')

    def get_dict(self, way=None):
        aux = super().get_dict(way)

        return aux


class Tipovehiculo(Serializable, Base):
    way = {}

    __tablename__ = 'tipo_vehiculo'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    estado = Column(Boolean, default=True)

class Color(Serializable, Base):
    way = {}

    __tablename__ = 'color'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    estado = Column(Boolean, default=True)




