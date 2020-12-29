from .managers import *
from server.common.controllers import CrudController
from ..movimiento.managers import *
from ..condominio.managers import *

import os.path
import uuid
import json


class NropaseController(CrudController):

    manager = NropaseManager
    html_index = "condominios/nropase/views/index.html"
    html_table = "condominios/nropase/views/table.html"
    routes = {
        '/nropase': {'GET': 'index', 'POST': 'table'},
        '/nropase_insert': {'POST': 'insert'},
        '/nropase_insert_sincro': {'POST': 'insert_sincro'},
        '/nropase_update': {'PUT': 'edit', 'POST': 'update'},
        '/nropase_delete': {'POST': 'state'},
        '/nropase_obtener': {'POST': 'obtener_x_id'},
        '/nropase_importar': {'POST': 'importar'},
        '/nropase_sincronizacion': {'POST': 'sincronizacion'},
        '/nropase_listar_condominio': {'POST': 'listar_x_condominio'},
        '/nropase_listar_tipo': {'POST': 'listar_x_tipo'},
        '/nropase_listar_todo': {'PUT': 'listar_todo'},
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()

        aux['sigas'] = us.sigas
        aux['condominios'] = CondominioManager(self.db).listar_todo()
        # aux['nropases'] = NropaseManager(self.db).listar_todo_condominio()
        aux['idcondominio'] = us.fkcondominio

        aux['admin'] = NropaseManager(self.db).get_employees_tree()

        return aux

    def importar(self):
        self.set_session()
        fileinfo = self.request.files['archivo'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open("server/common/resources/uploads/" + cname, 'wb')
        fh.write(fileinfo['body'])
        fh.close()
        if extn in ['.xlsx', '.xls']:
            mee = self.manager(self.db).importar_excel(cname,self.get_user_id(),self.request.remote_ip)
            self.respond(message=mee['message'], success=mee['success'])
        else:
            self.respond(message='Formato de Archivo no aceptado¡¡', success=False)
        self.db.close()

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        NropaseManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')


    def insert_sincro(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        NropaseManager(self.db).insert_sincronizacion(diccionary)
        self.respond(success=True, message='Sincronizado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        NropaseManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')


    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        state = diccionary['enabled']
        respuesta = NropaseManager(self.db).delete(id, self.get_user_id(), self.request.remote_ip,state)

        self.respond(success=True, message=respuesta)
        self.db.close()


    def state(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        result = NropaseManager(self.db).state(diccionary['id'], diccionary['estado'], self.get_user_id(), self.request.remote_ip)

        if result.estado:
            resultado = 'Habilito Correctamente.'
        elif not result.estado:
            resultado = 'Deshabilito Correctamente.'
        else:
            resultado = 'ERROR 403'

        self.respond(success=True, message=resultado)


    def sincronizacion(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        ConfiguraciondispositivoManager(self.db).insert_sincronizacion(diccionary)
        self.respond(success=True, message='Sincronizado correctamente.')


    def listar_x_condominio(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        arraT = self.manager(self.db).get_page(1, 10, None, None, True)
        arraT['objeto'] = NropaseManager(self.db).listar_x_condominio(data['idcondominio'])
        self.respond([item.get_dict() for item in arraT['objeto']])
        self.db.close()


    def listar_x_tipo(self):
        self.set_session()
        us = self.get_user()

        data = json.loads(self.get_argument("object"))
        arraT = self.manager(self.db).get_page(1, 10, None, None, True)
        arraT['objeto'] = NropaseManager(self.db).listar_x_tipo(us,data['tipopase'])
        self.respond([item.get_dict() for item in arraT['objeto']])
        self.db.close()


    def listar_todo(self):
        self.set_session()
        us = self.get_user()

        data = json.loads(self.get_argument("object"))
        arraT = self.manager(self.db).get_page(1, 10, None, None, True)
        arraT['objeto'] = NropaseManager(self.db).listar_todo()
        self.respond([item.get_dict() for item in arraT['objeto']])
        self.db.close()