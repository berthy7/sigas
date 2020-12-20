from ...database.connection import transaction
from ..usuario.models import *
from ...condominios.residente.models import *
from sqlalchemy.orm import joinedload, make_transient

import hashlib


class LoginManager:

    def usuario_x_id(self, idUsuario):
        """Retorna un usuario que coincida con el username y password dados.

        parameters
        ----------
        Usuarioname : str
        password : str
            El password deberá estar sin encriptar.

        returns
        -------
        Usuario
        None
            Retornará None si no encuentra nada.
        """

        with transaction() as session:

            usuario = session.query(Usuario).\
                filter(Usuario.id == idUsuario).\
                first()

        return usuario

    def verificar_usuario_correcto(self, username, password):

        password = hashlib.sha512(password.encode()).hexdigest()

        with transaction() as session:

            usuario = session.query(Usuario).\
                options(joinedload('rol').
                        joinedload('modulos').
                        joinedload('children')).\
                filter(Usuario.username == username).\
                filter(Usuario.password == password).\
                first()
            if not usuario:
                return None
            session.expunge(usuario)
            make_transient(usuario)
        usuario.rol.modulos = self.order_modules(usuario.rol.modulos)
        return usuario

    def login(self, username, password):
        """Retorna un usuario que coincida con el username y password dados.

        parameters
        ----------
        Usuarioname : str
        password : str
            El password deberá estar sin encriptar.

        returns
        -------
        Usuario
        None
            Retornará None si no encuentra nada.
        """
        password = hashlib.sha512(password.encode()).hexdigest()
        with transaction() as session:
            usuario = session.query(Usuario).\
                options(joinedload('rol').
                        joinedload('modulos').
                        joinedload('children')).\
                filter(Usuario.username == username).\
                filter(Usuario.password == password).\
                filter(Usuario.enabled).\
                first()
            if not usuario:
                return None
            session.expunge(usuario)
            make_transient(usuario)
        usuario.rol.modulos = self.order_modules(usuario.rol.modulos)
        return usuario

    def not_enabled(self, username, password):
        """Retorna un usuario que coincida con el username y password dados.

        parameters
        ----------
        Usuarioname : str
        password : str
            El password deberá estar sin encriptar.

        returns
        -------
        Usuario
        None
            Retornará None si no encuentra nada.
        """
        password = hashlib.sha512(password.encode()).hexdigest()
        with transaction() as session:
            usuario = session.query(Usuario).\
                options(joinedload('rol').
                        joinedload('modulos').
                        joinedload('children')).\
                filter(Usuario.username == username).\
                filter(Usuario.password == password).\
                filter(Usuario.enabled == False).\
                first()
            if not usuario:
                return None
            session.expunge(usuario)
            make_transient(usuario)
        usuario.rol.modulos = self.order_modules(usuario.rol.modulos)
        return usuario

    def get(self, key):
        with transaction() as session:
            usuario = session.query(Usuario).\
                options(joinedload('rol').
                        joinedload('modulos').
                        joinedload('children')).\
                filter(Usuario.id == key).\
                filter(Usuario.enabled).\
                first()
            if not usuario:
                return None
            session.expunge(usuario)
            make_transient(usuario)
        usuario.rol.modulos = self.order_modules(usuario.rol.modulos)
        return usuario

    def obtener_persona(self, key):
        with transaction() as session:
            persona = session.query(Persona).filter(Persona.id == key).first()

        return persona

    def order_modules(self, modules):
        modules.sort(key=lambda x: x.id)
        mods_parents = []
        mods = {}
        while len(modules) > 0:
            module = modules.pop(0)
            module.children = []
            mods[module.id] = module
            parent_module = mods.get(module.fkmodulo, None)
            if parent_module:
                parent_module.children.append(module)
            else:
                mods_parents.append(module)
        return mods_parents
