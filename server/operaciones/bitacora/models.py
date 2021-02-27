from sqlalchemy import Column, Integer, String, DateTime, BigInteger,Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from server.database.models import Base
from server.database.serializable import Serializable
import pytz

global fecha_zona
fecha_zona = datetime.now(pytz.timezone('America/La_Paz'))


class Bitacora(Serializable, Base):
    way = {'usuario': {}}

    __tablename__ = 'bitacora'

    id = Column(BigInteger,  primary_key=True)
    fkusuario = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    ip = Column(String(100), nullable=True, default="")
    accion = Column(String(200), nullable=True, default="")
    fecha = Column(DateTime, nullable=False, default=fecha_zona)
    tabla = Column(String(200), nullable=True, default="")
    identificador = Column(Integer, nullable=True)

    usuario = relationship('Usuario')
