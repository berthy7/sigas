from server.common.managers import SuperManager
from server.usuarios.usuario.models import *

from .models import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import Column, Integer, String, Date,func


import pytz
import calendar

from random import *
import random
import requests

class BitacoraManager(SuperManager):

    def __init__(self, db):
        super().__init__(Bitacora, db)

    # def list_all(self):
    #     x = dict(objects=self.db.query(Bitacora).order_by(Bitacora.id.asc()).limit(5000).all())
    #     return x


    def list_all(self):

        fecha = datetime.now(pytz.timezone('America/La_Paz'))
        fechahoy = str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)
        fechahoy = datetime.strptime(fechahoy, '%d/%m/%Y')

        return dict(objects=self.db.query(Bitacora).filter(self.entity.fecha.cast(Date) == fechahoy).order_by(Bitacora.id.asc()))

    def filtrar(self, fechainicio, fechafin, idusuario):
        # usuario = UsuarioManager(self.db).get_by_pass(usuario)

        if idusuario == "0":

            print("Filtrar por fecha todos")

            return self.db.query(Bitacora).filter(func.date(self.entity.fecha).between(fechainicio, fechafin)).order_by(Bitacora.id.asc())
        else:
            print("Filtrar por fecha usuario")
            return self.db.query(Bitacora).filter(self.entity.fkusuario == idusuario).filter(func.date(self.entity.fecha).between(fechainicio, fechafin)).order_by(Bitacora.id.asc())

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

    def fecha(self):
        fechaHora = datetime.now(pytz.timezone('America/La_Paz'))

        principal = self.db.query(Principal).first()

        if principal.estado:
            fecha_str = str(fechaHora)
            fecha_ = fecha_str[0:19]
            fechaHora = datetime.strptime(fecha_, '%Y-%m-%d %H:%M:%S')

            timezone = pytz.timezone('America/La_Paz')
            fechaHora = pytz.utc.localize(fechaHora, is_dst=None).astimezone(timezone)

        return fechaHora

    def obtener_dia(self,fecha):

        dia = calendar.day_name[fecha.weekday()]

        if dia == "Monday":
            dia = "Lu"
        elif dia == "Tuesday":
            dia = "Ma"
        elif dia == "Wednesday":
            dia = "Mi"
        elif dia == "Thursday":
            dia = "Ju"
        elif dia == "Friday":
            dia = "Vi"
        elif dia == "Saturday":
            dia = "Sa"
        elif dia == "Sunday":
            dia = "Do"

        return dia

    def rango_fechas(self,fechai, fechaf):
        rango = []
        dias_totales = (fechaf - fechai).days
        for days in range(dias_totales + 1):
            fecha = fechai + relativedelta(days=days)
            rango.append(fecha)
        return rango


    def generar_codigo(self):
        longitud = 5
        valores = "0123456789"

        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        return p