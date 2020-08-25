from .models import *
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ...usuarios.usuario.managers import *
from ..residente.managers import *

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font



class ModeloManager(SuperManager):

    def __init__(self, db):
        super().__init__(Modelo, db)


    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.estado == True))

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.nombre.asc()).all()

    def listar_x_marca(self, idmarca):
        return self.db.query(self.entity).filter(self.entity.fkmarca == idmarca).filter(
            self.entity.estado == True).all()

    def insert(self, diccionary):

        objeto = ModeloManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Modelo.", fecha=fecha,tabla="modelo", identificador=a.id)
        super().insert(b)
        return a

    def update(self, diccionary):
        objeto = ModeloManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Modelo.", fecha=fecha,tabla="modelo", identificador=a.id)
        super().insert(b)
        return a

    def delete(self, id,estado, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.estado = estado
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Eliminó Modelo.", fecha=fecha, tabla="modelo", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return x

