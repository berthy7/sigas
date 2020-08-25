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
        session.add(Interprete(id=2, nombre='Servidor Demo'))

        session.add(Dispositivoeventos(codigo=0, nombre='Apertura', descripcion="In [Card Only] verification mode, the person has open door permission punch the card and triggers this normal event of open the door."))
        session.add(Dispositivoeventos(codigo=1, nombre='Apertura normal dentro de la zona horaria', descripcion="At the normally open period (set to normally open period of a single door or the door open period after the first card normally open), or through the remote normal open operation, the person has open door permission punch the effective card at the opened door to trigger this normal events."))
        session.add(Dispositivoeventos(codigo=2, nombre='1ra apertura nomarl(tarjeta accion)', descripcion="In [Card Only] verification mode, the person has first card normally open permission, punch card at the setting first card normally open period but the door is not opened, and trigger the normal event."))
        session.add(Dispositivoeventos(codigo=3, nombre='Multitarjeta abierta (tarjeta accionada)', descripcion="In [Card Only] verification mode, multi-card combination can be used to open the door. After the last piece of card verified, the system trigger this normal event."))
        session.add(Dispositivoeventos(codigo=4, nombre='Contraseña de emergencia abierta', descripcion="The password (also known as the super password) set for the current door can be used for door open. It will trigger this normal event after the emergency password verified."))
        session.add(Dispositivoeventos(codigo=5, nombre='Apertura normal durante la zona horaria abierto', descripcion="If the current door is set a normally open period, the door will open automatically after the setting start time, and trigger this normal event."))
        session.add(Dispositivoeventos(codigo=6, nombre='Evento de vinculación activado', descripcion="When the linkage setting the system takes effect, trigger this normal event."))
        session.add(Dispositivoeventos(codigo=7, nombre='Alarma Cancelada', descripcion="When the user cancel the alarm of the corresponding door, and the operation is success, trigger this normal event."))
        session.add(Dispositivoeventos(codigo=8, nombre='Apertura remota', descripcion="When the user opens a door from remote and the operation is successful, it will trigger this normal event."))
        session.add(Dispositivoeventos(codigo=9, nombre='Cierre remoto', descripcion="When the user close a door from remote and the operation is successful, it will trigger this normal event."))
        session.add(Dispositivoeventos(codigo=10, nombre='Deshabilitar la zona horaria de apertura normal intradía', descripcion="When the door is in Normally Open (NO) state, swipe your valid card five times through the reader or call ControlDevice to disable the NO period on that day. In this case, trigger this normal event."))
        session.add(Dispositivoeventos(codigo=11, nombre='Habilitar zona horaria de apertura normal intradía', descripcion="When the door’s NO period is disabled, swipe your valid card (held by the same user) five times through the reader or call ControlDevice to enable the NO period on that day. In this case, trigger this normal event."))
        session.add(Dispositivoeventos(codigo=12, nombre='Salida auxiliar abierta', descripcion="If the output point address is set to a specific auxiliary output point and the action type is set enabled in a linkage setting record, then this normal event will be triggered as long as this linkage setting takes effect."))
        session.add(Dispositivoeventos(codigo=13, nombre='Cerrar salida auxiliar', descripcion="Events that are triggered when you disable the auxiliary input through linkage operations or by calling ControlDevice."))
        session.add(Dispositivoeventos(codigo=14, nombre='Apertura huella presionada', descripcion="Normal events that are triggered after any person authorized to open the door presses his fingerprint and passes the verification in “Fingerprint only” or “Card/Fingerprint” verification modes."))
        session.add(Dispositivoeventos(codigo=15, nombre='Multitarjeta abierta (presione la huella digital)', descripcion="Multi-card open(Fingerprint required): normal events that are triggered when the last person opens the door with his fingerprint in “Finger print” verification mode."))
        session.add(Dispositivoeventos(codigo=16, nombre='Apertura huella presionada durante la zona horaria', descripcion="Normal events that are triggered after any person authorized to open the door presses his valid fingerprint during the NO duration (including the NO durations set for single doors and the first-card NO duration) and through remote operations."))
        session.add(Dispositivoeventos(codigo=17, nombre='Apertura tarjejta mas huella', descripcion="Normal events that are triggered after any person authorized to open the door swipes his card and presses his fingerprint to pass the verification in the “Card + Fingerprint” verification mode."))
        session.add(Dispositivoeventos(codigo=18, nombre='1ra Apertura (Presione huella)', descripcion="Normal events that are triggered after any person authorized to open the door becomes the first one to press his fingerprint and pass the verification during the preset first-card NO duration and in either the “Fingerprint only” or the “Card/Fingerprint” verification mode."))
        session.add(Dispositivoeventos(codigo=19, nombre='1ra Apertura (Tarjeta mas huella)', descripcion="Normal events that are triggered after any person authorized to open the door becomes the first one to swipe his card and press his fingerprint to pass the verification during the preset first-card NO duration and in the “Card + Fingerprint” verification mode."))
        session.add(Dispositivoeventos(codigo=20, nombre='Intervalo de accion demasiado corto', descripcion="When the interval between two card punching is less than the interval preset for the door, trigger this abnormal event."))
        session.add(Dispositivoeventos(codigo=21, nombre='Puerta Inactiva por Zona horaria (Tarjeta Accion)', descripcion="In [Card Only] verification mode, the user has the door open permission, punch card but not at the door effective period of time, and trigger this abnormal event."))
        session.add(Dispositivoeventos(codigo=22, nombre='Zona horaria ilegal', descripcion="The user with the permission of opening the current door, punches the card during the invalid time zone, and triggers this abnormal event."))
        session.add(Dispositivoeventos(codigo=23, nombre='Acceso denegado', descripcion="The registered card without the access permission of the current door, punch to open the door, triggers this abnormal event."))
        session.add(Dispositivoeventos(codigo=24, nombre='Anti Passback', descripcion="When the anti-pass back setting of the system takes effect, triggers this abnormal event."))
        session.add(Dispositivoeventos(codigo=25, nombre='Interlock', descripcion="When the interlocking rules of the system take effect, trigger this abnormal event."))
        session.add(Dispositivoeventos(codigo=26, nombre='Autenticación de múltiples tarjetas (tarjeta Accionada)', descripcion="Use multi-card combination to open the door, the card verification before the last one (whether verified or not), trigger this normal event."))
        session.add(Dispositivoeventos(codigo=27, nombre='Tarjeta no registrada', descripcion="Refers to the current card is not registered in the system, trigger this abnormal event."))
        session.add(Dispositivoeventos(codigo=28, nombre='Apertura tiempo agotado', descripcion="The door sensor detect that it is expired the delay time after opened, if not close the door, trigger this abnormal event."))
        session.add(Dispositivoeventos(codigo=29, nombre='Tarjeta Expirada', descripcion="The person with the door access permission, punch card to open the door after the effective time of the access control, can not be verified and will trigger this abnormal event."))
        session.add(Dispositivoeventos(codigo=30, nombre='Error de contraseña', descripcion="Use card plus password, duress password or emergency password to open the door, trigger this event if the password is wrong."))
        session.add(Dispositivoeventos(codigo=31, nombre='Intervalo de presión de huellas dactilares demasiado corto', descripcion="When the interval between two consecutive fingerprints is less than the interval preset for the door, trigger this abnormal event."))
        session.add(Dispositivoeventos(codigo=32, nombre='Autenticación de múltiples tarjetas (presione con huella)', descripcion="In either the “Fingerprint only” or the “Card/Fingerprint” verification mode, when any person presses his fingerprint to open the door through the multi-card access mode and before the last verification, trigger this event regardless of whether the verification attempt succeeds."))
        session.add(Dispositivoeventos(codigo=33, nombre='Huella expirada', descripcion="When any person fails to pass the verification with his fingerprint at the end of the access control duration preset by himself, trigger this event."))
        session.add(Dispositivoeventos(codigo=34, nombre='Huella no registrada', descripcion="Events that are triggered when any fingerprints are not registered in the system or registered but not synchronized to the device."))
        session.add(Dispositivoeventos(codigo=35, nombre='Puerta inactiva por Zona horaria (Presione con huella)', descripcion="Abnormal events that are triggered when any person authorized to open the door presses his fingerprint during the preset valid duration."))
        session.add(Dispositivoeventos(codigo=36, nombre='Puerta inactiva por Zona horaria (Botón de salida)', descripcion="Abnormal events that are triggered when any person fails to open the door by pressing the Unlock button during the preset valid duration."))
        session.add(Dispositivoeventos(codigo=37, nombre='Error al cerrar durante la zona horaria de apertura normal', descripcion="Abnormal events that are triggered when any person fails to close the door in NO state by calling ControlDevice."))
        session.add(Dispositivoeventos(codigo=101, nombre='Coacción apertura contraseña', descripcion="Use the duress password of current door verified and triggered"))
        session.add(Dispositivoeventos(codigo=102, nombre='Abierto accidentalmente', descripcion="Except all the normal events (normal events such as user with door open permission to punch card and open the door, password open door, open the door at normally open period, remote door open, the linkage triggered door open), the door sensor detect the door is opened, that is the door is unexpectedly opened."))
        session.add(Dispositivoeventos(codigo=103, nombre='Coacción apertura huella', descripcion="Use the duress fingerprint of current door verified and triggered alarm event."))
        session.add(Dispositivoeventos(codigo=200, nombre='Puerta abierta correctamente', descripcion="When the door sensor detects that the door has been properly opened, triggering this normal event."))
        session.add(Dispositivoeventos(codigo=201, nombre='Puerta cerrada correctamente', descripcion="When the door sensor detects that the door has been properly closed, triggering this normal event."))
        session.add(Dispositivoeventos(codigo=202, nombre='Botón de salida abierta', descripcion="User press the exit button to open the door within the door valid time zone, and trigger this normal event."))
        session.add(Dispositivoeventos(codigo=203, nombre='Apertura multitarjeta (tarjeta más huella digital)', descripcion="Normal events that are triggered when any person passes the verification with his card and fingerprint in multi-card access mode."))
        session.add(Dispositivoeventos(codigo=204, nombre='Apertura normal sobre Zona horaria', descripcion="After the setting normal open time zone, the door will close automatically. The normal open time zone include the normal open time zone in door setting and the selected normal open time zone in first card setting."))
        session.add(Dispositivoeventos(codigo=205, nombre='Apertura normal remota', descripcion="Normal events that are triggered when the door is set to the NO state for remote opening operations."))
        session.add(Dispositivoeventos(codigo=206, nombre='Inicio del dispositivo', descripcion="When the device is being activated, this normal event is triggered."))
        session.add(Dispositivoeventos(codigo=220, nombre='Entrada auxiliar desconectada', descripcion="When any auxiliary input point breaks down, this normal event is triggered."))
        session.add(Dispositivoeventos(codigo=221, nombre='Entrada auxiliar en corto', descripcion="When any auxiliary input point has short circuited, this normal event is triggered."))
        session.add(Dispositivoeventos(codigo=255, nombre='Esta obteniendo el estado de la puerta y alarma', descripcion="Ver documentacion adjunto 7."))


        session.commit()


def dispositivo_schedule():

    def conectar():
        pass
        # print("sincronizar dispositivo")

        # with transaction() as db:
        #     events = DispositivoManager(db).sdk()
        #     for e in events:
        #         if e.event_type == '221' and e.door == '1':
        #             print("Auxiliary input on door {} shorted at {}".format(e.door, e.time))
        #         elif e.event_type == '220' and e.door == '1':
        #             print("Auxiliary input on door {} released at {}".format(e.door, e.time))

    # schedule.every().day.at("19:18").do(conectar)
    # schedule.every(1).minutes.do(conectar)
