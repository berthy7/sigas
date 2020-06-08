from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ...database.models import Base
from server.database.serializable import Serializable
from sqlalchemy.ext.hybrid import hybrid_property


class Residente(Serializable, Base):
    way = {'vehiculos': {},'domicilios': {},'acceso': {},'usuario': {},'nropase': {}}

    __tablename__ = 'residente'

    id = Column(Integer, primary_key=True)
    codigo = Column(String(100), nullable=True)
    nombre = Column(String(100), nullable=False)
    apellidop = Column(String(100), nullable=False)
    apellidom = Column(String(100), nullable=True)
    sexo = Column(String(10), nullable=True)
    ci = Column(String(50), nullable=False)
    expendido = Column(String(20), nullable=True)
    fechanacimiento = Column(Date, nullable=True)
    telefono = Column(String(100), nullable=True)
    foto = Column(Text,nullable=True)
    tipo = Column(String(20), nullable=True) #tipo = Propietario, Inquilino, Co-propietario,provper
    correo = Column(String(255), nullable=True)
    fknropase = Column(Integer, ForeignKey('nropase.id'), nullable=True)
    estado = Column(Boolean, default=True)


    domicilios = relationship('ResidenteDomicilio', cascade="save-update, merge, delete, delete-orphan")
    vehiculos = relationship('Vehiculo')
    acceso = relationship('ResidenteAcceso', cascade="save-update, merge, delete, delete-orphan")
    usuario = relationship('Usuario')
    nropase = relationship('Nropase')

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
        else:
            aux = " "

        return aux

    def get_dict(self, way=None):
        aux = super().get_dict(way)
        lista_domicilios = list()
        lista_vehiculos = list()
        aux['fullname'] = str(self.nombre) + " " + str(self.apellidop) + " " + str(self.apellidom)

        if aux['fknropase'] == 'None':
            aux['idtarjeta'] = ""
            aux['nrotarjeta'] = ""
        else:
            aux['idtarjeta'] = str(self.nropase.id)
            aux['nrotarjeta'] = str(self.nropase.tarjeta)


        if aux['fechanacimiento'] == 'None':
            aux['fechanacimiento'] = None
        else:
            aux['fechanacimiento'] = self.fechanacimiento.strftime('%d/%m/%Y')

        for a in self.domicilios:
            lista_domicilios.append(dict(id=a.id,fkdomicilio= a.fkdomicilio,codigo=a.domicilio.codigo, nombre=a.domicilio.nombre, vivienda=a.vivienda))

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



            lista_vehiculos.append(dict(id=v.id,placa=v.placa, tipo=v.tipo, color=v.color,fkmarca=v.fkmarca, nombremarca=v.marca.nombre,fkmodelo=fkmodelo,nombremodelo=nombremodelo,fknropase=fknropase,nropase=nropase))

        for acce in self.acceso:
            aux['idacceso'] = acce.id
            aux['fechai'] = acce.fechai.strftime('%d/%m/%Y')
            aux['fechaf'] = acce.fechaf.strftime('%d/%m/%Y')
            aux['estadoacceso'] = acce.estado
            break

        for use in self.usuario:
            aux['username'] = use.username
            break

        aux['domicilios'] = lista_domicilios
        aux['vehiculos'] = lista_vehiculos

        return aux


class ResidenteDomicilio(Serializable, Base):
    way = {'residente': {},'domicilio': {}}

    __tablename__ = 'residentedomicilio'

    id = Column(Integer, primary_key=True)
    fkresidente = Column(Integer, ForeignKey('residente.id'), nullable=True)
    fkdomicilio = Column(Integer, ForeignKey('domicilio.id'), nullable=True)
    vivienda = Column(Boolean, default=False)
    estado = Column(Boolean, default=True)

    residente = relationship('Residente')
    domicilio = relationship('Domicilio')


class ResidenteAcceso(Serializable, Base):
    way = {'residente': {}}

    __tablename__ = 'residenteacceso'

    id = Column(Integer, primary_key=True)
    fkresidente = Column(Integer, ForeignKey('residente.id'), nullable=True)
    fechai = Column(Date, nullable=True)
    fechaf = Column(Date, nullable=True)
    estado = Column(Boolean, default=True)

    residente = relationship('Residente')


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


