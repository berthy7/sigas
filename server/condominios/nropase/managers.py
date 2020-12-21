from .models import *
from ...common.managers import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ...usuarios.usuario.managers import *
from ..residente.managers import *
from ..condominio.models import *
from sqlalchemy import or_
from sqlalchemy import and_
from ..modelo.models import *

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font



class NropaseManager(SuperManager):

    def __init__(self, db):
        super().__init__(Nropase, db)


    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()


    def obtener_x_tarjeta(self,tarjeta):
        return self.db.query(self.entity).filter(self.entity.tarjeta == tarjeta).filter(self.entity.estado == True).first()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.estado == True))

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def listar_x_condominio(self, idcondominio):
        x = self.db.query(self.entity).join(CondominioPases).filter(CondominioPases.fkcondominio == idcondominio).filter(self.entity.estado == True).all()
        return x


    def listar_x_tipo(self, usuario,tipopase):


        if usuario.sigas:

            if tipopase == "Proveedor" or tipopase == "Taxi":
                return self.db.query(self.entity).filter(self.entity.estado == True).filter(
                    and_(self.entity.tipo != "Residente", self.entity.tipo != "Provper", self.entity.tipo != "Visita")).filter(
                    self.entity.situacion != "Ocupado").order_by(
                    self.entity.numero.asc()).all()
            else:
                return self.db.query(self.entity).filter(self.entity.estado == True).filter(
                    and_(self.entity.tipo != "Residente", self.entity.tipo != "Provper", self.entity.tipo != "Proveedor")).filter(
                    self.entity.situacion != "Ocupado").order_by(
                    self.entity.numero.asc()).all()


        if usuario.rol.nombre != "RESIDENTE":

            if tipopase == "Proveedor" or tipopase == "Taxi":

                return self.db.query(Nropase).join(CondominioPases).join(Condominio).filter(
                    Condominio.id == usuario.fkcondominio).filter(
                    and_(self.entity.tipo != "Residente", self.entity.tipo != "Provper", self.entity.tipo != "Visita")).filter(Nropase.estado == True).filter(
                    self.entity.situacion != "Ocupado").order_by(Nropase.numero.asc()).all()
            else:
                return self.db.query(Nropase).join(CondominioPases).join(Condominio).filter(
                    Condominio.id == usuario.fkcondominio).filter(
                    and_(self.entity.tipo != "Residente", self.entity.tipo != "Provper", self.entity.tipo != "Proveedor")).filter(Nropase.estado == True).filter(
                    self.entity.situacion != "Ocupado").order_by(Nropase.numero.asc()).all()

        else:
            return None

    def listar_numero_pases(self,usuario):

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(and_(self.entity.tipo != "Residente",self.entity.tipo != "Provper")).filter(self.entity.situacion != "Ocupado").order_by(
                self.entity.numero.asc()).all()

        if usuario.rol.nombre != "RESIDENTE":
            return self.db.query(Nropase).join(CondominioPases).join(Condominio).filter(Condominio.id == usuario.fkcondominio).filter(and_(Nropase.tipo != "Residente",Nropase.tipo != "Provper")).filter(Nropase.estado == True).filter(Nropase.situacion != "Ocupado").order_by(Nropase.numero.asc()).all()

        else:
            return None

    def listar_numero_pases_residente(self,usuario):

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.tipo == "Residente").filter(self.entity.situacion != "Ocupado").order_by(
                self.entity.numero.asc()).all()

        if usuario.rol.nombre != "RESIDENTE":
            return self.db.query(Nropase).join(CondominioPases).join(Condominio).filter(Condominio.id == usuario.fkcondominio).filter(Nropase.tipo == "Residente").filter(Nropase.estado == True).filter(self.entity.situacion != "Ocupado").order_by(Nropase.numero.asc()).all()

        else:
            return None

    def listar_tarjetas_provper(self,usuario):

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.tipo == "Provper").filter(self.entity.situacion != "Ocupado").order_by(
                self.entity.numero.asc()).all()

        if usuario.rol.nombre != "RESIDENTE":
            return self.db.query(Nropase).join(CondominioPases).join(Condominio).filter(Condominio.id == usuario.fkcondominio).filter(Nropase.tipo == "Provper").filter(Nropase.estado == True).filter(self.entity.situacion != "Ocupado").order_by(Nropase.numero.asc()).all()

        else:
            return None

    def listar_todo_condominio(self):
        list = {}
        vector = []
        c = 0

        objeto = self.db.query(self.entity).filter(self.entity.estado == True).all()

        for x in objeto:

            list[c] = dict(gestion=x.fecha.year)

            c = c + 1
            vector.append(x.fecha.year)

        return list


    def insert(self, diccionary):
        if diccionary['tipo'] == "":
            diccionary['tipo'] = "Visita"

        objeto = NropaseManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Nropase.", fecha=fecha,tabla="nropase", identificador=a.id)
        super().insert(b)
        return a

    def update(self, diccionary):
        objeto = NropaseManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Nropase.", fecha=fecha,tabla="nropase", identificador=a.id)
        super().insert(b)
        return a

    def delete(self, id,estado, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.estado = estado
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Eliminó Nropase.", fecha=fecha, tabla="nropase", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return x

    def situacion(self, id,situacion):
        x = self.db.query(Nropase).filter(Nropase.id == id).first()
        if x.tipo != "Excepcion":
            if x:
                x.situacion = situacion

                self.db.merge(x)
                self.db.commit()

        return x


    def importar_excel(self, cname,user,ip):
        try:
            wb = load_workbook(filename="server/common/resources/uploads/" + cname)
            ws = wb.active
            colnames = ['NUMERO_DE_PASE','TARJETA','TIPO','COD_CONDOMINIO']
            indices = {cell[0].value: n - 1 for n, cell in enumerate(ws.iter_cols(min_row=1, max_row=1), start=1) if
                       cell[0].value in colnames}
            if len(indices) == len(colnames):
                for row in ws.iter_rows(min_row=2):

                    nropase = row[indices['NUMERO_DE_PASE']].value
                    tarjeta = row[indices['TARJETA']].value
                    tipo = row[indices['TIPO']].value
                    cod_condominio = row[indices['COD_CONDOMINIO']].value

                    if tarjeta is not None:
                        if cod_condominio:
                            cod_condominio = cod_condominio.replace(" ", "")

                        list_condominio = list()

                        query = self.db.query(Nropase).filter(Nropase.tarjeta == str(tarjeta)).first()
                        query_condominio = self.db.query(Condominio).filter(
                            Condominio.codigo == str(cod_condominio)).first()

                        if not query:

                            if tipo:
                                tipo = tipo.replace(" ", "")

                            if tipo is None or tipo == "":
                                tipo = "Invitacion"


                            if nropase is None or nropase == "":
                                nropase = " "


                            if query_condominio:
                                list_condominio.append(dict(fkcondominio=query_condominio.id))

                            mode = Nropase(numero=str(nropase),tarjeta=str(tarjeta),tipo=str(tipo),condominios=list_condominio)
                            self.db.add(mode)
                            self.db.commit()

                        else:
                            query_cond = self.db.query(Nropase).join(CondominioPases).join(Condominio).filter(
                                Condominio.codigo == str(cod_condominio)).filter(
                                Nropase.tarjeta == str(tarjeta)).first()

                            if not query_cond:

                                if query_condominio:
                                    mode = CondominioPases(fknropase=query.id, fkcondominio=query_condominio.id)
                                    self.db.add(mode)
                                    self.db.commit()

                    else:

                        self.db.rollback()
                        return {'message': 'Hay Columnas vacias', 'success': False}

                self.db.commit()
                return {'message': 'Importado Todos Correctamente.', 'success': True}
            else:
                return {'message': 'Columnas Faltantes', 'success': False}
        except IntegrityError as e:
            self.db.rollback()
            if 'UNIQUE constraint' in str(e):
                return {'message': 'duplicado', 'success': False}
            if 'UNIQUE constraint failed' in str(e):
                return {'message': 'codigo duplicado', 'success': False}
            return {'message': str(e), 'success': False}

