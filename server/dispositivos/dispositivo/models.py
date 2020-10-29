from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property
from ...condominios.condominio.models import *


class Dispositivo(Serializable, Base):
    way = {'condominio': {},'tipodispositivo': {},'configuraciondispositivo': {},'interpretes': {'interprete': {}},'cerraduras': {'entrada': {}}}

    __tablename__ = 'dispositivo'

    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=True)
    ip = Column(String(100), nullable=False)
    puerto = Column(Integer, nullable=False)
    descripcion = Column(String(100), nullable=True, default="")
    modelo = Column(String(100), nullable=True, default="")
    fkcondominio = Column(Integer, ForeignKey('condominio.id'), nullable=True)
    fktipodispositivo = Column(Integer, ForeignKey('tipodispositivo.id'), nullable=True)
    situacion = Column(Boolean, nullable=True, default=True)
    estado = Column(Boolean,  default=True)

    condominio = relationship('Condominio')
    configuraciondispositivo = relationship('Configuraciondispositivo')
    interpretes = relationship('Dispositivointerprete')
    tipodispositivo = relationship('Tipodispositivo')
    cerraduras = relationship('Cerraduras', cascade="save-update, merge, delete, delete-orphan")

class Tipodispositivo(Serializable, Base):
    way = {}

    __tablename__ = 'tipodispositivo'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    estado = Column(Boolean,  default=True)


class Cerraduras(Serializable, Base):
    way = {'dispositivo': {},'entrada': {}}

    __tablename__ = 'cerraduras'

    id = Column(Integer, primary_key=True)
    numero = Column(Integer, nullable=False)
    nombre = Column(String(100), nullable=True, default="")
    fkdispositivo = Column(Integer, ForeignKey('dispositivo.id'), nullable=True)
    fkentrada = Column(Integer, ForeignKey('entrada.id'), nullable=True)
    estado = Column(Boolean, default=True)
    linea = Column(Boolean, default=True)

    dispositivo = relationship('Dispositivo')
    entrada = relationship('Entrada')



class Configuraciondispositivo(Serializable, Base):
    way = {}

    __tablename__ = 'configuraciondispositivo'

    id = Column(Integer, primary_key=True)
    codigo = Column(Text, nullable=False)
    tarjeta = Column(Text, nullable=False)
    situacion = Column(String(100), default="Acceso")  #Acceso Denegado Configuracion_inicial Abrir
    fkdispositivo = Column(Integer, ForeignKey('dispositivo.id'), nullable=True)
    estado = Column(Boolean, default=True)
    codigoacceso = Column(String(100), nullable=True, default="")

    dispositivo = relationship('Dispositivo')

class Interprete(Serializable, Base):
    way = {}

    __tablename__ = 'interprete'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=True, default="")
    estado = Column(Boolean, default=True)


class Dispositivointerprete(Serializable, Base):
    way = {'dispositivo': {},'interprete': {}}

    __tablename__ = 'dispositivointerprete'

    id = Column(Integer, primary_key=True)
    fkdispositivo = Column(Integer, ForeignKey('dispositivo.id'), nullable=True)
    fkinterprete = Column(Integer, ForeignKey('interprete.id'), nullable=True)
    estado = Column(Boolean, default=True)

    dispositivo = relationship('Dispositivo')
    interprete = relationship('Interprete')



class Dispositivoeventos(Serializable, Base):
    way = {}

    __tablename__ = 'dispositivoeventos'

    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)







