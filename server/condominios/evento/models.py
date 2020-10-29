from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence,Time
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property


class Evento(Serializable, Base):
    way = {'tipoevento': {},'residente': {},'invitaciones': {},'domicilio': {},'areasocial': {}}

    __tablename__ = 'evento'

    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=True)
    descripcion = Column(String(255), nullable=True, default="")
    fktipoevento = Column(Integer, ForeignKey('tipo_evento.id'), nullable=True)
    fkresidente = Column(Integer, ForeignKey('residente.id'), nullable=True)
    fechai = Column(Date, nullable=True)
    fechaf = Column(Date, nullable=True)
    horai = Column(Time, nullable=True)
    horaf = Column(Time, nullable=True)
    fkdomicilio = Column(Integer, ForeignKey('domicilio.id'), nullable=True)
    fkareasocial = Column(Integer, ForeignKey('areasocial.id'), nullable=True)
    situacion = Column(String(100), nullable=True, default="")
    multiacceso = Column(Boolean, default=False, nullable=True)
    sinregistro = Column(Boolean, default=False, nullable=True)

    estado = Column(Boolean, default=True)

    tipoevento = relationship('TipoEvento')
    residente = relationship('Residente')
    domicilio = relationship('Domicilio')
    areasocial = relationship('Areasocial')

    invitaciones = relationship("Invitacion", cascade="save-update, merge, delete, delete-orphan")

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

        if aux['horai'] == 'None':
            aux['horai'] = "----"
        else:
            aux['horai'] = self.horai.strftime("%H:%M")

        if aux['horaf'] == 'None':
            aux['horaf'] = "----"
        else:
            aux['horaf'] = self.horaf.strftime("%H:%M")

        return aux


class TipoEvento(Serializable, Base):
    way = {}

    __tablename__ = 'tipo_evento'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    estado = Column(Boolean, default=True)


class Invitacion(Serializable, Base):
    way = {'evento': {},'invitado': {},'tipopase': {}}

    __tablename__ = 'invitacion'

    id = Column(Integer, primary_key=True)
    fkevento = Column(Integer, ForeignKey('evento.id'), nullable=True)
    fkinvitado = Column(Integer, ForeignKey('invitado.id'), nullable=True)
    fktipopase = Column(Integer, ForeignKey('tipo_pase.id'), nullable=True)
    codigoautorizacion = Column(Text, nullable=True, default="")


    estado = Column(Boolean, default=True)

    evento = relationship('Evento')
    invitado = relationship('Invitado')
    tipopase = relationship('Tipopase')

    def get_dict(self, way=None):
        aux = super().get_dict(way)
        aux['nombre']= self.invitado.nombre
        aux['apellidop'] = self.invitado.apellidop
        aux['apellidom']= self.invitado.apellidom
        aux['ci'] = self.invitado.ci

        return aux

class Codigoqr(Serializable, Base):
    way = {}

    __tablename__ = 'codigoqr'

    id = Column(Integer, primary_key=True)
    codigo = Column(Text, nullable=False)
    tarjeta = Column(Text, nullable=False)
    situacion = Column(String(100), default="Acceso")
    dispositivo = Column(String(100))
    estado = Column(Boolean, default=True)



