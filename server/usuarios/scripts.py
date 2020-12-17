import hashlib
from server.database.connection import transaction
from .usuario.models import *
from .rol.models import Rol
from .ajuste.models import Ajuste


def insertions():
    with transaction() as session:
        user_m = session.query(Modulo).filter(Modulo.name == 'user_Modulo').first()
        if user_m is None:
            user_m = Modulo(title='Gestion de Usuarios Sigas', name='user_Modulo', icon='person')

        roles_m = session.query(Modulo).filter(Modulo.name == 'roles').first()
        if roles_m is None:
            roles_m = Modulo(title='Perfiles', route='/rol', name='roles', icon='dashboard')

        usuarios_m = session.query(Modulo).filter(Modulo.name == 'usuario').first()
        if usuarios_m is None:
            usuarios_m = Modulo(title='Usuario', route='/usuario', name='usuario', icon='account_box')

        perfil_m = session.query(Modulo).filter(Modulo.name == 'perfil').first()
        if perfil_m is None:
            perfil_m = Modulo(title='Perfil Usuario', route='/usuario_profile', name='perfil', icon='dvr')

        bitacora_m = session.query(Modulo).filter(Modulo.name == 'bitacora').first()
        if bitacora_m is None:
            bitacora_m = Modulo(title='Bitácora', route='/bitacora', name='bitacora', icon='dvr')

        ajuste_m = session.query(Modulo).filter(Modulo.name == 'ajuste').first()
        if ajuste_m is None:
            ajuste_m = Modulo(title='Ajustes', route='/ajuste', name='ajuste', icon='settings')

        user_m.children.append(roles_m)
        user_m.children.append(usuarios_m)
        user_m.children.append(perfil_m)
        user_m.children.append(bitacora_m)
        user_m.children.append(ajuste_m)

        query_rol = session.query(Modulo).filter(Modulo.name == 'rol_query').first()
        if query_rol is None:
            query_rol = Modulo(title='Consultar', route='', name='rol_query', menu=False)
        insert_rol = session.query(Modulo).filter(Modulo.name == 'rol_insert').first()
        if insert_rol is None:
            insert_rol = Modulo(title='Adicionar', route='/rol_insert', name='rol_insert', menu=False)
        update_rol = session.query(Modulo).filter(Modulo.name == 'rol_update').first()
        if update_rol is None:
            update_rol = Modulo(title='Actualizar', route='/rol_update', name='rol_update', menu=False)
        delete_rol = session.query(Modulo).filter(Modulo.name == 'rol_delete').first()
        if delete_rol is None:
            delete_rol = Modulo(title='Dar de Baja', route='/rol_delete', name='rol_delete', menu=False)

        roles_m.children.append(query_rol)
        roles_m.children.append(insert_rol)
        roles_m.children.append(update_rol)
        roles_m.children.append(delete_rol)

        query_usuario = session.query(Modulo).filter(Modulo.name == 'usuario_query').first()
        if query_usuario is None:
            query_usuario = Modulo(title='Consultar', route='', name='usuario_query', menu=False)
        insert_usuario = session.query(Modulo).filter(Modulo.name == 'usuario_insert').first()
        if insert_usuario is None:
            insert_usuario = Modulo(title='Adicionar', route='/usuario_insert', name='usuario_insert', menu=False)
        update_usuario = session.query(Modulo).filter(Modulo.name == 'usuario_update').first()
        if update_usuario is None:
            update_usuario = Modulo(title='Actualizar', route='/usuario_update', name='usuario_update', menu=False)
        state_usuario = session.query(Modulo).filter(Modulo.name == 'usuario_state').first()
        if state_usuario is None:
            state_usuario = Modulo(title='Habilitar', route='/usuario_state',
                                        name='usuario_state',menu=False)
        delete_usuario = session.query(Modulo).filter(Modulo.name == 'usuario_delete').first()
        if delete_usuario is None:
            delete_usuario = Modulo(title='Dar de Baja', route='/usuario_delete', name='usuario_delete', menu=False)

        sesion_usuario = session.query(Modulo).filter(Modulo.name == 'usuario_state').first()
        if sesion_usuario is None:
            sesion_usuario = Modulo(title='Session', route='/usuario_sesion',
                                        name='usuario_sesion',menu=False)

        usuarios_m.children.append(query_usuario)
        usuarios_m.children.append(insert_usuario)
        usuarios_m.children.append(update_usuario)
        usuarios_m.children.append(state_usuario)
        usuarios_m.children.append(delete_usuario)
        usuarios_m.children.append(sesion_usuario)

        query_bitacora = session.query(Modulo).filter(Modulo.name == 'bitacora_query').first()
        if query_bitacora is None:
            query_bitacora = Modulo(title='Consultar', route='', name='bitacora_query', menu=False)

        bitacora_m.children.append(query_bitacora)

        query_ajuste = session.query(Modulo).filter(Modulo.name == 'ajuste_query').first()
        if query_ajuste is None:
            query_ajuste = Modulo(title='Consultar', route='', name='ajuste_query', menu=False)
        insert_ajuste = session.query(Modulo).filter(Modulo.name == 'ajuste_insert').first()
        if insert_ajuste is None:
            insert_ajuste = Modulo(title='Adicionar', route='/ajuste_insert', name='ajuste_insert', menu=False)
        update_ajuste = session.query(Modulo).filter(Modulo.name == 'ajuste_update').first()
        if update_ajuste is None:
            update_ajuste = Modulo(title='Actualizar', route='/ajuste_update', name='ajuste_update', menu=False)
        delete_ajuste = session.query(Modulo).filter(Modulo.name == 'ajuste_delete').first()
        if delete_ajuste is None:
            delete_ajuste = Modulo(title='Dar de Baja', route='/ajuste_delete', name='ajuste_delete', menu=False)

        ajuste_m.children.append(query_ajuste)
        ajuste_m.children.append(insert_ajuste)
        ajuste_m.children.append(update_ajuste)
        ajuste_m.children.append(delete_ajuste)


        superadmin_role = session.query(Rol).filter(Rol.nombre == 'SUPER ADMINISTRADOR').first()
        if superadmin_role is None:
            superadmin_role = Rol(nombre='SUPER ADMINISTRADOR', descripcion='Todos los permisos')

        admin_role = session.query(Rol).filter(Rol.nombre == 'ADMINISTRADOR').first()
        if admin_role is None:
            admin_role = Rol(nombre='ADMINISTRADOR', descripcion='Permisos de Administrador')

        registrador_role = session.query(Rol).filter(Rol.nombre == 'REGISTRADOR').first()
        if registrador_role is None:
            registrador_role = Rol(nombre='REGISTRADOR', descripcion='')

        supervisor_role = session.query(Rol).filter(Rol.nombre == 'SUPERVISOR').first()
        if supervisor_role is None:
            supervisor_role = Rol(nombre='SUPERVISOR', descripcion='')


        operador_role = session.query(Rol).filter(Rol.nombre == 'OPERADOR').first()
        if operador_role is None:
            operador_role = Rol(nombre='OPERADOR', descripcion='')

        guardia_role = session.query(Rol).filter(Rol.nombre == 'GUARDIA').first()
        if guardia_role is None:
            guardia_role = Rol(nombre='GUARDIA', descripcion='')

        residente_role = session.query(Rol).filter(Rol.nombre == 'RESIDENTE').first()
        if residente_role is None:
            residente_role = Rol(nombre='RESIDENTE', descripcion='')


        ###Modulo de Usuarios
        superadmin_role.modulos.append(user_m)
        superadmin_role.modulos.append(roles_m)
        superadmin_role.modulos.append(usuarios_m)
        superadmin_role.modulos.append(perfil_m)
        superadmin_role.modulos.append(bitacora_m)
        superadmin_role.modulos.append(ajuste_m)
        superadmin_role.modulos.append(query_usuario)
        superadmin_role.modulos.append(insert_usuario)
        superadmin_role.modulos.append(update_usuario)
        superadmin_role.modulos.append(state_usuario)
        superadmin_role.modulos.append(delete_usuario)
        superadmin_role.modulos.append(sesion_usuario)
        superadmin_role.modulos.append(query_rol)
        superadmin_role.modulos.append(insert_rol)
        superadmin_role.modulos.append(update_rol)
        superadmin_role.modulos.append(delete_rol)
        superadmin_role.modulos.append(query_bitacora)
        superadmin_role.modulos.append(query_ajuste)
        superadmin_role.modulos.append(insert_ajuste)
        superadmin_role.modulos.append(update_ajuste)
        superadmin_role.modulos.append(delete_ajuste)

        admin_role.modulos.append(user_m)
        admin_role.modulos.append(usuarios_m)
        admin_role.modulos.append(perfil_m)
        admin_role.modulos.append(bitacora_m)
        admin_role.modulos.append(query_usuario)
        admin_role.modulos.append(insert_usuario)
        admin_role.modulos.append(update_usuario)
        admin_role.modulos.append(state_usuario)
        admin_role.modulos.append(delete_usuario)
        admin_role.modulos.append(sesion_usuario)
        admin_role.modulos.append(query_bitacora)

        super_user = session.query(Usuario).filter(Usuario.username == 'admin').first()
        if super_user is None:
            # hex_dig = hashlib.sha512(b'Password2020').hexdigest()
            hex_dig = hashlib.sha512(b'SigasProduccion2021').hexdigest()
            super_user = Usuario(username='admin', password=hex_dig,sigas=True)
            super_user.rol = superadmin_role

        servidor = ServidorCorreo(id=1, servidor='smtp.gmail.com', puerto='587',correo='NotificacionSigas@gmail.com', password='Sigas2020', estado=True)
        session.add(servidor)

        versionMovil = VersionMovil(id=1, version='0.6.7', estado=True)
        session.add(versionMovil)

        ajuste_web = Ajuste(id=1, claveSecreta='SECRETSIGAS', estado=True)
        session.add(ajuste_web)

        servidor = Principal(id=1, estado=False)
        session.add(servidor)

        session.add(super_user)
        session.add(superadmin_role)
        session.add(admin_role)
        session.add(supervisor_role)
        session.add(registrador_role)
        session.add(operador_role)
        session.add(guardia_role)
        session.add(residente_role)
        session.commit()
