from .models import *
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ...usuarios.usuario.managers import *
from ..residente.managers import *
from ..marca.managers import *
from ..modelo.managers import *
from ..nropase.managers import *

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font



class VehiculoManager(SuperManager):
    def __init__(self, db):
        super().__init__(Vehiculo, db)

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.placa.asc()).all()

    def listar_disponibles(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(and_(self.entity.fkresidente == None,self.entity.fkinvitado == None)).order_by(self.entity.placa.asc()).all()


    def obtener_x_id(self,idvehiculo):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.id == idvehiculo).first()

    def obtener_x_placa(self,placavehiculo):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.placa == placavehiculo).first()

    def consultar_vehiculo_invitado(self,idvehiculo,idinvitado):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.id == idvehiculo).filter(self.entity.fkinvitado == idinvitado).first()

    def consultar_vehiculo(self,idvehiculo,idresidente):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.id == idvehiculo).filter(self.entity.fkresidente == idresidente).first()

    def registrar_vehiculo(self, diccionario):
        placa = diccionario['placa']
        tipo = diccionario['tipo']
        fkmarca = diccionario['fkmarca']
        fkmodelo = diccionario['fkmodelo']
        color = diccionario['color']
        idinvitado = diccionario['fkinvitado']

        if fkmarca == "":
            fkmarca = None
        elif fkmarca == "0":
            marc = Marca(nombre=diccionario['nombre_marca'])
            obj_marca = super().insert(marc)
            fkmarca = obj_marca.id
        if fkmodelo == "":
            fkmodelo = None

        vehiculo = VehiculoManager(self.db).obtener_x_placa(placa)

        if vehiculo:
            return vehiculo.id
        else:
            if placa == "":
                return None
            else:
                # dict_vehiculo = dict(placa=placa, tipo=tipo,marca=marca,color=color,fkpropietarioinvitado=idinvitado)
                dict_vehiculo = dict(placa=placa, tipo=tipo, fkmarca=fkmarca, fkmodelo=fkmodelo, color=color)
                objeto = VehiculoManager(self.db).entity(**dict_vehiculo)
                fecha = BitacoraManager(self.db).fecha_actual()
                a = super().insert(objeto)
                b = Bitacora(fkusuario=diccionario['user'], ip=diccionario['ip'], accion="Registro Vehiculo.", fecha=fecha,
                             tabla="vehiculo", identificador=a.id)
                super().insert(b)

        return a.id

    def registrar_vehiculo_invitado(self, diccionario,idinvitado):

        if diccionario['id'] !="":
            respuesta = VehiculoManager(self.db).consultar_vehiculo_invitado(diccionario['id'],idinvitado)
            if respuesta is None:
                objeto = VehiculoManager(self.db).entity(**diccionario)
                objeto.fkinvitado = idinvitado
                super().update(objeto)
        else:
            diccionario['id'] = None
            objeto = VehiculoManager(self.db).entity(**diccionario)
            objeto.fkinvitado = idinvitado
            super().insert(objeto)

    def registrar_vehiculo_residente(self, diccionario,idresidente):

        if diccionario['id'] !="":
            respuesta = VehiculoManager(self.db).consultar_vehiculo(diccionario['id'],idresidente)
            if respuesta is None:
                objeto = VehiculoManager(self.db).entity(**diccionario)
                objeto.fkresidente = idresidente
                a = super().update(objeto)
                if a.fknropase:
                    NropaseManager(self.db).situacion(a.fknropase, "Ocupado")
            elif respuesta.fknropase is None:
                respuesta.fknropase = diccionario['fknropase']
                a = super().update(respuesta)
                if a.fknropase:
                    NropaseManager(self.db).situacion(a.fknropase, "Ocupado")
            elif int(diccionario['fknropase']) != respuesta.fknropase:
                NropaseManager(self.db).situacion(respuesta.fknropase, "Libre")
                NropaseManager(self.db).situacion(diccionario['fknropase'], "Ocupado")


        else:
            diccionario['id'] = None
            objeto = VehiculoManager(self.db).entity(**diccionario)
            objeto.fkresidente = idresidente
            a = super().insert(objeto)

            if a.fknropase:
                NropaseManager(self.db).situacion(a.fknropase, "Ocupado")


    def insert(self, diccionary):
        objeto = VehiculoManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()
    
        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Vehiculo.", fecha=fecha, tabla="vehiculo",
                     identificador=a.id)
        super().insert(b)
        return a
    
    
    def update(self, diccionary):
        objeto = VehiculoManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()
    
        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Vehiculo.", fecha=fecha, tabla="vehiculo",
                     identificador=a.id)
        super().insert(b)
        return a
    
    
    def delete(self, id, estado, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.estado = estado
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Eliminó Vehiculo.", fecha=fecha, tabla="vehiculo", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()
    
        return x

    def obtener_vehiculo(self, placa,color,tipovehiculo,marca,modelo,tarjeta):

        query_vehiculo = self.db.query(Vehiculo).filter(Vehiculo.placa == str(placa)).first()
        query_tarjeta = self.db.query(Nropase).filter(Nropase.tarjeta == str(tarjeta)).first()

        if query_tarjeta:
            idtarjeta = query_tarjeta.id
        else:
            idtarjeta = None

        if query_vehiculo:

            return  dict(id=query_vehiculo.id,placa="",color="",tipo="",fkmarca="",fkmodelo="", fknropase=idtarjeta)
        else:
            if placa:

                query_marca = self.db.query(Marca).filter(Marca.nombre == str(marca)).first()
                if query_marca:
                    idmarca = query_marca.id
                else:
                    marc = Marca(nombre=marca)
                    obj_marca = super().insert(marc)
                    idmarca = obj_marca.id


                if modelo:
                    query_modelo = self.db.query(Modelo).filter(Modelo.nombre == str(modelo)).first()
                    if query_modelo:
                        idmodelo = query_modelo.id
                    else:
                        mod = Modelo(nombre=modelo,fkmarca=idmarca)
                        obj_modelo = super().insert(mod)
                        idmodelo = obj_modelo.id

                else:
                    idmodelo = modelo

                return  dict(id="", placa=placa, color=color, tipo=tipovehiculo, fkmarca=idmarca, fkmodelo=idmodelo, fknropase=idtarjeta)
            else:
                return ""