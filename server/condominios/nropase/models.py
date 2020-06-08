from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property


class Nropase(Serializable, Base):
    way = {'condominios': {}}

    __tablename__ = 'nropase'

    id = Column(Integer, primary_key=True)
    numero = Column(Text, default=" ")
    tarjeta = Column(Text, nullable=True)
    tipo = Column(String(200), default="Visita") #tipo = Residente, Visita, Proveedores,provper,Excepcion
    situacion = Column(String(200), default="") #situacion = ocupado,Libre
    estado = Column(Boolean, default=True)

    condominios = relationship('CondominioPases', cascade="save-update, merge, delete, delete-orphan")


    def get_dict(self, way=None):
        aux = super().get_dict(way)
        lista_condominios = list()


        for a in self.condominios:
            lista_condominios.append(
                dict(id=a.id, fkcondominio=a.fkcondominio, nombre=a.condominio.nombre))

        aux['condominios'] = lista_condominios

        return aux
