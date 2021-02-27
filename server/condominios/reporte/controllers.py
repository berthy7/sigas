from .managers import *
from server.common.controllers import CrudController
from server.condominios.condominio.managers import CondominioManager
from ..movimiento.managers import *
from ..movimiento_p.managers import *

import os.path
import uuid
import json


class ReporteController(CrudController):

    manager = MovimientoManager
    html_index = "condominios/reporte/views/index.html"
    html_table = "condominios/reporte/views/table.html"
    routes = {
        '/reporte': {'GET': 'index', 'POST': 'table'},
        '/reporte_general': {'POST': 'reporte_general'},
        '/reporte_vehicular_visita': {'PUT': 'vehicular_visita'},
        '/reporte_peatonal_visita': {'PUT': 'peatonal_visita'},
        '/reporte_vehicular_residente': {'PUT': 'vehicular_residente'},
        '/reporte_peatonal_residente': {'PUT': 'peatonal_residente'},
        '/reporte_singuardia_visita': {'PUT': 'singuardia_visita'}
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []
        aux['movimientos'] = MovimientoManager(self.db).list_all()
        aux['condominios'] = CondominioManager(self.db).listar_todo()

        return aux


    def reporte_general(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        fechainicio = diccionary['fechainicio']
        fechafin = diccionary['fechafin']
        cname = self.manager(self.db).reporte_movimientos_vehicular(diccionary)
        self.respond({'nombre': cname, 'url': 'resources/downloads/' + cname}, True)
        self.db.close()


    def vehicular_visita(self):
        self.set_session()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        # indicted_object = ins_manager.obtain(diccionary['id'])
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.reporte_movimientos_vehicular(diccionary)
        print("entrando al respond")
        self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
        print("saliendo del respond")
        self.db.close()


    def peatonal_visita(self):
        self.set_session()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        # indicted_object = ins_manager.obtain(diccionary['id'])
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = Movimiento_pManager(self.db).reporte_movimientos_peatonal(diccionary)
        self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
        self.db.close()

    def vehicular_residente(self):
        self.set_session()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        # indicted_object = ins_manager.obtain(diccionary['id'])
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.list_all_reporte()
        self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
        self.db.close()

    def peatonal_residente(self):
        self.set_session()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        # indicted_object = ins_manager.obtain(diccionary['id'])
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.list_all_reporte()
        self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
        self.db.close()

    def singuardia_visita(self):
        self.set_session()
        ins_manager = self.manager(self.db)
        diccionary = json.loads(self.get_argument("object"))
        # indicted_object = ins_manager.obtain(diccionary['id'])
        arraT = ins_manager.get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.list_all_reporte()
        self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
        self.db.close()
