from .managers import *
from ...common.controllers import CrudController
from ..condominio.managers import *

import json


class AreasocialController(CrudController):

    manager = AreasocialManager
    html_index = "condominios/areasocial/views/index.html"
    html_table = "condominios/areasocial/views/table.html"
    routes = {
        '/areasocial': {'GET': 'index', 'POST': 'table'},
        '/areasocial_insert': {'POST': 'insert'},
        '/areasocial_update': {'PUT': 'edit', 'POST': 'update'},
        '/areasocial_delete': {'POST': 'delete'},
        '/areasocial_filtrar': {'POST': 'filtrar'},
        '/areasocial_obtener': {'POST': 'obtener_x_id'},
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()

        aux['idcondominio'] = us.fkcondominio
        aux['sigas'] = us.sigas
        aux['condominios'] = CondominioManager(self.db).listar_todo()
        aux['areas'] = AreasocialManager(self.db).listar_x_usuario(us)
        # actualizacion

        return aux

    def insert(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        AreasocialManager(self.db).insert(objeto)
        arraT = AreasocialManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = AreasocialManager(self.db).listar_todo(us)

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']],success=True, message='Insertado correctamente.')


    def update(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        AreasocialManager(self.db).update(objeto)
        arraT = AreasocialManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = AreasocialManager(self.db).listar_todo(us)
        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True, message='Modificado correctamente.')

    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        id = diccionary['id']
        estado = diccionary['enabled']
        user = self.get_user_id()
        ip = self.request.remote_ip
        result = AreasocialManager(self.db).delete(id, estado, user, ip)
        if result.enabled:
            self.respond(success=True, message='Alta Realizada Correctamente.')
        elif not result.enabled:
            self.respond(success=False, message='Baja Realizada Correctamente.')
        else:
            self.respond(success=False, message='ERROR 403')

    def obtener_x_id(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        indicted_object = AreasocialManager(self.db).obtener_x_id(diccionary['id'])
        self.respond(indicted_object.get_dict(), message='Operacion exitosa!')
        self.db.close()

    def filtrar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        idcondominio = data['idcondominio']
        ins_manager = self.manager(self.db)
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.filtrar(idcondominio)
        self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
        self.db.close()

