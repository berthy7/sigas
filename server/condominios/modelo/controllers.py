from .managers import *
from server.common.controllers import CrudController
from ..movimiento.managers import *
from ..marca.managers import *

import os.path
import uuid
import json


class ModeloController(CrudController):

    manager = ModeloManager
    html_index = "condominios/modelo/views/index.html"
    html_table = "condominios/modelo/views/table.html"
    routes = {
        '/modelo': {'GET': 'index', 'POST': 'table'},
        '/modelo_insert': {'POST': 'insert'},
        '/modelo_update': {'PUT': 'edit', 'POST': 'update'},
        '/modelo_delete': {'POST': 'delete'},
        '/modelo_listar_x_marca': {'POST': 'listar_x_marca'},
        '/modelo_importar': {'POST': 'importar'}
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

        aux['objeto'] = objeto
        aux['marcas'] = MarcaManager(self.db).listar_todo()

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
            mee = MarcaManager(self.db).importar_excel(cname,self.get_user_id(),self.request.remote_ip)
            self.respond(message=mee['message'], success=mee['success'])
        else:
            self.respond(message='Formato de Archivo no aceptado¡¡', success=False)
        self.db.close()

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        ModeloManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        ModeloManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')

    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        state = diccionary['enabled']
        respuesta = ModeloManager(self.db).delete(id, self.get_user_id(), self.request.remote_ip,state)

        self.respond(success=True, message=respuesta)
        self.db.close()

    def listar_x_marca(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        arraT = self.manager(self.db).get_page(1, 10, None, None, True)
        arraT['objeto'] = ModeloManager(self.db).listar_x_marca(data['idmarca'])
        self.respond([item.get_dict() for item in arraT['objeto']])
        self.db.close()

