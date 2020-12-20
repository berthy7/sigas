from .managers import *
from server.common.controllers import CrudController
from ..movimiento.managers import *

import os.path
import uuid
import json


class MarcaController(CrudController):

    manager = MarcaManager
    html_index = "condominios/marca/views/index.html"
    html_table = "condominios/marca/views/table.html"
    routes = {
        '/marca': {'GET': 'index', 'POST': 'table'},
        '/marca_insert': {'POST': 'insert'},
        '/marca_update': {'PUT': 'edit', 'POST': 'update'},
        '/marca_delete': {'POST': 'delete'},
        '/marca_obtener': {'POST': 'obtener_x_id'},
        '/marca_importar': {'POST': 'importar'}
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

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
        MarcaManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        MarcaManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')


    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        state = diccionary['enabled']
        respuesta = MarcaManager(self.db).delete(id, self.get_user_id(), self.request.remote_ip,state)

        self.respond(success=True, message=respuesta)
        self.db.close()

