from sqlalchemy import Column, Integer, String, Boolean, Sequence, Date,Text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from ...database.serializable import Serializable


class Condominio(Serializable, Base):
    way = {'nropase': {},'entradas': {'entrada': {}}}

    __tablename__ = 'condominio'

    id = Column(Integer, primary_key=True)
    codigo = Column(String(100), nullable=True)
    nombre = Column(String(100), nullable=True)
    cant_casas = Column(Integer, nullable=True)
    cant_departamentos = Column(Integer, nullable=True)
    cant_vehiculos = Column(Integer, nullable=True)
    cant_residentes = Column(Integer, nullable=True)
    cant_tarjetas = Column(Integer, nullable=True)
    contrato = Column(Integer, nullable=True)
    fechai = Column(Date, nullable=True)
    fechaf = Column(Date, nullable=True)
    singuardia = Column(Boolean, default=False, nullable=True)
    estado = Column(Boolean, default=True)
    ip_publica = Column(String(100), nullable=True, default="")
    ip_privada = Column(String(100), nullable=True, default="")
    puerto = Column(String(100), nullable=True, default="")
    invitacionpaselibre = Column(Boolean, default=False, nullable=True)
    invitacionmultiple = Column(Boolean, default=False, nullable=True)



    nropase = relationship('CondominioPases')
    entradas = relationship('Condominioentrada', cascade="save-update, merge, delete, delete-orphan")

    def get_dict(self, way=None):
        aux = super().get_dict(way)
        if aux['fechai'] == 'None':
            aux['fechai'] = None
        else:
            aux['fechai'] = self.fechai.strftime('%d/%m/%Y')

        if aux['fechaf'] == 'None':
            aux['fechaf'] = None
        else:
            aux['fechaf'] = self.fechaf.strftime('%d/%m/%Y')

        return aux



class CondominioPases(Serializable, Base):
    way = {'condominio': {},'nropase': {}}

    __tablename__ = 'condominiopases'

    id = Column(Integer, primary_key=True)
    fkcondominio = Column(Integer, ForeignKey('condominio.id'), nullable=True)
    fknropase = Column(Integer, ForeignKey('nropase.id'), nullable=True)
    estado = Column(Boolean, default=True)


    condominio = relationship('Condominio')
    nropase = relationship('Nropase')


class Condominioentrada(Serializable, Base):
    way = {'condominio': {}, 'entrada': {}}
    __tablename__ = 'condominioentrada'

    id = Column(Integer, primary_key=True)
    fkcondominio = Column(Integer, ForeignKey('condominio.id'), nullable=True)
    fkentrada = Column(Integer, ForeignKey('entrada.id'), nullable=True)
    estado = Column(Boolean, default=True)

    condominio = relationship('Condominio')
    entrada = relationship('Entrada')


class Entrada(Serializable, Base):
    way = {}
    __tablename__ = 'entrada'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=True)
    estado = Column(Boolean, default=True)





