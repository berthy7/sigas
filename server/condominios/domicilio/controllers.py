from .managers import *
from ...common.controllers import CrudController
from ..condominio.managers import *

import os.path
import uuid
import json



class DomicilioController(CrudController):

    manager = DomicilioManager
    html_index = "condominios/domicilio/views/index.html"
    html_table = "condominios/domicilio/views/table.html"
    routes = {
        '/domicilio': {'GET': 'index', 'POST': 'table'},
        '/domicilio_insert': {'POST': 'insert'},
        '/domicilio_update': {'PUT': 'edit', 'POST': 'update'},
        '/domicilio_delete': {'POST': 'delete'},
        '/domicilio_obtener': {'POST': 'obtener_x_id'},
        '/domicilio_obtener_casas': {'POST': 'obtener_casas'},
        '/domicilio_obtener_departamentos': {'POST': 'obtener_departamentos'},
        '/domicilio_filtrar': {'POST': 'filtrar'},
        '/domicilio_importar': {'POST': 'importar'}
    }

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

    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()

        aux['idcondominio'] = us.fkcondominio
        aux['sigas'] = us.sigas
        aux['condominios'] = CondominioManager(self.db).listar_todo()

        return aux


    def insert(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        DomicilioManager(self.db).insert(objeto)
        arraT = DomicilioManager(self.db).get_page(1, 10, None, None, True)

        if diccionary['tipo'] == "Casa":
            arraT['datos'] = DomicilioManager(self.db).listar_casas(us)
        else:
            arraT['datos'] = DomicilioManager(self.db).listar_departamentos(us)

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']],success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        objeto = self.manager(self.db).entity(**diccionary)
        DomicilioManager(self.db).update(objeto)
        arraT = DomicilioManager(self.db).get_page(1, 10, None, None, True)

        if diccionary['tipo'] == "Casa":
            arraT['datos'] = DomicilioManager(self.db).listar_casas(us)
        else:
            arraT['datos'] = DomicilioManager(self.db).listar_departamentos(us)

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']],success=True, message='Modificado correctamente.')

    def delete(self):
        self.set_session()
        id = json.loads(self.get_argument("id"))
        estado = json.loads(self.get_argument("enabled"))
        user = self.get_user_id()
        ip = self.request.remote_ip

        result = DomicilioManager(self.db).delete(id,estado, user, ip)

        if result:
            self.respond(success=True, message='Eliminado Correctamente.')
        else:
            self.respond(success=False, message='ERROR 403')

    def obtener_x_id(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        indicted_object = DomicilioManager(self.db).obtener_x_id(diccionary['id'])
        self.respond(indicted_object.get_dict(), message='Operacion exitosa!')
        self.db.close()

    def obtener_casas(self):
        self.set_session()
        us = self.get_user()
        data = json.loads(self.get_argument("object"))
        ins_manager = self.manager(self.db)
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.listar_casas(us)
        self.respond([objeto.get_dict() for objeto in arraT['datos']])
        self.db.close()

    def obtener_departamentos(self):
        self.set_session()
        us = self.get_user()
        data = json.loads(self.get_argument("object"))
        ins_manager = self.manager(self.db)
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.listar_departamentos(us)
        self.respond([objeto.get_dict() for objeto in arraT['datos']])
        self.db.close()

    def filtrar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        idcondominio = data['idcondominio']
        domicilio = data['domicilio']
        ins_manager = self.manager(self.db)
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.filtrar(idcondominio,domicilio)
        self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
        self.db.close()

