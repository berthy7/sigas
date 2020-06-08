from .managers import *
from server.common.controllers import CrudController

import os.path
import uuid
import json


class RegistrosController(CrudController):

    manager = RegistrosManager
    html_index = "dispositivos/registros/views/index.html"
    html_table = "dispositivos/registros/views/table.html"
    routes = {
        '/registros': {'GET': 'index', 'POST': 'table'},
        '/registros_filtrar': {'POST': 'filtrar'},
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []
        aux['registros'] = RegistrosManager(self.db).listar_todo_diccionario()

        return aux


    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        RegistrosManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        RegistrosManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')

    def filtrar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))

        ins_manager = self.manager(self.db)
        fechainicio = datetime.strptime(data['fechainicio'], '%d/%m/%Y')
        fechafin = datetime.strptime(data['fechafin'], '%d/%m/%Y')
        indicted_object = ins_manager.filtrar(fechainicio, fechafin)
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object, message='Operacion exitosa!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al insertar')
        self.db.close()


