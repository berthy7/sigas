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
        '/api/v1/logout_movil': {'POST': 'logout_movil'},
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

        '/api/v1/buscar_invitado': {'POST': 'buscar_invitado'},
        '/api/v1/buscar_vehiculo': {'POST': 'buscar_vehiculo'},

        '/api/v1/listar_dispositivos': {'POST': 'listar_dispositivos'},
        '/api/v1/listar_dispositivos_locales': {'POST': 'listar_dispositivos_locales'},
        '/api/v1/marcaciones_dispositivo': {'POST': 'marcaciones_dispositivo'},
        '/api/v1/listar_nuevas_configuraciones': {'POST': 'listar_nuevas_configuraciones'},
        '/api/v1/configuraciones_procesadas': {'POST': 'configuraciones_procesadas'},

        '/api/v1/sincronizar_condominio': {'POST': 'sincronizar_condominio'},
        '/api/v1/sincronizar_usuario': {'POST': 'sincronizar_usuario'},
        '/api/v1/sincronizar_usuario_estado': {'POST': 'sincronizar_usuario_estado'},
        '/api/v1/sincronizar_residente': {'POST': 'sincronizar_residente'},
        '/api/v1/sincronizar_invitado': {'POST': 'sincronizar_invitado'},
        '/api/v1/sincronizar_evento': {'POST': 'sincronizar_evento'},
        '/api/v1/sincronizar_invitacion': {'POST': 'sincronizar_invitacion'},
        '/api/v1/sincronizar_movimiento': {'POST': 'sincronizar_movimiento'},
        '/api/v1/sincronizar_movimiento_salida': {'POST': 'sincronizar_movimiento_salida'},
        '/api/v1/sincronizar_invitacion_rapida': {'POST': 'sincronizar_invitacion_rapida'},
        '/api/v1/sincronizar_cancelar_evento': {'POST': 'sincronizar_cancelar_evento'},
        '/api/v1/sincronizar_cancelar_invitacion': {'POST': 'sincronizar_cancelar_invitacion'},
        '/api/v1/sincronizar_cancelar_invitacion_rapida': {'POST': 'sincronizar_cancelar_invitacion_rapida'},
        '/api/v1/sincronizar_actualizar_evento': {'POST': 'sincronizar_actualizar_evento'}
    }

    def buscar_invitado(self):
        print("consulto buscar_invitado")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                indicted_object = InvitadoManager(self.db).buscar_ci(data['ci'])

                self.db.close()

                if indicted_object:
                    self.respond(response=indicted_object, success=True, message='Resultado Obtenido!')
                else:
                    self.respond(response=None, success=False, message='No se encontraron resultados')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def buscar_vehiculo(self):
        print("consulto buscar_vehiculo")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                indicted_object = VehiculoManager(self.db).buscar_placa(data['placa'])

                self.db.close()

                if indicted_object:
                    self.respond(response=indicted_object, success=True, message='Resultado Obtenido!')
                else:
                    self.respond(response=None, success=False, message='No se encontraron resultados')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()


    def login_movil(self):
        self.set_session()
        data = json.loads(self.request.body.decode('utf-8'))

        Respuestaversion = self.consultar_version(data)

        if Respuestaversion['respuesta']:
            print("login_movil: "+ Respuestaversion['mensaje'])
            print("login: " + data['username'])

            user_correcto = LoginManager().verificar_usuario_correcto(data['username'], data['password'])

            if user_correcto:

                user = LoginManager().login(data['username'], data['password'])

                if user:
                    if user.login is False:
                        fecha = self.fecha_actual()
                        b = Bitacora(fkusuario=user.id, ip=data['ip'], accion="Inicio de sesión movil.", fecha=fecha)
                        self.insertar_bitacora(b)
                        users =  UsuarioManager(self.db).get_by_pass(user.id)
                        usuario = users.get_dict()
                        usuario['rol']['modulos'] = None

                        users = UsuarioManager(self.db).login_token(users)
                        usuario['token'] = users.token


                        self.respond(success=True, response=usuario, message='Usuario Logueado correctamente.')

                    else:
                        self.respond(success=False, response='', message='Este usuario ya esta logeado')


                else:
                    self.respond(success=False, response='', message='Usuario Deshabilitado')
            else:
                self.respond(success=False, response='', message='Usuario o Contraseña Incorrrecto')
        else:
            self.respond(success=False, response=Respuestaversion['mensaje'], message="version incorrecta")

    def logout_movil(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            user = UsuarioManager(self.db).obtener_x_codigo(data['user'])

            UsuarioManager(self.db).logout_sin_token(user)

            fecha = self.fecha_actual()
            b = Bitacora(fkusuario=user.id, ip=data['ip'], accion="Cierre de sesión movil.", fecha=fecha)
            self.insertar_bitacora(b)

            self.respond(response='', success=True, message="Usuario cerro sesion.")

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))


    def listar_tipo_pase(self):
        print("consulto listar_tipo_pase")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = TipopaseManager(self.db).listar_todo()
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Tipo pase recuperados correctamente.")

            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'], message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()


    def listar_tipo_documento(self):
        print("consulto listar_tipo_documento")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = TipodocumentoManager(self.db).listar_todo()
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Tipo documento recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                                 message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_tipo_autorizacion(self):
        print("consulto listar_tipo_autorizacion")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = AutorizacionManager(self.db).listar_todo()
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Tipo autorizacion recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_tipo_evento(self):
        print("consulto listar_tipo_evento")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = TipoEventoManager(self.db).listar_todo()
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Tipo evento recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_tipo_vehiculo(self):
        print("consulto listar_tipo_vehiculo")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = TipovehiculoManager(self.db).listar_todo()
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Tipo evento recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_color(self):
        print("consulto listar_color")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = ColorManager(self.db).listar_todo()
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="colores recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_marcas(self):
        print("consulto listar_marcas")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:
                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = MarcaManager(self.db).listar_todo()
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Marcas recuperadas correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_modelos(self):
        print("consulto listar_modelos")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = ModeloManager(self.db).listar_todo()
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Modelos recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_modelos_x_marca(self):
        print("consulto listar_modelos_x_marca")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = ModeloManager(self.db).listar_x_marca(data['idmarca'])
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Modelos recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_vehiculo(self):
        print("consulto listar_vehiculos")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT = VehiculoManager(self.db).listar_todo_dict()
                # for item in arraT['objeto']:
                #     obj_dict = item.get_dict()
                #     obj_dict['residente'] = None
                #     obj_dict['invitado'] = None
                #     obj_dict['nropase'] =  None
                #
                #     resp.append(obj_dict)

                self.db.close()

                print("response listar_vehiculo")

                self.respond(response=[item.get_dict() for item in arraT['objeto']], success=True, message="Vehiculos recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_invitados_todos(self):
        print("consulto listar_invitados_todos")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:
                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = InvitadoManager(self.db).listar_todo()
                cont = 1
                for item in arraT['objeto']:
                    print("conteo" + str(cont))
                    obj_dict = item.get_dict()
                    obj_dict['vehiculos'] = None
                    resp.append(obj_dict)
                    cont = cont + 1
                self.db.close()
                print("response listar_invitados_todos")
                self.respond(response=resp, success=True, message="Eventos recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_invitados(self):
        print("consulto listar_invitados")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT = InvitadoManager(self.db).listar_x_usuario_dict(usuario)

                # for item in arraT['objeto']:
                #     print("conteo"+ str(cont))
                #     obj_dict = item.get_dict()
                #     obj_dict['vehiculos'] = None
                #     resp.append(obj_dict)
                #     cont = cont +1
                self.db.close()

                print("response listar_invitados")

                self.respond(response=[item.get_dict() for item in arraT['objeto']], success=True, message="Invitados recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_numero_pases(self):
        print("consulto listar_numero_pases")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = NropaseManager(self.db).listar_numero_pases(usuario)
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Domicilios recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_domicilios(self):
        print("consulto listar_domicilios")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = DomicilioManager(self.db).listar_domicilios(usuario)
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Domicilios recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_areas_sociales(self):
        print("consulto listar_areas_sociales")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = AreasocialManager(self.db).listar_todo(usuario)
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Areas Sociales recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_eventos(self):
        print("consulto listar_eventos")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:
                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = EventoManager(self.db).filtrar(data['fechai'], data['fechaf'], data['user'])
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Eventos recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: evento
    def listar_invitacion(self):
        print("consulto listar_invitacion")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = InvitacionManager(self.db).obtener_invitaciones(data['evento'])
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Invitaciones recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_residentes(self):
        print("consulto listar_residentes")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = CondominioManager(self.db).obtener_residentes(usuario.fkcondominio)
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Residentes recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    # parametro: user
    def listar_movimientos(self):
        print("consulto listar_movimientos")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])

                arraT = self.manager(self.db).get_page(1, 10, None, None, True)
                resp = []

                arraT['objeto'] = MovimientoManager(self.db).filtrar_movil(data['fechai'], data['fechaf'], usuario)
                for item in arraT['objeto']:
                    obj_dict = item.get_dict()
                    resp.append(obj_dict)
                self.db.close()

                self.respond(response=resp, success=True, message="Movimientos recuperados correctamente.")
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()


    # insercciones

    # sincr
    def insertar_invitado(self):
        print("consulto insertar_invitado")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = u.id

                invi =InvitadoManager(self.db).insert(data)
                invita = invi.get_dict()

                principal = self.db.query(Principal).first()
                if principal.estado:
                        self.funcion_sincronizar(u, data, "sincronizar_invitado")


                self.respond(response=invita,success=True, message='Insertado correctamente.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def insertar_vehiculo(self):
        print("consulto insertar_vehiculo")

        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                data['id']= ""
                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id

                VehiculoManager(self.db).registrar_vehiculo_invitado(data,data['fkinvitado'])
                self.respond(success=True, message='Insertado correctamente.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def insertar_evento(self):
        print("consulto insertar_evento")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

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
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def insertar_invitacion(self):
        print("consulto insertar_invitacion")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

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

                invitacion['evento'] = None
                invitacion['invitado'] = None

                self.respond(response=invitacion, success=True, message='Insertado correctamente.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def insertar_invitacion_rapida(self):
        print("consulto insertar_invitacion_rapida")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

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
                resp_dict['residente'] = None
                resp_dict['domicilio'] = None
                resp_dict['areasocial'] = None

                self.respond(response=resp_dict,success=True, message='Insertado correctamente.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def insertar_movimiento(self):
        print("consulto insertar_movimiento")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:
                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id
                print("ingreso Vehicular movil ci: " + str(data['ci']))

                mov = MovimientoManager(self.db).insert(data)

                principal = self.db.query(Principal).first()
                if principal.estado:
                    mov.codigo = mov.id
                    data['codigo'] = mov.id
                    data['fechar'] = mov.fechar.strftime('%d/%m/%Y %H:%M:%S')
                    data['nombre_marca'] = mov.vehiculo.marca.nombre
                    data['nombre_modelo'] = mov.vehiculo.modelo.nombre if mov.vehiculo.fkmodelo else ""

                    if mov.nropase:
                        data['tarjeta'] = mov.nropase.tarjeta
                    else:
                        data['tarjeta'] = ""


                    if mov.fkdomicilio:
                        data['codigo_destino'] = mov.domicilio.codigo
                        condominio = CondominioManager(self.db).obtener_x_id(mov.domicilio.fkcondominio)

                    elif mov.fkareasocial:
                        data['codigo_destino'] = mov.areasocial.codigo
                        condominio = CondominioManager(self.db).obtener_x_id(mov.areasocial.fkcondominio)

                    else:
                        data['codigo_destino'] = ""
                        condominio = None

                    data['fkinvitado'] = ""
                    data['fkconductor'] = ""

                    self.funcion_sincronizar_x_condominio(condominio,data,"sincronizar_movimiento")

                objeto = mov.get_dict()
                objeto['residente'] = None
                objeto['domicilio'] = None
                objeto['areasocial'] = None
                self.respond(response=objeto, success=True, message='Insertado correctamente.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def insertar_movimiento_peatonal(self):
        print("consulto insertar_movimiento_peatonal")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id
                print("ingreso Peatonal movil ci: " + str(data['ci']))
                resp = Movimiento_pManager(self.db).insert(data)
                objeto = resp.get_dict()
                objeto['residente'] = None
                objeto['domicilio'] = None
                objeto['areasocial'] = None
                self.respond(response=objeto, success=True, message='Insertado correctamente.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def validar_codigo(self):
        print("consulto validar_codigo")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                resp = EventoManager(self.db).validar_invitacion_lector(data['codigo'])
                if resp:
                    invitacion = resp.get_dict()
                    invitacion['residente'] = None
                    invitacion['domicilio'] = None
                    invitacion['areasocial'] = None
                    self.respond(response=invitacion, success=True, message='Codigo Aceptado.')
                else:
                    self.respond(response=resp, success=False, message='Codigo Denegado.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def validar_qr_residente(self):
        print("consulto validar_qr_residente")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                resp = ResidenteManager(self.db).validar_codigo(data['codigo'])
                if resp:
                    self.respond(response=resp, success=True, message='Codigo Aceptado.')
                else:
                    self.respond(response=resp, success=False, message='Codigo Denegado.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def cancelar_evento(self):
        print("consulto cancelar_evento")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = u.id

                print(str(data))

                resp = EventoManager(self.db).delete(data['idevento'],data['estado'], data['user'], data['ip'])

                principal = self.db.query(Principal).first()
                if principal.estado:

                    self.funcion_sincronizar(u,data,"sincronizar_cancelar_evento")


                self.respond(response=None, success=True, message='Evento Cancelado.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def cancelar_invitacion(self):
        print("consulto cancelar_invitacion")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = u.id
                resp = InvitacionManager(self.db).delete(data['idinvitacion'], data['estado'], data['user'], data['ip'])

                principal = self.db.query(Principal).first()
                if principal.estado:

                    data['codigoqr'] = resp.codigoautorizacion

                    self.funcion_sincronizar(u,data,"sincronizar_cancelar_invitacion")

                self.respond(response=None, success=True, message='Invitacion Cancelada.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    # sincr
    def cancelar_invitacion_rapida(self):
        print("consulto cancelar_invitacion_rapida")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id
                resp = InvitacionManager(self.db).delete_invitacion_rapida(data['idinvitacion'], data['estado'], data['user'], data['ip'])

                principal = self.db.query(Principal).first()
                if principal.estado:

                    data['codigoqr'] = resp.codigoautorizacion

                    self.funcion_sincronizar(usuario, data, "sincronizar_cancelar_invitacion_rapida")

                self.respond(response=None, success=True, message='Invitacion rapida Cancelada.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_credenciales(self):
        print("consulto actualizar_credenciales")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id

                resp = UsuarioManager(self.db).actualizar_credenciales(data)
                self.respond(response=resp['response'], success=resp['success'], message=resp['message'])
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_foto(self):
        print("consulto actualizar_foto")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id

                resp =ResidenteManager(self.db).actualizar_foto(data)


                self.respond(response=None, success=resp['success'], message=resp['message'])
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])
        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_invitado(self):
        print("consulto actualizar_invitado")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:
                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id

                InvitadoManager(self.db).update(data)
                self.respond(success=True, message='Insertado correctamente.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])
        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_vehiculo(self):
        print("consulto actualizar_vehiculo")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id
                data['id']= ""

                VehiculoManager(self.db).update(data)
                self.respond(success=True, message='Insertado correctamente.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])
        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def movimiento_salida(self):
        print("consulto movimiento_salida")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:
                usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = usuario.id

                resp = MovimientoManager(self.db).salida(data['idmovimiento'], data['user'], data['ip'])

                principal = self.db.query(Principal).first()
                if principal.estado:

                     destino = MovimientoManager(self.db).obtener_destino(data['idmovimiento'])

                     if destino:
                         condominio = CondominioManager(self.db).obtener_x_id(destino.fkcondominio)

                     else:
                         condominio = None

                     data['fechaf'] = resp.fechaf.strftime('%d/%m/%Y %H:%M:%S')


                     self.funcion_sincronizar_x_condominio(condominio, data, "sincronizar_movimiento_salida")


                self.respond(response=None, success=True, message='Salida Actualizada Correctamente.')
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def actualizar_evento(self):
        print("consulto actualizar_evento")
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            Respuestausuario = self.verificar_usuario(data)

            if Respuestausuario['success']:

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
            else:
                self.respond(success=Respuestausuario['success'], response=Respuestausuario['response'],
                             message=Respuestausuario['message'])

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
            # x = ast.literal_eval(data)
            x = json.loads(data)

            resp = DispositivoManager(self.db).listar_todo_cant_marcaciones(x)
            DispositivoManager(self.db).verificar_estado(x)

            self.db.close()

            self.respond(response=resp,success=True, message="dispositivos recuperados correctamente.")
        except Exception as e:
            print(e)
            self.respond(response=0, success=False, message=str(e))
        self.db.close()

    def listar_dispositivos_locales(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            # x = ast.literal_eval(data)
            x = json.loads(data)

            print("servicio local")
            resp = DispositivoManager(self.db).listar_locales_cant_marcaciones(x)
            DispositivoManager(self.db).verificar_estado(x)

            self.db.close()

            self.respond(response=resp, success=True, message="dispositivos recuperados correctamente.")
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

    def funcion_sincronizar_x_condominio(self, condominio, data, ws):
        try:

            if condominio.ip_publica != "":
                url = "http://" + condominio.ip_publica + ":" + condominio.puerto + "/api/v1/" + ws

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

            user = UsuarioManager(self.db).insert(data)
            # user = user.get_dict()
            self.respond(response=None, success=True, message='Usuario Registrado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_usuario_estado(self):
        try:
            self.set_session()
            diccionary = json.loads(self.request.body.decode('utf-8'))

            u = UsuarioManager(self.db).obtener_x_codigo(diccionary['id'])

            user = UsuarioManager(self.db).state(u.id, diccionary['estado'], diccionary['user'], diccionary['ip'])
            # user = user.get_dict()
            self.respond(response=None, success=True, message='Actualizacion de estado correctamente.')

        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()

    def sincronizar_residente(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))

            data['dict_residente']['codigo'] = data['dict_usuario']['fkresidente']
            data['dict_residente']['codigoqr'] = data['dict_usuario']['codigoqr_residente']

            for vehiculos in data['dict_residente']['vehiculos']:

                marca = MarcaManager(self.db).obtener_o_crear(vehiculos['nombre_marca'])
                vehiculos['fkmarca'] = marca.id

                modelo = ModeloManager(self.db).obtener_o_crear(vehiculos['nombre_modelo'],vehiculos['fkmarca'])

                vehiculos['fkmodelo'] = modelo.id if modelo else modelo


                tarjeta = NropaseManager(self.db).obtener_x_tarjeta(vehiculos['tarjeta'])

                vehiculos['fknropase'] = tarjeta.id if tarjeta else tarjeta


            for domicilios in data['dict_residente']['domicilios']:
                domi = DomicilioManager(self.db).obtener_x_codigo(domicilios['codigo_domicilio'])
                domicilios['fkdomicilio'] = domi.id


            nro = NropaseManager(self.db).obtener_x_tarjeta(data['dict_usuario']['tarjeta_residente'])

            data['dict_residente']['fknropase'] = nro.id if nro else nro


            dict_usuario = ResidenteManager(self.db).insert(data['dict_residente'])
            data['dict_usuario']['fkresidente'] = dict_usuario['fkresidente']
            print("diccionario: " + str(data))

            UsuarioManager(self.db).insert_residente(data['dict_usuario'])


            self.respond(response=None, success=True, message='Insertado correctamente.')
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

    def sincronizar_movimiento(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            print("sincronizar movimiento")

            u = UsuarioManager(self.db).obtener_x_codigo(data['user'])

            data['user'] = u.id


            data['fkvehiculo'] =  ""
            data['fkinvitado'] = ""


            print("nombre_marca: "+str(data['nombre_marca']))

            marca = MarcaManager(self.db).obtener_o_crear(data['nombre_marca'])
            print("marca: " + str(marca))

            data['fkmarca'] = marca.id

            if data['codigoautorizacion'] != "":

                print("codigoautorizacion: " + str(data['codigoautorizacion']))
                invitacion = InvitacionManager(self.db).obtener_x_codigo(data['codigoautorizacion'])
                print("invitacion: " + str(invitacion))
                if invitacion:

                    data['fkinvitacion'] = invitacion.id
                else:
                    data['fkinvitacion'] = invitacion

            print("tarjeta: " + str(data['tarjeta']))
            tarjeta = NropaseManager(self.db).obtener_x_tarjeta(data['tarjeta'])
            print("tarjeta: " + str(tarjeta))

            if tarjeta:

                data['fknropase'] = tarjeta.id
            else:
                data['fknropase'] = tarjeta


            if data['nombre_modelo'] != "":

                print("modelo: " + str(data['nombre_modelo']))
                modelo = ModeloManager(self.db).obtener_o_crear(data['nombre_modelo'], data['fkmarca'])
                print("modelo: " + str(modelo))
                data['fkmodelo'] = modelo.id if modelo else modelo
            else:
                data['fkmodelo'] = None


            if data['fkresidente'] != "":
                resi = ResidenteManager(self.db).obtener_x_codigo(data['fkresidente'])
                print("resi: " + str(resi))
                data['fkresidente'] = resi.id


            if data['fkdomicilio'] != "":
                domi = DomicilioManager(self.db).obtener_x_codigo(data['codigo_destino'])
                print("domi: " + str(domi))
                data['fkdomicilio'] = domi.id

            elif data['fkareasocial'] != "":
                domi = AreasocialManager(self.db).obtener_x_codigo(data['codigo_destino'])
                print("area: " + str(domi))
                data['fkareasocial'] = domi.id


            if data['codigoautorizacion'] != "":
                invi = InvitacionManager(self.db).obtener_x_codigoqr(data['codigoautorizacion'])
                print("invi: " + str(invi))
                data['fkinvitacion'] = invi.id


            MovimientoManager(self.db).insert(data)
            self.respond(response=None, success=True, message='Insertado correctamente.')
        except Exception as e:
            print(e)
            self.respond(response=str(e), success=False, message=str(e))
        self.db.close()


    def sincronizar_movimiento_salida(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            usuario = UsuarioManager(self.db).obtener_x_codigo(data['user'])

            print(str(data))
            print(str(usuario))

            mov = MovimientoManager(self.db).obtener_x_codigo(data['idmovimiento'])

            if mov:

                print("mov: " +str(mov.id))
                print("usuario: " +str(usuario.id))

                MovimientoManager(self.db).salida_sincronizada(mov.id, data['fechaf'], usuario.id, data['ip'])
                self.respond(response=None, success=True, message='Salida movimiento.')
            else:
                self.respond(response=None, success=True, message='No Sincronizo Salida movimiento.')

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

    # Funciones de Usuario
    def verificar_usuario(self, data):
        with transaction() as session:
            try:
                resp_user = UsuarioManager(session).verificar_x_codigo(data['user'])

                if resp_user['respuesta']:

                    try:

                        resp_version = VersionMovilManager(session).verificar_version_actual(data['version'])

                        if resp_version['respuesta']:

                            try:

                                resp_token = UsuarioManager(session).verificar_x_token(data['token'])

                                if resp_token['respuesta']:

                                    return dict(success=True, response="", message="Usuario Correcto")


                                else:
                                    return dict(success=False, response="token",  message=resp_token['mensaje'])

                            except Exception as e:
                                print(e)
                                return dict(success=False, response="token",
                                            message="No se esta enviando el token")


                        else:
                            return dict(success=False, response="version", message=resp_version['mensaje'])

                    except Exception as e:
                        print(e)
                        return dict(success=False, response="version", message="No se esta enviando la version")

                else:
                    return dict(success=False, response="user", message=resp_user['mensaje'])


            except Exception as e:
                print(e)
                return dict(success=False, response="user", message="No se esta enviando el usuario")


    # Funciones de Usuario
    def consultar_usuario(self, data):
        with transaction() as session:
            try:
                return UsuarioManager(session).verificar_x_codigo(data['user'])

            except Exception as e:
                print(e)

                return dict(respuesta=True, usuario="No se esta enviando el usuario")

    # Funciones de Version
    def consultar_version(self, data):
        with transaction() as session:

            try:

                return VersionMovilManager(session).verificar_version_actual(data['version'])

            except Exception as e:
                print(e)

                return dict(respuesta=True, version="No se esta enviando la version movil")


    # Funciones de Bitacora
    def insertar_bitacora(self, bitacora):
        with transaction() as session:
            session.add(bitacora)
            session.commit()
    def obtener_usuario(self, Usuario_id):
        with transaction() as session:
            return session.query(Usuario).filter(Usuario.id == Usuario_id).first()
    def fecha_actual(self):
        fechaHora = datetime.now(pytz.timezone('America/La_Paz'))
        principal = self.db.query(Principal).first()

        if principal.estado:
            fecha_str = str(fechaHora)
            fecha_ = fecha_str[0:19]
            fechaHora = datetime.strptime(fecha_, '%Y-%m-%d %H:%M:%S')

            timezone = pytz.timezone('America/La_Paz')
            fechaHora = pytz.utc.localize(fechaHora, is_dst=None).astimezone(timezone)

        return fechaHora