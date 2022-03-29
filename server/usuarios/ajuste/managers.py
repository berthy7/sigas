from ...operaciones.bitacora.managers import *
from .models import *
from server.common.managers import SuperManager
from ...condominios.domicilio.models import Domicilio
from ...condominios.residente.models import Residente , ResidenteDomicilio
from ...condominios.movimiento.models import Movimiento
from configparser import ConfigParser
from sqlalchemy import create_engine

from sqlalchemy.sql import func,or_,and_


class AjusteManager(SuperManager):
    def __init__(self, db):
        super().__init__(Ajuste, db)

    def sincronizar_movimiento(self):
        print("sincronizar descripcion residente")
        cont = 1

        movimientos = self.db.query(Movimiento).all()

        for objeto in movimientos:

            if objeto.fkresidente:
                objeto.descripcion_residente = objeto.residente.fullname
            else:
                if objeto.fkdomicilio:
                    residomi = self.db.query(ResidenteDomicilio).filter(ResidenteDomicilio.fkdomicilio == objeto.fkdomicilio).first()

                    if residomi:

                        resi = self.db.query(Residente).filter(
                            Residente.id == residomi.fkresidente).first()

                        objeto.fkresidente = resi.id

                        objeto.descripcion_residente = resi.fullname
                    else:
                        objeto.descripcion_residente = '-----'


                else:

                    objeto.descripcion_residente = '-----'

            self.db.merge(objeto)
            print(str(cont))
            cont = cont + 1

        fecha = BitacoraManager(self.db).fecha_actual()

        print("sincronizar inicio commit " + fecha.strftime('%d/%m/%Y %H:%M:%S'))
        self.db.commit()
        print("sincronizar fin commit " + fecha.strftime('%d/%m/%Y %H:%M:%S'))


    def sincronizar_condominio(self):
        residentes = self.db.query(Residente).all()

        print("inicio sincronizar_condominio: " + str(BitacoraManager(self.db).fecha_actual()))

        for res in residentes:
            domicilioid = res.domicilios[0].fkdomicilio
            domi = self.db.query(Domicilio).filter(Domicilio.id == domicilioid).first()

            res.fkcondominio = domi.fkcondominio

            self.db.merge(res)

            # super().update(res)

        self.db.commit()
        print("final sincronizar_condominio: "+ str(BitacoraManager(self.db).fecha_actual()))
        return




    def update_onesignal(self, diccionary):

        x = self.db.query(self.entity).filter(self.entity.enabled == True).first()
        x.app_id =  diccionary['app_id']
        x.rest_api_key = diccionary['rest_api_key']
        x.channel_id = diccionary['channel_id']

        fecha = BitacoraManager(self.db).fecha_actual()

        self.db.add(Bitacora(fkusuario=diccionary['user'], ip=diccionary['ip'], accion="Modifico Ajuste onesignal.", fecha=fecha, tabla="ajuste",
                     identificador=x.id))


        self.db.merge(x)
        self.db.commit()

        return x

    def obtener(self):

        x = self.db.query(self.entity).filter(self.entity.enabled == True).first()
        mov = self.db.query(VersionMovil).filter(VersionMovil.estado == True).first()

        return dict(id=x.id,claveSecreta=x.claveSecreta,id_movil=mov.id,version=mov.version
                    , app_id=x.app_id,rest_api_key=x.rest_api_key,channel_id=x.channel_id)


    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.enabled == True).order_by(self.entity.nombre.asc()).all()



    def ejecutar_consuta(self,dic):
        try:
            config = ConfigParser()
            config.read('settings.ini')
            conexion = config['Database']['url']
            engine = create_engine(conexion)
            conn = engine.connect()
            trans = conn.begin()
            res = conn.execute("update rol set enabled = FALSE where id = 7 ")
            # res = conn.execute(
            #     "select ID_AREA,DESCRIPCION,IDEMPRESA from SIS_ELFEC.RH_AREAS where nivel in (2,3) and utilizable = 1 and idempresa = 1")

            for _row in res:
                print(_row)

            conn.close()

            return True
        except Exception as e:
            print(e)
            return False

    def insert(self, diccionary):
        objeto = AjusteManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()
    
        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Ajuste.", fecha=fecha, tabla="ajuste",
                     identificador=a.id)
        super().insert(b)
    
        return a
    
    
    def update(self, diccionary):
        objeto = AjusteManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()
    
        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Ajuste.", fecha=fecha, tabla="ajuste",
                     identificador=a.id)
        super().insert(b)
    
        return a

    def update_movil(self, diccionary):
        objeto = VersionMovilManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Version Movil.", fecha=fecha, tabla="versionmovil",
                     identificador=a.id)
        super().insert(b)

        return a
    
    
    def delete(self, id, Usuario, ip, enable):
        x = self.db.query(self.entity).filter(self.entity.id == id).first()
    
        x.enabled = enable
    
        if enable:
            mensaje = "Se habilitó Ajuste."
        else:
            mensaje = "Se deshabilitó Ajuste."
    
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuario, ip=ip, accion=mensaje, fecha=fecha)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()
    
        return mensaje


class VersionMovilManager(SuperManager):
    def __init__(self, db):
        super().__init__(VersionMovil, db)

    def obtener(self):

        x = self.db.query(self.entity).filter(self.entity.enabled == True).first()
        mov = self.db.query(VersionMovil).filter(VersionMovil.estado == True).first()

        return dict(id=x.id, claveSecreta=x.claveSecreta, id_movil=mov.id, version=mov.version)

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.enabled == True).order_by(self.entity.nombre.asc()).all()

    def insert(self, diccionary):
        objeto = AjusteManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Ajuste.", fecha=fecha, tabla="ajuste",
                     identificador=a.id)
        super().insert(b)

        return a

    def update(self, diccionary):
        objeto = AjusteManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Ajuste.", fecha=fecha, tabla="ajuste",
                     identificador=a.id)
        super().insert(b)

        return a

    def update_movil(self, diccionary):
        objeto = VersionMovilManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Ajuste.", fecha=fecha, tabla="ajuste",
                     identificador=a.id)
        super().insert(b)

        return a

    def delete(self, id, Usuario, ip, enable):
        x = self.db.query(self.entity).filter(self.entity.id == id).first()

        x.enabled = enable

        if enable:
            mensaje = "Se habilitó Ajuste."
        else:
            mensaje = "Se deshabilitó Ajuste."

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuario, ip=ip, accion=mensaje, fecha=fecha)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return mensaje