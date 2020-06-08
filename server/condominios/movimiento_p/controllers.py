from .managers import *
from server.common.controllers import CrudController
from ..invitado.managers import *
from ..residente.managers import *
from ..domicilio.managers import *
from ..vehiculo.managers import *
from ..marca.managers import *
from ..modelo.managers import *
from ..areasocial.managers import *
from ..nropase.managers import *
from ..movimiento.managers import *

import os.path
import uuid
import json


class Movimiento_pController(CrudController):

    manager = Movimiento_pManager
    html_index = "condominios/movimiento_p/views/index.html"
    html_table = "condominios/movimiento_p/views/table.html"
    routes = {
        '/movimiento_p': {'GET': 'index', 'POST': 'table'},
        '/movimiento_p_insert': {'POST': 'insert'},
        '/movimiento_p_update': {'PUT': 'edit', 'POST': 'update'},
        '/movimiento_p_delete': {'POST': 'delete'},
        '/movimiento_p_importar': {'POST': 'importar'},
        '/movimiento_p_salida': {'POST': 'salida'},
        '/movimiento_p_reporte_xls': {'POST': 'imprimirxls'},
        '/movimiento_p_actualizar': {'POST': 'actualizar'},
        '/movimiento_p_filtrar': {'POST': 'filtrar'}
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

        aux['objeto'] = objeto
        aux['tipodocumento'] = TipodocumentoManager(self.db).listar_todo()
        aux['invitados'] = InvitadoManager(self.db).listar_todo()
        aux['vehiculos'] = VehiculoManager(self.db).listar_todo()

        aux['areasociales'] = AreasocialManager(self.db).listar_todo(us)
        aux['tipopases'] = TipopaseManager(self.db).listar_todo()
        aux['autorizaciones'] = AutorizacionManager(self.db).listar_todo()
        aux['marcas'] = MarcaManager(self.db).listar_todo()
        aux['modelos'] = ModeloManager(self.db).listar_todo()
        aux['idperfil'] = us.fkrol
        aux['nropases'] = NropaseManager(self.db).listar_numero_pases(us)

        aux['domicilios'] = DomicilioManager(self.db).listar_domicilios(us)
        aux['movimientos_peatonal'] = Movimiento_pManager(self.db).listar_movimiento_dia(us)

        return aux

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip

        Movimiento_pManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        MovimientoManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')

    def imprimirxls(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        cname = self.manager(self.db).movimiento_p_excel(diccionary['datos'])
        self.respond({'nombre': cname, 'url': 'resources/downloads/movimiento_p/' + cname}, True)
        self.db.close()

    def salida(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        fechainicio = diccionary['fechai']
        fechafin = diccionary['fechaf']

        MovimientoManager(self.db).salida(id, self.get_user_id(), self.request.remote_ip)

        arraT = Movimiento_pManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] =  Movimiento_pManager(self.db).filtrar(fechainicio, fechafin,self.get_user_id())

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='actualizado correctamente.')

    def actualizar(self):
        self.set_session()
        arraT = MovimientoManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = MovimientoManager(self.db).listar_todo()

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='actualizado correctamente.')

    def filtrar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))

        ins_manager = self.manager(self.db)
        fechainicio = datetime.strptime(data['fechainicio'], '%d/%m/%Y')
        fechafin = datetime.strptime(data['fechafin'], '%d/%m/%Y')
        user = self.get_user_id()
        arraT = Movimiento_pManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.filtrar(fechainicio, fechafin,user)

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='actualizado correctamente.')


