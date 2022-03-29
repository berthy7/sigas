from .models import *
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ...usuarios.usuario.managers import *
from ..invitado.models import *
from ..vehiculo.managers import *

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font



class ProvperManager(SuperManager):
    def __init__(self, db):
        super().__init__(Invitado, db)

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.permanente == True).all()

    def listar_x_residente(self,usuario):

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.enabled == True).filter(self.entity.permanente == True).order_by(
                self.entity.apellidop.asc()).all()

        else:
            return self.db.query(self.entity).filter(self.entity.enabled == True).filter(self.entity.fkcondominio == usuario.fkcondominio).filter(self.entity.permanente == True).order_by(
                self.entity.apellidop.asc()).all()


    def obtener_x_id(self,idinvitado):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.id == idinvitado).first()

    def obtener_x_ci(self,ciinvitado):

        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.ci == ciinvitado).first()

    def insert(self, diccionary):

        if diccionary['fkcondominio'] == '':
            diccionary['fkcondominio'] = None

        if diccionary['fknropase'] == '':
            diccionary['fknropase'] = None

        objeto = ProvperManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()
        objeto.vehiculos = []
        objeto.enabled = True

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro provper.", fecha=fecha,tabla="invitado", identificador=a.id)
        super().insert(b)

        if diccionary['fkresidente']:

            amistadActual = self.db.query(Amistad).filter(Amistad.fkresidente == diccionary['fkresidente']).filter(Amistad.fkinvitado == a.id).first()

            if amistadActual == None:
                amistad = Amistad(fkresidente=diccionary['fkresidente'], fkinvitado=a.id,proveedor=True)
                super().insert(amistad)

        for vehi in diccionary['vehiculos']:
            VehiculoManager(self.db).registrar_vehiculo_invitado(vehi,a.id)

        return a

    def update(self, diccionary):

        objeto = ProvperManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico provper.", fecha=fecha,tabla="invitado", identificador=a.id)
        super().insert(b)

        if diccionary['fkresidente']:

            amistadActual = self.db.query(Amistad).filter(Amistad.fkresidente == diccionary['fkresidente']).filter(Amistad.fkinvitado == a.id).first()

            if amistadActual == None:
                amistad = Amistad(fkresidente=diccionary['fkresidente'], fkinvitado=a.id,proveedor=True)
                super().insert(amistad)

        for vehi in diccionary['vehiculos']:
            VehiculoManager(self.db).registrar_vehiculo_invitado(vehi,a.id)

        return a


    def registrar_invitado(self, diccionario):
        usuario = UsuarioManager(self.db).get_by_pass(diccionario['user'])
        nombre = diccionario['nombre']
        apellidop = diccionario['apellidop']
        apellidom = diccionario['apellidom']
        ci = diccionario['ci']
        expendido = diccionario['expendido']

        invitado = ProvperManager(self.db).obtener_x_ci(ci)

        if invitado:
            return invitado
        else:
            dict_invitado = dict(nombre=nombre,apellidop=apellidop,apellidom=apellidom,ci=ci, expendido=expendido)

            objeto = ProvperManager(self.db).entity(**dict_invitado)
            fecha = BitacoraManager(self.db).fecha_actual()
            a = super().insert(objeto)
            b = Bitacora(fkusuario=diccionario['user'], ip=diccionario['ip'], accion="Registro provper.", fecha=fecha,
                         tabla="invitado", identificador=a.id)
            super().insert(b)

        if usuario.fkresidente != None:
            amistad = Amistad(fkresidente=usuario.fkresidente, fkinvitado=a.id)
            super().insert(amistad)

        return a

    def registrar_conductor(self, diccionario):
        usuario = UsuarioManager(self.db).get_by_pass(diccionario['user'])
        nombre = diccionario['nombre_conductor']
        apellidop = diccionario['apellidop_conductor']
        apellidom = diccionario['apellidom_conductor']
        ci = diccionario['ci_conductor']
        expendido = diccionario['expendido_conductor']

        invitado = ProvperManager(self.db).obtener_x_ci(ci)

        if invitado:
            return invitado
        else:
            dict_invitado = dict(nombre=nombre, apellidop=apellidop, apellidom=apellidom, ci=ci, expendido=expendido)

            objeto = ProvperManager(self.db).entity(**dict_invitado)
            fecha = BitacoraManager(self.db).fecha_actual()
            a = super().insert(objeto)
            b = Bitacora(fkusuario=diccionario['user'], ip=diccionario['ip'], accion="Registro conductor de taxi.", fecha=fecha,
                         tabla="invitado", identificador=a.id)
            super().insert(b)

        return a

    def actualizar_invitado(self, diccionario):

        id = diccionario['fkinvitado']
        nombre = diccionario['nombre']
        apellidop = diccionario['apellidop']
        apellidom = diccionario['apellidom']
        ci = diccionario['ci']
        expendido = diccionario['expendido']

        invitado = ProvperManager(self.db).obtener_x_id(id)

        invitado.nombre = nombre
        invitado.apellidop = apellidop
        invitado.apellidom = apellidom
        invitado.ci = ci
        invitado.expendido = expendido

        super().update(invitado)

    def actualizar_conductor(self, diccionario):

        id = diccionario['fkconductor']
        nombre = diccionario['nombre_conductor']
        apellidop = diccionario['apellidop_conductor']
        apellidom = diccionario['apellidom_conductor']
        ci = diccionario['ci_conductor']
        expendido = diccionario['expendido_conductor']

        invitado = ProvperManager(self.db).obtener_x_id(id)

        invitado.nombre = nombre
        invitado.apellidop = apellidop
        invitado.apellidom = apellidom
        invitado.ci = ci
        invitado.expendido = expendido

        super().update(invitado)



