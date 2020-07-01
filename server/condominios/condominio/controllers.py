from .managers import *
from ...common.controllers import CrudController
from ...usuarios.rol.managers import *

import json


class CondominioController(CrudController):

    manager = CondominioManager
    html_index = "condominios/condominio/views/index.html"
    html_table = "condominios/condominio/views/table.html"
    routes = {
        '/condominio': {'GET': 'index', 'POST': 'table'},
        '/condominio_insert': {'POST': 'insert'},
        '/condominio_update': {'PUT': 'edit', 'POST': 'update'},
        '/condominio_delete': {'POST': 'delete'},
        '/condominio_obtener': {'POST': 'obtener_x_id'},
        '/condominio_entrada': {'POST': 'entrada'},
        '/condominio_listar_residente': {'POST': 'listar_x_residente'}
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        us = super().get_user()
        aux['roles'] = RolManager(self.db).listar_x_condominio(us)

        return aux

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        CondominioManager(self.db).insert(objeto)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        CondominioManager(self.db).update(objeto)
        self.respond(success=True, message='Modificado correctamente.')

    def delete(self):
        self.set_session()
        id = json.loads(self.get_argument("id"))
        estado = json.loads(self.get_argument("enabled"))
        user = self.get_user_id()
        ip = self.request.remote_ip

        result = CondominioManager(self.db).delete(id,estado, user, ip)

        if result:
            self.respond(success=True, message='Eliminado Correctamente.')
        else:
            self.respond(success=False, message='ERROR 403')

    def obtener_x_id(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        indicted_object = CondominioManager(self.db).obtener_x_id(diccionary['id'])
        self.respond(indicted_object.get_dict(), message='Operacion exitosa!')
        self.db.close()

    def entrada(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        ins_manager = EntradaManager(self.db)
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.obtener_entradas()
        self.respond([objeto.get_dict() for objeto in arraT['datos']])
        self.db.close()


    def listar_x_residente(self):
        self.set_session()
        us = self.get_user()

        data = json.loads(self.get_argument("object"))
        arraT = self.manager(self.db).get_page(1, 10, None, None, True)
        arraT['objeto'] = CondominioManager(self.db).obtener_residentes(data['fkdomicilio'])
        self.respond([item.get_dict() for item in arraT['objeto']])
        self.db.close()


