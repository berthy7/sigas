from .managers import *
from server.common.controllers import CrudController
from ...dispositivos.registros.managers import *

import os.path
import uuid
import json


class Registros_cController(CrudController):

    manager = Registros_cManager
    html_index = "condominios/registros_c/views/index.html"
    html_table = "condominios/registros_c/views/table.html"
    routes = {
        '/registros_c': {'GET': 'index', 'POST': 'table'},
        '/registros_c_filtrar': {'POST': 'filtrar'},
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []
        aux['registros'] = RegistrosManager(self.db).listar_todo_diccionario(us)

        return aux


    def filtrar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        us = self.get_user()
        ins_manager = self.manager(self.db)
        fechainicio = datetime.strptime(data['fechainicio'], '%d/%m/%Y')
        fechafin = datetime.strptime(data['fechafin'], '%d/%m/%Y')
        indicted_object = ins_manager.filtrar(fechainicio, fechafin,us)
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object, message='Operacion exitosa!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al insertar')
        self.db.close()


