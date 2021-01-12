from .models import *
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ...usuarios.usuario.managers import *
from ..registros.models import *
from ...condominios.nropase.models import *
from ...condominios.evento.models import *
from sqlalchemy.sql import func, extract, cast, text


from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font

# import ctypes
# from ctypes import *
# from ctypes.wintypes import HANDLE,POINT
from sqlalchemy import or_
from sqlalchemy import and_


class DispositivoManager(SuperManager):

    def __init__(self, db):
        super().__init__(Dispositivo, db)

    def verificar_estado(self, x):

        for estado in x['estadoDispositivos']:
            domi = Dispositivo(id=estado['fkdispositivo'],
                               situacion=estado['conexion'])

            self.db.merge(domi)
            print(str(estado['fkdispositivo']) + " " + str(estado['conexion']) )
        self.db.commit()


    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.estado == True))

    def listar_x_condominio(self,idcondominio):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.fkcondominio == idcondominio).all()

    def listar_todo_cant_marcaciones(self,x):

        dispositivos = self.db.query(Dispositivo).join(Condominio)\
            .filter(Dispositivo.fkcondominio == Condominio.id)\
            .filter(Dispositivo.estado == True)\
            .filter(Condominio.ip_publica == "").all()

        resp = []
        resp_config = []

        for dispo in dispositivos:

            config = self.db.query(Configuraciondispositivo) \
                .filter(Configuraciondispositivo.fkdispositivo == dispo.id) \
                .filter(Configuraciondispositivo.estado == True) \
                .order_by(Configuraciondispositivo.id.asc()).all()

            dispo.configuraciondispositivo = config

            for disconfig in dispo.configuraciondispositivo:
                disconfig = disconfig.get_dict()
                resp_config.append(disconfig)

            marcaciones = self.db.query(func.count(RegistrosControlador.id)).filter(RegistrosControlador.fkdispositivo == dispo.id)

            cantidad = marcaciones[0][0]
            resp.append(dict(id=dispo.id,ip=dispo.ip,puerto=dispo.puerto,estado=dispo.estado,tipo=dispo.fktipodispositivo,cant_marcaciones=cantidad,accesos=resp_config))

        return resp

    def listar_locales_cant_marcaciones(self, x):

        dispositivos = self.db.query(Dispositivo).filter(Dispositivo.estado == True).all()

        resp = []
        resp_config = []

        for dispo in dispositivos:

            config = self.db.query(Configuraciondispositivo) \
                .filter(Configuraciondispositivo.fkdispositivo == dispo.id) \
                .filter(Configuraciondispositivo.estado == True) \
                .order_by(Configuraciondispositivo.id.asc()).all()

            dispo.configuraciondispositivo = config

            for disconfig in dispo.configuraciondispositivo:
                disconfig = disconfig.get_dict()
                resp_config.append(disconfig)

            marcaciones = self.db.query(func.count(RegistrosControlador.id)).filter(
                RegistrosControlador.fkdispositivo == dispo.id)

            cantidad = marcaciones[0][0]
            resp.append(
                dict(id=dispo.id, ip=dispo.ip, puerto=dispo.puerto, estado=dispo.estado, tipo=dispo.fktipodispositivo,
                     cant_marcaciones=cantidad, accesos=resp_config))

        return resp

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()


    def listar_cerraduras(self):

        lista = list()

        imagen = "/resources/images/dispositivo.PNG"

        for x in  self.db.query(Cerraduras).filter(Cerraduras.estado == True).all():

            if x.dispositivo.situacion:
                imagen = "/resources/images/dispositivo.PNG"
            else:
                imagen ="/resources/images/dispositivo_off.png"

            lista.append(dict(id=x.id,fkdispositivo=x.fkdispositivo,dispositivo=x.dispositivo.descripcion,nro=x.numero,cerradura=x.nombre,imagen=imagen))
        return lista

    def listar_x_usuario(self,usuario):

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).all()

        else:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.fkcondominio == usuario.fkcondominio).all()

    def listar_cerraduras_x_usuario(self, usuario):

        if usuario.sigas:
            return self.db.query(Cerraduras).filter(Cerraduras.estado == True).all()

        else:
            return self.db.query(Cerraduras).join(Dispositivo).filter(Cerraduras.estado == True).filter(Dispositivo.fkcondominio == usuario.fkcondominio).all()


    def listar_tipos_dispositivo(self):
        return self.db.query(Tipodispositivo).filter(Tipodispositivo.estado == True).all()

    def insert(self, diccionary):

        objeto = DispositivoManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip_local, accion="Registro Dispositivo.", fecha=fecha,tabla="dispositivo", identificador=a.id)
        super().insert(b)
        return a

    def update(self, diccionary):
        objeto = DispositivoManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip_local, accion="Modifico Dispositivo.", fecha=fecha,tabla="dispositivo", identificador=a.id)
        super().insert(b)
        return a

    def delete(self, id,estado, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.estado = estado
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Eliminó Dispositivo.", fecha=fecha, tabla="dispositivo", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return x


    def sdk(self):
        print("sdk")
        # zk = windll.LoadLibrary("C:/Windows/system32/plcommpro.dll")
        #
        # zk.Connect.argtypes = [c_char_p]
        # zk.Connect.restype = HANDLE
        #
        # zk.Disconnect.argtypes = [HANDLE]
        # zk.Disconnect.restype = c_void_p
        #
        # zk.DeleteDeviceData.argtypes = [HANDLE,c_char_p,c_char_p,c_char_p]
        #
        # zk.SearchDevice.argtypes = [c_char_p,c_char_p,c_char_p]
        # zk.SearchDevice.restype = c_int
        #
        # zk.GetDeviceParam.argtypes = [HANDLE,c_char_p,c_int,c_char_p]
        # zk.GetDeviceParam.restype = c_char_p
        #
        # zk.GetDeviceData.argtypes = [HANDLE,c_char_p,c_int,c_char_p,c_char_p,c_char_p,c_char_p]
        # zk.GetDeviceData.restype = c_char_p
        #
        # zk.GetDeviceDataCount.argtypes = [HANDLE,c_char_p,c_char_p,c_char_p]
        # zk.GetDeviceDataCount.restype = c_int
        #
        # zk.PullLastError.restype = ctypes.c_int
        #
        # zk.GetRTLog.argtypes = [HANDLE,c_char_p,c_int]
        # zk.GetRTLog.restype = c_int
        #
        # params = b"protocol=TCP,ipaddress=192.168.1.201,port=4370,timeout=2000,passwd="
        # params_buf = c_char_p(params)
        #
        # handler = zk.Connect(params_buf)
        # if handler:
        #
        #     string = "Id dispositivo: {0}\n".format(handler)
        #     print(string)
        #
        #     try:
        #
        #         # buffer = create_string_buffer(2048)
        #         # items = (b"DeviceID,Door1SensorType,Door1Drivertime,Door1Intertime")
        #         # p_items = create_string_buffer(items)
        #         # ret = zk.GetDeviceParam(handler, buffer, 256, p_items)
        #
        #
        #         # table = b"transaction"
        #         # query_table = create_string_buffer(table)
        #         #
        #         # data = (b"Cardno,Pin,Verified,DoorID,EventType,InOutState,Time_second")
        #         # query_data = create_string_buffer(data)
        #         #
        #         # options = b""
        #         # query_options = create_string_buffer(options)
        #         #
        #         # ret = zk.DeleteDeviceData(handler, query_table, query_data, query_options)
        #
        #         table = b"transaction"  # Download the user data from the user table
        #         fielname =b"*"  # Download all field information in the table
        #         pfilter = b""# Have no filtering conditions and thus vvvvdownload all information
        #         options = b""
        #         query_buf = create_string_buffer(10 * 1024 * 1024)
        #         query_table = create_string_buffer(table)
        #         query_fieldname = create_string_buffer(fielname)
        #         query_filter = create_string_buffer(pfilter)
        #         query_options = create_string_buffer(options)
        #         try:
        #          # ret = zk.GetDeviceData(handler,query_buf ,10 * 1024 * 1024, query_table, query_fieldname,query_filter, query_options)
        #          # ret = zk.GetDeviceDataCount(pointer(handler), query_table, query_filter,query_options)
        #          dev_buf = create_string_buffer(b"", 64 * 1024)
        #          res = zk.SearchDevice(b"UDP", b"255.255.255.255", dev_buf)
        #
        #         except Exception as ett:
        #             print(ett)
        #
        #
        #
        #         # buffer_size = 4096
        #         # buf = ctypes.create_string_buffer(buffer_size)
        #         #
        #         # res = zk.GetRTLog(handler, buf, buffer_size)
        #
        #
        #         if res < 0:
        #             raise RuntimeError('GetRTLog failed, returned: {}'.format(str(res)))
        #
        #         raw = dev_buf.value.decode('utf-8')
        #         *events_s, empty = raw.split('\r\n')
        #
        #         # return (ZKRealtimeEvent(s) for s in events_s)
        #
        #
        #
        #     except Exception as e:
        #         print("error")
        #         print(e)
        #
        #     des = zk.Disconnect(handler)
        #     print(str(des))
        # else:
        #     int = zk.PullLastError()
        #     print(str(int))


# class ZKRealtimeEvent:
#     """
#     Represents one realtime event occured on the device
#     Since the device returns event as string we need to parse it to the structured view. This class does this.
#     """
#     __slots__ = (
#         'time',
#         'pin',
#         'card',
#         'door',
#         'event_type',
#         'entry_exit',
#         'verify_mode'
#     )
#
#     def __init__(self, s=None):
#         """
#         :param s: Optional. Event string to be parsed.
#         """
#         if s:
#             self.parse(s)
#
#     def parse(self, s):
#         """
#         Parse one event string and fills out slots
#         :param s: event string
#         :raises ValueError: event string is invalid
#         :return:
#         """
#         if s == '' or s == '\r\n':
#             raise ValueError("Empty event string")
#
#         items = s.split(',')
#         if len(items) != 7:
#             raise ValueError("Event string has not 7 comma-separated parts")
#
#         items[0] = datetime.strptime(items[0], '%Y-%m-%d %H:%M:%S')
#         for i in range(len(self.__slots__)):
#             setattr(self, self.__slots__[i], items[i])
#
#


class ConfiguraciondispositivoManager(SuperManager):
    def __init__(self, db):
        super().__init__(Configuraciondispositivo, db)

    def listar_todo(self,x):

        dispos = self.db.query(Dispositivo).join(Configuraciondispositivo)\
                .filter(Dispositivo.estado == True) \
                .filter(Configuraciondispositivo.estado == True) \
                .filter(Configuraciondispositivo.situacion != "Abrir").all()

        for dis in dispos:
            config = self.db.query(Configuraciondispositivo) \
                .filter(Configuraciondispositivo.fkdispositivo == dis.id) \
                .filter(Configuraciondispositivo.estado == True).order_by(Configuraciondispositivo.id.asc()).all()

            dis.configuraciondispositivo = config

        return dispos

    def insert_configuracion_inicial(self, diccionary):
        codigo = "1,2359,0,0,2359,0,0,2359,0,0,2359,0,0,2359,0,0,2359,0,0,2359,0,0,2359,0,0,2359,0,0,2359,0,0"
        config = dict(codigo=codigo, tarjeta="", situacion="Configuracion_Inicial", fkdispositivo=diccionary['id'])

        objeto = ConfiguraciondispositivoManager(self.db).entity(**config)
        super().insert(objeto)

    def insert_sincronizacion(self, diccionary):
        x = self.db.query(Nropase).filter(Nropase.id == diccionary['id']).first()
        fkcondominio = x.condominios[0].fkcondominio

        sincro = dict(codigo=x.id, tarjeta=x.tarjeta, situacion="Acceso", fkdispositivo=diccionary['id'], fkcondominio=fkcondominio)

        ConfiguraciondispositivoManager(self.db).funcion_configuracion_dispositivo(sincro)


    def insert_acceso_Tarjetas(self, diccionary):
        x = self.db.query(Nropase).filter(Nropase.id == diccionary['id']).first()

        fkcondominio = x.condominios[0].fkcondominio

        sincro = dict(codigo=x.id, tarjeta=x.tarjeta, situacion="Acceso", fkdispositivo=diccionary['id'], fkcondominio=fkcondominio)

        ConfiguraciondispositivoManager(self.db).funcion_configuracion_dispositivo(sincro)


    def insert_qr_residente(self, diccionary):
        diccionary['codigo'] = str(diccionary['codigo'])

        ConfiguraciondispositivoManager(self.db).funcion_configuracion_dispositivo(diccionary)


    def insert_qr_invitacion(self, diccionary):
        invitacion = self.db.query(Invitacion).filter(Invitacion.codigoautorizacion == str(diccionary['tarjeta'])).first()

        fkcondominio = None
        if invitacion.evento.fkdomicilio:
            fkcondominio = invitacion.evento.domicilio.fkcondominio
        elif invitacion.evento.fkareasocial:
            fkcondominio = invitacion.evento.areasocial.fkcondominio

        diccionary['fkcondominio']  =  fkcondominio

        ConfiguraciondispositivoManager(self.db).funcion_configuracion_dispositivo(diccionary)



    def denegar_qr_invitacion(self, diccionary):
        invitacion = self.db.query(Invitacion).filter(Invitacion.codigoautorizacion == diccionary['tarjeta']).first()

        fkcondominio = None
        if invitacion.evento.fkdomicilio:
            fkcondominio = invitacion.evento.domicilio.fkcondominio
        elif invitacion.evento.fkareasocial:
            fkcondominio = invitacion.evento.areasocial.fkcondominio

        diccionary['fkcondominio'] = fkcondominio

        ConfiguraciondispositivoManager(self.db).funcion_configuracion_dispositivo(diccionary)


    def funcion_configuracion_dispositivo(self,diccionary):

        dispositivos = DispositivoManager(self.db).listar_x_condominio(diccionary['fkcondominio'])

        for dis in dispositivos:
            diccionary['fkdispositivo'] = dis.id

            if dis.fktipodispositivo == 4:
                diccionary['tarjeta'] = diccionary['residente']

            objeto = ConfiguraciondispositivoManager(self.db).entity(**diccionary)
            super().insert(objeto)


    def obtener_codigo_acceso(self, list_cerraduras):
        codigo_acceso = 0
        try:

            if list_cerraduras[0]['estado']:
                codigo_acceso = 1

            if list_cerraduras[1]['estado']:
                if codigo_acceso ==0:
                    codigo_acceso = 2
                else:
                    codigo_acceso = 3

            if list_cerraduras[2]['estado']:

                if codigo_acceso ==0:
                    codigo_acceso = 4
                elif codigo_acceso == 1:
                    codigo_acceso = 5
                elif codigo_acceso == 2:
                    codigo_acceso = 6
                elif codigo_acceso == 3:
                    codigo_acceso = 7

            if list_cerraduras[3]['estado']:

                if codigo_acceso ==0:
                    codigo_acceso = 8
                elif codigo_acceso == 1:
                    codigo_acceso = 9
                elif codigo_acceso == 2:
                    codigo_acceso = 10
                elif codigo_acceso == 3:
                    codigo_acceso = 11
                elif codigo_acceso == 4:
                    codigo_acceso = 12
                elif codigo_acceso == 5:
                    codigo_acceso = 13
                elif codigo_acceso == 6:
                    codigo_acceso = 14
                elif codigo_acceso == 7:
                    codigo_acceso = 15


        except Exception as ex:
            print("Dispositivo solo tiene dos Cerraduras")


        return  codigo_acceso

    def actualizar_codigos(self,codigos):

        for cod in codigos:

            respuesta = self.db.query(self.entity).filter(self.entity.id == cod).first()

            if respuesta:
                respuesta.estado = False
                self.db.merge(respuesta)

        self.db.commit()
        self.db.close()


    def abrir_cerradura(self, diccionary):

        sincro = dict(codigo=diccionary['cerradura'], tarjeta="", situacion="Abrir", fkdispositivo=diccionary['id'])

        objeto = ConfiguraciondispositivoManager(self.db).entity(**sincro)
        super().insert(objeto)

        fecha = BitacoraManager(self.db).fecha_actual()

        b = Bitacora(fkusuario=diccionary['user'], ip=diccionary['ip_local'], accion="Abrió cerradura Nº"+str(diccionary['cerradura']), fecha=fecha, tabla="dispositivo")
        super().insert(b)



class DispositivoeventosManager(SuperManager):

    def __init__(self, db):
        super().__init__(Dispositivoeventos, db)

    def obtener_x_codigo(self, codigo):
        return self.db.query(self.entity).filter(self.entity.codigo == codigo).first()






