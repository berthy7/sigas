from server.database.connection import transaction
from ..usuarios.rol.models import *
from .dispositivo.managers import *

import schedule
import pytz



def insertions():
    with transaction() as session:
        ###Modulo de Operaciones

        dispositivos_m = session.query(Modulo).filter(Modulo.name == 'dispositivos').first()
        if dispositivos_m is None:
            dispositivos_m = Modulo(title='Gestion de Dispositivos', name='dispositivos', icon='devices_other')

        dispositivo_m = session.query(Modulo).filter(Modulo.name == 'dispositivo').first()
        if dispositivo_m is None:
            dispositivo_m = Modulo(title='Dispositivos', route='/dispositivo', name='dispositivo', icon='devices')

        config_acceso_m = session.query(Modulo).filter(Modulo.name == 'config_acceso').first()
        if config_acceso_m is None:
            config_acceso_m = Modulo(title='Configuracion de Acceso', route='/config_acceso', name='config_acceso', icon='settings_applications')

        registros_m = session.query(Modulo).filter(Modulo.name == 'registros').first()
        if registros_m is None:
            registros_m = Modulo(title='Registros', route='/registros', name='registros', icon='assignment')

        dispositivos_m.children.append(dispositivo_m)
        dispositivos_m.children.append(config_acceso_m)
        dispositivos_m.children.append(registros_m)

        query_dispositivo = session.query(Modulo).filter(Modulo.name == 'dispositivo_query').first()
        if query_dispositivo is None:
            query_dispositivo = Modulo(title='Consultar', route='',
                                       name='dispositivo_query',
                                       menu=False)

        insert_dispositivo = session.query(Modulo).filter(Modulo.name == 'dispositivo_insert').first()
        if insert_dispositivo is None:
            insert_dispositivo = Modulo(title='Adicionar', route='/dispositivo_insert',
                                        name='dispositivo_insert',
                                        menu=False)
        update_dispositivo = session.query(Modulo).filter(Modulo.name == 'dispositivo_update').first()
        if update_dispositivo is None:
            update_dispositivo = Modulo(title='Actualizar', route='/dispositivo_update',
                                        name='dispositivo_update',
                                        menu=False)
        delete_dispositivo = session.query(Modulo).filter(Modulo.name == 'dispositivo_delete').first()
        if delete_dispositivo is None:
            delete_dispositivo = Modulo(title='Dar de Baja', route='/dispositivo_delete',
                                        name='dispositivo_delete',
                                        menu=False)

        dispositivo_m.children.append(query_dispositivo)
        dispositivo_m.children.append(insert_dispositivo)
        dispositivo_m.children.append(update_dispositivo)
        dispositivo_m.children.append(delete_dispositivo)

        query_config_acceso = session.query(Modulo).filter(Modulo.name == 'config_acceso_query').first()
        if query_config_acceso is None:
            query_config_acceso = Modulo(title='Consultar', route='',
                                       name='config_acceso_query',
                                       menu=False)

        insert_config_acceso = session.query(Modulo).filter(Modulo.name == 'config_acceso_insert').first()
        if insert_config_acceso is None:
            insert_config_acceso = Modulo(title='Adicionar', route='/config_acceso_insert',
                                        name='config_acceso_insert',
                                        menu=False)
        update_config_acceso = session.query(Modulo).filter(Modulo.name == 'config_acceso_update').first()
        if update_config_acceso is None:
            update_config_acceso = Modulo(title='Actualizar', route='/config_acceso_update',
                                        name='config_acceso_update',
                                        menu=False)
        delete_config_acceso = session.query(Modulo).filter(Modulo.name == 'config_acceso_delete').first()
        if delete_config_acceso is None:
            delete_config_acceso = Modulo(title='Dar de Baja', route='/config_acceso_delete',
                                        name='config_acceso_delete',
                                        menu=False)

        config_acceso_m.children.append(query_config_acceso)
        config_acceso_m.children.append(insert_config_acceso)
        config_acceso_m.children.append(update_config_acceso)
        config_acceso_m.children.append(delete_config_acceso)


        query_registros = session.query(Modulo).filter(Modulo.name == 'registros_query').first()
        if query_registros is None:
            query_registros = Modulo(title='Consultar', route='',
                                    name='registros_query',
                                    menu=False)

        imprimir_registros = session.query(Modulo).filter(Modulo.name == 'registros_imprimir').first()
        if imprimir_registros is None:
            imprimir_registros = Modulo(title='Imprimir', route='/registros_imprimir',
                                       name='registros_imprimir',
                                       menu=False)

        registros_m.children.append(query_registros)
        registros_m.children.append(imprimir_registros)


        superadmin_role = session.query(Rol).filter(Rol.nombre == 'SUPER ADMINISTRADOR').first()
        admin_role = session.query(Rol).filter(Rol.nombre == 'ADMINISTRADOR').first()

        supervisor_role = session.query(Rol).filter(Rol.nombre == 'SUPERVISOR').first()
        operador_role = session.query(Rol).filter(Rol.nombre == 'OPERADOR').first()
        registrador_role = session.query(Rol).filter(Rol.nombre == 'REGISTRADOR').first()


        ###Modulos de Operaciones

        superadmin_role.modulos.append(dispositivos_m)
        superadmin_role.modulos.append(dispositivo_m)
        superadmin_role.modulos.append(config_acceso_m)
        superadmin_role.modulos.append(registros_m)


        admin_role.modulos.append(dispositivos_m)
        admin_role.modulos.append(dispositivo_m)
        admin_role.modulos.append(config_acceso_m)
        admin_role.modulos.append(registros_m)


        supervisor_role.modulos.append(dispositivos_m)
        supervisor_role.modulos.append(dispositivo_m)
        supervisor_role.modulos.append(config_acceso_m)
        supervisor_role.modulos.append(registros_m)

        operador_role.modulos.append(dispositivos_m)
        operador_role.modulos.append(dispositivo_m)
        operador_role.modulos.append(config_acceso_m)
        operador_role.modulos.append(registros_m)

        registrador_role.modulos.append(dispositivos_m)
        registrador_role.modulos.append(dispositivo_m)
        registrador_role.modulos.append(config_acceso_m)
        registrador_role.modulos.append(registros_m)


        superadmin_role.modulos.append(query_dispositivo)
        superadmin_role.modulos.append(insert_dispositivo)
        superadmin_role.modulos.append(update_dispositivo)
        superadmin_role.modulos.append(delete_dispositivo)

        superadmin_role.modulos.append(query_config_acceso)
        superadmin_role.modulos.append(insert_config_acceso)
        superadmin_role.modulos.append(update_config_acceso)
        superadmin_role.modulos.append(delete_config_acceso)

        superadmin_role.modulos.append(query_registros)
        superadmin_role.modulos.append(imprimir_registros)

        admin_role.modulos.append(query_dispositivo)
        admin_role.modulos.append(insert_dispositivo)
        admin_role.modulos.append(update_dispositivo)
        admin_role.modulos.append(delete_dispositivo)

        admin_role.modulos.append(query_config_acceso)
        admin_role.modulos.append(insert_config_acceso)
        admin_role.modulos.append(update_config_acceso)
        admin_role.modulos.append(delete_config_acceso)

        admin_role.modulos.append(query_registros)
        admin_role.modulos.append(imprimir_registros)

        supervisor_role.modulos.append(query_dispositivo)
        supervisor_role.modulos.append(insert_dispositivo)
        supervisor_role.modulos.append(update_dispositivo)
        supervisor_role.modulos.append(delete_dispositivo)

        supervisor_role.modulos.append(query_config_acceso)
        supervisor_role.modulos.append(insert_config_acceso)
        supervisor_role.modulos.append(update_config_acceso)
        supervisor_role.modulos.append(delete_config_acceso)

        supervisor_role.modulos.append(query_registros)
        supervisor_role.modulos.append(imprimir_registros)

        registrador_role.modulos.append(query_dispositivo)
        registrador_role.modulos.append(insert_dispositivo)
        registrador_role.modulos.append(update_dispositivo)
        registrador_role.modulos.append(delete_dispositivo)

        registrador_role.modulos.append(query_config_acceso)
        registrador_role.modulos.append(insert_config_acceso)
        registrador_role.modulos.append(update_config_acceso)
        registrador_role.modulos.append(delete_config_acceso)

        registrador_role.modulos.append(query_registros)
        registrador_role.modulos.append(imprimir_registros)

        operador_role.modulos.append(query_dispositivo)
        operador_role.modulos.append(insert_dispositivo)
        operador_role.modulos.append(update_dispositivo)
        operador_role.modulos.append(delete_dispositivo)

        operador_role.modulos.append(query_config_acceso)
        operador_role.modulos.append(insert_config_acceso)
        operador_role.modulos.append(update_config_acceso)
        operador_role.modulos.append(delete_config_acceso)

        operador_role.modulos.append(query_registros)
        operador_role.modulos.append(imprimir_registros)

        session.add(Tipodispositivo(id=1,nombre='Controlador de 1 Cerradura'))
        session.add(Tipodispositivo(id=2,nombre='Controlador de 2 Cerraduras'))
        session.add(Tipodispositivo(id=3,nombre='Controlador de 4 Cerraduras'))
        session.add(Tipodispositivo(id=4,nombre='Terminal Biometrico'))

        session.add(Interprete(id=1, nombre='Servidor Ciudad Jardin'))
        session.add(Interprete(id=3, nombre='Servidor Demo'))

        session.commit()


def dispositivo_schedule():

    def conectar():

        with transaction() as db:
            events = DispositivoManager(db).sdk()
            for e in events:
                if e.event_type == '221' and e.door == '1':
                    print("Auxiliary input on door {} shorted at {}".format(e.door, e.time))
                elif e.event_type == '220' and e.door == '1':
                    print("Auxiliary input on door {} released at {}".format(e.door, e.time))

    # schedule.every().day.at("19:18").do(conectar)
    # schedule.every(0.05).minutes.do(conectar)
