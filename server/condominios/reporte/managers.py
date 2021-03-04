from .models import *
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ...usuarios.usuario.managers import *
from ..residente.managers import *



class ReporteManager(SuperManager):

    def __init__(self, db):
        super().__init__(Condominio, db)


    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()


    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.estado == True))

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()


    def insert(self, diccionary):

        objeto = ReporteManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Reporte.", fecha=fecha,tabla="marca", identificador=a.id)
        super().insert(b)
        return a

    def update(self, diccionary):
        objeto = ReporteManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Reporte.", fecha=fecha,tabla="marca", identificador=a.id)
        super().insert(b)
        return a


