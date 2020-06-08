from .managers import *
from ...common.controllers import CrudController
from ..usuario.managers import *

import json


class RolController(CrudController):
    manager = RolManager
    html_index = "usuarios/rol/views/index.html"
    html_table = "usuarios/rol/views/table.html"
    routes = {
        '/rol': {'GET': 'index', 'POST': 'table'},
        '/rol_insert': {'POST': 'insert'},
        '/rol_update': {'PUT': 'edit', 'POST': 'update'},
        '/rol_delete': {'POST': 'delete_rol'}
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        aux['modulos'] = ModuloManager(self.db).list_all()
        return aux

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        RolManager(self.db).insert(objeto)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        RolManager(self.db).update(objeto)
        self.respond(success=True, message='Modificado correctamente.')

    def delete_rol(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        id = diccionary['id']
        enable = diccionary['enabled']

        RolManager(self.db).delete_rol(id, enable, self.get_user_id(), self.request.remote_ip)
        if enable == True:
            msg = 'Perfil Habilitado'
        else:
            msg = 'Perfil Deshabilitado'
        self.respond(success=True, message=msg)
