from .models import *
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ...usuarios.usuario.managers import *
from ..residente.managers import *
from ..areasocial.models import Areasocial
from ..movimiento.models import Movimiento



class ReporteManager(SuperManager):

    def __init__(self, db):
        super().__init__(Movimiento, db)

    def reporte_vehicular_visita(self, diccionario):
        lista = list()
        diccionario['fechainicio'] = datetime.strptime(diccionario['fechainicio'], '%d/%m/%Y')
        diccionario['fechafin'] = datetime.strptime(diccionario['fechafin'], '%d/%m/%Y')

        domicilio = self.db.query(self.entity).join(Domicilio).filter(
            Domicilio.fkcondominio == diccionario['fkcondominio']).filter(
            func.date(self.entity.fechar).between(diccionario['fechainicio'], diccionario['fechafin'])).filter(
            self.entity.tipo == "Vehicular").filter(self.entity.estado == True).all()

        areasocial = self.db.query(self.entity).join(Areasocial).filter(
            Areasocial.fkcondominio == diccionario['fkcondominio']).filter(
            func.date(self.entity.fechar).between(diccionario['fechainicio'], diccionario['fechafin'])).filter(
            self.entity.tipo == "Vehicular").filter(self.entity.estado == True).all()


        for d in domicilio:
            lista.append(dict(id=d.id,fechai=d.descripcion_fechai,fechaf=d.descripcion_fechaf,documento=d.descripcion_documento,
                              ci_invitado=d.descripcion_ci_invitado,nombre_invitado=d.descripcion_nombre_invitado,
                              nombre_conductor=d.descripcion_nombre_conductor,cantpasajeros=d.cantpasajeros,
                              placa=d.descripcion_placa,tipo=d.descripcion_tipo,marca=d.descripcion_marca,modelo=d.descripcion_modelo,
                              color=d.descripcion_color,destino=d.descripcion_destino,autorizacion=d.autorizacion.nombre,
                              nropase=d.descripcion_nropase,tipopase=d.tipopase.nombre,observacion=d.observacion))

        for a in areasocial:
            lista.append(dict(id=a.id,fechai=a.descripcion_fechai,fechaf=a.descripcion_fechaf,documento=a.descripcion_documento,
                              ci_invitado=a.descripcion_ci_invitado,nombre_invitado=a.descripcion_nombre_invitado,
                              nombre_conductor=a.descripcion_nombre_conductor,cantpasajeros=a.cantpasajeros,
                              placa=a.descripcion_placa,tipo=a.descripcion_tipo,marca=a.descripcion_marca,modelo=a.descripcion_modelo,
                              color=a.descripcion_color,destino=a.descripcion_destino,autorizacion=a.autorizacion.nombre,
                              nropase=a.descripcion_nropase,tipopase=a.tipopase.nombre,observacion=a.observacion))



        print("retorno de movimientos :" + str(len(lista)))
        return lista

