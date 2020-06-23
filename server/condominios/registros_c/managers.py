from .models import *
from tornado.gen import coroutine
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ...condominios.movimiento.managers import *


from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font

import asyncio

class Registros_cManager(SuperManager):

    def __init__(self, db):
        super().__init__(RegistrosControlador, db)


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
            cerradura = ""

            if reg.codigo != "0":
                codigo = reg.codigo
                residente_vehi = self.db.query(Residente).join(Vehiculo).filter(Vehiculo.fkresidente == Residente.id).filter(Vehiculo.fknropase == reg.codigo).first()
                if residente_vehi:
                    codigo = residente_vehi.fullname + " - Vehicular"

                residente = self.db.query(Residente).filter(Residente.fknropase == reg.codigo).first()
                if residente:
                    codigo = residente.fullname + " - Peatonal"


            else:
                codigo = "Usuario no resgistrado"

            res_dispotivo = self.db.query(Dispositivo).filter(Dispositivo.id == reg.fkdispositivo).first()
            res_cerradura = self.db.query(Cerraduras).filter(Cerraduras.fkdispositivo == res_dispotivo.id).filter(Cerraduras.numero == reg.puerta ).first()

            if res_cerradura:
                cerradura =res_cerradura.nombre

            list.append(dict(id=reg.id,tarjeta=reg.tarjeta,codigo=codigo,dia=reg.time.day,mes=nombre_meses[reg.time.month],año=reg.time.year,hora=reg.time.strftime("%H:%M:%S"),dispositivo=reg.dispositivo.descripcion,cerradura=cerradura))

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
            cerradura = ""

            if reg.codigo != "0":
                codigo = reg.codigo
                residente_vehi = self.db.query(Residente).join(Vehiculo).filter(Vehiculo.fkresidente == Residente.id).filter(Vehiculo.fknropase == reg.codigo).first()
                if residente_vehi:
                    codigo = residente_vehi.fullname + " - Vehicular"

                residente = self.db.query(Residente).filter(Residente.fknropase == reg.codigo).first()
                if residente:
                    codigo = residente.fullname + " - Peatonal"


            else:
                codigo = "Usuario no resgistrado"

            res_dispotivo = self.db.query(Dispositivo).filter(Dispositivo.id == reg.fkdispositivo).first()
            res_cerradura = self.db.query(Cerraduras).filter(Cerraduras.fkdispositivo == res_dispotivo.id).filter(Cerraduras.numero == reg.puerta ).first()

            if res_cerradura:
                cerradura =res_cerradura.nombre

            list.append(dict(id=reg.id,tarjeta=reg.tarjeta,codigo=codigo,dia=reg.time.day,mes=nombre_meses[reg.time.month],año=reg.time.year,hora=reg.time.strftime("%H:%M:%S"),dispositivo=reg.dispositivo.descripcion,cerradura=cerradura))

        return list


    # def funcionRegistros(self,marcaciones):
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(asyncio.run(RegistrosManager(self.db).insertRegistros(marcaciones)))
    #     loop.close()


    def insertRegistros(self,marcaciones):
        for marcacion in marcaciones['marcaciones']:

            marcacion[6] = datetime.strptime(marcacion[6], '%d/%m/%Y %H:%M:%S')
            respuesta = self.db.query(self.entity).filter(self.entity.time == marcacion[6]).filter(self.entity.tarjeta == marcacion[0]).filter(self.entity.fkdispositivo == marcaciones['iddispositivo']).first()

            if not respuesta:
                object = RegistrosControlador(tarjeta=marcacion[0],codigo=marcacion[1],verificado=marcacion[2],puerta=marcacion[3],evento=marcacion[4],estado=marcacion[5],time=marcacion[6],fkdispositivo=marcaciones['iddispositivo'])
                MovimientoManager(self.db).actualizar_movimiento(object)
                self.db.add(object)

        self.db.commit()
        self.db.close()

