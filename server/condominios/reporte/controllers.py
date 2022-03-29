from .managers import *
from server.common.controllers import CrudController
from server.condominios.condominio.managers import CondominioManager
from ..movimiento.managers import *
from ..movimiento_p.managers import *

import os.path
import uuid
import json
import threading


class ReporteController(CrudController):

    manager = ReporteManager
    html_index = "condominios/reporte/views/index.html"

    routes = {
        '/reporte': {'GET': 'index', 'POST': 'table'},
        '/reporte_general': {'POST': 'reporte_general_excel'},
        '/reporte_generar': {'POST': 'reporte_generar'},
        '/reporte_vehicular_visita': {'POST': 'vehicular_visita'},
        '/reporte_peatonal_visita': {'POST': 'peatonal_visita'},
        '/reporte_vehicular_residente': {'PUT': 'vehicular_residente'},
        '/reporte_peatonal_residente': {'PUT': 'peatonal_residente'},
        '/reporte_singuardia_visita': {'PUT': 'singuardia_visita'}
    }


    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

        aux['idcondominio'] = us.fkcondominio
        aux['sigas'] = us.sigas
        aux['movimientos'] = MovimientoManager(self.db).list_all()
        aux['condominios'] = CondominioManager(self.db).listar_todo()

        return aux


    def vehicular_visita(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))

        ins_manager = self.manager(self.db)

        lista_dict = ins_manager.reporte_vehicular_visita(data)

        self.respond(response=lista_dict, success=True,
                     message='actualizado correctamente.')


    def peatonal_visita(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))

        ins_manager = self.manager(self.db)

        lista_dict = ins_manager.reporte_peatonal_visita(data)

        self.respond(response=lista_dict, success=True,
                     message='actualizado correctamente.')


    # def table(self):
    #     self.set_session()
    #     self.verif_privileges()
    #     data = json.loads(self.get_argument('data'))
    #     employees_id = data['employees'][:]
    #     i_date = datetime.strptime(data['i_date'], '%d/%m/%Y').date()
    #     f_date = datetime.strptime(data['f_date'], '%d/%m/%Y').date()
    #     report = self.reports[data['type_rp']]
    #     if report == 'temporal':
    #         self.render('attendance/views/report_' + report + '.html',
    #                     report=getattr(AttendanceReport(self.db),self.reports[data['type_rp']])(i_date, f_date,
    #                                                                   employees_id,
    #                                                                   data['empresa_id'],
    #                                                                   data['sucursal_id'],
    #                                                                   data['mngmn_id'],
    #                                                                   data['group_id'],
    #                                                                   data['emp_id'],
    #                                                                   data['h_tipo']))
    #     else:
    #         self.render('attendance/views/report_' + report + '.html',
    #                     report=getattr(AttendanceReport(self.db),
    #                                    self.reports[data['type_rp']])(i_date, f_date,
    #                                                                   employees_id,
    #                                                                   data['mngmn_id'],
    #                                                                   data['group_id'],
    #                                                                   data['emp_id'],
    #                                                                   data['sucursal_id'],
    #                                                                   data['empresa_id']))
    #     self.db.close()

    # def reporte_general(self):
    #     self.set_session()
    #     diccionary = json.loads(self.get_argument("object"))
    #     fechainicio = diccionary['fechainicio']
    #     fechafin = diccionary['fechafin']
    #
    #
    #     cname = self.manager(self.db).reporte_movimientos_vehicular(diccionary)
    #
    #
    #
    #     self.respond({'nombre': cname, 'url': 'resources/downloads/' + cname}, True)
    #     self.render('attendance/views/tabla_vehicular_visita.html',report=self.manager(self.db).delay(diccionary))
    #     self.db.close()

    # def reporte_general(self):
    #     self.set_session()
    #     diccionary = json.loads(self.get_argument("object"))
    #     fechainicio = diccionary['fechainicio']
    #     fechafin = diccionary['fechafin']
    #
    #delay
    #     cname = self.manager(self.db).reporte_movimientos_vehicular(diccionary)
    #
    #
    #
    #     self.respond({'nombre': cname, 'url': 'resources/downloads/' + cname}, True)
    #     self.db.close()

    # def vehicular_visita(self):
    #     self.set_session()
    #     ins_manager = self.manager(self.db)
    #     diccionary = json.loads(self.get_argument("object"))
    #     # indicted_object = ins_manager.obtain(diccionary['id'])
    #     arraT = ins_manager.get_page(1, 10, None, None, True)
    #     arraT['datos'] = ins_manager.reporte_movimientos_vehicular(diccionary)
    #     print("entrando al respond")
    #     self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
    #     print("saliendo del respond")
    #     self.db.close()


    # def index(self):
    #     self.set_session()
    #     self.verif_privileges()
    #     usuario = self.get_user()
    #     result = self.manager(self.db).list_all()
    #     result['privileges'] = UsuarioManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
    #     result['condominio'] = CondominioManager(self.db).obtener_condominio_x_usuario(usuario)
    #     result.update(self.get_extra_data())
    #     self.render(self.html_index, **result)
    #     self.db.close()


    # def vehicular_visita(self):
    #     self.set_session()
    #     ins_manager = self.manager(self.db)
    #     diccionary = json.loads(self.get_argument("object"))
    #
    #     # indicted_object = ins_manager.delay(diccionary)
    #
    #     # self.respond(indicted_object, message='Operacion exitosa!')
    #     # self.render(self.html_table, **indicted_object)
    #     self.render('condominios/reporte/views/tabla_vehicular_visita-.html', report=self.manager(self.db).delay(diccionary))
    #     self.db.close()


    # def filtrar(self):
    #     self.set_session()
    #     data = json.loads(self.get_argument("object"))
    #     us = self.get_user()
    #     ins_manager = self.manager(self.db)
    #     fechainicio = datetime.strptime(data['fechainicio'], '%d/%m/%Y')
    #     fechafin = datetime.strptime(data['fechafin'], '%d/%m/%Y')
    #     indicted_object = ins_manager.filtrar(fechainicio, fechafin,us)
    #     self.respond(indicted_object, message='Operacion exitosa!')
    #     self.db.close()

    # def vehicular_visita(self):
    #     self.set_session()
    #     ins_manager = self.manager(self.db)
    #     diccionary = json.loads(self.get_argument("object"))
    #     # indicted_object = ins_manager.obtain(diccionary['id'])
    #     arraT = ins_manager.get_page(1, 10, None, None, True)
    #     arraT['datos'] = ins_manager.list_all_reporte()
    #     self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
    #     self.db.close()



    # def peatonal_visita(self):
    #     self.set_session()
    #     ins_manager = self.manager(self.db)
    #     diccionary = json.loads(self.get_argument("object"))
    #     # indicted_object = ins_manager.obtain(diccionary['id'])
    #     arraT = ins_manager.get_page(1, 10, None, None, True)
    #     arraT['datos'] = Movimiento_pManager(self.db).reporte_movimientos_peatonal(diccionary)
    #     self.respond([objeto_regreso.get_dict() for objeto_regreso in arraT['datos']])
    #     self.db.close()

    def reporte_generar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))

        ins_manager = MovimientoManager(self.db)
        arraT = BitacoraManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.reporte_generar(data)

        self.respond(response='', success=True,
                     message='actualizado correctamente.')




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
