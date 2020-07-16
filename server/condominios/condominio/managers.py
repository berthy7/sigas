from ...operaciones.bitacora.managers import *
from ..domicilio.managers import *
from ..evento.managers import *
from ..movimiento.managers import *
from ..areasocial.models import *
from server.common.managers import SuperManager
from .models import *


class CondominioManager(SuperManager):

    def __init__(self, db):
        super().__init__(Condominio, db)

    def obtener_departamentos(self, idcondominio):
        x = self.db.query(Domicilio).filter(Domicilio.fkcondominio == idcondominio).filter(Domicilio.estado == True).order_by(Domicilio.tipo.desc(),Domicilio.ubicacion.asc()).all()

        return x

    def obtener_eventos(self, idcondominio):

        x = self.db.query(Evento).join(Residente).join(ResidenteDomicilio).join(Domicilio).join(Condominio).filter(Evento.estado == True) \
                                 .filter(ResidenteDomicilio.vivienda == True).filter(Condominio.id == idcondominio).all()

        return x

    def obtener_residentes(self, idcondominio):

        x = self.db.query(Residente).join(ResidenteDomicilio).join(Domicilio).join(Condominio).filter(Residente.estado == True) \
                                 .filter(ResidenteDomicilio.vivienda == True).filter(Condominio.id == idcondominio).all()

        return x

    def obtener_movimientos(self, idcondominio):

        domicilio = self.db.query(Movimiento).join(Domicilio).filter(Domicilio.fkcondominio == idcondominio).filter(Movimiento.estado == True).all()
        areasocial = self.db.query(Movimiento).join(Areasocial).filter(Areasocial.fkcondominio == idcondominio).filter(Movimiento.estado == True).all()

        for area in areasocial:
            domicilio.append(area)

        return domicilio

    def obtener_x_nombre(self, nombre):
        return self.db.query(self.entity).filter(self.entity.nombre == nombre).first()

    def get_all(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

    def list_all(self):
        return dict(objects=self.db.query(self.entity).filter(self.entity.estado == True))

    def listar_todo(self):

        return self.db.query(self.entity).filter(self.entity.estado == True).order_by(self.entity.nombre.asc()).all()

    def listar_x_sucursal(self, idsurcusal):
        return self.db.query(self.entity).filter(self.entity.fksucursal == idsurcusal).filter(
            self.entity.estado == True)

    def insert(self, diccionary):

        objeto = CondominioManager(self.db).entity(**diccionary)

        objeto.fechai = datetime.strptime(objeto.fechai, '%d/%m/%Y')
        objeto.fechaf = datetime.strptime(objeto.fechaf, '%d/%m/%Y')
        fecha = BitacoraManager(self.db).fecha_actual()

        c = super().insert(objeto)

        principal = self.db.query(Principal).first()

        if principal.estado:

            if c.ip_publica != "":
                url = "http://" + c.ip_publica + ":" + c.puerto + "/api/v1/registrar_condominio"

                headers = {'Content-Type': 'application/json'}
                diccionary['id'] = c.id

                cadena = json.dumps(diccionary)
                body = cadena
                resp = requests.post(url, data=body, headers=headers, verify=False)
                response = json.loads(resp.text)

                print(response)

        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Condominio.", fecha=fecha,tabla="condominio", identificador=c.id)
        super().insert(b)
        return c

    def update(self, objeto):
        objeto.fechai = datetime.strptime(objeto.fechai, '%d/%m/%Y')
        objeto.fechaf = datetime.strptime(objeto.fechaf, '%d/%m/%Y')
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().update(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Modifico Condominio.", fecha=fecha,tabla="condominio", identificador=a.id)
        super().insert(b)
        return a

    def delete(self, id,estado, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.estado = estado
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion="Eliminó Condominio.", fecha=fecha, tabla="condominio", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return x

    def obtener_condominio_x_usuario(self, usuario):

        if usuario.fkcondominio:
            x = self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.id == usuario.fkcondominio).first()
            return x.nombre
        elif usuario.fkresidente:
            x = self.db.query(Condominio).join(Domicilio).join(ResidenteDomicilio).join(Residente).filter(Condominio.estado == True).filter(ResidenteDomicilio.vivienda == True) \
                .filter(Residente.id == usuario.fkresidente).first()

            return x.nombre
        else:
            return "-------"


    def obtener_x_id(self,id):
        return self.db.query(self.entity).filter(self.entity.estado == True).filter(self.entity.id == id).first()


class EntradaManager(SuperManager):

    def __init__(self, db):
        super().__init__(Entrada, db)

    def obtener_entradas(self):
        return self.db.query(self.entity).filter(self.entity.estado == True).all()

