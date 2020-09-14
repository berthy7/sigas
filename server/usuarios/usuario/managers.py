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

class UsuarioManager(SuperManager):

    def __init__(self, db):
        super().__init__(Usuario, db)

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

    def insert(self, diccionary):

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
            u.codigo = u.id
            super().update(u)

            principal = self.db.query(Principal).first()

            # if principal:
            #     try:
            #         if u.fkcondominio:
            #
            #             if u.condominio.ip_publica !="":
            #                 url = "http://"+u.condominio.ip_publica+":"+u.condominio.puerto+"/api/v1/registrar_usuario"
            #
            #                 headers = {'Content-Type': 'application/json'}
            #                 string = diccionary
            #                 cadena = json.dumps(string)
            #                 body = cadena
            #                 resp = requests.post(url, data=body, headers=headers, verify=False)
            #                 response = json.loads(resp.text)
            #
            #                 # print(response)
            #
            #
            #     except Exception as e:
            #         # Other errors are possible, such as IOError.
            #         print("Error de conexion: " + str(e))

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
            resi = self.db.query(Residente).filter(Residente.id == x.fkresidente).first()
            resiacce = self.db.query(ResidenteAcceso).filter(ResidenteAcceso.fkresidente == x.fkresidente).first()
            resi.estado = enable
            resiacce.estado = enable
            self.db.merge(resi)
            self.db.merge(resiacce)

            if x.condominio.singuardia:

                situacion = ""
                if enable:
                    situacion = "Acceso"
                else:
                    situacion = "Denegado"

                inicial_cod = 100000
                codigoInbio = inicial_cod + int(resi.codigo)

                diccionary = dict(codigo=str(codigoInbio), tarjeta=resi.codigoqr, situacion=situacion, fkcondominio=x.fkcondominio)

                ConfiguraciondispositivoManager(self.db).insert_qr_residente(diccionary)


        fecha = BitacoraManager(self.db).fecha_actual()
        b = Bitacora(fkusuario=Usuariocr, ip=ip, accion=message, fecha=fecha)
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
            cuerpo = "Saludos "+ str(usuario.nombre) +" "+ str(usuario.apellidop) +" "+" "+ str(usuario.apellidom) + "\n" + "Se le ha creado acceso al sistema SIGAS"+ "\n" + "Url: http://sistemacondominio.herokuapp.com"+ "\n" + "\n" + "Credenciales: "+ "\n" + str(condominio)+ "\n" + "Username: "+ str(usuario.username) + "\n" + "Password: "+ str(password) + "\n" + "Perfil: "+ str(usuario.rol.nombre) + "\n" + "\n" +  "Saludos"
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
                usuario.apellidom) + "\n" + "Se ha reiniciado su contraseña de acceso al sistema SIGAS" + "\n" + "Url: http://sistemacondominio.herokuapp.com" + "\n" + "\n" + "Credenciales: " + "\n" + str(
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

                url = "http://sistemacondominio.herokuapp.com/api/v1/actualizar_credenciales"

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

        nuevo_password = hashlib.sha512(diccionary['password'].encode()).hexdigest()

        usuario.password = nuevo_password


        fecha = BitacoraManager(self.db).fecha_actual()
        u = super().update(usuario)

        b = Bitacora(fkusuario=diccionary['user'], ip=diccionary['ip'], accion="Restablecio Password", fecha=fecha,
                     tabla="usuario", identificador=usuario.id)
        super().insert(b)

        UsuarioManager(self.db).correo_password_reinicio(u, diccionary['password'])

        return dict(response=None, success=True, message="Actualizado Correctamente")


class ModuloManager:

    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Modulo).filter(Modulo.fkmodulo==None)
