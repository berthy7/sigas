from ...operaciones.bitacora.managers import *
from ...usuarios.usuario.managers import *
from server.common.managers import SuperManager
from .models import *
from sqlalchemy import or_
from sqlalchemy import and_


class AreasocialManager(SuperManager):

    def __init__(self, db):
        super().__init__(Areasocial, db)

    def obtener_x_nombre(self, nombre):
        return self.db.query(self.entity).filter(self.entity.nombre == nombre).first()

    def obtener_x_id(self,idinvitado):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.id == idinvitado).first()


    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def listar_x_usuario(self,usuario):


        if usuario.sigas:
            return self.db.query(self.entity).order_by(self.entity.nombre.asc()).all()
        else:
            return self.db.query(self.entity).filter(self.entity.fkcondominio== usuario.fkcondominio).order_by(
                self.entity.nombre.asc()).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.estado == True))

    def listar_todo(self,usuario):

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.nombre.asc()).all()
        else:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.fkcondominio== usuario.fkcondominio).order_by(
                self.entity.nombre.asc()).all()


    def insert(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Areasocial.", fecha=fecha,tabla="areasocial", identificador=a.id)
        super().insert(b)
        return a

    def update(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Areasocial.", fecha=fecha,tabla="areasocial", identificador=a.id)
        super().insert(b)
        return a

    def delete(self, id,estado, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.enabled = estado
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Cambio estado Area Social", fecha=fecha,
                     tabla="areasocial", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()
        return x

    def filtrar(self, idcondominio):
        if idcondominio != "0":
            objeto = self.db.query(self.entity).filter(self.entity.fkcondominio == idcondominio).order_by(self.entity.nombre.asc()).all()

        else:
            objeto = self.db.query(self.entity).order_by(self.entity.nombre.asc()).all()

        return objeto