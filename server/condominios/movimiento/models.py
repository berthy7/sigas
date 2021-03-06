from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence,Time
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ..vehiculo.models import *
from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property


class Movimiento(Serializable, Base):
    way = {'invitacion': {},'invitado': {},'residente': {},'conductor': {},'tipodocumento': {},'tipodocumento_conductor': {},'vehiculo': {'tipo': {},'color': {},'marca': {},'modelo': {}},'tipopase': {},'autorizacion': {},'domicilio': {},'areasocial': {},'nropase': {}}

    __tablename__ = 'movimiento'

    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=True)
    fkinvitacion = Column(Integer, ForeignKey('invitacion.id'), nullable=True)
    fktipodocumento = Column(Integer, ForeignKey('tipo_documento.id'), nullable=True)
    fkinvitado = Column(Integer, ForeignKey('invitado.id'), nullable=True)
    fkvehiculo = Column(Integer, ForeignKey('vehiculo.id'), nullable=True)
    fechai = Column(DateTime, nullable=True)
    fechaf = Column(DateTime, nullable=True)
    fechar = Column(DateTime, nullable=True)
    fkresidente = Column(Integer, ForeignKey('residente.id'), nullable=True)
    fkautorizacion = Column(Integer, ForeignKey('autorizacion.id'), nullable=True)

    fkdomicilio = Column(Integer, ForeignKey('domicilio.id'), nullable=True)
    fkareasocial = Column(Integer, ForeignKey('areasocial.id'), nullable=True)
    fktipopase = Column(Integer, ForeignKey('tipo_pase.id'), nullable=True)
    codigoautorizacion = Column(Text, nullable=True)
    fknropase = Column(Integer, ForeignKey('nropase.id'), nullable=True)
    observacion = Column(Text, nullable=True)
    tipo = Column(String(50), nullable=False) #tipo = Vehicular, Peatonal,

    cantpasajeros = Column(Integer, nullable=True)
    fktipodocumento_conductor = Column(Integer, ForeignKey('tipo_documento.id'), nullable=True)
    fkconductor = Column(Integer, ForeignKey('invitado.id'), nullable=True)
    visita = Column(Boolean, default=True)

    estado = Column(Boolean, default=True)

    descripcion_fechai = Column(String(50), nullable=True,default='-----')
    descripcion_fechaf = Column(String(50), nullable=True, default='-----')
    descripcion_documento = Column(String(20), nullable=True, default=' ')
    descripcion_ci_invitado = Column(String(50), nullable=True, default=' ')
    descripcion_nombre_invitado = Column(String(100), nullable=True, default=' ')
    descripcion_nombre_conductor = Column(String(100), nullable=True, default=' ')
    descripcion_placa = Column(String(50), nullable=True, default=' ')
    descripcion_tipo = Column(String(50), nullable=True, default=' ')
    descripcion_marca = Column(String(50), nullable=True, default=' ')
    descripcion_modelo = Column(String(50), nullable=True, default=' ')
    descripcion_color = Column(String(20), nullable=True, default=' ')
    descripcion_destino = Column(String(50), nullable=True, default=' ')
    descripcion_nropase = Column(String(50), nullable=True, default=' ')

    invitacion = relationship('Invitacion')
    invitado = relationship('Invitado', foreign_keys=[fkinvitado])
    conductor = relationship('Invitado', foreign_keys=[fkconductor])

    tipodocumento_conductor = relationship('Tipodocumento', foreign_keys=[fktipodocumento_conductor])
    tipodocumento = relationship('Tipodocumento', foreign_keys=[fktipodocumento])
    vehiculo = relationship('Vehiculo')
    tipopase = relationship('Tipopase')
    autorizacion = relationship('Autorizacion')
    domicilio = relationship('Domicilio')
    areasocial = relationship('Areasocial')
    nropase = relationship('Nropase')
    residente = relationship('Residente')

    def get_dict(self, way=None):
        aux = super().get_dict(way)
        if aux['fechai'] == 'None':
            aux['fechai'] = None
        else:
            aux['fechai'] = self.fechai.strftime('%d/%m/%Y %H:%M:%S')

        if aux['fechaf'] == 'None':
            aux['fechaf'] = None
        else:
            aux['fechaf'] = self.fechaf.strftime('%d/%m/%Y %H:%M:%S')

        if aux['fechar'] == 'None':
            aux['fechar'] = None
        else:
            aux['fechar'] = self.fechar.strftime('%d/%m/%Y %H:%M:%S')

        return aux


class Tipodocumento(Serializable, Base):
    way = {}

    __tablename__ = 'tipo_documento'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    estado = Column(Boolean, default=True)


class Tipopase(Serializable, Base):
    way = {}

    __tablename__ = 'tipo_pase'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    estado = Column(Boolean, default=True)


class Autorizacion(Serializable, Base):
    way = {}

    __tablename__ = 'autorizacion'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    estado = Column(Boolean, default=True)



