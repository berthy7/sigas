from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property

class RegistrosControlador(Serializable, Base):
    way = {'dispositivo': {}}

    __tablename__ = 'registroscontrolador'

    id = Column(Integer, primary_key=True)
    tarjeta = Column(Text, nullable=False)
    codigo = Column(Text, nullable=False)
    verificado = Column(Integer, nullable=False)
    puerta = Column(Integer, nullable=False)
    evento = Column(Integer, nullable=False)
    estado = Column(Integer, nullable=False)
    time = Column(DateTime)
    fkdispositivo = Column(Integer, ForeignKey('dispositivo.id'), nullable=True)
    sincronizado = Column(Boolean, default=False)

    dispositivo = relationship('Dispositivo')