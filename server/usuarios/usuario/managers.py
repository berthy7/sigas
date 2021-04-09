from ...operaciones.bitacora.managers import *
from ...condominios.residente.models import *
from ..rol.models import *

from server.common.managers import SuperManager, Error
from .models import *
from sqlalchemy.sql import func
from random import *

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from ...dispositivos.dispositivo.managers import *

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from xhtml2pdf import pisa

import string
from random import *
import random
import requests
import jwt
import time
import hashlib
import json
from configparser import ConfigParser
import uuid

from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font

from onesignal_sdk.client import Client
from onesignal_sdk.error import OneSignalHTTPError

class UsuarioManager(SuperManager):

    def __init__(self, db):
        super().__init__(Usuario, db)


    def listar_todo_arbol(self):
        return  self.db.query(self.entity) \
            .filter(self.entity.fkcondominio != None) \
            .order_by(self.entity.username.asc()).all()

    def get_employees_tree(self):
        query = self.db.query(Condominio).filter(Condominio.estado == True).all()
        admin = dict()
        cont_tipo = 1
        for condominio in query:
            con = (condominio.id, condominio.nombre)
            admin[con] = dict()

            list_tipo_tarjeta = ['Residente', 'Visita', 'Proveedor', 'Provper', 'Excepcion']
            list_rol = self.db.query(Rol).filter(Rol.enabled == True).filter(Rol.id != 1).filter(Rol.id != 3).filter(Rol.id != 5).all()

            for role in list_rol:

                rol = (cont_tipo, role.nombre)

                cont_tipo = cont_tipo + 1

                admin[con][rol] = dict()

                listar_usuarios = UsuarioManager(self.db).listar_usuarios_x_rol(condominio.id, role.id)
                html_e = ""
                for usuario in listar_usuarios:
                    html = '<li class="dd-item" data-id="' + str(usuario.id) + str(
                        usuario.id) + '"><div class="dd-handle"><input id="' + str(usuario.id) + str(
                        usuario.id) + '" data-id="' + str(usuario.id) + '" data-sex="' + str(usuario.nombre) + \
                           '"type="checkbox" class="module chk-col-deep-purple employee"><label for="' + str(usuario.id) + str(usuario.id) + \
                           '">' + str(usuario.username) + '</label></div></li>'

                    html_e = html_e + html

                    admin[con][rol] = html_e

        return admin

    def listar_usuarios_x_rol(self, idcondominio,idRole):

        x = self.db.query(self.entity) \
            .filter(self.entity.fkcondominio != None) \
            .filter(self.entity.fkcondominio == idcondominio) \
            .filter(self.entity.fkrol == idRole) \
            .order_by(self.entity.username.asc()).all()

        return x

    def insert_sincronizacion(self, diccionary):

        for tar in diccionary['usuarios']:
            t = self.db.query(self.entity).filter(self.entity.id == tar['id']).first()

            if t.estado != tar['estado']:
                UsuarioManager(self.db).state(tar['id'],tar['estado'],diccionary['user'],diccionary['ip'])


    def sincronizar_login_token(self, user,token):
        usuario = UsuarioManager(self.db).get_by_pass(user)
        usuario.token = token

        return super().update(usuario)


    def registrar_token(self, user,token):
        usuario = UsuarioManager(self.db).get_by_pass(user)
        usuario.token_notificacion = token

        return super().update(usuario)


    def eliminar_token(self, user):
        usuario = UsuarioManager(self.db).get_by_pass(user)
        usuario.token_notificacion = ""

        return super().update(usuario)


    def listar_notificacion(self,Idusuario):

        return self.db.query(Notificacion).filter(Notificacion.fkreceptor == Idusuario).filter(Notificacion.enabled).all()

    def estado_notificacion(self, id, user, ip):
        x = self.db.query(Notificacion).filter(Notificacion.id == id).first()

        x.estado = True
        mensaje = "Leyo Notificacion"


        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion=mensaje, fecha=fecha, tabla="notificacion", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return mensaje

    def eliminar_notificacion(self, id, user, ip):
        x = self.db.query(Notificacion).filter(Notificacion.id == id).first()

        x.enabled = False
        mensaje = "Elimino Notificacion"

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion=mensaje, fecha=fecha, tabla="notificacion", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return mensaje

    def generar_contraseña(self):
        longitud = 6
        valores = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        return p

    def state(self, id,estado, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.estado = estado

        if estado :
            mensaje = "Habilito Usuario"
        else:
            mensaje = "Deshabilito Usuario"

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion=mensaje, fecha=fecha,
                     tabla="usuario", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        if x.rol.nombre == "RESIDENTE":

            resi = self.db.query(Residente).filter(Residente.id == x.fkresidente).first()
            resiacce = self.db.query(ResidenteAcceso).filter(ResidenteAcceso.fkresidente == x.fkresidente).first()
            resi.estado = estado
            resiacce.estado = estado
            resi = self.db.merge(resi)
            self.db.merge(resiacce)
            self.db.commit()

            if x.condominio.singuardia:
                UsuarioManager(self.db).sincronizar_dispositivos(x, estado,resi)


        principal = self.db.query(Principal).first()

        if principal.estado:

            try:
                if x.fkcondominio:

                    if x.condominio.ip_publica != "":

                        diccionary = dict( id=id,estado=estado, user=user, ip=ip)


                        url = "http://" + x.condominio.ip_publica + ":" + x.condominio.puerto + "/api/v1/sincronizar_usuario_estado"

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

    def sesion(self, id,estado, user, ip):
        x = self.db.query(self.entity).filter(self.entity.id == id).one()
        x.login = estado

        if estado :
            mensaje = "Inicio session del Usuario " + x.username
        else:
            mensaje = "Cerro session del Usuario " + x.username

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=user, ip=ip, accion=mensaje, fecha=fecha,
                     tabla="usuario", identificador=id)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()
        return x

    def login_token(self, usuario):
        usuario.login = True
        usuario.token = str(uuid.uuid4()).replace('-', '')

        return super().update(usuario)

    def logout_sin_token(self, usuario):
        usuario.login = False
        usuario.token = "Sin Token"
        super().update(usuario)


    def obtener_principal(self):
        x = self.db.query(Principal).first()

        return x.estado

    def obtener_administrador(self):
        return self.db.query(Usuario).filter(Usuario.nombre == "Administrador").one()

    def obtener_x_condominio(self,idcondominio):
        return self.db.query(Usuario).filter(Usuario.fkcondominio == idcondominio).all()

    def usuarios_sigas(self,user):

        if user.rol.nombre == "SUPER ADMINISTRADOR":
            x = self.db.query(Usuario).filter(Usuario.sigas == True)
        else:
            x = self.db.query(Usuario).join(Rol).filter(Usuario.sigas == True).filter(Rol.nombre != "SUPER ADMINISTRADOR")

        return x

    def usuarios_condominio(self,user):
        if user.fkcondominio:

            return self.db.query(Usuario).filter(Usuario.fkcondominio == user.fkcondominio).all()
        else:
            return self.db.query(Usuario).filter(Usuario.sigas == False).all()

    def name_role(self, rol):
        role = self.db.query(Rol).filter_by(id=rol).first()
        nombre_rol = role.name
        return nombre_rol

    def get_random_string(self):
        random_list = []
        for i in range(8):
            random_list.append(random.choice(string.ascii_uppercase + string.digits))
        return ''.join(random_list)

    def insert_residente(self, diccionary):
        password_desencriptado = diccionary['default']

        diccionary['password'] = hashlib.sha512(diccionary['default'].encode()).hexdigest()

        usuario = UsuarioManager(self.db).entity(**diccionary)
        user = self.db.query(Usuario).filter(Usuario.username == usuario.username).first()

        if user:
            return dict(respuesta=False, response=None ,Mensaje="Nombre de Usuario ya Existe")

        else:

            fecha = BitacoraManager(self.db).fecha_actual()
            b = Bitacora(fkusuario=usuario.user_id, ip=usuario.ip, accion="Se registró un usuario.", fecha=fecha)
            super().insert(b)
            u = super().insert(usuario)

            print("codigo usuario : "+str(u.codigo))

            if u.codigo == None:
                print("codigo is none")
                u.codigo = u.id
                super().update(u)


            # UsuarioManager(self.db).correo_creacion_usuarios(u,diccionary['password'])
            return dict(respuesta=True, response=u, Mensaje="Insertado Correctamente")

    def insert(self, diccionary):
        password_desencriptado = diccionary['password']

        diccionary['password']= hashlib.sha512(diccionary['password'].encode()).hexdigest()

        usuario = UsuarioManager(self.db).entity(**diccionary)
        user = self.db.query(Usuario).filter(Usuario.username == usuario.username).first()

        if user:
            return dict(respuesta=False, Mensaje="Nombre de Usuario ya Existe")

        else:

            fecha = BitacoraManager(self.db).fecha_actual()
            b = Bitacora(fkusuario=usuario.user_id, ip=usuario.ip, accion="Se registró un usuario.", fecha=fecha)
            super().insert(b)
            u = super().insert(usuario)

            principal = self.db.query(Principal).first()

            if principal.estado:
                u.codigo = u.id
                super().update(u)
                diccionary['codigo'] = u.codigo
                diccionary['password'] = password_desencriptado
                diccionary['default'] = password_desencriptado

                try:
                    if u.fkcondominio:

                        if u.condominio.ip_publica !="":
                            url = "http://"+u.condominio.ip_publica+":"+u.condominio.puerto+"/api/v1/sincronizar_usuario"

                            headers = {'Content-Type': 'application/json'}
                            string = diccionary
                            cadena = json.dumps(string)
                            body = cadena
                            resp = requests.post(url, data=body, headers=headers, verify=False)
                            response = json.loads(resp.text)

                            print(response)

                    if u.sigas:
                        url = "http://190.186.79.215:5000/api/v1/sincronizar_usuario"

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

            #UsuarioManager(self.db).correo_creacion_usuarios(u,diccionary['password'])
            return dict(respuesta=True, Mensaje="Insertado Correctamente")


    def update(self, usuario):

        if not usuario.password or usuario.password == '':
            usuario.password = (self.db.query(Usuario.password)
                .filter(Usuario.id == usuario.id).first())[0]
        else:
            usuario.password = hashlib.sha512(usuario.password.encode()).hexdigest()

        fecha = BitacoraManager(self.db).fecha_actual()
        a = super().update(usuario)
        b = Bitacora(fkusuario=usuario.user_id, ip=usuario.ip, accion="Modificó Usuario.", fecha=fecha, tabla="usuario", identificador=a.id)
        super().insert(b)

        return a


    def update_users(self, emailprev, emailnew, nameprev, namenew):
        u = self.db.query(Usuario).filter(Usuario.correo == emailprev).one()

        if u:
            ap_user = u.apellido
            result = nameprev.index(ap_user)
            u.correo = emailnew

    def sincronizar_dispositivos(self,x,enable,resi):

        if enable:
            situacion = "Acceso"
        else:
            situacion = "Denegado"


        diccionary = dict(codigo=resi.codigoqr, tarjeta=resi.codigoqr, situacion=situacion,
                          fkcondominio=x.fkcondominio, residente=resi.nombre + " " + resi.apellidop)

        ConfiguraciondispositivoManager(self.db).insert_qr_residente(diccionary)


    def delete_user(self, id, enable, Usuariocr, ip):
        x = self.db.query(Usuario).filter(Usuario.id == id).one()

        if enable == True:
            r = self.db.query(Rol).filter(Rol.id == x.fkrol).one()
            if r.enabled:
                x.enabled = enable
            else:
                return False
            message = "Se habilitó un usuario."
        else:
            x.enabled = enable
            message = "Se deshabilitó un usuario."

        if x.rol.nombre == "RESIDENTE":
            if x.condominio.singuardia:
                UsuarioManager(self.db).sincronizar_dispositivos(x, enable)

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuariocr, ip=ip, accion=message, fecha=fecha)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()



        return True

    def exit_user(self, id,  Usuariocr, ip):
        x = self.db.query(Usuario).filter(Usuario.id == id).one()

        x.login = False

        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuariocr, ip=ip, accion="Cierre de Session Forzado"+x.username , fecha=fecha)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

        return True

    def activate_Usuarios(self, id, Usuario, ip):
        x = self.db.query(Usuario).filter(Usuario.id == id).one()
        x.enabled = 1
        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuario, ip=ip, accion="Se activó un usuario.", fecha=fecha)
        super().insert(b)
        self.db.merge(x)
        self.db.commit()

    def get_privileges(self, id, route):
        parent_module = self.db.query(Modulo).join(Rol.modulos).join(Usuario).            \
            filter(Modulo.route == route).\
            filter(Usuario.id == id).\
            filter(Usuario.enabled).\
            first()
        if not parent_module:
            return dict()
        modules = self.db.query(Modulo).\
            join(Rol.modulos).join(Usuario).\
            filter(Modulo.fkmodulo == parent_module.id).\
            filter(Usuario.id == id).\
            filter(Usuario.enabled)
        privileges = {parent_module.name: parent_module}
        for module in modules:
            privileges[module.name] = module
        return privileges

    def list_all(self):
        return dict(objects=self.db.query(Usuario).filter(Usuario.fkrol == Rol.id).filter(Rol.nombre != "Super Administrador").distinct())

    def has_access(self, id, route):
        aux = self.db.query(Usuario.id).\
            join(Rol).join(Acceso).join(Modulo).\
            filter(Usuario.id == id).\
            filter(Modulo.route == route).\
            filter(Usuario.enabled).\
            all()
        return len(aux) != 0

    def get_page(self, page_nr=1, max_entries=10, like_search=None, order_by=None, ascendant=True, query=None):
        query = self.db.query(Usuario).join(Rol).filter(Rol.id > 1)
        return super().get_page(page_nr, max_entries, like_search, order_by, ascendant, query)

    def login_Usuario(self, username, password):
        password = hashlib.sha512(password.encode()).hexdigest()
        return self.db.query(Usuario).filter(Usuario.username == username).filter(Usuario.password == password).filter(
            Usuario.enabled == 1)

    def get_userById(self, id):
        return dict(profile=self.db.query(Usuario).filter(Usuario.id == id).first())

    def obtener_diccionario_usuario(self, id):
        usuario = self.db.query(Usuario).filter(Usuario.id == id).first()

        if usuario.fkresidente:
            nombre = usuario.residente.fullname
        else:
            nombre = "---------"

        return dict(id=usuario.id, username=usuario.username,rol=usuario.rol.nombre,nombre = nombre)

    def update_password(self, Usuario):
        Usuario.password = hashlib.sha512(Usuario.password.encode()).hexdigest()
        return super().update(Usuario)



    def get_by_password(self, Usuario_id, password):
        return self.db.query(Usuario).filter(Usuario.id == Usuario_id). \
            filter(Usuario.password == hashlib.sha512(str(password).encode()).hexdigest()).first()

    def get_by_pass(self, Usuario_id):
        return self.db.query(Usuario).filter(Usuario.id == Usuario_id).first()

    def obtener_x_codigo(self, codigo):
        return self.db.query(Usuario).filter(Usuario.codigo == codigo).first()

    def verificar_x_codigo(self,codigo):
        ver = self.db.query(Usuario).filter(Usuario.codigo==codigo).filter(Usuario.enabled==True).first()

        if ver:

            return dict(respuesta=True, mensaje='')
        else:

            return dict(respuesta=False,mensaje='Usuario Deshabilitado')


    def verificar_x_token(self,token):
        tok = self.db.query(Usuario).filter(Usuario.token==token).first()

        if tok:

            return dict(respuesta=True, mensaje='')
        else:

            return dict(respuesta=False,mensaje='Token Incorrecto')

    def obtener_x_id(self, user):
        return self.db.query(Usuario).filter(Usuario.id == user).first()

    def obtener_x_fkresidente(self, resi):
        return self.db.query(Usuario).filter(Usuario.fkresidente == resi).first()


    def update_profile(self, Usuarioprf, ip):
        usuario = self.db.query(Usuario).filter_by(id=Usuarioprf.id).first()
        usuario.username = Usuarioprf.username
        self.db.merge(usuario)
        b = Bitacora(fkusuario=usuario.id, ip=ip, accion="Se actualizó perfil de usuario.", fecha=fecha_zona, tabla='usuario', identificador=usuario.id)
        super().insert(b)
        self.db.commit()
        return usuario

    def validar_usuario(self, username, password):
        password = hashlib.sha512(password.encode()).hexdigest()
        return self.db.query(func.count(Usuario.id)).filter(Usuario.username == username).filter(
            Usuario.enabled == True).filter(Usuario.password == password).scalar()

    def validar_usuario_sesion(self, codigo, usuario):
        return self.db.query(func.count(Usuario.id)).filter(Usuario.codigo == codigo).filter(
            Usuario.enabled == True).filter(Usuario.id == usuario).scalar()

    def activate_Usuario(self, usuario):
        usuario = self.db.query(Usuario).filter_by(id=usuario).first()
        usuario.activo = 1
        self.db.merge(usuario)
        self.db.commit()

    def update_codigo(self, usuario):
        x = self.db.query(Usuario).filter(Usuario.id == usuario).one()
        x.activo = 0
        x.codigo = self.get_random_string()
        x.token = "Sin Token"
        self.db.commit()
        self.db.close()
        return x

    def listar_todo(self, id):
        return self.db.query(Usuario).filter(Usuario.enabled == True).filter(Usuario.id == id)

    def correo_creacion_usuarios(self,usuario,password):
        correos = []
        server = self.db.query(ServidorCorreo).filter(ServidorCorreo.estado == True).filter(ServidorCorreo.id == 1).first()

        correos.append(usuario.correo)

        if usuario.fkcondominio:
            condominio = "Condominio: "+usuario.condominio.nombre + " "
        else:
            condominio = " "

        if len(correos)> 0:

            # Iniciamos los parámetros del script
            remitente = "<"+server.correo+">"
            destinatarios = correos
            asunto = 'Creacion de Usuario SIGAS'
            cuerpo = "Saludos "+ str(usuario.nombre) +" "+ str(usuario.apellidop) +" "+" "+ str(usuario.apellidom) + "\n" + "Se le ha creado acceso al sistema SIGAS"+ "\n" + "Url: http://sigas-web.herokuapp.com"+ "\n" + "\n" + "Credenciales: "+ "\n" + str(condominio)+ "\n" + "Username: "+ str(usuario.username) + "\n" + "Password: "+ str(password) + "\n" + "Perfil: "+ str(usuario.rol.nombre) + "\n" + "\n" +  "Saludos"
            # Creamos el objeto mensaje
            mensaje = MIMEMultipart('alternative')
            # Establecemos los atributos del mensaje
            mensaje['From'] = remitente
            mensaje['To'] = ", ".join(destinatarios)
            mensaje['Subject'] = asunto
            # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
            mensaje.attach(MIMEText(cuerpo, 'plain'))
            # Abrimos el archivo que vamos a adjuntar
            # Creamos un objeto MIME base
            # Creamos la conexión con el servidor
            sesion_smtp = smtplib.SMTP(server.servidor)
            # Ciframos la conexión
            sesion_smtp.starttls()
            # Iniciamos sesión en el servidor
            sesion_smtp.login(server.correo, server.password)
            # Convertimos el objeto mensaje a texto
            texto = mensaje.as_string()
            # Enviamos el mensaje
            sesion_smtp.sendmail(remitente, destinatarios, texto)
            # Cerramos la conexión
            sesion_smtp.quit()
            print("correo enviado")

    def correo_password_reinicio(self, usuario, password):
        correos = []
        server = self.db.query(ServidorCorreo).filter(ServidorCorreo.estado == True).filter(
            ServidorCorreo.id == 1).first()

        correos.append(usuario.correo)

        if usuario.fkcondominio:
            condominio = "Condominio: " + usuario.condominio.nombre + " "
        else:
            condominio = " "

        if len(correos) > 0:
            # Iniciamos los parámetros del script
            remitente = "<" + server.correo + ">"
            destinatarios = correos
            asunto = 'Reinicio de Contraseña usuario SIGAS'
            cuerpo = "Saludos " + str(usuario.nombre) + " " + str(usuario.apellidop) + " " + " " + str(
                usuario.apellidom) + "\n" + "Se ha reiniciado su contraseña de acceso al sistema SIGAS" + "\n" + "Url: http://sigas-web.herokuapp.com" + "\n" + "\n" + "Credenciales: " + "\n" + str(
                condominio) + "\n" + "Username: " + str(usuario.username) + "\n" + "Password: " + str(
                password) + "\n" + "Perfil: " + str(usuario.rol.nombre) + "\n" + "\n" + "Saludos"
            # Creamos el objeto mensaje
            mensaje = MIMEMultipart('alternative')
            # Establecemos los atributos del mensaje
            mensaje['From'] = remitente
            mensaje['To'] = ", ".join(destinatarios)
            mensaje['Subject'] = asunto
            # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
            mensaje.attach(MIMEText(cuerpo, 'plain'))
            # Abrimos el archivo que vamos a adjuntar
            # Creamos un objeto MIME base
            # Creamos la conexión con el servidor
            sesion_smtp = smtplib.SMTP(server.servidor)
            # Ciframos la conexión
            sesion_smtp.starttls()
            # Iniciamos sesión en el servidor
            sesion_smtp.login(server.correo, server.password)
            # Convertimos el objeto mensaje a texto
            texto = mensaje.as_string()
            # Enviamos el mensaje
            sesion_smtp.sendmail(remitente, destinatarios, texto)
            # Cerramos la conexión
            sesion_smtp.quit()
            print("correo enviado")


    def verificar_username(self, username):
        n = self.db.query(func.count(Usuario.id)).filter(Usuario.username == username).scalar()

        if n > 0:
            return dict(respuesta=True)

        else:
            return dict(respuesta=False)


    def actualizar_credenciales(self, diccionary):

        usuario = UsuarioManager(self.db).get_by_pass(diccionary['user'])
        old_password = hashlib.sha512(diccionary['password'].encode()).hexdigest()
        if usuario.password == old_password:
            usuario.password = diccionary['nuevo_password']
            if not usuario.password or usuario.password == '':
                usuario.password = (self.db.query(Usuario.password)
                                    .filter(Usuario.id == usuario.id).first())[0]
            else:
                usuario.password = hashlib.sha512(usuario.password.encode()).hexdigest()

            if diccionary['username'] or diccionary['username'] != '':
                usuario.username = diccionary['username']


            fecha = BitacoraManager(self.db).fecha_actual()
            us = self.db.merge(usuario)
            self.db.commit()

            b = Bitacora(fkusuario=diccionary['user'], ip=diccionary['ip'], accion="Modificó Credenciales", fecha=fecha,
                         tabla="usuario", identificador=usuario.id)
            super().insert(b)

            principal = self.db.query(Principal).first()

            if principal.estado == False:

                url = "http://sigas-web.herokuapp.com/api/v1/actualizar_credenciales"

                headers = {'Content-Type': 'application/json'}
                diccionary['user'] = us.codigo
                cadena = json.dumps(diccionary)
                body = cadena
                resp = requests.post(url, data=body, headers=headers, verify=False)
                response = json.loads(resp.text)

            return dict(response=None,success=True,message="Actualizado Correctamente")
        else:
            return dict(response=None,success=False,message="Password Incorrecto")


    def restablecer_password(self, diccionary):

        usuario = UsuarioManager(self.db).get_by_pass(diccionary['idusuario'])

        diccionary['password'] = UsuarioManager(self.db).generar_contraseña()


        nuevo_password = hashlib.sha512(diccionary['password'].encode()).hexdigest()

        usuario.password = nuevo_password
        usuario.default = diccionary['password']


        fecha = BitacoraManager(self.db).fecha_actual()
        u = super().update(usuario)

        b = Bitacora(fkusuario=diccionary['user'], ip=diccionary['ip'], accion="Restablecio Password", fecha=fecha,
                     tabla="usuario", identificador=usuario.id)
        super().insert(b)

        # UsuarioManager(self.db).correo_password_reinicio(u, diccionary['password'])

        return dict(response=diccionary['password'], success=True, message="Actualizado Correctamente")


