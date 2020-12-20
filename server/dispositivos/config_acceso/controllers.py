from .managers import *
from server.common.controllers import CrudController
from server.condominios.condominio.managers import *

import os.path
import uuid
import json


class ConfigaccesoController(CrudController):

    manager = ConfigaccesoManager
    html_index = "dispositivos/config_acceso/views/index.html"
    html_table = "dispositivos/config_acceso/views/table.html"
    routes = {
        '/config_acceso': {'GET': 'index', 'POST': 'table'},
        '/config_acceso_insert': {'POST': 'insert'},
        '/config_acceso_update': {'PUT': 'edit', 'POST': 'update'},
        '/config_acceso_delete': {'POST': 'delete'},
        '/config_acceso_obtener': {'POST': 'obtener_x_id'},
        '/config_acceso_importar': {'POST': 'importar'},
        '/config_acceso_interpretes': {'POST': 'interpretes'}
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()

        aux['condominios'] = CondominioManager(self.db).listar_todo()
        aux['entradas'] = EntradaManager(self.db).obtener_entradas()
        return aux



    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip_local'] = self.request.remote_ip
        ConfigaccesoManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip_local'] = self.request.remote_ip
        ConfigaccesoManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')


    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        state = diccionary['enabled']
        respuesta = ConfigaccesoManager(self.db).delete(id, self.get_user_id(), self.request.remote_ip,state)

        self.respond(success=True, message=respuesta)
        self.db.close()

    def interpretes(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        ins_manager = InterpreteManager(self.db)
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.obtener_interpretes()
        self.respond([objeto.get_dict() for objeto in arraT['datos']])
        self.db.close()

