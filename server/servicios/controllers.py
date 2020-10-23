from tornado.gen import coroutine

from server.condominios.condominio.managers import *
from server.condominios.domicilio.managers import *
from server.condominios.evento.managers import *
from server.condominios.invitado.managers import *
from server.condominios.movimiento.managers import *
from server.condominios.residente.managers import *
from server.condominios.areasocial.managers import *
from server.condominios.marca.managers import *
from server.condominios.modelo.managers import *
from server.condominios.nropase.managers import *
from server.dispositivos.registros.managers import *
from server.condominios.movimiento_p.managers import *
from server.dispositivos.dispositivo.managers import *
from server.condominios.vehiculo.managers import *


from server.usuarios.login.managers import *
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from server.common.controllers import CrudController, SuperController, ApiController
import os.path
import json
import ast


class ApiCondominioController(ApiController):
    manager = ResidenteManager
    routes = {
        '/api/v1/login_movil': {'POST': 'login_movil'},
        '/api/v1/listar_tipo_documento': {'POST': 'listar_tipo_documento'},
        '/api/v1/listar_tipo_autorizacion': {'POST': 'listar_tipo_autorizacion'},
        '/api/v1/listar_tipo_pase': {'POST': 'listar_tipo_pase'},
        '/api/v1/listar_tipo_evento': {'POST': 'listar_tipo_evento'},
        '/api/v1/listar_tipo_vehiculo': {'POST': 'listar_tipo_vehiculo'},
        '/api/v1/listar_color': {'POST': 'listar_color'},
        '/api/v1/listar_marcas': {'POST': 'listar_marcas'},
        '/api/v1/listar_modelos': {'POST': 'listar_modelos'},
        '/api/v1/listar_modelos_x_marca': {'POST': 'listar_modelos_x_marca'},
        '/api/v1/listar_numero_pases': {'POST': 'listar_numero_pases'},

        '/api/v1/listar_vehiculo': {'POST': 'listar_vehiculo'},
        '/api/v1/listar_invitados_todos': {'POST': 'listar_invitados_todos'},
        '/api/v1/listar_invitados': {'POST': 'listar_invitados'},
        '/api/v1/listar_domicilios': {'POST': 'listar_domicilios'},
        '/api/v1/listar_areas_sociales': {'POST': 'listar_areas_sociales'},
        '/api/v1/listar_eventos': {'POST': 'listar_eventos'},
        '/api/v1/listar_invitacion': {'POST': 'listar_invitacion'},
        '/api/v1/listar_residentes': {'POST': 'listar_residentes'},
        '/api/v1/listar_movimientos': {'POST': 'listar_movimientos'},
        '/api/v1/insertar_invitado': {'POST': 'insertar_invitado'},
        '/api/v1/insertar_vehiculo': {'POST': 'insertar_vehiculo'},
        '/api/v1/insertar_evento': {'POST': 'insertar_evento'},
        '/api/v1/insertar_invitacion': {'POST': 'insertar_invitacion'},
        '/api/v1/insertar_invitacion_rapida': {'POST': 'insertar_invitacion_rapida'},
        '/api/v1/insertar_movimiento': {'POST': 'insertar_movimiento'},
        '/api/v1/insertar_movimiento_peatonal': {'POST': 'insertar_movimiento_peatonal'},
        '/api/v1/validar_codigo': {'POST': 'validar_codigo'},
        '/api/v1/validar_qr_residente': {'POST': 'validar_qr_residente'},
        '/api/v1/cancelar_evento': {'POST': 'cancelar_evento'},
        '/api/v1/cancelar_invitacion': {'POST': 'cancelar_invitacion'},
        '/api/v1/cancelar_invitacion_rapida': {'POST': 'cancelar_invitacion_rapida'},
        '/api/v1/actualizar_credenciales': {'POST': 'actualizar_credenciales'},
        '/api/v1/actualizar_foto': {'POST': 'actualizar_foto'},
        '/api/v1/actualizar_evento': {'POST': 'actualizar_evento'},

        '/api/v1/actualizar_invitado': {'POST': 'actualizar_invitado'},
        '/api/v1/actualizar_vehiculo': {'POST': 'actualizar_vehiculo'},
        '/api/v1/movimiento_salida': {'POST': 'movimiento_salida'},

        '/api/v1/listar_dispositivos': {'POST': 'listar_dispositivos'},
        '/api/v1/marcaciones_dispositivo': {'POST': 'marcaciones_dispositivo'},
        '/api/v1/listar_nuevas_configuraciones': {'POST': 'listar_nuevas_configuraciones'},
        '/api/v1/configuraciones_procesadas': {'POST': 'configuraciones_procesadas'},

        '/api/v1/sincronizar_condominio': {'POST': 'sincronizar_condominio'},
        '/api/v1/sincronizar_usuario': {'POST': 'sincronizar_usuario'},
        '/api/v1/sincronizar_invitado': {'POST': 'sincronizar_invitado'},
        '/api/v1/sincronizar_evento': {'POST': 'sincronizar_evento'},
        '/api/v1/sincronizar_invitacion': {'POST': 'sincronizar_invitacion'},
        '/api/v1/sincronizar_invitacion_rapida': {'POST': 'sincronizar_invitacion_rapida'},
        '/api/v1/sincronizar_cancelar_evento': {'POST': 'sincronizar_cancelar_evento'},
        '/api/v1/sincronizar_cancelar_invitacion': {'POST': 'sincronizar_cancelar_invitacion'},
        '/api/v1/sincronizar_cancelar_invitacion_rapida': {'POST': 'sincronizar_cancelar_invitacion_rapida'},
        '/api/v1/sincronizar_actualizar_evento': {'POST': 'sincronizar_actualizar_evento'}
    }


    def login_movil(self):
        self.set_session()
        data = json.loads(self.request.body.decode('utf-8'))
        username = data['username']
        password = data['password']
        ip = data['ip']
        user = LoginManager().login(username, password)
        print("login user:" + str(username))

        if user:
            fecha = self.fecha_actual()
            b = Bitacora(fkusuario=user.id, ip=ip, accion="Inicio de sesión.", fecha=fecha)
            self.insertar_bitacora(b)
            users =  UsuarioManager(self.db).get_by_pass(user.id)
            usuario = users.get_dict()
            usuario['rol']['modulos'] = None

            self.respond(success=True, response=usuario, message='Usuario Logueado correctamente.')

        else:
            self.respond(success=False, response="", message='El Usuario no se pudo Loguear.')

    def listar_tipo_pase(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = TipopaseManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Tipo pase recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_tipo_documento(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = TipodocumentoManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Tipo documento recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_tipo_autorizacion(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = AutorizacionManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Tipo autorizacion recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_tipo_evento(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = TipoEventoManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Tipo evento recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_tipo_vehiculo(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = TipovehiculoManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Tipo evento recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_color(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = ColorManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Tipo evento recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_marcas(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = MarcaManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Marcas recuperadas correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_modelos(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = ModeloManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Modelos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_modelos_x_marca(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            idmarca = data['idmarca']
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = ModeloManager(self.db).listar_x_marca(idmarca)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Modelos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_vehiculo(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = VehiculoManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                obj_dict['residente'] = None
                obj_dict['invitado'] = None
                obj_dict['nropase'] =  None

                resp.append(obj_dict)

            self.db.close()

            self.respond(response=resp, success=True, message="Vehiculos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_invitados_todos(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = InvitadoManager(self.db).listar_todo()
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                obj_dict['vehiculos'] = None
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Eventos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_invitados(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            user= data['user']
            usuario = UsuarioManager(self.db).obtener_x_codigo(user)

            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = InvitadoManager(self.db).listar_x_residente(usuario)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                obj_dict['vehiculos'] = None
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Eventos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_numero_pases(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            user= data['user']
            usuario = UsuarioManager(self.db).obtener_x_codigo(user)

            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = NropaseManager(self.db).listar_numero_pases(usuario)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Domicilios recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_domicilios(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            user= data['user']
            usuario = UsuarioManager(self.db).obtener_x_codigo(user)

            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = DomicilioManager(self.db).listar_domicilios(usuario)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Domicilios recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_areas_sociales(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            user= data['user']
            usuario = UsuarioManager(self.db).obtener_x_codigo(user)

            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = AreasocialManager(self.db).listar_todo(usuario)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Areas Sociales recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_eventos(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            user= data['user']
            fechai = data['fechai']
            fechaf = data['fechaf']
            usuario = UsuarioManager(self.db).obtener_x_codigo(user)

            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            # arraT['objeto'] = EventoManager(self.db).listar_eventos(usuario)
            arraT['objeto'] = EventoManager(self.db).filtrar(fechai, fechaf, user)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Eventos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: evento
    def listar_invitacion(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            idevento= data['evento']

            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = InvitacionManager(self.db).obtener_invitaciones(idevento)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Invitaciones recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_residentes(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            user = data['user']
            usuario = UsuarioManager(self.db).obtener_x_codigo(user)

            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = CondominioManager(self.db).obtener_residentes(usuario.fkcondominio)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Residentes recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_movimientos(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            user = data['user']
            usuario = UsuarioManager(self.db).obtener_x_codigo(user)

            fechai = data['fechai']
            fechaf = data['fechaf']
            # usuario = UsuarioManager(self.db).get_by_pass(user)

            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            # arraT['objeto'] = CondominioManager(self.db).obtener_movimientos(usuario.fkcondominio)
            arraT['objeto'] = MovimientoManager(self.db).filtrar_movil(fechai, fechaf, usuario)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                resp.append(obj_dict)
            self.db.close()

            self.respond(response=resp, success=True, message="Movimientos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()


    # insercciones

    # sincr
    def insertar_invitado(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id

            invi =InvitadoManager(self.db).insert(data)
            invita = invi.get_dict()

            principal = self.db.query(Principal).first()
            if principal.estado:
                    self.funcion_sincronizar(u, data, "sincronizar_invitado")


            self.respond(response=invita,success=True, message='Insertado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def insertar_vehiculo(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            data['id']= ""
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id

            VehiculoManager(self.db).registrar_vehiculo_invitado(data,data['fkinvitado'])
            self.respond(success=True, message='Insertado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def insertar_evento(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id
            data['fkareasocial']  =""

            event = EventoManager(self.db).insert(data)

            principal = self.db.query(Principal).first()
            if principal.estado:
                event.codigo = event.id
                data['codigo'] = event.id
                self.db.merge(event)
                self.db.commit()
                self.funcion_sincronizar(u,data,"sincronizar_evento")

            self.respond(success=True, message='Insertado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def insertar_invitacion(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id

            resp = InvitacionManager(self.db).insert(data)

            principal = self.db.query(Principal).first()
            if principal.estado:
                data['codigoautorizacion'] = resp.codigoautorizacion

                invi = InvitadoManager(self.db).obtener_x_id(data['fkinvitado'])
                data['ci'] = invi.ci

                self.funcion_sincronizar(u,data,"sincronizar_invitacion")

            invitacion = resp.get_dict()
            self.respond(response=invitacion, success=True, message='Insertado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def insertar_invitacion_rapida(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id
            data['codigoautorizacion'] = ""

            resp = EventoManager(self.db).insertar_invitacion_rapida(data)

            principal = self.db.query(Principal).first()
            if principal.estado:
                resp.codigo = resp.id
                data['codigo'] = resp.id
                self.db.merge(resp)
                self.db.commit()

                invi = InvitadoManager(self.db).obtener_x_id(data['fkinvitado'])
                data['ci'] = invi.ci

                data['codigoautorizacion'] = resp.invitaciones[0].codigoautorizacion

                self.funcion_sincronizar(u, data, "sincronizar_invitacion_rapida")

            resp_dict = resp.get_dict()
            self.respond(response=resp_dict,success=True, message='Insertado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def insertar_movimiento(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id
            print("ingreso Vehicular movil ci: " + str(data['ci']))
            resp = MovimientoManager(self.db).insert(data)
            objeto = resp.get_dict()
            self.respond(response=objeto, success=True, message='Insertado correctamente.')


        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def insertar_movimiento_peatonal(self):
            try:
                self.set_session()
                data = json.loads(self.request.body.decode('utf-8'))
                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id
                print("ingreso Peatonal movil ci: " + str(data['ci']))
                resp = Movimiento_pManager(self.db).insert(data)
                objeto = resp.get_dict()
                self.respond(response=objeto, success=True, message='Insertado correctamente.')

            except Exception as e:
                print(e)
                self.respond(response=str(e), success=False, message=str(e))
            self.db.close()

    def validar_codigo(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            codigo = data['codigo']
            resp = EventoManager(self.db).validar_invitacion_lector(codigo)
            if resp:
                invitacion = resp.get_dict()
                self.respond(response=invitacion, success=True, message='Codigo Aceptado.')
            else:
                self.respond(response=resp, success=False, message='Codigo Denegado.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def validar_qr_residente(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            codigo = data['codigo']
            resp = ResidenteManager(self.db).validar_codigo(codigo)
            if resp:
                self.respond(response=resp, success=True, message='Codigo Aceptado.')
            else:
                self.respond(response=resp, success=False, message='Codigo Denegado.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def cancelar_evento(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id

            print(str(data))

            resp = EventoManager(self.db).delete(data['idevento'],data['estado'], data['user'], data['ip'])

            principal = self.db.query(Principal).first()
            if principal.estado:

                self.funcion_sincronizar(u,data,"sincronizar_cancelar_evento")


            self.respond(response=None, success=True, message='Evento Cancelado.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def cancelar_invitacion(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id
            resp = InvitacionManager(self.db).delete(data['idinvitacion'], data['estado'], data['user'], data['ip'])

            principal = self.db.query(Principal).first()
            if principal.estado:

                data['codigoqr'] = resp.codigoautorizacion

                self.funcion_sincronizar(u,data,"sincronizar_cancelar_invitacion")

            self.respond(response=None, success=True, message='Invitacion Cancelada.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def cancelar_invitacion_rapida(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id
            resp = InvitacionManager(self.db).delete_invitacion_rapida(data['idinvitacion'], data['estado'], data['user'], data['ip'])

            principal = self.db.query(Principal).first()
            if principal.estado:

                data['codigoqr'] = resp.codigoautorizacion

                self.funcion_sincronizar(usuario, data, "sincronizar_cancelar_invitacion_rapida")

            self.respond(response=None, success=True, message='Invitacion rapida Cancelada.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_credenciales(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id

            resp = UsuarioManager(self.db).actualizar_credenciales(data)
            self.respond(response=resp['response'], success=resp['success'], message=resp['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_foto(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id

            resp =ResidenteManager(self.db).actualizar_foto(data)


            self.respond(response=None, success=resp['success'], message=resp['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_invitado(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id

            InvitadoManager(self.db).update(data)
            self.respond(success=True, message='Insertado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_vehiculo(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id
            data['id']= ""

            VehiculoManager(self.db).update(data)
            self.respond(success=True, message='Insertado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def movimiento_salida(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id
            idmovimiento = data['idmovimiento']
            user = data['user']
            ip = data['ip']
            resp = MovimientoManager(self.db).salida(idmovimiento, user, ip)
            self.respond(response=None, success=True, message='Salida Actualizada Correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_evento(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id

            even = EventoManager(self.db).actualizar(data)

            principal = self.db.query(Principal).first()
            if principal.estado:
                print("principal")
                data['codigo'] = even.id
                print(data)
                self.funcion_sincronizar(u,data,"sincronizar_actualizar_evento")


            # evento = even.get_dict()
            self.respond(success=True, response=None, message='Evento Actualizado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()


    # Funciones de Integracion dispositivos

    def listar_nuevas_configuraciones(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            x = ast.literal_eval(data)
            print("ws listar nuevas configuraciones " + str(x['idinterprete']))
            self.set_session()
            arraT = self.manager(self.db).get_page(1, 10, None, None, True)
            resp = []

            arraT['objeto'] = ConfiguraciondispositivoManager(self.db).listar_todo(x)
            for item in arraT['objeto']:
                obj_dict = item.get_dict()
                obj_dict['condominio'] = None
                obj_dict['tipodispositivo'] = None
                obj_dict['interpretes'] = None
                obj_dict['cerraduras'] = None

                resp.append(obj_dict)

            self.db.close()

            self.respond(response=resp,success=True, message="nuevos accesos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def marcaciones_dispositivo(self):
        self.set_session()
        data = json.loads(self.request.body.decode('utf-8'))
        x = ast.literal_eval(data)
        print("ws marcaciones dispositivo " + str(x['iddispositivo']))

        RegistrosManager(self.db).insertRegistros(x)
        self.respond(success=True, message='Insertado correctamente.')

    def listar_dispositivos(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            x = ast.literal_eval(data)
            print("ws listar dispositivos " + str(data['idinterprete']))

            resp = DispositivoManager(self.db).listar_todo_cant_marcaciones(data)

            self.db.close()

            self.respond(response=resp,success=True, message="dispositivos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def configuraciones_procesadas(self):
        self.set_session()
        data = json.loads(self.request.body.decode('utf-8'))
        x = ast.literal_eval(data)
        print("ws configuraciones procesadas ")

        ConfiguraciondispositivoManager(self.db).actualizar_codigos(x)
        self.respond(success=True, message='Actualizado correctamente.')


    # Funciones de Sincronizacion

    def funcion_sincronizar(self ,u,data, ws):
        try:
            if u.fkcondominio:
                if u.condominio.ip_publica != "":
                    url = "http://" + u.condominio.ip_publica + ":" + u.condominio.puerto + "/api/v1/" + ws

                    headers = {'Content-Type': 'application/json'}
                    string = data
                    cadena = json.dumps(string)
                    body = cadena
                    resp = requests.post(url, data=body, headers=headers, verify=False)
                    response = json.loads(resp.text)

                    # print(response)


        except Exception as e:
            # Other errors are possible, such as IOError.
            print("Error de conexion funcion sincronizar: " + str(e))

    def sincronizar_condominio(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            print("servicio registrar condominio")

            CondominioManager(self.db).insert(data)
            self.respond(response=None, success=True, message='Condominio registrado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_usuario(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            # user = UsuarioManager(self.db).insert(data)
            # user = user.get_dict()
            self.respond(response=None, success=True, message='Usuario Registrado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_invitado(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id

            invi = InvitadoManager(self.db).insert(data)
            invita = invi.get_dict()
            self.respond(response=invita, success=True, message='Insertado correctamente.')
        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_evento(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id

            data['fkresidente'] = u.fkresidente

            domi = ResidenteManager(self.db).obtener_domicilios(u.fkresidente)
            data['fkdomicilio'] = domi.id

            EventoManager(self.db).insert(data)
            self.respond(response=None, success=True, message='Insertado correctamente.')
        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_invitacion(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id

            event = EventoManager(self.db).obtener_x_codigo(data['fkevento'])
            data['fkevento'] = event.id

            invi = InvitadoManager(self.db).obtener_x_ci(data['ci'])
            data['fkinvitado'] = invi.id

            resp = InvitacionManager(self.db).insert(data)
            invitacion = resp.get_dict()
            self.respond(response=invitacion, success=True, message='Insertado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_invitacion_rapida(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id

            data['fkresidente'] = u.fkresidente

            domi = ResidenteManager(self.db).obtener_domicilios(u.fkresidente)
            data['fkdomicilio'] = domi.id


            invi = InvitadoManager(self.db).obtener_x_ci(data['ci'])
            data['fkinvitado'] = invi.id


            EventoManager(self.db).insertar_invitacion_rapida(data)
            self.respond(response=None, success=True, message='Insertado correctamente.')
        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_cancelar_evento(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id

            event = EventoManager(self.db).obtener_x_codigo(data['idevento'])
            data['idevento'] = event.id

            resp = EventoManager(self.db).delete(data['idevento'], data['estado'], data['user'], data['ip'])
            self.respond(response=None, success=True, message='Evento Cancelado.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_cancelar_invitacion(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id

            inv = InvitacionManager(self.db).obtener_x_codigo(data['codigoqr'])
            data['idinvitacion'] = inv.id

            resp = InvitacionManager(self.db).delete(data['idinvitacion'], data['estado'], data['user'], data['ip'])

            self.respond(response=None, success=True, message='Invitacion Cancelada.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_cancelar_invitacion_rapida(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = usuario.id

            inv = InvitacionManager(self.db).obtener_x_codigo(data['codigoqr'])
            data['idinvitacion'] = inv.id

            resp = InvitacionManager(self.db).delete_invitacion_rapida(data['idinvitacion'], data['estado'], data['user'], data['ip'])

            self.respond(response=None, success=True, message='Invitacion Cancelada.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_actualizar_evento(self):
        try:
            self.set_session()

            data = json.loads(self.request.body.decode('utf-8'))

            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
            data['user'] = u.id

            event = EventoManager(self.db).obtener_x_codigo(data['codigo'])
            data['id'] = event.id


            EventoManager(self.db).actualizar(data)
            self.respond(response=None, success=True, message='Insertado correctamente.')
        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()



    # Funciones de Bitacora
    def insertar_bitacora(self, bitacora):
        with transaction() as session:
            session.add(bitacora)
            session.commit()
    def obtener_usuario(self, Usuario_id):
        with transaction() as session:
            return session.query(Usuario).filter(Usuario.id == Usuario_id).first()
    def fecha_actual(self):
        return datetime.now(pytz.timezone('America/La_Paz'))