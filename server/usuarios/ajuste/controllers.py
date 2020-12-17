from .managers import *
from server.common.controllers import CrudController

import json


class AjusteController(CrudController):

    manager = AjusteManager
    html_index = "usuarios/ajuste/views/index.html"

    routes = {
        '/ajuste': {'GET': 'index', 'POST': 'table'},
        '/ajuste_insert': {'POST': 'insert'},
        '/ajuste_update_movil': {'PUT': 'edit', 'POST': 'update_movil'},
        '/ajuste_delete': {'POST': 'delete'}
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        aux['ajuste'] = AjusteManager(self.db).obtener()

        return aux


    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        AjusteManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        diccionary['id'] = 1
        AjusteManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')


    def update_movil(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        diccionary['id'] = diccionary['id_movil']
        AjusteManager(self.db).update_movil(diccionary)
        self.respond(success=True, message='Modificado correctamente.')

