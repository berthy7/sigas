from .managers import *
from server.common.controllers import CrudController
from ..domicilio.managers import *
from ..vehiculo.managers import *
from ..marca.managers import *
from ..modelo.managers import *
from ..nropase.managers import *

import os.path
import uuid
import json


class ResidenteController(CrudController):

    manager = ResidenteManager
    html_index = "condominios/residente/views/index.html"
    html_table = "condominios/residente/views/table.html"
    routes = {
        '/residente': {'GET': 'index', 'POST': 'table'},
        '/residente_insert': {'POST': 'insert'},
        '/residente_update': {'PUT': 'edit', 'POST': 'update'},
        '/residente_delete': {'POST': 'delete'},
        '/residente_importar': {'POST': 'importar'},
        '/vehiculo_obtener': {'POST': 'obtener_vehiculo'},
        '/residente_reporte_xls': {'POST': 'imprimirxls'},
        '/residente_obtener_domicilios': {'POST': 'obtener_domicilios'},
        '/residente_validar_codigo': {'POST': 'validar_codigo'},

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
        objeto = []

        aux['objeto'] = objeto
        aux['viviendas'] = DomicilioManager(self.db).listar_domicilios(us)
        aux['residentes'] = ResidenteManager(self.db).listar_residentes(us)
        aux['vehiculos'] = VehiculoManager(self.db).listar_disponibles()
        aux['tipovehiculos'] = TipovehiculoManager(self.db).listar_todo()
        aux['colores'] = ColorManager(self.db).listar_todo()
        aux['marcas'] = MarcaManager(self.db).listar_todo()
        aux['modelos'] = ModeloManager(self.db).listar_todo()
        aux['nropases_residente'] = NropaseManager(self.db).listar_numero_pases_residente(us)

        return aux

    def insert(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        if "archivo" in self.request.files:
            fileinfo = self.request.files["archivo"][0]
            fname = fileinfo.filename
            extn = os.path.splitext(fname)[1]
            cname = str(uuid.uuid4()) + extn
            f = open("server/common/resources/images/residente/" + cname, 'wb')
            f.write(fileinfo.body)
            f.close()
            diccionary['foto'] = "/resources/images/residente/" + cname

        dict_usuario = ResidenteManager(self.db).insert(diccionary)
        c = UsuarioManager(self.db).insert_residente(dict_usuario)

        principal = self.db.query(Principal).first()

        if principal.estado:

            if c.condominio.ip_publica != "":
                url = "http://" + c.condominio.ip_publica + ":" + c.condominio.puerto + "/api/v1/sincronizar_residente"

                headers = {'Content-Type': 'application/json'}

                diccionary = dict(dict_usuario=dict_usuario, dict_residente=diccionary)

                cadena = json.dumps(diccionary)
                body = cadena
                resp = requests.post(url, data=body, headers=headers, verify=False)
                response = json.loads(resp.text)

                print(response)


        arraT = UsuarioManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = ResidenteManager(self.db).listar_residentes(us)
        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='Insertado correctamente.')

    def update(self):
        self.set_session()
        us = self.get_user()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        if "archivo" in self.request.files:
            fileinfo = self.request.files["archivo"][0]
            fname = fileinfo.filename
            extn = os.path.splitext(fname)[1]
            cname = str(uuid.uuid4()) + extn
            f = open("server/common/resources/images/residente/" + cname, 'wb')
            f.write(fileinfo.body)
            f.close()
            diccionary['foto'] = "/resources/images/residente/" + cname

        ResidenteManager(self.db).update(diccionary)
        arraT = UsuarioManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = ResidenteManager(self.db).listar_residentes(us)
        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='Insertado correctamente.')

    def imprimirxls(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        cname = self.manager(self.db).residente_excel(diccionary['datos'])
        self.respond({'nombre': cname, 'url': 'resources/downloads/residente/' + cname}, True)
        self.db.close()

    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        state = diccionary['enabled']
        respuesta = ResidenteManager(self.db).delete(id, self.get_user_id(), self.request.remote_ip,state)

        self.respond(success=True, message=respuesta)
        self.db.close()

    def obtener_vehiculo(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        indicted_object = VehiculoManager(self.db).obtener_x_id(diccionary['id'])
        self.respond(indicted_object.get_dict(), message='Operacion exitosa!')
        self.db.close()

    def obtener_domicilios(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        id = data['id']
        ins_manager = self.manager(self.db)
        indicted_object = ins_manager.obtener_domicilios(id)
        self.respond(indicted_object.get_dict(), message='Operacion exitosa!')
        self.db.close()


    def validar_codigo(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        indicted_object = ResidenteManager(self.db).validar_codigo(diccionary['codigoautorizacion'])
        if indicted_object:
            self.respond(indicted_object, success=True, message='/resources/images/aceptado.png')
            self.db.close()
        else:
            self.respond(success=False, message='/resources/images/rechazado.png')
            self.db.close()