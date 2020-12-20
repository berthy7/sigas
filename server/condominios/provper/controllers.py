from .managers import *
from server.common.controllers import CrudController
from ..movimiento.managers import *
from ..marca.managers import *
from ..modelo.managers import *

import os.path
import uuid
import json


class ProvperController(CrudController):

    manager = ProvperManager
    html_index = "condominios/provper/views/index.html"
    html_table = "condominios/provper/views/table.html"
    routes = {
        '/provper': {'GET': 'index', 'POST': 'table'},
        '/provper_insert': {'POST': 'insert'},
        '/provper_update': {'PUT': 'edit', 'POST': 'update'},
        '/provper_delete': {'POST': 'delete'},
        '/provper_obtener': {'POST': 'obtener_x_id'},
        '/provper_importar': {'POST': 'importar'},
        '/provper_reporte_xls': {'POST': 'imprimirxls'}
    }



    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

        aux['objeto'] = objeto
        aux['tipopases'] = TipopaseManager(self.db).listar_todo()
        aux['provpers'] = ProvperManager(self.db).listar_x_residente(us)
        aux['vehiculos'] = VehiculoManager(self.db).listar_disponibles()
        aux['marcas'] = MarcaManager(self.db).listar_todo()
        aux['modelos'] = ModeloManager(self.db).listar_todo()
        aux['nropases_provper'] = NropaseManager(self.db).listar_tarjetas_provper(us)
        aux['residentes'] = ResidenteManager(self.db).listar_residentes(us)

        return aux

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        diccionary['permanente'] = True
        ProvperManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        ProvperManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')

    def imprimirxls(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        cname = self.manager(self.db).provper_excel(diccionary['datos'])
        self.respond({'nombre': cname, 'url': 'resources/downloads/provper/' + cname}, True)
        self.db.close()

    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        state = diccionary['enabled']
        respuesta = ProvperManager(self.db).delete(id, self.get_user_id(), self.request.remote_ip,state)

        self.respond(success=True, message=respuesta)
        self.db.close()

    def obtener_x_id(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        indicted_object = ProvperManager(self.db).obtener_x_id(diccionary['id'])
        self.respond(indicted_object.get_dict(), message='Operacion exitosa!')
        self.db.close()
