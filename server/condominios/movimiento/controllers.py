from .managers import *
from server.common.controllers import CrudController
from ..invitado.managers import *
from ..condominio.managers import *
from ..residente.managers import *
from ..domicilio.managers import *
from ..vehiculo.managers import *
from ..marca.managers import *
from ..modelo.managers import *
from ..areasocial.managers import *
from ..nropase.managers import *
from threading import Thread

import os.path
import uuid
import json

global urlServidor
urlServidor = 'http://sigas-web.herokuapp.com/api/v1/'

class MovimientoController(CrudController):

    manager = MovimientoManager
    html_index = "condominios/movimiento/views/index.html"
    html_table = "condominios/movimiento/views/table.html"
    routes = {
        '/movimiento': {'GET': 'index', 'POST': 'table'},
        '/movimiento_insert': {'POST': 'insert'},
        '/movimiento_update': {'PUT': 'edit', 'POST': 'update'},
        '/movimiento_delete': {'POST': 'delete'},
        '/movimiento_importar': {'POST': 'importar'},
        '/movimiento_salida': {'POST': 'salida'},
        '/movimiento_reporte_xls': {'POST': 'imprimirxls'},
        '/movimiento_actualizar': {'POST': 'actualizar'},
        '/movimiento_actualizar_tabla': {'POST': 'actualizar_tabla'},
        '/movimiento_filtrar': {'POST': 'filtrar'},
        '/movimiento_recargar': {'POST': 'recargar'}
    }

    def get_extra_data(self):
        aux = super().get_extra_data()
        us = self.get_user()
        objeto = []

        aux['objeto'] = objeto
        aux['tipodocumento'] = TipodocumentoManager(self.db).listar_todo()
        aux['residentes'] = ResidenteManager(self.db).listar_residentes(us)

        aux['areasociales'] = AreasocialManager(self.db).listar_todo(us)
        aux['tipopases'] = TipopaseManager(self.db).listar_todo()
        aux['autorizaciones'] = AutorizacionManager(self.db).listar_todo()
        aux['tipovehiculos'] = TipovehiculoManager(self.db).listar_todo()
        aux['colores'] = ColorManager(self.db).listar_todo()
        aux['marcas'] = MarcaManager(self.db).listar_todo()
        aux['modelos'] = ModeloManager(self.db).listar_todo()
        aux['idperfil'] = us.fkrol
        aux['nropases'] = NropaseManager(self.db).listar_numero_pases(us)

        aux['domicilios'] = DomicilioManager(self.db).listar_domicilios(us)
        aux['movimientos_vehicular'] = MovimientoManager(self.db).listar_movimiento_dia(us)

        return aux

    def delete(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))
        id = diccionary['id']
        user = self.get_user_id()
        ip = self.request.remote_ip
        MovimientoManager(self.db).delete(id, user, ip)
        self.respond(success=True, message='Baja Realizada Correctamente.')


    def insert(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        data['user'] = self.get_user_id()
        data['ip'] = self.request.remote_ip
        data['fechar'] = ""
        print("ingreso Vehicular web nombre: " + str(data['nombre']))
        mov = MovimientoManager(self.db).insert(data)

        if mov:
            t = Thread(target=self.hilo_sincronizar, args=(mov, data,))
            t.start()

        self.respond(success=True, message='Insertado correctamente.')

    def hilo_sincronizar(self, mov, data):
        print("hilo sincronizar")

        principal = self.db.query(Principal).first()
        if principal.estado:
            destino = MovimientoManager(self.db).obtener_destino(mov.id)
            if destino.condominio.ip_publica != "":

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

                url = "http://" + destino.condominio.ip_publica + ":" + destino.condominio.puerto + "/api/v1/sincronizar_movimiento"

                headers = {'Content-Type': 'application/json'}

                cadena = json.dumps(data)
                body = cadena
                resp = requests.post(url, data=body, headers=headers, verify=False)
                response = json.loads(resp.text)

                print(response)

        else:
            data['fechar'] = mov.fechar.strftime('%d/%m/%Y %H:%M:%S')

            if mov.fkinvitacion and mov.invitacion.evento.paselibre:
                print("registro con pase libre")
                data['nombre_marca'] = ""
                data['nombre_modelo'] = ""

            else:

                data['nombre_marca'] = mov.vehiculo.marca.nombre if mov.vehiculo.fkmarca else ""
                data['nombre_modelo'] = mov.vehiculo.modelo.nombre if mov.vehiculo.fkmodelo else ""


            print(data['nombre_marca'])
            print(data['nombre_modelo'])

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


            if mov.fkresidente:
                residente = ResidenteManager(self.db).obtener_x_id(mov.fkresidente)
                data['fkresidente'] = residente.codigo
            else:

                data['fkresidente'] = None

            data['fkinvitado'] = ""
            data['fkconductor'] = ""



            try:
                url = urlServidor+"sincronizar_movimiento"

                headers = {'Content-Type': 'application/json'}

                u = UsuarioManager(self.db).obtener_x_codigo(data['user'])
                data['user'] = u.id

                cadena = json.dumps(data)
                body = cadena
                resp = requests.post(url, data=body, headers=headers, verify=False)
                response = json.loads(resp.text)

                print(response)
                MovimientoManager(self.db).asignar_codigo(mov.id, response['response'])

            except Exception as e:
                print(e)

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
        fechainicio = diccionary['fechainicio']
        fechafin = diccionary['fechafin']
        cname = self.manager(self.db).movimiento_excel(fechainicio, fechafin)
        self.respond({'nombre': cname, 'url': 'resources/downloads/' + cname}, True)
        self.db.close()

    def salida(self):
        self.set_session()
        diccionary = json.loads(self.get_argument("object"))

        fechainicio = diccionary['fechai']
        fechafin = diccionary['fechaf']

        resp = MovimientoManager(self.db).salida(diccionary['id'], self.get_user_id(), self.request.remote_ip)

        t = Thread(target=self.hilo_sincronizar_salida, args=(diccionary,resp,))
        t.start()

        lista_dict =  MovimientoManager(self.db).filtrar(fechainicio, fechafin,self.get_user_id())

        print("respuesta filtro")

        self.respond(response=lista_dict, success=True,
                     message='actualizado correctamente.')

    def hilo_sincronizar_salida(self, diccionary,respMov):
        print("hilo_sincronizar_salida")

        principal = self.db.query(Principal).first()
        if principal.estado:
            diccionary['user'] = self.get_user_id()
            diccionary['ip'] = self.request.remote_ip
            diccionary['idmovimiento'] = diccionary['id']
            destino = MovimientoManager(self.db).obtener_destino(diccionary['id'])

            if destino:
                condominio = CondominioManager(self.db).obtener_x_id(destino.fkcondominio)

            else:
                condominio = None

            diccionary['fechaf'] = respMov.fechaf.strftime('%d/%m/%Y %H:%M:%S')

            if condominio.ip_publica != "":
                url = "http://" + condominio.ip_publica + ":" + condominio.puerto + "/api/v1/sincronizar_movimiento_salida"

                headers = {'Content-Type': 'application/json'}

                cadena = json.dumps(diccionary)
                body = cadena
                resp = requests.post(url, data=body, headers=headers, verify=False)
                response = json.loads(resp.text)

                print(response)

        else:
            diccionary['user'] = self.get_user_id()
            diccionary['ip'] = self.request.remote_ip
            diccionary['idmovimiento'] = respMov.codigo
            # destino = MovimientoManager(self.db).obtener_destino(diccionary['id'])
            #
            # if destino:
            #     condominio = CondominioManager(self.db).obtener_x_id(destino.fkcondominio)
            #
            # else:
            #     condominio = None

            diccionary['fechaf'] = respMov.fechaf.strftime('%d/%m/%Y %H:%M:%S')

            try:

                url = urlServidor+"sincronizar_movimiento_salida_nube"

                headers = {'Content-Type': 'application/json'}

                cadena = json.dumps(diccionary)
                body = cadena
                print("body: "+str(body))
                resp = requests.post(url, data=body, headers=headers, verify=False)
                response = json.loads(resp.text)

                print(response)
            except Exception as e:
                print(e)

    def actualizar_tabla(self):
        self.set_session()
        arraT = MovimientoManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = MovimientoManager(self.db).listar_todo()

        self.respond(response=[objeto.get_dict() for objeto in arraT['datos']], success=True,
                     message='actualizado correctamente.')

    def filtrar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))

        ins_manager = self.manager(self.db)
        user = self.get_user_id()

        if data['fresidente'] != '':
            lista_ = ins_manager.filtrar_residente(datetime.strptime(data['fechainicio'], '%d/%m/%Y'),
                                         datetime.strptime(data['fechafin'], '%d/%m/%Y'),
                                         data['fresidente'])
            self.respond(response=lista_, success=True,
                         message='actualizado correctamente.')

        else:

            if data['fdomicilio'] != '':
                lista_ = ins_manager.filtrar_domicilio(datetime.strptime(data['fechainicio'], '%d/%m/%Y'),
                                                       datetime.strptime(data['fechafin'], '%d/%m/%Y'),
                                                       data['fdomicilio'])
                self.respond(response=lista_, success=True,
                             message='actualizado correctamente.')
            else:

                if data['fdomicilio'] == '' or data['fresidente'] == '':

                    lista_ = ins_manager.filtrar(datetime.strptime(data['fechainicio'], '%d/%m/%Y'),
                                             datetime.strptime(data['fechafin'], '%d/%m/%Y'),user)

                    self.respond(response=lista_, success=True,
                                message='actualizado correctamente.')





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
            mee = self.manager(self.db).importar_excel(cname, self.get_user_id(), self.request.remote_ip)
            self.respond(message=mee['message'], success=mee['success'])
        else:
            self.respond(message='Formato de Archivo no aceptado¡¡', success=False)
        self.db.close()

    def recargar(self):
        self.set_session()
        data = json.loads(self.get_argument("object"))
        us = self.get_user()
        ins_manager = self.manager(self.db)
        fechainicio = datetime.strptime(data['fechainicio'], '%d/%m/%Y')
        fechafin = datetime.strptime(data['fechafin'], '%d/%m/%Y')
        ult_registro = data['ult_registro']
        arraT = MovimientoManager(self.db).get_page(1, 10, None, None, True)
        arraT['datos'] = ins_manager.recargar(fechainicio, fechafin, us, ult_registro)
        if len(ins_manager.errors) == 0:
            self.respond([objeto.get_dict() for objeto in arraT['datos']], message='Operacion exitosa!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al insertar')
        self.db.close()