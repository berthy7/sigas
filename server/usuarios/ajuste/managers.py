from ...operaciones.bitacora.managers import *
from .models import *
from server.common.managers import SuperManager

from sqlalchemy.sql import func,or_,and_


class AjusteManager(SuperManager):
    def __init__(self, db):
        super().__init__(Ajuste, db)

    def obtener(self):

        x = self.db.query(self.entity).filter(self.entity.enabled == True).first()
        mov = self.db.query(VersionMovil).filter(VersionMovil.estado == True).first()

        return dict(id=x.id,claveSecreta=x.claveSecreta,id_movil=mov.id,version=mov.version)


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