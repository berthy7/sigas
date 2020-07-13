from .models import *
from ..invitado.managers import *
from ..residente.managers import *
from ..evento.managers import *
from ..areasocial.managers import *
from ..nropase.managers import *
from ..vehiculo.managers import *
from sqlalchemy import or_
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font


class PorterovirtualManager(SuperManager):
    def __init__(self, db):
        super().__init__(Porterovirtual, db)

    def get_all(self):
        return self.db.query(self.entity)

    def get_all_by_lastname(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.apellidopaterno.asc()).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.tipo == "Vehicular"))

    def listar_movimiento_dia(self,usuario):

        fecha = datetime.now(pytz.timezone('America/La_Paz'))
        fechahoy = str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)
        fechahoy = datetime.strptime(fechahoy, '%d/%m/%Y')


        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.fechar.cast(Date) == fechahoy).all()
        else:

            domicilio = self.db.query(self.entity).filter(self.entity.estado == True).join(Residente).filter(Residente.fkcondominio== usuario.fkcondominio)\
                .filter(self.entity.fechar.cast(Date) == fechahoy).all()

            return domicilio


    def list_all_reporte(self):
        return self.db.query(self.entity).filter(self.entity.tipo == "Vehicular").all()

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def insert(self, diccionary):

        if diccionary['fkinvitado'] == "" or diccionary['fkinvitado'] == "0":
            if diccionary['ci'] != "":
                invitado = InvitadoManager(self.db).registrar_invitado(diccionary)
                diccionary['fkinvitado'] = invitado.id
            else:
                diccionary['fkinvitado'] = None

        else:
            invitado = InvitadoManager(self.db).actualizar_invitado(diccionary)


        if diccionary['fkinvitacion'] == "":
            diccionary['fkinvitacion'] = None


        if diccionary['fkresidente'] == "":
            diccionary['fkresidente'] = None


        fecha = BitacoraManager(self.db).fecha_actual()

        diccionary['tipo'] = "Visita"
        diccionary['fechar'] = fecha
        # diccionary['fechai'] = fecha

        objeto = PorterovirtualManager(self.db).entity(**diccionary)

        a = super().insert(objeto)
        print("registro Ingreso portero virtual: " +str(a.id))
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro portero virtual.", fecha=fecha,tabla="portero_virtual", identificador=a.id)
        super().insert(b)

        abrir = dict(cerradura=a.cerradura.numero,id=a.cerradura.dispositivo.id)
        ConfiguraciondispositivoManager(self.db).abrir_cerradura(abrir)

        # deshabilitar invitacion
        if a.fkinvitacion:
            InvitacionManager(self.db).delete(a.fkinvitacion, False, objeto.user, objeto.ip)

        return a

    def update(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()
        objeto.fechanacimiento = datetime.strptime(objeto.fechanacimiento, '%d/%m/%Y')

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Porterovirtual.", fecha=fecha,tabla="residente", identificador=a.id)
        super().insert(b)
        return a

    def salida(self, id, user, ip):
        x = self.db.query(Porterovirtual).filter(Porterovirtual.id == id).first()
        fecha = BitacoraManager(self.db).fecha_actual()
        if x.fechai is None:
            x.fechai = x.fechar
        x.fechaf = fecha


        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Registro Salida", fecha=fecha, tabla="movimiento", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

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
                self.entity.tipo == "Visita").all()
        else:
            domicilio = self.db.query(self.entity).join(Domicilio).filter(Domicilio.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Visita").filter(self.entity.estado == True).all()

            areasocial = self.db.query(self.entity).join(Areasocial).filter(Areasocial.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Visita").filter(self.entity.estado == True).all()

            for area in areasocial:
                domicilio.append(area)

            return domicilio


    def filtrar_movil(self, fechainicio, fechafin,usuario):
        usuario = UsuarioManager(self.db).get_by_pass(usuario)

        list = {}
        c = 0

        fecha = fecha_zona
        fechahoy = str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)
        fechahoy = datetime.strptime(fechahoy, '%d/%m/%Y')


        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).all()
        else:
            domicilio = self.db.query(self.entity).filter(self.entity.estado == True).join(Domicilio).filter(Domicilio.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).all()

            areasocial = self.db.query(self.entity).filter(self.entity.estado == True).join(Areasocial).filter(Areasocial.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).all()

            for area in areasocial:
                domicilio.append(area)

            return domicilio


    def actualizar_marcacion(self, marcacion):

        mov = self.db.query(Porterovirtual).join(Cerraduras).filter(Porterovirtual.sincronizacion == True).filter(Cerraduras.numero == marcacion.puerta).filter(
                or_(Porterovirtual.fechai == None,Porterovirtual.fechaf == None)).first()
        if mov:
            if not mov.fechai:
                mov.fechai = marcacion.time
                mov.sincronizacion = True

                self.db.merge(mov)
                self.db.commit()
            elif not mov.fechaf:
                mov.fechaf = marcacion.time


        marcacion.sincronizado =True

        return marcacion
