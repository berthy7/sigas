from .models import *
from ..invitado.managers import *
from sqlalchemy.exc import IntegrityError
from ..condominio.models import *
from ..domicilio.models import *
from ..residente.models import *
from ...dispositivos.dispositivo.managers import *

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font


class EventoManager(SuperManager):
    def __init__(self, db):
        super().__init__(Evento, db)

    def get_all(self):
        return self.db.query(self.entity)

    def validar_eventos(self):

        fechadate = datetime.now(pytz.timezone('America/La_Paz'))
        fecha_hoy_str = fechadate.strftime('%Y-%m-%d %H:%M:%S')
        fechahoy = fecha_hoy_str[0:10]

        x= self.db.query(Invitacion).join(Evento).filter(Invitacion.estado == True).filter(Evento.fechai <= fechahoy).filter(
            Evento.fechaf >= fechahoy).filter(Evento.situacion != "Acceso").filter(Evento.situacion != "Denegado").all()

        for invi in x:
            respuesta = EventoManager(self.db).validar_invitacion(invi.codigoautorizacion)

            if respuesta:
                diccionary = dict(codigo=invi.id, tarjeta=invi.codigoautorizacion, situacion="Acceso")

                ConfiguraciondispositivoManager(self.db).insert_qr_invitacion(diccionary)

                event = self.db.query(Evento).filter(Evento.id == invi.fkevento).first()

                event.situacion = "Acceso"
                super().update(event)

    def expirar_eventos(self):

        fechadate = datetime.now(pytz.timezone('America/La_Paz'))
        fecha_hoy_str = fechadate.strftime('%Y-%m-%d %H:%M')
        fechahoy = fecha_hoy_str[0:10]
        horahoy = fecha_hoy_str[11:16]

        horahoy = datetime.strptime(horahoy, '%H:%M').time()

        list_evento = self.db.query(Evento).filter(Evento.fechai <= fechahoy).filter(
            Evento.fechaf >= fechahoy).filter(Evento.estado == True).filter(Evento.situacion == "Acceso").all()

        for even in list_evento:
            if even.horaf:
                if even.horaf < horahoy:

                    for invi in even.invitaciones:
                            diccionary = dict(codigo=invi.id, tarjeta=invi.codigoautorizacion, situacion="Denegado")

                            ConfiguraciondispositivoManager(self.db).insert_qr_invitacion(diccionary)

                    even.situacion = "Denegado"
                    super().update(even)

    def expirar_eventos_pasados(self):

        fechadate = datetime.now(pytz.timezone('America/La_Paz'))
        fecha_hoy_str = fechadate.strftime('%Y-%m-%d %H:%M')
        fechahoy = fecha_hoy_str[0:10]


        list_evento_pasados = self.db.query(Evento).filter(
            Evento.fechaf < fechahoy).filter(Evento.estado == True).filter(Evento.situacion == "Acceso").all()

        for even in list_evento_pasados:
            for invi in even.invitaciones:
                    diccionary = dict(codigo=invi.id, tarjeta=invi.codigoautorizacion, situacion="Denegado")

                    ConfiguraciondispositivoManager(self.db).insert_qr_invitacion(diccionary)

            even.situacion = "Denegado"
            super().update(even)

    def list_all(self):
        return dict(objects=self.db.query(self.entity))

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.apellidopaterno.asc()).all()

    def obtener_x_residente(self,idresidente):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.fkresidente == idresidente).all()

    def insert(self, diccionary):

        if diccionary['fkdomicilio'] == "":
            diccionary['fkdomicilio'] = None
        if diccionary['fkareasocial'] == "":
            diccionary['fkareasocial'] = None

        for dicci in diccionary['invitaciones']:
            dicci['user'] = diccionary['user']
            dicci['ip'] = diccionary['ip']
            if dicci['fkinvitado'] == "":

                invitado = InvitadoManager(self.db).registrar_invitado(dicci)
                dicci['fkinvitado'] = invitado.id

        objeto = EventoManager(self.db).entity(**diccionary)

        objeto.fechai = datetime.strptime(objeto.fechai, '%d/%m/%Y')
        objeto.fechaf = datetime.strptime(objeto.fechaf, '%d/%m/%Y')

        if objeto.horai == "":
            objeto.horai = None
        else:
            objeto.horai = datetime.strptime(objeto.horai, '%H:%M').time()

        if objeto.horaf == "":
            objeto.horaf = None
        else:
            objeto.horaf = datetime.strptime(objeto.horaf, '%H:%M').time()
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        print("registro evento: " + str(a.id))

        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Evento.", fecha=fecha,tabla="evento", identificador=a.id)
        super().insert(b)

        for invi in a.invitaciones:

            EventoManager(self.db).generar_codigo_autorizacion(invi)

        return a

    def insertar_invitacion_rapida(self, diccionary):

        lista = list()
        diccionary['fechai'] = diccionary['fecha']
        diccionary['fechaf'] = diccionary['fecha']
        diccionary['horai'] = diccionary['hora']
        diccionary['horaf'] = ""
        diccionary['fktipoevento'] = 6
        diccionary['descripcion'] = "Invitacion rapida"
        lista.append(dict(fkinvitado=diccionary['fkinvitado'],fktipopase=diccionary['fktipopase']))
        diccionary['invitaciones'] = lista

        objeto = EventoManager(self.db).entity(**diccionary)

        objeto.fechai = datetime.strptime(objeto.fechai, '%d/%m/%Y')
        objeto.fechaf = datetime.strptime(objeto.fechaf, '%d/%m/%Y')

        if objeto.horai == "":
            objeto.horai = None
        else:
            objeto.horai = datetime.strptime(objeto.horai, '%H:%M')

        if objeto.horaf == "":
            objeto.horaf = None
        else:
            objeto.horaf = datetime.strptime(objeto.horaf, '%H:%M')
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        print("registro invitacion rapida: " + str(a.id))

        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Invitacion rapida.", fecha=fecha, tabla="evento",
                     identificador=a.id)
        super().insert(b)
        for invi in a.invitaciones:
            EventoManager(self.db).generar_codigo_autorizacion(invi)

        return a

    def update(self, diccionary):
        objeto = EventoManager(self.db).entity(**diccionary)

        objeto.fechai = datetime.strptime(objeto.fechai, '%d/%m/%Y')
        objeto.fechaf = datetime.strptime(objeto.fechaf, '%d/%m/%Y')

        if objeto.horai == "":
            objeto.horai = None
        else:
            objeto.horai = datetime.strptime(objeto.horai, '%H:%M')

        if objeto.horaf == "":
            objeto.horaf = None
        else:
            objeto.horaf = datetime.strptime(objeto.horaf, '%H:%M')
        fecha = BitacoraManager(self.db).fecha_actual()
        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Evento.", fecha=fecha,tabla="evento", identificador=a.id)
        super().insert(b)

        return a

    def actualizar(self, diccionary):
        objeto = EventoManager(self.db).entity(**diccionary)


        if objeto.horai == "":
            objeto.horai = None
        else:
            objeto.horai = datetime.strptime(objeto.horai, '%H:%M')

        if objeto.horaf == "":
            objeto.horaf = None
        else:
            objeto.horaf = datetime.strptime(objeto.horaf, '%H:%M')

        fecha = BitacoraManager(self.db).fecha_actual()
        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Evento.", fecha=fecha,tabla="evento", identificador=a.id)
        super().insert(b)

        return a

    def delete(self, id,state, user, ip):
        x = self.db.query(Evento).filter(Evento.id == id).one()

        for invitacion in x.invitaciones:
            invitacion.estado = state

            diccionary = dict(codigo=invitacion.id, tarjeta=invitacion.codigoautorizacion, situacion="Denegado")
            ConfiguraciondispositivoManager(self.db).denegar_qr_invitacion(diccionary)

        x.estado = state
        if state:
            mensaje = "Habilito Evento"
        else:
            mensaje = "Deshabilito Evento"

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion=mensaje, fecha=fecha, tabla="evento", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return mensaje

    def generar_codigo_autorizacion(self, objeto):

        if objeto.codigoautorizacion == "":
            # codigoqr = random.randrange(9999)
            # obj.codigoautorizacion = "EVEN" +str(objeto.id) + "INVI" +str(obj.id)
            #obj.codigoautorizacion = str(objeto.id) + str(obj.id) + str(codigoqr)
            objeto.codigoautorizacion = str(objeto.fkevento) + str(objeto.id)

        objeto = super().update(objeto)

        sin_guardia = False
        if objeto.evento.fkdomicilio:
            sin_guardia = objeto.evento.domicilio.condominio.singuardia
        elif objeto.evento.fkareasocial:
            sin_guardia = objeto.evento.areasocial.condominio.singuardia

        if sin_guardia:

            respuesta = EventoManager(self.db).validar_invitacion(objeto.codigoautorizacion)
            if respuesta:


                diccionary = dict(codigo=objeto.id, tarjeta=objeto.codigoautorizacion, situacion="Acceso")

                ConfiguraciondispositivoManager(self.db).insert_qr_invitacion(diccionary)

                event = self.db.query(Evento).filter(Evento.id == objeto.fkevento).first()

                event.situacion = "Acceso"
                super().update(event)


        return objeto

    def validar_invitacion(self,codigoautorizacion):

        fechadate = datetime.now(pytz.timezone('America/La_Paz'))
        fecha_hoy_str = fechadate.strftime('%Y-%m-%d %H:%M:%S')
        fechahoy = fecha_hoy_str[0:10]
        horahoy = fecha_hoy_str[11:19]

        time_horahoy = datetime.strptime(horahoy, '%H:%M:%S').time()

        x= self.db.query(Invitacion).join(Evento).filter(Invitacion.estado == True).filter(Evento.fechai <= fechahoy).filter(
            Evento.fechaf >= fechahoy).filter(Invitacion.codigoautorizacion == codigoautorizacion).first()

        if x:
            if x.evento.horai:
                if time_horahoy >= x.evento.horai.time():
                    if x.evento.horaf:
                        if time_horahoy <= x.evento.horaf.time():
                            return x
                        else:
                            return None
                    else:
                        return x
                else:
                    return None

            elif x.evento.horaf:
                if time_horahoy <= x.evento.horaf.time():
                    return x
                else:
                    return None
            else:

                return x
        else:
            return x

    def validar_invitacion_lector(self,codigoautorizacion):

        fechadate = datetime.now(pytz.timezone('America/La_Paz'))
        fecha_hoy_str = fechadate.strftime('%Y-%m-%d %H:%M:%S')
        fechahoy = fecha_hoy_str[0:10]
        horahoy = fecha_hoy_str[11:19]

        time_horahoy = datetime.strptime(horahoy, '%H:%M:%S').time()

        x= self.db.query(Invitacion).join(Evento).filter(Invitacion.estado == True).filter(Evento.fechai <= fechahoy).filter(
            Evento.fechaf >= fechahoy).filter(Invitacion.codigoautorizacion == codigoautorizacion).first()

        if x:
            if x.evento.horai:
                if time_horahoy >= x.evento.horai:
                    if x.evento.horaf:
                        if time_horahoy <= x.evento.horaf:
                            return x
                        else:
                            return None
                    else:
                        return x
                else:
                    return None

            elif x.evento.horaf:
                if time_horahoy <= x.evento.horaf:
                    return x
                else:
                    return None
            else:

                return x
        else:
            return x

    def listar_eventos(self,usuario):

        if usuario.sigas:
            return self.db.query(Evento).filter(self.entity.estado == True).all()
        elif usuario.rol.nombre == "RESIDENTE":
            return self.db.query(Evento).filter(Evento.fkresidente == usuario.fkresidente).filter(
                self.entity.estado == True).all()
        else:
            return self.db.query(Evento).join(Residente).join(ResidenteDomicilio).join(Domicilio).join(Condominio).filter(
                Evento.estado == True).filter(ResidenteDomicilio.vivienda == True).filter(Condominio.id == usuario.fkcondominio).all()


    def listar_eventos_dia(self, usuario):
        fecha = datetime.now(pytz.timezone('America/La_Paz'))
        fechahoy = str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year)
        fechahoy = datetime.strptime(fechahoy, '%d/%m/%Y')

        if usuario.sigas:
            return self.db.query(Evento).filter(self.entity.estado == True).filter(
                Evento.fechai.cast(Date) == fechahoy).all()
        elif usuario.rol.nombre == "RESIDENTE":
            return self.db.query(Evento).filter(Evento.fkresidente == usuario.fkresidente).filter(
                Evento.fechai.cast(Date) == fechahoy).filter(
                self.entity.estado == True).all()
        else:
            return self.db.query(Evento).join(Residente).join(ResidenteDomicilio).join(Domicilio).join(Condominio).filter(
                Evento.fechai.cast(Date) == fechahoy).filter(
                Evento.estado == True).filter(ResidenteDomicilio.vivienda == True).filter(
                Condominio.id == usuario.fkcondominio).all()


    def filtrar(self, fechainicio, fechafin,usuario):
        usuario = UsuarioManager(self.db).get_by_pass(usuario)

        list = {}
        c = 0


        if usuario.sigas:
            return self.db.query(Evento).filter(self.entity.estado == True).filter(func.date(Evento.fechai).between(fechainicio, fechafin)).all()
        elif usuario.rol.nombre == "RESIDENTE":
            return self.db.query(Evento).filter(Evento.fkresidente == usuario.fkresidente).filter(func.date(Evento.fechai).between(fechainicio, fechafin)).filter(
                self.entity.estado == True).all()
        else:
            return self.db.query(Evento).join(Residente).join(ResidenteDomicilio).join(Domicilio).join(
                Condominio).filter(func.date(Evento.fechai).between(fechainicio, fechafin)).filter(
                Evento.estado == True).filter(ResidenteDomicilio.vivienda == True).filter(
                Condominio.id == usuario.fkcondominio).all()


