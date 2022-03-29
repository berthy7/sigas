from sqlalchemy import Column, Integer, String, Boolean, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from ...database.models import Base
from ...database.serializable import Serializable


class Domicilio(Serializable, Base):
    way = {'condominio': {}}

    __tablename__ = 'domicilio'

    id = Column(Integer, primary_key=True)
    codigo = Column(String(100), nullable=True)
    numero = Column(String(100), nullable=True)
    ubicacion = Column(String(100), nullable=True)
    fkcondominio = Column(Integer, ForeignKey('condominio.id'), nullable=True)
    tipo = Column(String(100), nullable=True)
    interno = Column(String(100), nullable=True)
    estado = Column(Boolean, default=True)
    codigocondominio = Column(String(100), nullable=True)

    condominio = relationship('Condominio')

    @hybrid_property
    def nombre(self):
        aux = ""
        if self.numero:
            aux = self.ubicacion + " " + str(self.numero)
        else:
            aux = self.ubicacion
        return aux
