from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property

class Vehiculo(Serializable, Base):
    way = {'residente': {},'invitado': {},'marca': {},'modelo': {},'nropase': {}}

    __tablename__ = 'vehiculo'

    id = Column(Integer, primary_key=True)
    placa = Column(String(100), nullable=False)
    tipo = Column(String(100), nullable=False)
    color = Column(String(100), nullable=False)
    fkmarca = Column(Integer, ForeignKey('marca.id'), nullable=True)
    fkmodelo = Column(Integer, ForeignKey('modelo.id'), nullable=True)
    fkresidente = Column(Integer, ForeignKey('residente.id'), nullable=True)
    fkinvitado = Column(Integer, ForeignKey('invitado.id'), nullable=True)
    fknropase = Column(Integer, ForeignKey('nropase.id'), nullable=True)
    estado = Column(Boolean, default=True)

    residente = relationship('Residente')
    invitado = relationship('Invitado')
    marca = relationship('Marca')
    modelo = relationship('Modelo')
    nropase = relationship('Nropase')

    def get_dict(self, way=None):
        aux = super().get_dict(way)

        return aux





