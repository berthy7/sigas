from .managers import *
from server.common.controllers import CrudController
from ..invitado.managers import *
from ...condominios.movimiento.managers import *
from ..residente.managers import *
from ..domicilio.managers import *
from ..vehiculo.managers import *
from ..marca.managers import *
from ..modelo.managers import *
from ..areasocial.managers import *
from ..nropase.managers import *

import os.path
import uuid
import json


class PorterovirtualController(CrudController):

    manager = PorterovirtualManager
    html_index = "condominios/portero_virtual/views/index.html"
    html_table = "condominios/portero_virtual/views/table.html"
    routes = {
        '/portero_virtual': {'GET': 'index', 'POST': 'table'},
        '/portero_virtual_insert': {'POST': 'insert'},
        '/portero_virtual_update': {'PUT': 'edit', 'POST': 'update'},
        '/portero_virtual_delete': {'POST': 'delete'},
        '/portero_virtual_importar': {'POST': 'importar'},
        '/portero_virtual_salida': {'POST': 'salida'},
        '/portero_virtual_reporte_xls': {'POST': 'imprimirxls'},
        '/portero_virtual_actualizar': {'POST': 'actualizar'},
        '/portero_virtual_actualizar_tabla': {'POST': 'actualizar_tabla'},
        '/portero_virtual_filtrar': {'POST': 'filtrar'}
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

        aux['objeto'] = objeto
        aux['tipodocumento'] = TipodocumentoManager(self.db).listar_todo()
        aux['invitados'] = InvitadoManager(self.db).listar_todo()
        aux['residentes'] = ResidenteManager(self.db).listar_residentes(us)
        aux['tipopases'] = TipopaseManager(self.db).listar_todo()
        aux['autorizaciones'] = AutorizacionManager(self.db).listar_todo()
        aux['idperfil'] = us.fkrol

        aux['portero_virtual'] = PorterovirtualManager(self.db).listar_movimiento_dia(us)
        aux['domicilios'] = DomicilioManager(self.db).listar_domicilios(us)
        aux['cerraduras'] = DispositivoManager(self.db).listar_cerraduras_x_usuario(us)

        return aux

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip

        PorterovirtualManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        PorterovirtualManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')

    def imprimirxls(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        cname = self.manager(self.db).movimiento_excel(diccionary['datos'])
        self.respond({'nombre': cname, 'url': 'resources/downloads/movimiento/' + cname}, True)
        self.db.close()

    def salida(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        fechainicio = diccionary['fechai']
        fechafin = diccionary['fechaf']

        PorterovirtualManager(self.db).salida(id, self.get_user_id(), self.request.remote_ip)

        arraT = PorterovirtualManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] =  PorterovirtualManager(self.db).filtrar(fechainicio, fechafin,self.get_user_id())

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='actualizado correctamente.')

    def actualizar_tabla(self):
        self.set_session()
        arraT = PorterovirtualManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = PorterovirtualManager(self.db).listar_todo()

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='actualizado correctamente.')


    def filtrar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))

        ins_manager = self.manager(self.db)
        fechainicio = datetime.strptime(data['fechainicio'], '%d/%m/%Y')
        fechafin = datetime.strptime(data['fechafin'], '%d/%m/%Y')
        user = self.get_user_id()
        arraT = PorterovirtualManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.filtrar(fechainicio, fechafin,user)

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='actualizado correctamente.')

