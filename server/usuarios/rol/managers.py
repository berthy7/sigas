from ...operaciones.bitacora.managers import *

from server.common.managers import SuperManager
from .models import *
from sqlalchemy.sql import func,or_,and_


class RolManager(SuperManager):
    def __init__(self, db):
        super().__init__(Rol, db)

    def get_page(self, page_nr=1, max_entries=10, like_search=None, order_by=None, ascendant=True, query=None):
        query = self.db.query(self.entity).filter(Rol.id > 1)
        return super().get_page(page_nr, max_entries, like_search, order_by, ascendant, query)

    def insert(self, rol):
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=rol.user, ip=rol.ip, accion="Se registró un rol.", fecha=fecha)
        super().insert(b)
        a = super().insert(rol)
        return a

    def listar_x_usuario(self,user):
        if user.rol.nombre == "SUPER ADMINISTRADOR":
            x =self.db.query(Rol).filter(Rol.enabled == True)
        else:
            x = self.db.query(Rol).filter(Rol.enabled == True).filter(Rol.nombre != "SUPER ADMINISTRADOR")

        return x

    def listar_x_condominio(self,user):

        if user.sigas == True:
            x =self.db.query(Rol).filter(Rol.enabled == True).filter(or_(Rol.nombre == "ADMINISTRADOR",Rol.nombre == "REGISTRADOR",Rol.nombre == "GUARDIA",Rol.nombre == "RESIDENTE"))
        else:
            x = self.db.query(Rol).filter(Rol.enabled == True).filter(or_(Rol.nombre == "REGISTRADOR",Rol.nombre == "RESIDENTE"))

        return x

    def update(self, rol):
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=rol.user, ip=rol.ip, accion="Se modificó un rol.", fecha=fecha)
        super().insert(b)
        a = super().update(rol)
        return a

    def list_all(self):
        return dict(objects=self.db.query(Rol).filter(Rol.nombre != "Super Administrador").distinct())

    def get_all(self):
        return self.db.query(Rol).filter(Rol.enabled == True).filter(Rol.nombre != "Super Administrador")

    def obtener_condominio(self):
        return self.db.query(Rol).filter(Rol.enabled == True).filter(Rol.nombre == "REGISTRADOR")

    def delete_rol(self, id, enable, Usuariocr, ip):
        x = self.db.query(Rol).filter(Rol.id == id).one()
        x.enabled = enable

        if enable == True:
            message = "Se habilitó un rol."
        else:
            users = self.db.query(Usuario).filter(Usuario.enabled == True).filter(Usuario.fkrol == id).all()
            for u in users:
                u.enabled = False

            message = "Se inhabilitó un rol y usuarios relacionados."

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuariocr, ip=ip, accion=message, fecha=fecha)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()
