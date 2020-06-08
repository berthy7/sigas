from .managers import *
from server.common.controllers import CrudController
from ..movimiento.managers import *
from ..condominio.managers import *
from ...usuarios.rol.managers import *

import os.path
import uuid
import json


class UsuarioCondominioController(CrudController):

    manager = UsuarioManager
    html_index = "condominios/usuario/views/index.html"
    html_table = "condominios/usuario/views/table.html"
    routes = {
        '/usuarioCondominio': {'GET': 'index', 'POST': 'table'},
        '/usuarioCondominio_insert': {'POST': 'insert'},
        '/usuarioCondominio_update': {'PUT': 'edit', 'POST': 'update'},
        '/usuarioCondominio_delete': {'POST': 'delete'},
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

        aux['objeto'] = objeto
        aux['idcondominio'] = us.fkcondominio
        aux['sigas'] = us.sigas
        aux['condominios'] = CondominioManager(self.db).listar_todo()
        aux['usuarios_condominio'] = UsuarioManager(self.db).usuarios_condominio(us)
        aux['roles'] = RolManager(self.db).listar_x_condominio(us)

        return aux

    def insert(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user_id'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        diccionary['username'] = diccionary['correo']
        diccionary['password'] = diccionary['ci']
        diccionary['sigas'] = False

        respuesta = UsuarioManager(self.db).insert(diccionary)
        arraT = UsuarioManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = UsuarioManager(self.db).usuarios_condominio(us)
        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='Insertado correctamente.')

    def update(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user_id'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        UsuarioManager(self.db).update(objeto)
        arraT = UsuarioManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = UsuarioManager(self.db).usuarios_condominio(us)
        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='Insertado correctamente.')


    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        id = diccionary['id']
        enable = diccionary['enabled']
        resp = UsuarioManager(self.db).delete_user(id, enable, self.get_user_id(), self.request.remote_ip)

        if resp:
            if enable == True:
                msg = 'Usuario activado correctamente.'
            else:
                msg = 'Usuario eliminado correctamente.'
            self.respond(success=True, message=msg)
        else:
            msg = 'Perfil asignado deshabilitado, no es posible habilitar el usuario.'
            self.respond(success=False, message=msg)