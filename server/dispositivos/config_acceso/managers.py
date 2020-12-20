from .models import *
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ...usuarios.usuario.managers import *
from ..registros.models import *
from ..dispositivo.managers import *


from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font

# import ctypes
# from ctypes import *
# from ctypes.wintypes import HANDLE,POINT


class ConfigaccesoManager(SuperManager):

    def __init__(self, db):
        super().__init__(Configacceso, db)


    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.estado == True))


    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def insert(self, diccionary):

        codigo_acceso = ConfiguraciondispositivoManager(self.db).obtener_codigo_acceso(diccionary['configcerraduras'])

        diccionary['codigoacceso'] = codigo_acceso

        objeto = ConfigaccesoManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip_local, accion="Registro Configacceso.", fecha=fecha,tabla="configuracionacceso", identificador=a.id)
        super().insert(b)

        # ConfiguraciondispositivoManager(self.db).insert_config_acceso(a)

        return a

    def update(self, diccionary):
        codigo_acceso = ConfiguraciondispositivoManager(self.db).obtener_codigo_acceso(diccionary['configcerraduras'])

        diccionary['codigoacceso'] = codigo_acceso

        objeto = ConfigaccesoManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip_local, accion="Modifico Configacceso.", fecha=fecha,tabla="configuracionacceso", identificador=a.id)
        super().insert(b)
        return a

    def delete(self, id,estado, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.estado = estado
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Eliminó Configacceso.", fecha=fecha, tabla="configuracionacceso", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return x
