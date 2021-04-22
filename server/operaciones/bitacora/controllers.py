from ..bitacora.managers import *
from server.common.controllers import CrudController
from server.usuarios.usuario.managers import UsuarioManager

import json


class BitacoraController(CrudController):

    manager = BitacoraManager
    html_index = "operaciones/bitacora/views/index.html"
    html_table = "operaciones/bitacora/views/table.html"
    routes = {
        '/bitacora': {'GET': 'index', 'POST': 'table'},
        '/bitacora_filtrar': {'POST': 'filtrar'}
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        aux['usuarios'] = UsuarioManager(self.db).listar_todos()


        return aux

    def filtrar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))

        ins_manager = self.manager(self.db)
        fechainicio = datetime.strptime(data['fechainicio'], '%d/%m/%Y')
        fechafin = datetime.strptime(data['fechafin'], '%d/%m/%Y')
        user = self.get_user_id()
        arraT = BitacoraManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.filtrar(fechainicio, fechafin,data['idusuario'])

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='actualizado correctamente.')