class InvitacionManager(SuperManager):
    def __init__(self, db):
        super().__init__(Invitacion, db)

    def obtener_invitaciones(self,idevento):
        return self.db.query(Invitacion).filter(Invitacion.estado == True).filter(Invitacion.fkevento == idevento).all()

    def insert(self, diccionary):

        objeto = InvitacionManager(self.db).entity(**diccionary)

        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        print("registro invitacion: " + str(a.id))

        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Invitacion.", fecha=fecha,tabla="invitacion", identificador=a.id)
        super().insert(b)

        EventoManager(self.db).generar_codigo_autorizacion(a)

        return a

    def delete(self, id,state, user, ip):
        x = self.db.query(Invitacion).filter(Invitacion.id == id).one()
        x.estado = state
        if state:
            mensaje = "Habilito Invitacion"
        else:
            mensaje = "Deshabilito Invitacion"

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion=mensaje, fecha=fecha, tabla="invitacion", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        # diccionary = dict(codigo=x.id, tarjeta=x.codigoautorizacion, situacion="Denegado")
        # ConfiguraciondispositivoManager(self.db).denegar_qr_invitacion(diccionary)

        return mensaje

    def delete_invitacion_rapida(self, id,state, user, ip):
        x = self.db.query(Invitacion).filter(Invitacion.id == id).first()
        x.estado = state

        even = self.db.query(Evento).filter(Evento.id == x.fkevento).first()
        even.estado = state

        if state:
            mensaje = "Habilito Invitacion rapida"
        else:
            mensaje = "Deshabilito Invitacion rapida"

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion=mensaje, fecha=fecha, tabla="invitacion", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.merge(even)
        self.db.commit()

        diccionary = dict(codigo=x.id, tarjeta=x.codigoautorizacion, situacion="Denegado")
        ConfiguraciondispositivoManager(self.db).denegar_qr_invitacion(diccionary)

        return mensaje




class TipoEventoManager(SuperManager):
    def __init__(self, db):
        super().__init__(TipoEvento, db)

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()







