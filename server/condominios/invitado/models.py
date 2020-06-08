from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property


class Invitado(Serializable, Base):
    way = {'vehiculos': {},'nropase': {},'amistad': {}}

    __tablename__ = 'invitado'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=True)
    apellidop = Column(String(100), nullable=True)
    apellidom = Column(String(100), nullable=True)
    sexo = Column(String(10), nullable=True)
    ci = Column(String(50), nullable=True)
    expendido = Column(String(20), nullable=True)
    telefono = Column(String(100), nullable=True)
    descripcion = Column(Text, nullable=True)
    permanente = Column(Boolean, default=False)
    fknropase = Column(Integer, ForeignKey('nropase.id'), nullable=True)
    estado = Column(Boolean, default=True)

    vehiculos = relationship('Vehiculo')
    nropase = relationship('Nropase')
    amistad = relationship('Amistad')

    def get_dict(self, way=None):
        aux = super().get_dict(way)

        lista_vehiculos = list()

        for v in self.vehiculos:
            lista_vehiculos.append(dict(id=v.id,placa=v.placa, tipo=v.tipo, color=v.color,fkmarca=v.fkmarca, nombremarca=v.marca.nombre,fkmodelo=v.fkmodelo,nombremodelo=v.modelo.nombre,controlacceso=v.controlacceso))

        for v in self.amistad:
            aux['fkresidente'] = v.fkresidente

            break


        aux['vehiculos'] = lista_vehiculos

        return aux

    @hybrid_property
    def fullname(self):
        aux = ""
        if self.nombre is not None:
            aux = self.nombre + " "
        else:
            aux = " "

        if self.apellidop is not None:
            aux = aux + self.apellidop + " "
        else:
            aux = " "

        if self.apellidom is not None:
            aux += self.apellidom
        else:
            aux = " "

        return aux


class Amistad(Serializable, Base):
    way = {'residente': {},'invitado': {}}

    __tablename__ = 'amistad'

    id = Column(Integer, primary_key=True)
    fkresidente = Column(Integer, ForeignKey('residente.id'), nullable=True)
    fkinvitado = Column(Integer, ForeignKey('invitado.id'), nullable=True)

    estado = Column(Boolean, default=True)

    residente = relationship('Residente')
    invitado = relationship('Invitado')
