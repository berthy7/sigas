from .models import *
from sqlalchemy.exc import IntegrityError
from ...common.managers import *
from ...operaciones.bitacora.managers import *
from ..domicilio.managers import *
from ..condominio.models import *
from ..vehiculo.managers import *
from ..nropase.managers import *


from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font


class ResidenteManager(SuperManager):
    def __init__(self, db):
        super().__init__(Residente, db)

    def get_all(self):
        return self.db.query(self.entity)

    def get_all_by_lastname(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.apellidop.asc()).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity))

    def listar_todo(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.apellidop.asc()).all()

    def insert(self, diccionary):
        estado = diccionary['acceso'][0]['estado']
        if diccionary['b_fknropase'] == "0":
            if diccionary['fknropase']:
                NropaseManager(self.db).situacion(diccionary['fknropase'], "Libre")
                diccionary['fknropase'] = None

        if diccionary['fknropase'] == "":
            diccionary['fknropase'] = None

        objeto = ResidenteManager(self.db).entity(**diccionary)
        objeto.fechanacimiento = datetime.strptime(objeto.fechanacimiento, '%d/%m/%Y')
        for acce in objeto.acceso:
            acce.fechai = datetime.strptime(acce.fechai, '%d/%m/%Y')
            acce.fechaf = datetime.strptime(acce.fechaf, '%d/%m/%Y')

        fecha = BitacoraManager(self.db).fecha_actual()
        objeto.vehiculos = []
        objeto.estado = estado

        objeto.codigoqr = str(objeto.codigo) + str(objeto.ci)


        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Residente.", fecha=fecha,tabla="residente", identificador=a.id)
        super().insert(b)

        if a.fknropase:
            NropaseManager(self.db).situacion(a.fknropase, "Ocupado")

        for vehi in diccionary['vehiculos']:
            VehiculoManager(self.db).registrar_vehiculo_residente(vehi,a.id)

        idcondominio=None

        for domi in a.domicilios:
            if domi.vivienda:
                d = domi.fkdomicilio
                idcondominio = DomicilioManager(self.db).obtener_fkcondominio(d)
                break

        dict_usuario = dict(nombre=a.nombre,apellidop=a.apellidop,apellidom=a.apellidom,ci=a.ci,expendido=a.expendido,correo=a.correo,telefono=a.telefono,username=a.ci,password="residente2020",fkrol=7,fkresidente=a.id, fkcondominio=idcondominio,sigas=False,user_id=objeto.user,ip=objeto.ip,enabled=estado)
        UsuarioManager(self.db).insert(dict_usuario)

        return a

    def update(self, diccionary):
        estado = diccionary['acceso'][0]['estado']

        if diccionary['b_fknropase'] == "0":
            if diccionary['fknropase']:
                NropaseManager(self.db).situacion(diccionary['fknropase'], "Libre")
                diccionary['fknropase'] = None
            else:
                diccionary['fknropase'] = None

        if diccionary['fknropase'] == "":
            diccionary['fknropase'] = None

        if diccionary['actual_fknropase'] != diccionary['fknropase']:
            if diccionary['actual_fknropase'] != "":
                NropaseManager(self.db).situacion(diccionary['actual_fknropase'], "Libre")


        for vehi in diccionary['vehiculos']:
            vehiculo = VehiculoManager(self.db).registrar_vehiculo_residente(vehi,diccionary['id'])
            if vehiculo:
                vehi['id'] = vehiculo.id

        objeto = ResidenteManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()
        objeto.fechanacimiento = datetime.strptime(objeto.fechanacimiento, '%d/%m/%Y')
        for acce in objeto.acceso:
            acce.fechai = datetime.strptime(acce.fechai, '%d/%m/%Y')
            acce.fechaf = datetime.strptime(acce.fechaf, '%d/%m/%Y')

        objeto.estado = estado

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Residente.", fecha=fecha,tabla="residente", identificador=a.id)
        super().insert(b)

        if a.fknropase:
            NropaseManager(self.db).situacion(a.fknropase, "Ocupado")

        use = self.db.query(Usuario).filter(Usuario.fkresidente == a.id).first()
        use.enabled = estado
        self.db.merge(use)
        self.db.commit()


        return a

    def delete(self, id, user, ip, state):
        x = self.db.query(Residente).filter(Residente.id == id).one()
        x.estado = state
        if state:
            mensaje = "Habilito Residente"
        else:
            mensaje = "Deshabilito Residente"

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion=mensaje, fecha=fecha, tabla="residente", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return mensaje

    def importar_excel(self, cname,user,ip):
        i = 0
        try:
            wb = load_workbook(filename="server/common/resources/uploads/" + cname)
            ws = wb.active
            colnames = ['CODIGO', 'NOMBRE','APELLIDOP','APELLIDOM', 'CI', 'UBICACION', 'SEXO', 'FECHANACIMIENTO', 'TELEFONO', 'TIPO', 'CORREO',
                        'DOMICILIO','NUMERO','TARTEJAPEATONAL', 'PLACA', 'COLOR', 'TIPOVEHICULO', 'MARCA', 'MODELO', 'TARJETAVEHICULAR', 'FECHAI', 'FECHAF']
            indices = {cell[0].value: n - 1 for n, cell in enumerate(ws.iter_cols(min_row=1, max_row=1), start=1) if
                       cell[0].value in colnames}
            if len(indices) == len(colnames):
                for row in ws.iter_rows(min_row=2):
                    codigo = row[indices['CODIGO']].value
                    nombre =  row[indices['NOMBRE']].value
                    apellidop = row[indices['APELLIDOP']].value
                    apellidom = row[indices['APELLIDOM']].value
                    ci = row[indices['CI']].value
                    ubicacion = row[indices['UBICACION']].value
                    sexo = row[indices['SEXO']].value
                    fechanacimiento = row[indices['FECHANACIMIENTO']].value
                    telefono =  row[indices['TELEFONO']].value
                    tipo =  row[indices['TIPO']].value
                    correo = row[indices['CORREO']].value
                    domicilio =  row[indices['DOMICILIO']].value
                    numero = row[indices['NUMERO']].value
                    tarjetapeatonal = row[indices['TARTEJAPEATONAL']].value
                    placa = row[indices['PLACA']].value
                    color = row[indices['COLOR']].value
                    tipovehiculo = row[indices['TIPOVEHICULO']].value
                    marca =  row[indices['MARCA']].value
                    modelo =  row[indices['MODELO']].value
                    tarjetavehicular = row[indices['TARJETAVEHICULAR']].value
                    fechai =  row[indices['FECHAI']].value
                    fechaf = row[indices['FECHAF']].value

                    fechanacimiento = fechanacimiento.strftime('%d/%m/%Y')
                    fechai = fechai.strftime('%d/%m/%Y')
                    fechaf = fechaf.strftime('%d/%m/%Y')


                    if codigo is not None and nombre is not None and domicilio is not None and numero is not None:
                        print(codigo)
                        query = self.db.query(self.entity).filter(
                            self.entity.codigo == str(codigo)).filter(
                            self.entity.ci == str(ci)).all()

                        list_domicilio = list()
                        list_vehiculo = list()
                        list_acceso = list()

                        domicilio = domicilio.replace(" ", "")

                        query_domicilio = self.db.query(Domicilio).filter(Domicilio.ubicacion == str(domicilio)).filter(Domicilio.numero == str(numero)).first()

                        if query_domicilio:
                            if not query:
                                dict_vehiculo = VehiculoManager(self.db).obtener_vehiculo(placa, color, tipovehiculo,marca, modelo,tarjetavehicular)
                                list_domicilio.append(dict(fkdomicilio=query_domicilio.id, vivienda=True))
                                if dict_vehiculo != "":
                                    list_vehiculo.append(dict_vehiculo)

                                query_tarjeta = self.db.query(Nropase).filter(Nropase.tarjeta == str(tarjetapeatonal)).first()

                                if query_tarjeta:
                                    idtarjeta = query_tarjeta.id
                                else:
                                    idtarjeta = None

                                list_acceso.append(dict(fechai=fechai, fechaf=fechaf, estado=True))
                                residente = dict(codigo=str(codigo),
                                                  nombre=str(nombre),
                                                  apellidop=str(apellidop),
                                                  apellidom=str(apellidom),
                                                  ci=str(ci),
                                                  expendido=str(ubicacion),
                                                  sexo=str(sexo),
                                                  fechanacimiento=fechanacimiento,
                                                  telefono=str(telefono),
                                                  tipo=str(tipo),
                                                  correo=str(correo),
                                                  fknropase=idtarjeta,
                                                  b_fknropase=idtarjeta,
                                                  domicilios= list_domicilio,
                                                  vehiculos= list_vehiculo,
                                                  acceso=list_acceso,
                                                  user=user,
                                                  ip=ip)

                                ResidenteManager(self.db).insert(residente)
                                # self.db.merge(propietario)
                                # self.db.flush()
                    else:

                        self.db.rollback()
                        return {'message': 'Hay Columnas vacias', 'success': False}

                self.db.commit()
                return {'message': 'Importado Todos Correctamente.', 'success': True}
            else:
                return {'message': 'Columnas Faltantes', 'success': False}
        except IntegrityError as e:
            self.db.rollback()
            if 'UNIQUE constraint failed: residente.ci' in str(e):
                return {'message': 'CI duplicado', 'success': False}
            if 'UNIQUE constraint failed: residente.codigo' in str(e):
                return {'message': 'codigo de residente', 'success': False}
            return {'message': str(e), 'success': False}


    def persona_excel(self, empleados):
        fecha = datetime.now()
        cname = "Empleados" + fecha.strftime('%Y-%m-%d') + ".xlsx"

        wb = Workbook()
        ws = wb.active
        ws.title = 'Reporte Empleados'

        indice = 0
        # --------------------------------------------------------------------
        indice = indice + 1
        ws['A' + str(indice)] = 'Nº'
        ws['B' + str(indice)] = 'PAIS'
        ws['C' + str(indice)] = 'DEPARTAMENTO'
        ws['D' + str(indice)] = 'CIUDAD'
        ws['E' + str(indice)] = 'EMPRESA'
        ws['F' + str(indice)] = 'SUCURSAL'
        ws['G' + str(indice)] = 'CENTRO DE COSTO'
        ws['H' + str(indice)] = 'SECCION'
        ws['I' + str(indice)] = 'CODIGO'
        ws['J' + str(indice)] = 'NOMBRE'
        ws['K' + str(indice)] = 'APELLIDO_P'
        ws['L' + str(indice)] = 'APELLIDO_M'
        ws['M' + str(indice)] = 'CI'
        ws['N' + str(indice)] = 'SEXO'
        ws['O' + str(indice)] = 'FECHA_NACIMIENTO'
        ws['P' + str(indice)] = 'CARGO'
        ws['Q' + str(indice)] = 'CONTRATO_PLAZO'
        ws['R' + str(indice)] = 'FECHA_INGRESO_NOM'
        ws['S' + str(indice)] = 'FECHA_VENCIMIENTO'
        ws['T' + str(indice)] = 'CORREO'

        ws['A' + str(indice)].font = Font(bold=True)
        ws['B' + str(indice)].font = Font(bold=True)
        ws['C' + str(indice)].font = Font(bold=True)
        ws['D' + str(indice)].font = Font(bold=True)
        ws['E' + str(indice)].font = Font(bold=True)
        ws['F' + str(indice)].font = Font(bold=True)
        ws['G' + str(indice)].font = Font(bold=True)
        ws['H' + str(indice)].font = Font(bold=True)
        ws['I' + str(indice)].font = Font(bold=True)
        ws['J' + str(indice)].font = Font(bold=True)
        ws['K' + str(indice)].font = Font(bold=True)
        ws['L' + str(indice)].font = Font(bold=True)
        ws['M' + str(indice)].font = Font(bold=True)
        ws['N' + str(indice)].font = Font(bold=True)
        ws['O' + str(indice)].font = Font(bold=True)
        ws['P' + str(indice)].font = Font(bold=True)
        ws['Q' + str(indice)].font = Font(bold=True)
        ws['R' + str(indice)].font = Font(bold=True)
        ws['S' + str(indice)].font = Font(bold=True)
        ws['T' + str(indice)].font = Font(bold=True)

        for i in empleados:
            x = ResidenteManager(self.db).get_dataemp(i['id'])

            indice = indice + 1
            ws['A' + str(indice)] = x[0].id
            ws['B' + str(indice)] = x[0].empleado[0].pais.nombre
            ws['C' + str(indice)] = x[0].empleado[0].domicilios.nombre
            ws['D' + str(indice)] = x[0].empleado[0].ciudad.nombre
            ws['E' + str(indice)] = x[0].empleado[0].sucursal.empresa.nombre
            ws['F' + str(indice)] = x[0].empleado[0].sucursal.nombre
            ws['G' + str(indice)] = x[0].empleado[0].centro.nombre
            ws['H' + str(indice)] = x[0].empleado[0].gerencia.nombre
            ws['I' + str(indice)] = x[0].empleado[0].codigo
            ws['J' + str(indice)] = x[0].nombres
            ws['K' + str(indice)] = x[0].apellidopaterno
            ws['L' + str(indice)] = x[0].apellidomaterno
            ws['M' + str(indice)] = x[0].ci
            ws['N' + str(indice)] = x[0].sexo
            ws['O' + str(indice)] = x[0].fechanacimiento.strftime('%d/%m/%Y')
            ws['P' + str(indice)] = x[0].empleado[0].cargo.nombre
            ws['Q' + str(indice)] = x[0].contrato[0].tipo
            ws['R' + str(indice)] = x[0].contrato[0].fechaIngreso.strftime('%d/%m/%Y')
            ws['S' + str(indice)] = x[0].contrato[0].fechaFin.strftime('%d/%m/%Y')
            ws['T' + str(indice)] = x[0].empleado[0].email

        for col in ws.columns:
            row_idx = 0
            max_length = 0
            column = col[0].column
            for cell in col:
                row_idx = row_idx + 1
                try:
                    max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            if column not in ['N']:
                ws.column_dimensions[column].width = adjusted_width

        wb.save("server/common/resources/downloads/residente/" + cname)
        return cname

    def get_all_data(self, id):
        list = {}
        c = 0
        for dataper in self.db.query(Residente).filter(Residente.estado == True).filter(Residente.id == id):
            #list[c] = dict(id=dataper.ValorParametro.id, nombre=dataper.ValorParametro.nombre, valor=dataper.ValorParametro.valor)
            c = c + 1
        return list

    def obtener_domicilios(self, idresidente):

        x = self.db.query(Domicilio).join(ResidenteDomicilio).filter(ResidenteDomicilio.fkresidente == idresidente).filter(ResidenteDomicilio.vivienda == True).filter(Domicilio.estado == True).order_by(Domicilio.tipo.desc(),Domicilio.ubicacion.asc()).first()

        return x



    def listar_residentes(self,usuario):

        if usuario.sigas:
            return self.db.query(Residente).join(ResidenteDomicilio).join(Domicilio).join(Condominio).filter(Residente.estado == True).filter(ResidenteDomicilio.vivienda == True).order_by(Residente.nombre.asc()).all()

        elif usuario.rol.nombre == "RESIDENTE":
            return self.db.query(Residente).filter(Residente.id == usuario.fkresidente).order_by(Residente.nombre.asc()).all()

        else:
            return self.db.query(Residente).join(ResidenteDomicilio).join(Domicilio).join(Condominio).filter(Residente.estado == True) \
                .filter(ResidenteDomicilio.vivienda == True).filter(Condominio.id == usuario.fkcondominio).order_by(Residente.nombre.asc()).all()


    def validar_codigo(self, codigoautorizacion):
        domicilio = ""

        x = self.db.query(Residente).filter(Residente.estado == True).filter(Residente.codigoqr == codigoautorizacion).first()
        if x:
            for domi in x.domicilios:
                if domi.vivienda:
                    domicilio = domi.fkdomicilio
                    break

            residente = dict(idresidente= x.id,iddomicilio=domicilio,fotoresidente=x.foto,tipodocumento=4)
        else:
            residente = None
        return residente


    def actualizar_foto(self, data):
        try:
            print("servicio foto")
            x = self.db.query(Usuario).filter(Usuario.id == data['user']).first()
            persona = self.db.query(Residente).filter(Residente.id == x.fkresidente).first()
            persona.foto = data['foto']
            fecha = BitacoraManager(self.db).fecha_actual()
            b = Bitacora(fkusuario=data['user'], ip=data['ip'], accion="Actualizo Foto", fecha=fecha,
                         tabla="residente", identificador=persona.id)
            super().insert(b)
            self.db.merge(persona)
            self.db.commit()
            self.db.close()
            return dict(response=None, success=True, message="Actualizado correctamente")

        except Exception as e:
            return dict(response=str(e), success=False, message="Error al actualizar")



