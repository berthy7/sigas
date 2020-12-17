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
        '/usuarioCondominio_state': {'POST': 'state'},
        '/usuarioCondominio_delete': {'POST': 'delete'},
        '/usuarioCondominio_sesion': {'POST': 'sesion'}
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

        contraseña_default = UsuarioManager(self.db).generar_contraseña()

        diccionary['username'] = diccionary['correo']
        diccionary['password'] = contraseña_default
        diccionary['default'] = contraseña_default

        diccionary['sigas'] = False

        respuesta = UsuarioManager(self.db).insert(diccionary)
        arraT = UsuarioManager(self.db).get_page(1, 10, None, None, True)
        # arraT['datos'] = UsuarioManager(self.db).usuarios_condominio(us)
        # self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
        #              message='Insertado correctamente.')

        arraT['datos'] = UsuarioManager(self.db).usuarios_condominio(us)
        arraT['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']],success=[objeto_success for objeto_success in arraT['privileges']], message='Insertado correctamente.')


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

    def state(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        objeto = self.manager(self.db).entity(**diccionary)
        result = UsuarioManager(self.db).state(diccionary['id'], diccionary['enabled'], self.get_user_id(), self.request.remote_ip)
        arraT = UsuarioManager(self.db).get_page(1, 10, None, None, True)

        arraT['datos'] = UsuarioManager(self.db).usuarios_condominio(us)
        arraT['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)

        if result.fkresidente:
            ResidenteManager(self.db).delete(result.fkresidente, self.get_user_id(), self.request.remote_ip, diccionary['enabled'])

        resultado = ""

        if result.estado:
            resultado = 'Habilito Correctamente.'
        elif not result.estado:
            resultado = 'Deshabilito Correctamente.'
        else:
            resultado = 'ERROR 403'

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']],
                     success=[objeto_success for objeto_success in arraT['privileges']],
                     message=resultado)


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

    def sesion(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        objeto = self.manager(self.db).entity(**diccionary)
        result = UsuarioManager(self.db).sesion(diccionary['id'], diccionary['enabled'], self.get_user_id(), self.request.remote_ip)
        arraT = UsuarioManager(self.db).get_page(1, 10, None, None, True)

        arraT['datos'] = UsuarioManager(self.db).usuarios_condominio(us)
        arraT['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)

        resultado = ""

        if result.login:
            resultado = 'Inicio Session'
        elif not result.login:
            resultado = 'Cerro Session'
        else:
            resultado = 'ERROR 403'

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']],
                     success=[objeto_success for objeto_success in arraT['privileges']],
                     message=resultado)


    def exit(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        id = diccionary['id']
        resp = UsuarioManager(self.db).exit_user(id, self.get_user_id(), self.request.remote_ip)

        self.respond(success=True, message="Cierre de session")
