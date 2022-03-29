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

# from onesignal_sdk.client import Client
# from onesignal_sdk.error import OneSignalHTTPError


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
                        invitado = InvitadoManager(self.db).registrar_invitado_movimiento(diccionary)
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


        if a.fknropase:
            # actualizar siuacion
            NropaseManager(self.db).situacion(a.fknropase, "Ocupado")

        # deshabilitar invitacion
        if a.fkinvitacion:
            accesos_invitacion = InvitacionManager(self.db).obtener_accesos_evento(a.fkinvitacion)

            if accesos_invitacion['multiacceso'] is False:
                if accesos_invitacion['multiple'] is False:
                    #if accesos_invitacion['paselibre'] is False:

                    InvitacionManager(self.db).delete(a.fkinvitacion, False, objeto.user, objeto.ip)


            principal = self.db.query(Principal).first()
            if principal.estado:
                NotificacionManager(self.db).registrar_notificacion_(a,objeto)

        self.hilo_sincronizar_update_descripcion(a)
        return a

    def delete(self, id, user, ip):
        x = self.db.query(Movimiento).filter(Movimiento.id == id).first()
        x.estado = False

        mensaje = "Deshabilito Movimiento"

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion=mensaje, fecha=fecha, tabla="movimiento", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        principal = self.db.query(Principal).first()

        if principal.estado:
            condominio = self.db.query(Condominio).filter(Condominio.codigo == x.descripcion_condominio).first()
            try:
                if condominio:

                    if condominio.ip_publica != "":
                        diccionary = dict(id=id, estado=False, user=user, ip=ip)

                        url = "http://" + condominio.ip_publica + ":" + condominio.puerto + "/api/v1/sincronizar_movimiento_estado"

                        headers = {'Content-Type': 'application/json'}
                        string = diccionary
                        cadena = json.dumps(string)
                        body = cadena
                        resp = requests.post(url, data=body, headers=headers, verify=False)
                        response = json.loads(resp.text)

                        print(response)


            except Exception as e:
                # Other errors are possible, such as IOError.
                print("Error de conexion: " + str(e))

        return x

        return x

    def hilo_sincronizar_update_descripcion(self, objeto):
        if objeto.codigo == "":
            objeto.codigo = objeto.id
        objeto.descripcion_documento = objeto.tipodocumento.nombre
        objeto.descripcion_fechai = objeto.fechar.strftime('%d/%m/%Y %H:%M:%S')

        if objeto.fkresidente:
            objeto.descripcion_residente = objeto.residente.fullname
        else:
            objeto.descripcion_residente = '-----'

        if objeto.fkinvitado:
            if objeto.fkconductor:
                objeto.descripcion_nombre_conductor = objeto.conductor.fullname
            else:
                objeto.descripcion_nombre_conductor = '-----'

            objeto.descripcion_ci_invitado = objeto.invitado.ci
            objeto.descripcion_nombre_invitado = objeto.invitado.fullname


        else:
            objeto.descripcion_ci_invitado = '-----'
            objeto.descripcion_nombre_invitado = '-----'
        if objeto.fkvehiculo:
            objeto.descripcion_placa = objeto.vehiculo.placa
            objeto.descripcion_tipo = objeto.vehiculo.tipo.nombre
            objeto.descripcion_marca = objeto.vehiculo.marca.nombre
            objeto.descripcion_modelo = objeto.vehiculo.modelo.nombre if objeto.vehiculo.fkmodelo else '-----'
            objeto.descripcion_color = objeto.vehiculo.color.nombre


        else:
            objeto.descripcion_placa = '-----'
            objeto.descripcion_tipo = '-----'
            objeto.descripcion_marca = '-----'
            objeto.descripcion_modelo = '-----'
            objeto.descripcion_color = '-----'



        if objeto.fkdomicilio:
            objeto.descripcion_destino = objeto.domicilio.nombre
            objeto.descripcion_condominio = objeto.domicilio.codigocondominio
        elif objeto.fkareasocial:
            objeto.descripcion_destino = objeto.areasocial.nombre
            objeto.descripcion_condominio = objeto.areasocial.codigocondominio
        else:
            objeto.descripcion_destino = '-----'
            objeto.descripcion_condominio = '-----'

        if objeto.fknropase:
            objeto.descripcion_nropase = objeto.nropase.numero + ' ' + objeto.nropase.tipo
        else:
            objeto.descripcion_nropase = '-----'

        self.db.merge(objeto)
        self.db.commit()


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
        x.descripcion_fechaf = fecha.strftime('%d/%m/%Y %H:%M:%S')


        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Registro Salida", fecha=fecha, tabla="movimiento", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        if x.fknropase:
            # actualizar siuacion
            NropaseManager(self.db).situacion(x.fknropase, "Libre")

        return x

    def armado_diccionario(self, d):
        return dict(id=d.id, fechar=d.fechar.strftime('%d/%m/%Y %H:%M:%S'),
                          fechai=d.descripcion_fechai, fechaf=d.descripcion_fechaf,
                          documento=d.descripcion_documento,
                          ci_invitado=d.descripcion_ci_invitado,
                          nombre_invitado=d.descripcion_nombre_invitado,
                          residente=d.descripcion_residente,
                          destino=d.descripcion_destino,
                          autorizacion=d.autorizacion.nombre,
                          nropase=d.descripcion_nropase, tipopase=d.tipopase.nombre,
                          observacion=d.observacion)

    def filtrar(self, fechainicio, fechafin, usuario):
        usuario = UsuarioManager(self.db).get_by_pass(usuario)
        lista = list()


        if usuario.sigas:
            movimientos = self.db.query(self.entity).filter(self.entity.estado == True).filter(
                func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Peatonal").all()

            for d in movimientos:
                lista.append(self.armado_diccionario(d))

            return lista

        else:

            movimientos = self.db.query(self.entity) \
                .filter(self.entity.descripcion_condominio == usuario.condominio.codigo) \
                .filter(func.date(self.entity.fechar).between(fechainicio, fechafin)) \
                .filter(self.entity.tipo == "Peatonal") \
                .filter(self.entity.estado == True).all()

            for d in movimientos:
                lista.append(self.armado_diccionario(d))

            return lista

    def filtrar_residente(self, fechainicio, fechafin, fresidente):
        lista = list()
        movimientos = self.db.query(self.entity) \
            .filter(self.entity.fkresidente == fresidente) \
            .filter(func.date(self.entity.fechar).between(fechainicio, fechafin)) \
            .filter(self.entity.tipo == "Peatonal") \
            .filter(self.entity.estado == True).all()

        for d in movimientos:
            lista.append(self.armado_diccionario(d))

        return lista

    def filtrar_domicilio(self, fechainicio, fechafin, fdomicilio):
        lista = list()
        movimientos = self.db.query(self.entity) \
            .filter(self.entity.estado == True) \
            .filter(self.entity.fkdomicilio == fdomicilio) \
            .filter(self.entity.tipo == "Peatonal") \
            .filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).all()

        for d in movimientos:
            lista.append(self.armado_diccionario(d))

        return lista

    # def filtrar(self, fechainicio, fechafin,usuario,fresidente):
    #     usuario = UsuarioManager(self.db).get_by_pass(usuario)
    #
    #     c = 0
    #
    #     fecha = fecha_zona
    #     fechahoy = str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)
    #     fechahoy = datetime.strptime(fechahoy, '%d/%m/%Y')
    #
    #     if fresidente == '':
    #         if usuario.sigas:
    #             return self.db.query(self.entity).filter(self.entity.estado == True).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
    #                 self.entity.tipo == "Peatonal").all()
    #         else:
    #
    #             return self.db.query(self.entity) \
    #                 .filter(self.entity.descripcion_condominio == usuario.condominio.codigo) \
    #                 .filter(func.date(self.entity.fechar).between(fechainicio, fechafin))\
    #                 .filter(self.entity.tipo == "Peatonal") \
    #                 .filter(self.entity.estado == True).all()
    #     else:
    #         listaDomicilios = list()
    #         idDomiciliosResidente = self.db.query(ResidenteDomicilio).filter(ResidenteDomicilio.fkresidente == fresidente).all()
    #
    #
    #         for idDomicilio in idDomiciliosResidente:
    #             listaDomicilios.append(idDomicilio.fkdomicilio)
    #
    #
    #         if usuario.sigas:
    #             return self.db.query(self.entity).filter(self.entity.estado == True) \
    #                 .filter(self.entity.fkdomicilio.in_(listaDomicilios)) \
    #                 .filter(func.date(self.entity.fechar).between(fechainicio, fechafin))\
    #                 .filter(self.entity.tipo == "Peatonal").all()
    #         else:
    #
    #             return self.db.query(self.entity) \
    #                 .filter(self.entity.fkdomicilio.in_(listaDomicilios)) \
    #                 .filter(self.entity.descripcion_condominio == usuario.condominio.codigo) \
    #                 .filter(func.date(self.entity.fechar).between(fechainicio, fechafin)) \
    #                 .filter(self.entity.tipo == "Peatonal") \
    #                 .filter(self.entity.estado == True).all()


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
        condominio = self.db.query(Condominio).filter(Condominio.id == usuario.fkcondominio).first()
        list = {}
        c = 0

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(
                self.entity.id > ult_registro).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Peatonal").order_by(self.entity.id.desc()).all()
        else:
            domicilio = self.db.query(self.entity)\
                .filter(self.entity.id > ult_registro).filter(self.entity.descripcion_condominio== condominio.codigo)\
                .filter(func.date(self.entity.fechar).between(fechainicio, fechafin))\
                .filter(self.entity.tipo == "Peatonal")\
                .filter(self.entity.estado == True)\
                .order_by(self.entity.id.desc()).all()

            return domicilio