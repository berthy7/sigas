from .models import *
from ..invitado.managers import *
from ..residente.managers import *
from ..evento.managers import *
from ..nropase.managers import *
from ..movimiento.models import *
from ..areasocial.models import *
from sqlalchemy import or_
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font

from onesignal_sdk.client import Client
from onesignal_sdk.error import OneSignalHTTPError


class Movimiento_pManager(SuperManager):
    def __init__(self, db):
        super().__init__(Movimiento, db)


    def reporte_movimientos_peatonal(self,diccionario):

        diccionario['fechainicio'] = datetime.strptime(diccionario['fechainicio'], '%d/%m/%Y')
        diccionario['fechafin'] = datetime.strptime(diccionario['fechafin'], '%d/%m/%Y')

        domicilio = self.db.query(self.entity).join(Domicilio).filter(
            Domicilio.fkcondominio == diccionario['fkcondominio']).filter(
            func.date(self.entity.fechar).between(diccionario['fechainicio'], diccionario['fechafin'])).filter(
                self.entity.tipo == "Peatonal").filter(self.entity.estado == True).all()

        areasocial = self.db.query(self.entity).join(Areasocial).filter(
            Areasocial.fkcondominio == diccionario['fkcondominio']).filter(
            func.date(self.entity.fechar).between(diccionario['fechainicio'], diccionario['fechafin'])).filter(
                self.entity.tipo == "Peatonal").filter(self.entity.estado == True).all()

        for area in areasocial:
            domicilio.append(area)

        return domicilio

    def get_all(self):
        return self.db.query(self.entity)

    def get_all_by_lastname(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.apellidopaterno.asc()).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.tipo == "Peatonal"))

    def list_all_reporte(self):
        return self.db.query(self.entity).filter(self.entity.tipo == "Peatonal").all()

    def listar_movimiento_dia(self, usuario):

        fecha = datetime.now(pytz.timezone('America/La_Paz'))
        fechahoy = str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year)
        fechahoy = datetime.strptime(fechahoy, '%d/%m/%Y')

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.fechar.cast(Date) == fechahoy).filter(
                self.entity.tipo == "Peatonal").all()
        else:

            domicilio = self.db.query(self.entity).filter(self.entity.estado == True).join(Domicilio).filter(Domicilio.fkcondominio== usuario.fkcondominio).filter(self.entity.fechar.cast(Date) == fechahoy).filter(
                self.entity.tipo == "Peatonal").all()

            areasocial = self.db.query(self.entity).filter(self.entity.estado == True).join(Areasocial).filter(Areasocial.fkcondominio== usuario.fkcondominio).filter(self.entity.fechar.cast(Date) == fechahoy).filter(
                self.entity.tipo == "Peatonal").all()

            for area in areasocial:
                domicilio.append(area)

            return domicilio

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def insert(self, diccionary):

        if diccionary['fkinvitacion'] == "":
            diccionary['fkinvitacion'] = None

        accesos_invitacion = InvitacionManager(self.db).obtener_accesos_evento(diccionary['fkinvitacion'])


        if accesos_invitacion['paselibre']:
            diccionary['fkvehiculo'] = None
            diccionary['fkconductor'] = None
            diccionary['fkinvitado'] = None
        else:
            if diccionary['visita']:
                if diccionary['fkinvitado'] == "" or diccionary['fkinvitado'] == "0":
                    if diccionary['ci'] != "":
                        invitado = InvitadoManager(self.db).registrar_invitado(diccionary)
                        diccionary['fkinvitado'] = invitado.id
                    else:
                        diccionary['fkinvitado'] = None
                else:
                    invitado = InvitadoManager(self.db).actualizar_invitado(diccionary)
            else:
                diccionary['fkinvitado'] = None


       # if diccionary['fktipodocumento_conductor'] == "":
        #    diccionary['fktipodocumento_conductor'] = None


        if diccionary['fkdomicilio'] == "":
            diccionary['fkdomicilio'] = None

        if diccionary['fkareasocial'] == "":
            diccionary['fkareasocial'] = None

        if diccionary['fknropase'] == "":
            diccionary['fknropase'] = None

        fecha = BitacoraManager(self.db).fecha_actual()

        diccionary['tipo'] = "Peatonal"
        diccionary['fechar'] = fecha

        try:
            if diccionary['fkresidente'] == "":
                diccionary['fkresidente'] = None

        except Exception as e:
            print("no se envio fkresidente")

            diccionary['fkresidente'] = None


        # diccionary['fechai'] = fecha

        objeto = Movimiento_pManager(self.db).entity(**diccionary)

        a = super().insert(objeto)
        print("registro ingreso Peatonal: " + str(a.id))
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Movimiento_p.", fecha=fecha,tabla="movimiento", identificador=a.id)
        super().insert(b)
        a.codigo = a.id
        self.db.merge(a)

        if a.fknropase:
            # actualizar siuacion
            NropaseManager(self.db).situacion(a.fknropase, "Ocupado")

        # deshabilitar invitacion
        if a.fkinvitacion:
            accesos_invitacion = InvitacionManager(self.db).obtener_accesos_evento(a.fkinvitacion)

            if accesos_invitacion['multiacceso'] is False:
                if accesos_invitacion['multiple'] is False:
                    if accesos_invitacion['paselibre'] is False:

                        InvitacionManager(self.db).delete(a.fkinvitacion, False, objeto.user, objeto.ip)


            usuario = UsuarioManager(self.db).obtener_x_fkresidente(a.invitacion.evento.fkresidente)
            notificacion = NotificacionManager(self.db).insert(dict(fkremitente=1,fkreceptor=usuario.id,mensaje="llego su visita",
            titulo="Notificacion de llegada",fecha =fecha,user =objeto.user,ip=objeto.ip))

            Movimiento_pManager(self.db).enviar_notificacion_onesignal(notificacion)


        return a

    def enviar_notificacion_onesignal(self, notificacion):
        # print("Enviando Notificacion a un solo cliente")

        try:
            # Parametros
            APP_ID = 'd99d9fe9-1f01-4b4a-a929-069a9813788c'
            REST_API_KEY = 'MWI1Y2Y2MWEtZGY1OC00MjI1LTk0NTctNTQ5ZjI4NzViNWRk'
            CHANNEL_ID = '4d4c7bc7-0221-4e6a-bedb-0093499f9424'  # DE LA CATEGORIA PRIORITARY
            cli = notificacion.receptor.token_notificacion
            if cli and cli != 'undefined' and cli != '0':
                print('Token..:')
                print(cli)

                client = Client(app_id=APP_ID, rest_api_key=REST_API_KEY)
                img = ''
                notification_body = {
                    'contents': {'en': notificacion.mensaje, 'es': notificacion.mensaje},
                    # 'subtitle': {'en': n.subtitle, 'es': n.subtitle}, // Si se quiere agregar un subtitulo
                    'headings': {'en': notificacion.titulo, 'es': notificacion.titulo},
                    # 'included_segments': ['Active Users', 'Inactive Users'], // cuando se especifica el include_player_ids, los segmentos ya no se envian
                    'include_player_ids': [cli],
                    'big_picture': img,  # Foto cuando la notificacion se expande
                    'small_icon': 'icon',  # Icono de la notificacion
                    # 'android_accent_color': '0065ab',# Color de fondo del small_icon
                    # 'huawei_accent_color': '0065ab',# Color de fondo del small_icon
                    'huawei_small_icon': 'icon',
                    'large_icon': img,  # Foto con la notificacion sin expandirse
                    'huawei_large_icon': img,  # Foto con la notificacion sin expandirse
                    'android_channel_id': CHANNEL_ID,  # Categoria de la notificacion definida en OneSignal
                    'huawei_channel_id': CHANNEL_ID,  # Categoria de la notificacion definida en OneSignal
                    'android_background_layout': '{"headings_color": "FFFF0000", "contents_color": "FF00FF00"}'
                }
                print('Cuerpo de la Notificacion..')
                print('..')
                print('..')
                print(notification_body)
                print('..')
                print('..')
                response = client.send_notification(notification_body)
                # print('Notificacion enviada: ')
                # print(response)
                # self.deshabilitar_notificacion(n)
        except OneSignalHTTPError as e:
            print("Error al enviar la notificacion: " + str(notificacion.id) + ' ' + str(notificacion.titulo))
            print(e)
            print(e.message)

    def update(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()
        objeto.fechanacimiento = datetime.strptime(objeto.fechanacimiento, '%d/%m/%Y')

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Movimiento_p.", fecha=fecha,tabla="residente", identificador=a.id)
        super().insert(b)
        return a



    def salida(self, id, user, ip):
        x = self.db.query(Movimiento).filter(Movimiento.id == id).first()
        fecha = BitacoraManager(self.db).fecha_actual()
        x.fechaf = fecha


        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Registro Salida", fecha=fecha, tabla="movimiento", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        if x.fknropase:
            # actualizar siuacion
            NropaseManager(self.db).situacion(x.fknropase, "Libre")

        return x

    def filtrar(self, fechainicio, fechafin,usuario):
        usuario = UsuarioManager(self.db).get_by_pass(usuario)

        list = {}
        c = 0

        fecha = fecha_zona
        fechahoy = str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)
        fechahoy = datetime.strptime(fechahoy, '%d/%m/%Y')


        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Peatonal").all()
        else:
            domicilio = self.db.query(self.entity).filter(self.entity.estado == True).join(Domicilio).filter(Domicilio.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Peatonal").all()

            areasocial = self.db.query(self.entity).filter(self.entity.estado == True).join(Areasocial).filter(Areasocial.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Peatonal").all()

            for area in areasocial:
                domicilio.append(area)

            return domicilio

    def actualizar_movimiento(self, marcacion):

        mov = self.db.query(Movimiento).join(Nropase).filter(Movimiento.estado == True).filter(Nropase.tarjeta == marcacion.tarjeta).filter(
                or_(Movimiento.fechai == None,Movimiento.fechaf == None)).first()
        if mov:
            if not mov.fechai:
                mov.fechai = marcacion.time

                self.db.merge(mov)
                self.db.commit()
            elif not mov.fechaf:
                mov.fechaf = marcacion.time
                self.db.merge(mov)

                nropase = self.db.query(Nropase).filter(Nropase.id == mov.fknropase).first()
                nropase.situacion = "Libre"
                self.db.merge(nropase)
                self.db.commit()

        marcacion.sincronizado =True

        return marcacion


    def recargar(self, fechainicio, fechafin, usuario, ult_registro):
        list = {}
        c = 0

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(
                self.entity.id > ult_registro).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Peatonal").order_by(self.entity.id.desc()).all()
        else:
            domicilio = self.db.query(self.entity).join(Domicilio).filter(self.entity.id > ult_registro).filter(
                Domicilio.fkcondominio == usuario.fkcondominio).filter(
                func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Peatonal").filter(self.entity.estado == True).order_by(self.entity.id.desc()).all()

            areasocial = self.db.query(self.entity).join(Areasocial).filter(self.entity.id > ult_registro).filter(
                Areasocial.fkcondominio == usuario.fkcondominio).filter(
                func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Peatonal").filter(self.entity.estado == True).order_by(self.entity.id.desc()).all()

            for area in areasocial:
                domicilio.append(area)

            return domicilio