class ModuloManager:

    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Modulo).filter(Modulo.fkmodulo==None)


class VersionMovilManager:

    def __init__(self, db):
        self.db = db

    def version_actual(self):

        verActual = self.db.query(VersionMovil).filter(
            VersionMovil.estado == True).first()

        return verActual.version

    def verificar_version_actual(self,version):

        ver = self.db.query(VersionMovil).filter(VersionMovil.version==version).filter(VersionMovil.estado==True).first()

        if ver:
            return dict(respuesta=True, mensaje='')

        else:

            return dict(respuesta=False, mensaje=self.version_actual())


class NotificacionManager(SuperManager):

    def __init__(self, db):
        super().__init__(Notificacion, db)


    def insert(self, diccionary):
        objeto = NotificacionManager(self.db).entity(**diccionary)
        fecha = BitacoraManager(self.db).fecha_actual()

        a = super().insert(objeto)
        b = Bitacora(fkusuario=objeto.user, ip=objeto.ip, accion="Registro Notificacion.", fecha=fecha, tabla="notificacion",
                     identificador=a.id)
        super().insert(b)
        return a

    def registrar_notificacion_onesignal(self, a,objeto):
        usuario = UsuarioManager(self.db).obtener_x_fkresidente(a.invitacion.evento.fkresidente)
        fecha = BitacoraManager(self.db).fecha_actual()
        Nombrevisita = ""
        if a.invitacion.fkinvitado:
            Nombrevisita = a.invitacion.invitado.fullname
        elif a.invitacion.evento.paselibre:
            Nombrevisita = "Pase Libre"

        notificacion = NotificacionManager(self.db).insert(
            dict(fkremitente=1, fkreceptor=usuario.id, mensaje="llego su visita " + Nombrevisita,
                 titulo="Notificacion de llegada", fecha=fecha, user=objeto.user, ip=objeto.ip))

        print("entrando a funcion enviar")
        NotificacionManager(self.db).enviar_notificacion_onesignal(notificacion)

    def enviar_notificacion_onesignal(self, notificacion):
        print("Enviando Notificacion a un solo cliente")

        try:
            # Parametros
            APP_ID = 'd99d9fe9-1f01-4b4a-a929-069a9813788c'
            REST_API_KEY = 'MWI1Y2Y2MWEtZGY1OC00MjI1LTk0NTctNTQ5ZjI4NzViNWRk'
            CHANNEL_ID = '4d4c7bc7-0221-4e6a-bedb-0093499f9424'  # DE LA CATEGORIA PRIORITARY
            cli = notificacion.receptor.token_notificacion
            if cli and cli != 'undefined' and cli != '0':
                print('Token..:')
                print(cli)

                client = Client(app_id=APP_ID, rest_api_key=REST_API_KEY)
                img = ''
                notification_body = {
                    'contents': {'en': notificacion.mensaje, 'es': notificacion.mensaje},
                    # 'subtitle': {'en': n.subtitle, 'es': n.subtitle}, // Si se quiere agregar un subtitulo
                    'headings': {'en': notificacion.titulo, 'es': notificacion.titulo},
                    # 'included_segments': ['Active Users', 'Inactive Users'], // cuando se especifica el include_player_ids, los segmentos ya no se envian
                    'include_player_ids': [cli],
                    'big_picture': img,  # Foto cuando la notificacion se expande
                    'small_icon': 'icon',  # Icono de la notificacion
                    # 'android_accent_color': '0065ab',# Color de fondo del small_icon
                    # 'huawei_accent_color': '0065ab',# Color de fondo del small_icon
                    'huawei_small_icon': 'icon',
                    'large_icon': img,  # Foto con la notificacion sin expandirse
                    'huawei_large_icon': img,  # Foto con la notificacion sin expandirse
                    'android_channel_id': CHANNEL_ID,  # Categoria de la notificacion definida en OneSignal
                    'huawei_channel_id': CHANNEL_ID,  # Categoria de la notificacion definida en OneSignal
                    'android_background_layout': '{"headings_color": "FFFF0000", "contents_color": "FF00FF00"}'
                }
                print('Cuerpo de la Notificacion..')
                print('..')
                print('..')
                print(notification_body)
                print('..')
                print('..')
                response = client.send_notification(notification_body)
                # print('Notificacion enviada: ')
                # print(response)
                # self.deshabilitar_notificacion(n)
        except OneSignalHTTPError as e:
            print("Error al enviar la notificacion: " + str(notificacion.id) + ' ' + str(notificacion.titulo))
            print(e)
            print(e.message)
