from .models import *
from tornado.gen import coroutine
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ..dispositivo.models import *
from ...condominios.movimiento.managers import *
from ...condominios.portero_virtual.managers import *
from ...condominios.evento.managers import *


from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font

import asyncio



class RegistrosManager(SuperManager):

    def __init__(self, db):
        super().__init__(RegistrosControlador, db)

    def alerta(self, id, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.alertado = True
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Se activo Alarma.", fecha=fecha, tabla="registroscontrolador", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return x


    def get_all(self):
        return self.db.query(self.entity).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity))

    def listar_todo(self):
        return self.db.query(self.entity).all()

    def filtrar(self, fechainicio, fechafin,usuario):
        list = {}
        c = 0

        if usuario.sigas:
            registros = self.db.query(self.entity).filter(func.date(self.entity.time).between(fechainicio, fechafin)).order_by(self.entity.id.desc()).all()
        else:
            registros = self.db.query(self.entity).join(Dispositivo).filter(Dispositivo.fkcondominio == usuario.fkcondominio).filter(func.date(self.entity.time).between(fechainicio, fechafin)).order_by(self.entity.id.desc()).all()

        list = []
        nombre_meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
                       9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}

        for reg in registros:

            codigo = ""
            tarjeta = ""
            cerradura = ""
            autorizacion = ""
            destino = ""

            if reg.evento == 0:

                if reg.codigo != "0":
                    codigo = reg.codigo
                    tarjeta = reg.tarjeta

                    if reg.fkdispositivo:

                        if reg.dispositivo.fktipodispositivo != 4:

                            idcondominio = reg.dispositivo.fkcondominio

                            residente_qr = self.db.query(Residente).join(ResidenteDomicilio).join(Domicilio).filter(Domicilio.fkcondominio == idcondominio).filter(Residente.codigoqr == reg.tarjeta).first()

                            if residente_qr:
                                codigo =  "Codigo Qr"
                                tarjeta = "Residente"
                                autorizacion = residente_qr.fullname

                            residente_vehi = self.db.query(Residente).join(ResidenteDomicilio).join(Domicilio).filter(Domicilio.fkcondominio == idcondominio).join(Vehiculo).filter(Vehiculo.fkresidente == Residente.id).filter(Vehiculo.fknropase == reg.codigo).first()

                            if residente_vehi:
                                codigo = "Tag Vehicular"
                                autorizacion = residente_vehi.fullname

                            residente = self.db.query(Residente).join(ResidenteDomicilio).join(Domicilio).filter(Domicilio.fkcondominio == idcondominio).filter(Residente.fknropase == reg.codigo).first()
                            if residente:
                                codigo = "Tarjeta Peatonal"
                                autorizacion = residente.fullname

                            tarjetaObj = self.db.query(Nropase).filter(Nropase.tarjeta == reg.tarjeta).first()
                            if tarjetaObj:
                                if tarjetaObj.tipo == "Provper":
                                    provper = self.db.query(Invitado).filter(Invitado.fknropase == tarjetaObj.id).first()
                                    if provper:
                                        codigo = str(tarjetaObj.tarjeta)
                                        tarjeta = str(tarjetaObj.tipo)
                                        autorizacion = str(provper.fullname)

                                else:
                                    autorizacion = ""
                                    codigo = str(tarjetaObj.tarjeta)
                                    tarjeta = str(tarjetaObj.tipo)

                            codigo_normalizado = int(reg.codigo) - 500000
                            invitacion = self.db.query(Invitacion).filter(
                                Invitacion.codigoautorizacion == str(codigo_normalizado)).first()
                            if invitacion:
                                codigo = invitacion.invitado.fullname
                                tarjeta = invitacion.tipopase.nombre
                                autorizacion = invitacion.evento.residente.nombre + " " + invitacion.evento.residente.apellidop + " Cel:" + invitacion.evento.residente.telefono

                                if invitacion.evento.fkdomicilio:

                                    destino = invitacion.evento.domicilio.nombre

                                elif invitacion.evento.fkareasocial:

                                    destino = invitacion.evento.areasocial.nombre

                        else:
                            codigo_normalizado_residente = int(reg.codigo) - 100000
                            residente_biometrico = self.db.query(Residente).filter(Residente.codigo == codigo_normalizado_residente).first()

                            if residente_biometrico:
                                autorizacion = residente_biometrico.nombre + " " + residente_biometrico.apellidop
                            else:
                                autorizacion = ""

                            if reg.verificado == 16:
                                codigo = "Apertura Rostro"
                            else:
                                codigo = "Apertura Huella"

                            tarjeta = reg.codigo


                else:
                    codigo = "Usuario no registrado"
                    tarjeta = reg.tarjeta

            else:

                evento = DispositivoeventosManager(self.db).obtener_x_codigo(reg.evento)

                if evento:
                    codigo = evento.nombre
                else:
                    codigo ="Evento no registrado"


            res_dispotivo = self.db.query(Dispositivo).filter(Dispositivo.id == reg.fkdispositivo).first()
            res_cerradura = self.db.query(Cerraduras).filter(Cerraduras.fkdispositivo == res_dispotivo.id).filter(Cerraduras.numero == reg.puerta ).first()

            if res_cerradura:
                cerradura =res_cerradura.nombre
            list.append(dict(id=reg.id,evento=reg.evento,alertado=reg.alertado,tarjeta=tarjeta,codigo=codigo,autorizacion=autorizacion,destino=destino,dia=reg.time.day,mes=nombre_meses[reg.time.month],año=reg.time.year,hora=reg.time.strftime("%H:%M:%S"),dispositivo=reg.dispositivo.descripcion,cerradura=cerradura))

        return list


    def listar_todo_diccionario(self,usuario):

        fecha = datetime.now(pytz.timezone('America/La_Paz'))
        fechahoy = str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)
        fechahoy = datetime.strptime(fechahoy, '%d/%m/%Y')

        if usuario.sigas:
            registros = self.db.query(self.entity).filter(self.entity.time.cast(Date) == fechahoy).order_by(
                self.entity.time.cast(Date).asc(), self.entity.time.cast(Time).asc()).all()
        else:
            registros = self.db.query(self.entity).join(Dispositivo).filter(Dispositivo.fkcondominio == usuario.fkcondominio).filter(self.entity.time.cast(Date) == fechahoy).order_by(
                self.entity.time.cast(Date).asc(), self.entity.time.cast(Time).asc()).all()


        list = []
        nombre_meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
                       9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}

        for reg in registros:

            codigo = ""
            tarjeta = ""
            cerradura = ""
            autorizacion = ""
            destino = ""

            if reg.evento == 0:

                tarjeta = reg.tarjeta
                if reg.codigo != "0":
                    codigo = reg.codigo
                    tarjeta = reg.tarjeta

                    if reg.fkdispositivo:

                        if reg.dispositivo.fktipodispositivo != 4:

                            idcondominio = reg.dispositivo.fkcondominio


                            residente_qr = self.db.query(Residente).join(ResidenteDomicilio).join(Domicilio).filter(Domicilio.fkcondominio == idcondominio).filter(Residente.codigoqr == reg.tarjeta).first()

                            if residente_qr:
                                codigo =  "Codigo Qr"
                                tarjeta = "Residente"
                                autorizacion = residente_qr.fullname

                            residente_vehi = self.db.query(Residente).join(ResidenteDomicilio).join(Domicilio).filter(Domicilio.fkcondominio == idcondominio).join(Vehiculo).filter(Vehiculo.fkresidente == Residente.id).filter(Vehiculo.fknropase == reg.codigo).first()

                            if residente_vehi:
                                codigo = "Tag Vehicular"
                                autorizacion = residente_vehi.fullname

                            residente = self.db.query(Residente).join(ResidenteDomicilio).join(Domicilio).filter(Domicilio.fkcondominio == idcondominio).filter(Residente.fknropase == reg.codigo).first()
                            if residente:
                                codigo = "Tarjeta Peatonal"
                                autorizacion = residente.fullname

                            tarjetaObj = self.db.query(Nropase).filter(Nropase.tarjeta == reg.tarjeta).first()
                            if tarjetaObj:
                                if tarjetaObj.tipo == "Provper":
                                    provper = self.db.query(Invitado).filter(Invitado.fknropase == tarjetaObj.id).first()
                                    if provper:
                                        codigo = str(tarjetaObj.tarjeta)
                                        tarjeta = str(tarjetaObj.tipo)
                                        autorizacion = str(provper.fullname)

                                else:
                                    autorizacion = ""
                                    codigo = str(tarjetaObj.tarjeta)
                                    tarjeta = str(tarjetaObj.tipo)



                            codigo_normalizado = int(reg.codigo) - 500000
                            invitacion = self.db.query(Invitacion).filter(Invitacion.codigoautorizacion == str(codigo_normalizado)).first()
                            if invitacion:
                                codigo = invitacion.invitado.fullname
                                tarjeta = invitacion.tipopase.nombre
                                autorizacion = invitacion.evento.residente.nombre + " " + invitacion.evento.residente.apellidop + " Cel:" + invitacion.evento.residente.telefono

                                if invitacion.evento.fkdomicilio:

                                    destino = invitacion.evento.domicilio.nombre

                                elif invitacion.evento.fkareasocial:

                                    destino = invitacion.evento.areasocial.nombre

                        else:
                            codigo_normalizado_residente = int(reg.codigo) - 100000

                            residente_biometrico = self.db.query(Residente).filter(
                                Residente.codigo == codigo_normalizado_residente).first()

                            if residente_biometrico:
                                autorizacion = residente_biometrico.nombre + " " + residente_biometrico.apellidop
                            else:
                                autorizacion = ""

                            if reg.verificado == 16:
                                codigo = "Apertura Rostro"
                            else:
                                codigo = "Apertura Huella"

                            tarjeta = reg.codigo

                else:
                    codigo = "Usuario no registrado"
                    tarjeta = reg.tarjeta

            else:

                evento = DispositivoeventosManager(self.db).obtener_x_codigo(reg.evento)

                if evento:
                    codigo = evento.nombre
                else:
                    codigo ="Evento no registrado"


            res_dispotivo = self.db.query(Dispositivo).filter(Dispositivo.id == reg.fkdispositivo).first()
            res_cerradura = self.db.query(Cerraduras).filter(Cerraduras.fkdispositivo == res_dispotivo.id).filter(Cerraduras.numero == reg.puerta ).first()

            if res_cerradura:
                cerradura =res_cerradura.nombre

            list.append(dict(id=reg.id,evento=reg.evento,alertado=reg.alertado,tarjeta=tarjeta,codigo=codigo,autorizacion=autorizacion,destino=destino,dia=reg.time.day,mes=nombre_meses[reg.time.month],año=reg.time.year,hora=reg.time.strftime("%H:%M:%S"),dispositivo=reg.dispositivo.descripcion,cerradura=cerradura))

        return list


    # def funcionRegistros(self,marcaciones):
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(asyncio.run(RegistrosManager(self.db).insertRegistros(marcaciones)))
    #     loop.close()


    def insertRegistros(self,marcaciones):
        for marcacion in marcaciones['marcaciones']:

            marcacion[6] = datetime.strptime(marcacion[6], '%d/%m/%Y %H:%M:%S')

            print("llegaron marcaciones: "+str(marcacion[6]))
            respuesta = self.db.query(self.entity).filter(self.entity.evento == marcacion[4]).filter(self.entity.time == marcacion[6]).filter(self.entity.tarjeta == marcacion[0]).filter(self.entity.fkdispositivo == marcaciones['iddispositivo']).first()

            if not respuesta:
                print("registro marcacion")
                object = RegistrosControlador(tarjeta=marcacion[0],codigo=marcacion[1],verificado=marcacion[2],puerta=marcacion[3],evento=marcacion[4],estado=marcacion[5],time=marcacion[6],fkdispositivo=marcaciones['iddispositivo'])
                MovimientoManager(self.db).actualizar_movimiento(object)
                # PorterovirtualManager(self.db).actualizar_marcacion(object)

                # i = InvitacionManager(self.db).obtener_x_codigoqr(marcacion[0])
                #
                # # deshabilitar invitacion
                # if i:
                #     multi = InvitacionManager(self.db).multiacceso(i.id)
                #
                #     if multi:
                #         InvitacionManager(self.db).delete(i.id, False, None, None)

                self.db.add(object)

        self.db.commit()
        self.db.close()



