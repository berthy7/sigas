from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property


class Invitado(Serializable, Base):
    way = {'condominio': {},'vehiculos': {},'nropase': {},'amistad': {}}

    __tablename__ = 'invitado'

    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=True)
    nombre = Column(String(100), nullable=True)
    apellidop = Column(String(100), nullable=True)
    apellidom = Column(String(100), nullable=True)
    sexo = Column(String(10), nullable=True)
    ci = Column(String(50), nullable=True)
    expendido = Column(String(20), nullable=True)
    telefono = Column(String(100), nullable=True)
    foto = Column(Text, nullable=True)
    descripcion = Column(Text, nullable=True)
    permanente = Column(Boolean, default=False)
    fknropase = Column(Integer, ForeignKey('nropase.id'), nullable=True)
    huella = Column(Text, nullable=True)
    rostro = Column(Text, nullable=True)
    estado = Column(Boolean, default=True)
    enabled = Column(Boolean, default=False)
    fkcondominio = Column(Integer, ForeignKey('condominio.id'), nullable=True)

    condominio = relationship('Condominio')
    vehiculos = relationship('Vehiculo')
    nropase = relationship('Nropase')
    amistad = relationship('Amistad')

    def get_dict(self, way=None):
        aux = super().get_dict(way)

        lista_vehiculos = list()

        for v in self.vehiculos:
            if v.fknropase:
                fknropase = v.fknropase
                nropase = v.nropase.tarjeta
            else:
                fknropase = None
                nropase = ""

            if v.fkmodelo:
                fkmodelo = v.fkmodelo
                nombremodelo = v.modelo.nombre
            else:
                fkmodelo = None
                nombremodelo = ""

                lista_vehiculos.append(dict(id=v.id, placa=v.placa, fktipo=v.fktipo, fkcolor=v.fkcolor, fkmarca=v.fkmarca,
                                            nombremarca=v.marca.nombre, fkmodelo=fkmodelo, nombremodelo=nombremodelo,
                                            fknropase=fknropase, nropase=nropase))

        for v in self.amistad:
            aux['fkresidente'] = v.fkresidente

            break


        aux['vehiculos'] = lista_vehiculos
        aux['fullname'] = str(self.nombre) + " " + str(self.apellidop) + " " + str(self.apellidom)

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


        return aux


class Amistad(Serializable, Base):
    way = {'residente': {},'invitado': {}}

    __tablename__ = 'amistad'

    id = Column(Integer, primary_key=True)
    fkresidente = Column(Integer, ForeignKey('residente.id'), nullable=True)
    fkinvitado = Column(Integer, ForeignKey('invitado.id'), nullable=True)
    proveedor = Column(Boolean, default=False)
    estado = Column(Boolean, default=True)

    residente = relationship('Residente')
    invitado = relationship('Invitado')
