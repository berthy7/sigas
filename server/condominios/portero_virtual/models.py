from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence,Time
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ..vehiculo.models import *
from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property


class Porterovirtual(Serializable, Base):
    way = {'invitacion': {},'invitado': {},'residente': {},'tipopase': {},'autorizacion': {},'tipodocumento': {},'cerradura': {'dispositivo': {}}}

    __tablename__ = 'portero_virtual'

    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=True)
    fkinvitacion = Column(Integer, ForeignKey('invitacion.id'), nullable=True)

    fkcerradura = Column(Integer, ForeignKey('cerraduras.id'), nullable=True)
    fktipodocumento = Column(Integer, ForeignKey('tipo_documento.id'), nullable=True)
    fkinvitado = Column(Integer, ForeignKey('invitado.id'), nullable=True)
    fechai = Column(DateTime, nullable=True)
    fechaf = Column(DateTime, nullable=True)
    fechar = Column(DateTime, nullable=True)
    fkresidente = Column(Integer, ForeignKey('residente.id'), nullable=True)
    fkautorizacion = Column(Integer, ForeignKey('autorizacion.id'), nullable=True)

    fktipopase = Column(Integer, ForeignKey('tipo_pase.id'), nullable=True)
    codigoautorizacion = Column(Text, nullable=True)
    observacion = Column(Text, nullable=True)
    tipo = Column(String(50), nullable=False) #tipo = Residente, Visita,
    sincronizacion = Column(Boolean, default=False)
    estado = Column(Boolean, default=True)

    invitacion = relationship('Invitacion')
    cerradura = relationship('Cerraduras')
    tipodocumento = relationship('Tipodocumento')
    invitado = relationship('Invitado')

    tipopase = relationship('Tipopase')
    autorizacion = relationship('Autorizacion')
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
