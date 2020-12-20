from .models import *
from ..invitado.managers import *
from ..residente.managers import *
from ..evento.managers import *
from ..areasocial.managers import *
from ..nropase.managers import *
from ..vehiculo.managers import *
from sqlalchemy import or_,and_
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font


class MovimientoManager(SuperManager):
    def __init__(self, db):
        super().__init__(Movimiento, db)

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
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.fechar.cast(Date) == fechahoy).filter(
                self.entity.tipo == "Vehicular").order_by(self.entity.id.desc()).all()
        else:

            domicilio = self.db.query(self.entity).filter(self.entity.estado == True).join(Domicilio).filter(Domicilio.fkcondominio== usuario.fkcondominio).filter(self.entity.fechar.cast(Date) == fechahoy).filter(
                self.entity.tipo == "Vehicular").order_by(self.entity.id.desc()).all()

            areasocial = self.db.query(self.entity).filter(self.entity.estado == True).join(Areasocial).filter(Areasocial.fkcondominio== usuario.fkcondominio).filter(self.entity.fechar.cast(Date) == fechahoy).filter(
                self.entity.tipo == "Vehicular").order_by(self.entity.id.desc()).all()

            for area in areasocial:
                domicilio.append(area)

            return domicilio


    def list_all_reporte(self):
        return self.db.query(self.entity).filter(self.entity.tipo == "Vehicular").all()

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def insert(self, diccionary):

        diccionary['cantpasajeros'] = abs(int(diccionary['cantpasajeros']))

        diccionary['placa'] = diccionary['placa'].replace(" ", "")

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
                    if diccionary['nombre'] != "":
                        invitado = InvitadoManager(self.db).registrar_invitado(diccionary)
                        diccionary['fkinvitado'] = invitado.id
                    else:
                        diccionary['fkinvitado'] = None

                else:
                    invitado = InvitadoManager(self.db).actualizar_invitado(diccionary)
            else:
                diccionary['fkinvitado'] = None


            if diccionary['fkconductor'] == "" or diccionary['fkconductor'] == "0":
                diccionary['nombre_conductor'] = diccionary['nombre_conductor'].replace(" ", "")
                if diccionary['nombre_conductor'] != "":
                    conductor = InvitadoManager(self.db).registrar_conductor(diccionary)
                    diccionary['fkconductor'] = conductor.id
                else:
                    diccionary['fkconductor'] = None
            else:
                conductor = InvitadoManager(self.db).registrar_conductor(diccionary)


            if diccionary['fkvehiculo'] == "" or diccionary['fkvehiculo'] == "0":
                vehiculo = VehiculoManager(self.db).registrar_vehiculo(diccionary)
                diccionary['fkvehiculo'] = vehiculo


        if diccionary['fktipodocumento_conductor'] == "":
            diccionary['fktipodocumento_conductor'] = None

        if diccionary['fkdomicilio'] == "":
            diccionary['fkdomicilio'] = None

        if diccionary['fkareasocial'] == "":
            diccionary['fkareasocial'] = None

        if diccionary['fkmodelo'] == "":
            diccionary['fkmodelo'] = None

        if diccionary['fkmarca'] == "":
            diccionary['fkmarca'] = None
        elif diccionary['fkmarca'] == "0":
            diccionary['fkmarca'] = None

        if diccionary['cantpasajeros'] == "":
            diccionary['cantpasajeros'] = None

        try:
            if diccionary['fkresidente'] == "":
                diccionary['fkresidente'] = None

        except Exception as e:
            print("no se envio fkresidente")

            diccionary['fkresidente'] = None


        fecha = BitacoraManager(self.db).fecha_actual()

        diccionary['tipo'] = "Vehicular"
        diccionary['fechar'] = fecha
        # diccionary['fechai'] = fecha

        objeto = MovimientoManager(self.db).entity(**diccionary)

        a = super().insert(objeto)
        print("registro ingreso Vehicular: " +str(a.id))
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Movimiento.", fecha=fecha,tabla="movimiento", identificador=a.id)
        super().insert(b)


        if a.fknropase:
            # actualizar siuacion
            NropaseManager(self.db).situacion(a.fknropase, "Ocupado")

        # deshabilitar invitacion
        if a.fkinvitacion:

            if accesos_invitacion['multiacceso'] is False:
                if accesos_invitacion['multiple'] is False:
                    if accesos_invitacion['paselibre'] is False:
                        InvitacionManager(self.db).delete(a.fkinvitacion, False, objeto.user, objeto.ip)


        return a

    def update(self, objeto):
        fecha = BitacoraManager(self.db).fecha_actual()
        objeto.fechanacimiento = datetime.strptime(objeto.fechanacimiento, '%d/%m/%Y')

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Movimiento.", fecha=fecha,tabla="residente", identificador=a.id)
        super().insert(b)
        return a

    def salida(self, id, user, ip):
        x = self.db.query(Movimiento).filter(Movimiento.id == id).first()
        fecha = BitacoraManager(self.db).fecha_actual()
        if x.fechai is None:
            x.fechai = x.fechar
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
                self.entity.tipo == "Vehicular").all()
        else:
            domicilio = self.db.query(self.entity).join(Domicilio).filter(Domicilio.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Vehicular").filter(self.entity.estado == True).all()

            areasocial = self.db.query(self.entity).join(Areasocial).filter(Areasocial.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Vehicular").filter(self.entity.estado == True).all()

            for area in areasocial:
                domicilio.append(area)

            return domicilio


    def filtrar_movil(self, fechainicio, fechafin,usuario):

        list = {}
        c = 0

        fecha = fecha_zona
        fechahoy = str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)
        # fechahoy = datetime.strptime(fechahoy, '%d/%m/%Y')

        if fechainicio == "undefined":
            fechainicio = fechahoy
            fechafin = fechahoy



        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).all()
        else:
            domicilio = self.db.query(self.entity).filter(self.entity.estado == True).join(Domicilio).filter(Domicilio.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).all()

            areasocial = self.db.query(self.entity).filter(self.entity.estado == True).join(Areasocial).filter(Areasocial.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).all()

            for area in areasocial:
                domicilio.append(area)

            return domicilio


    def actualizar_movimiento(self, marcacion):

        mov = self.db.query(Movimiento).join(Nropase).filter(Movimiento.estado == True).filter(Nropase.tarjeta == marcacion.tarjeta).filter(
                or_(Movimiento.fechai == None,Movimiento.fechaf == None)).first()
        if mov:
            if not mov.fechai:
                mov.fechai = marcacion.time

                if mov.nropase.tipo == "Excepcion":
                    mov.fechaf = marcacion.time

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

    def movimiento_excel(self):

        codigo = BitacoraManager(self.db).generar_codigo()

        cname = "movimiento_"+codigo+".xlsx"

        movimientos = self.db.query(self.entity).order_by(self.entity.id.asc()).all()

        wb = Workbook()
        ws = wb.active
        ws.title = 'a'

        indice = 1

        ws['A' + str(indice)] = 'ID'
        ws['B' + str(indice)] = 'Fecha Registro'
        ws['C' + str(indice)] = 'Fecha Ingreso'
        ws['D' + str(indice)] = 'Fecha Salida'
        ws['E' + str(indice)] = 'Tipo documento'
        ws['F' + str(indice)] = 'Nº documento'
        ws['G' + str(indice)] = 'Expedido documento'
        ws['H' + str(indice)] = 'Nombre Invitado'
        ws['I' + str(indice)] = 'Apellidop Invitado'
        ws['J' + str(indice)] = 'Apellidom Invitado'
        ws['K' + str(indice)] = 'Nº documento conductor'
        ws['L' + str(indice)] = 'Nombre Conductor'
        ws['M' + str(indice)] = 'Apellidop Conductor'
        ws['N' + str(indice)] = 'Apellidom Conductor'
        ws['O' + str(indice)] = 'Cant. Pasajeros'
        ws['P' + str(indice)] = 'Placa'
        ws['Q' + str(indice)] = 'Tipo vehiculo'
        ws['R' + str(indice)] = 'Marca'
        ws['S' + str(indice)] = 'Modelo'
        ws['T' + str(indice)] = 'Color'
        ws['U' + str(indice)] = 'Destino'
        ws['V' + str(indice)] = 'Autorizacion'
        ws['W' + str(indice)] = 'Tipo de pase'
        ws['X' + str(indice)] = 'Observacion'
        ws['Y' + str(indice)] = 'Tipo'

        for i in movimientos:

            if i.fkinvitado:
                print("movimiento exportar: "+ str(i.id))

                indice = indice + 1
                ws['A' + str(indice)] = i.id
                ws['B' + str(indice)] = i.fechar
                ws['C' + str(indice)] = i.fechai
                ws['D' + str(indice)] = i.fechaf
                ws['E' + str(indice)] = i.fktipodocumento

                ws['F' + str(indice)] = i.invitado.ci
                ws['G' + str(indice)] = i.invitado.expendido
                ws['H' + str(indice)] = i.invitado.nombre
                ws['I' + str(indice)] = i.invitado.apellidop
                ws['J' + str(indice)] = i.invitado.apellidom

                if i.fkconductor:

                    ws['K' + str(indice)] = i.conductor.ci
                    ws['L' + str(indice)] = i.conductor.nombre
                    ws['M' + str(indice)] = i.conductor.apellidop
                    ws['N' + str(indice)] = i.conductor.apellidom

                else:
                    ws['K' + str(indice)] = None
                    ws['L' + str(indice)] = None
                    ws['M' + str(indice)] = None
                    ws['N' + str(indice)] = None

                ws['O' + str(indice)] = i.cantpasajeros
                if i.tipo == "Vehicular":

                    ws['P' + str(indice)] = i.vehiculo.placa
                    ws['Q' + str(indice)] = i.vehiculo.tipo.nombre
                    ws['R' + str(indice)] = i.vehiculo.marca.nombre
                    ws['S' + str(indice)] = None
                    ws['T' + str(indice)] = i.vehiculo.color.nombre
                else:
                    ws['P' + str(indice)] = None
                    ws['Q' + str(indice)] = None
                    ws['R' + str(indice)] = None
                    ws['S' + str(indice)] = None
                    ws['T' + str(indice)] = None


                ws['U' + str(indice)] = i.domicilio.codigo
                ws['V' + str(indice)] = i.autorizacion.nombre
                ws['W' + str(indice)] = i.tipopase.nombre
                ws['X' + str(indice)] = i.observacion
                ws['Y' + str(indice)] = i.tipo


        wb.save("server/common/resources/downloads/" + cname)
        return cname

    def importar_excel(self, cname, user, ip):
        try:
            wb = load_workbook(filename="server/common/resources/uploads/" + cname)
            ws = wb.active
            colnames = ['ID', 'Fecha Registro', 'Fecha Ingreso', 'Fecha Salida', 'Tipo documento', 'Nº documento', 'Expedido documento', 'Nombre Invitado', 'Apellidop Invitado',
                        'Apellidom Invitado',
                        'Nº documento conductor',
                        'Nombre Conductor',
                        'Apellidop Conductor',
                        'Apellidom Conductor',
                        'Cant. Pasajeros',
                        'Placa',
                        'Tipo vehiculo',
                        'Marca',
                        'Modelo',
                        'Color',
                        'Destino',
                        'Autorizacion',
                        'Tipo de pase',
                        'Observacion',
                        'Tipo']
            indices = {cell[0].value: n - 1 for n, cell in enumerate(ws.iter_cols(min_row=1, max_row=1), start=1) if
                       cell[0].value in colnames}
            if len(indices) == len(colnames):
                for row in ws.iter_rows(min_row=2):

                    id = row[indices['ID']].value

                    ci = row[indices['Nº documento']].value
                    expedido = row[indices['Expedido documento']].value
                    nombre = row[indices['Nombre Invitado']].value
                    apellidop = row[indices['Apellidop Invitado']].value
                    apellidom = row[indices['Apellidom Invitado']].value

                    ci_conductor = row[indices['Nº documento conductor']].value
                    nombre_conductor = row[indices['Nombre Conductor']].value
                    apellidop_conductor = row[indices['Apellidop Conductor']].value
                    apellidom_conductor = row[indices['Apellidom Conductor']].value


                    if row[indices['ID']].value is not None:

                        print("movimiento import: " + str(row[indices['ID']].value))

                        fkinvitado = None
                        fkconductor = None
                        fkvehiculo = None


                        query_invitado = self.db.query(Invitado).filter(and_(Invitado.ci == ci,Invitado.nombre == nombre,Invitado.apellidop== apellidop,Invitado.apellidom == apellidom)).first()

                        if query_invitado :
                            print("existe invitado")
                            fkinvitado = query_invitado.id

                        else:
                            invi = Invitado(nombre=nombre, apellidop=apellidop, apellidom=apellidom,
                                            ci=ci, expendido=expedido)

                            self.db.add(invi)
                            self.db.flush()

                            fkinvitado = invi.id


                        if nombre_conductor:
                            query_conductor = self.db.query(Invitado).filter(and_(Invitado.ci == ci_conductor,Invitado.nombre == nombre_conductor,Invitado.apellidop== apellidop_conductor,
                                                                                  Invitado.apellidom == apellidom_conductor)).first()

                            if query_conductor :
                                print("existe conductor")
                                fkconductor = query_conductor.id

                            else:
                                condu = Invitado(nombre=nombre_conductor, apellidop=apellidop_conductor, apellidom=apellidom_conductor,
                                                ci=ci_conductor, expendido=expedido)

                                self.db.add(condu)
                                self.db.flush()

                                fkconductor = condu.id

                        if row[indices['Placa']].value:

                            dict_vehiculo = VehiculoManager(self.db).obtener_vehiculo(row[indices['Placa']].value, row[indices['Color']].value, row[indices['Tipo vehiculo']].value, row[indices['Marca']].value,
                                                                                      row[indices['Modelo']].value, '')

                            if dict_vehiculo['id'] != "":
                                print("existe vehiculo")
                                fkvehiculo = dict_vehiculo['id']

                            else:
                                dict_vehiculo['id'] = None

                                vehi = Vehiculo(placa=dict_vehiculo['placa'], fkcolor=dict_vehiculo['fkcolor'], fktipo=dict_vehiculo['fktipo'], fkmarca=dict_vehiculo['fkmarca'], fkmodelo=dict_vehiculo['fkmodelo'])

                                self.db.add(vehi)
                                self.db.flush()

                                fkvehiculo = vehi.id


                        query_domicilio = self.db.query(Domicilio).filter(Domicilio.codigo == row[indices['Destino']].value).first()

                        if query_domicilio:
                            result_domicilio =query_domicilio.id
                            result_areasocial = None
                        else:
                            query_areasocial = self.db.query(Areasocial).filter(Areasocial.codigo == row[indices['Destino']].value).first()

                            if query_areasocial:
                                result_domicilio = None
                                result_areasocial = query_areasocial.id

                            else:
                                result_domicilio = None
                                result_areasocial = None


                        query_domicilio = self.db.query(Domicilio).filter(Domicilio.codigo == row[indices['Destino']].value).first()

                        query_tipo_pase = self.db.query(Tipopase).filter(Tipopase.nombre == row[indices['Tipo de pase']].value).first()

                        query_autorizacion = self.db.query(Autorizacion).filter(Autorizacion.nombre == row[indices['Autorizacion']].value).first()

                        movi = Movimiento(fktipodocumento=row[indices['Tipo documento']].value,
                                          fkinvitado=fkinvitado, fkvehiculo=fkvehiculo,
                                          fechai=row[indices['Fecha Ingreso']].value, fechaf=row[indices['Fecha Salida']].value, fechar=row[indices['Fecha Registro']].value, fkautorizacion=query_autorizacion.id,
                                          fkdomicilio=result_domicilio, fkareasocial=result_areasocial, fktipopase=query_tipo_pase.id, observacion=row[indices['Observacion']].value, tipo=row[indices['Tipo']].value,
                                          cantpasajeros=row[indices['Cant. Pasajeros']].value,fktipodocumento_conductor=None,fkconductor=fkconductor)

                        self.db.merge(movi)
                        self.db.flush()

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


    def recargar(self, fechainicio, fechafin,usuario,ult_registro):

        list = {}
        c = 0

        if usuario.sigas:
            return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.id > ult_registro).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Vehicular").order_by(self.entity.id.desc()).all()
        else:
            domicilio = self.db.query(self.entity).join(Domicilio).filter(self.entity.id > ult_registro).filter(Domicilio.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Vehicular").filter(self.entity.estado == True).order_by(self.entity.id.desc()).all()

            areasocial = self.db.query(self.entity).join(Areasocial).filter(self.entity.id > ult_registro).filter(Areasocial.fkcondominio== usuario.fkcondominio).filter(func.date(self.entity.fechar).between(fechainicio, fechafin)).filter(
                self.entity.tipo == "Vehicular").filter(self.entity.estado == True).order_by(self.entity.id.desc()).all()

            for area in areasocial:
                domicilio.append(area)

            return domicilio


class TipopaseManager(SuperManager):
    def __init__(self, db):
        super().__init__(Tipopase, db)

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()


class TipodocumentoManager(SuperManager):
    def __init__(self, db):
        super().__init__(Tipodocumento, db)

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()


class AutorizacionManager(SuperManager):
    def __init__(self, db):
        super().__init__(Autorizacion, db)

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.id.asc()).all()