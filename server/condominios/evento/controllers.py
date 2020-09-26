from .managers import *
from server.common.controllers import CrudController
from ..residente.managers import *
from ..domicilio.managers import *
from ..movimiento.managers import *
from ..invitado.managers import *
from ..areasocial.managers import *
import os.path
import uuid
import json


class EventoController(CrudController):

    manager = EventoManager
    html_index = "condominios/evento/views/index.html"
    html_table = "condominios/evento/views/table.html"
    routes = {
        '/evento': {'GET': 'index', 'POST': 'table'},
        '/evento_insert': {'POST': 'insert'},
        '/evento_update': {'PUT': 'edit', 'POST': 'update'},
        '/evento_delete': {'POST': 'delete'},
        '/evento_validar_invitacion': {'POST': 'validar_invitacion'},
        '/evento_importar': {'POST': 'importar'},
        '/evento_reporte_xls': {'POST': 'imprimirxls'},
        '/evento_filtrar': {'POST': 'filtrar'}
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

        aux['objeto'] = objeto
        aux['residentes'] = ResidenteManager(self.db).listar_residentes(us)
        aux['invitados'] = InvitadoManager(self.db).listar_x_residente(us)
        aux['tipoeventos'] = TipoEventoManager(self.db).listar_todo()
        aux['areasociales'] = AreasocialManager(self.db).listar_todo(us)
        aux['tipopases'] = TipopaseManager(self.db).listar_todo()
        aux['eventos'] = EventoManager(self.db).listar_eventos_dia(us)

        return aux

    def insert(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        EventoManager(self.db).insert(diccionary)
        self.respond(success=True, message='Insertado correctamente.')

    def update(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        diccionary['user'] = self.get_user_id()
        diccionary['ip'] = self.request.remote_ip
        EventoManager(self.db).update(diccionary)
        self.respond(success=True, message='Modificado correctamente.')


    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        id = diccionary['id']
        state = diccionary['enabled']
        respuesta = EventoManager(self.db).delete(id, self.get_user_id(), self.request.remote_ip,state)

        self.respond(success=True, message=respuesta)
        self.db.close()

    def validar_invitacion(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        indicted_object = EventoManager(self.db).validar_invitacion_lector(diccionary['codigoautorizacion'])
        objeto_dict = indicted_object.get_dict()


        if indicted_object:
            self.respond(objeto_dict,success=True, message='/resources/images/aceptado.png')
            self.db.close()
        else:
            self.respond(success=False, message='/resources/images/rechazado.png')
            self.db.close()


    def filtrar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))

        ins_manager = self.manager(self.db)
        fechainicio = datetime.strptime(data['fechainicio'], '%d/%m/%Y')
        fechafin = datetime.strptime(data['fechafin'], '%d/%m/%Y')
        user = self.get_user_id()
        arraT = EventoManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.filtrar(fechainicio, fechafin, user)

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='actualizado correctamente.')

