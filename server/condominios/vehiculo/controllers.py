from .managers import *
from server.common.controllers import CrudController
from ..movimiento.managers import *
from ..marca.managers import *
from ..modelo.managers import *

import os.path
import uuid
import json


class VehiculoController(CrudController):

    manager = VehiculoManager
    html_index = "condominios/vehiculo/views/index.html"
    html_table = "condominios/vehiculo/views/table.html"
    routes = {
        '/vehiculo': {'GET': 'index', 'POST': 'table'},
        '/vehiculo_insert': {'POST': 'insert'},
        '/vehiculo_update': {'PUT': 'edit', 'POST': 'update'},
        '/vehiculo_delete': {'POST': 'delete'},
        '/vehiculo_obtener': {'POST': 'obtener_x_id'},
        '/vehiculo_importar': {'POST': 'importar'},
        '/vehiculo_reporte_xls': {'POST': 'imprimirxls'}
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

        aux['objeto'] = objeto
        aux['marcas'] = MarcaManager(self.db).listar_todo()
        aux['modelos'] = ModeloManager(self.db).listar_todo()

        return aux

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        VehiculoManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        VehiculoManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')


    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        state = diccionary['enabled']
        respuesta = VehiculoManager(self.db).delete(id, self.get_user_id(), self.request.remote_ip,state)

        self.respond(success=True, message=respuesta)
        self.db.close()

    def obtener_x_id(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        indicted_object = VehiculoManager(self.db).obtener_x_id(diccionary['id'])
        self.respond(indicted_object.get_dict(), message='Operacion exitosa!')
        self.db.close()
