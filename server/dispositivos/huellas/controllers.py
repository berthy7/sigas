from .managers import *
from server.common.controllers import CrudController
from server.condominios.condominio.managers import *

import os.path
import uuid
import json


class DispositivoController(CrudController):

    manager = DispositivoManager
    html_index = "dispositivos/dispositivo/views/index.html"
    html_table = "dispositivos/dispositivo/views/table.html"
    routes = {
        '/dispositivo': {'GET': 'index', 'POST': 'table'},
        '/dispositivo_insert': {'POST': 'insert'},
        '/dispositivo_update': {'PUT': 'edit', 'POST': 'update'},
        '/dispositivo_delete': {'POST': 'delete'},
        '/dispositivo_obtener': {'POST': 'obtener_x_id'},
        '/dispositivo_listar_condominio': {'POST': 'listar_x_condominio'},
        '/dispositivo_importar': {'POST': 'importar'},
        '/dispositivo_interpretes': {'POST': 'interpretes'},
        '/dispositivo_configuracion': {'POST': 'configuracion'},
        '/dispositivo_abrir_cerradura': {'POST': 'abrir_cerradura'}
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()

        aux['condominios'] = CondominioManager(self.db).listar_todo()
        aux['tiposdispositivos'] = DispositivoManager(self.db).listar_tipos_dispositivo()
        aux['entradas'] = EntradaManager(self.db).obtener_entradas()
        return aux



    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip_local'] = self.request.remote_ip
        DispositivoManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip_local'] = self.request.remote_ip
        DispositivoManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')


    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        state = diccionary['enabled']
        respuesta = DispositivoManager(self.db).delete(id, self.get_user_id(), self.request.remote_ip,state)

        self.respond(success=True, message=respuesta)
        self.db.close()


    def configuracion(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        ConfiguraciondispositivoManager(self.db).insert_configuracion_inicial(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def listar_x_condominio(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        arraT = self.manager(self.db).get_page(1, 10, None, None, True)
        arraT['objeto'] = DispositivoManager(self.db).listar_x_condominio(data['idcondominio'])
        self.respond([item.get_dict() for item in arraT['objeto']])
        self.db.close()

    def abrir_cerradura(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip_local'] = self.request.remote_ip
        ConfiguraciondispositivoManager(self.db).abrir_cerradura(diccionary)
        self.respond(success=True, message='Apertura remota.')

