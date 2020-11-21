from server.database.connection import transaction
from ..usuarios.rol.models import *
from .domicilio.models import *
from .evento.models import *
from .evento.managers import *
from .movimiento.models import *
from .condominio.models import *

from .residente.models import *

import schedule
import pytz


def insertions():
    with transaction() as session:
        ###Modulo de Operaciones

        condominios_m = session.query(Modulo).filter(Modulo.name == 'condominios').first()
        if condominios_m is None:
            condominios_m = Modulo(title='Gestion de Condominio', name='condominios', icon='domain')

        condominio_m = session.query(Modulo).filter(Modulo.name == 'condominio').first()
        if condominio_m is None:
            condominio_m = Modulo(title='Condominios', route='/condominio', name='condominio', icon='location_city')

        nropase_m = session.query(Modulo).filter(Modulo.name == 'condominio').first()
        if nropase_m is None:
            nropase_m = Modulo(title='Cant. de Tarjetas', route='/nropase', name='nropase', icon='credit_card')

        usuarioCondominio_m = session.query(Modulo).filter(Modulo.name == 'usuarioCondominio').first()
        if usuarioCondominio_m is None:
            usuarioCondominio_m = Modulo(title='Usuarios', route='/usuarioCondominio', name='usuarioCondominio', icon='assignment_ind')

        areasocial_m = session.query(Modulo).filter(Modulo.name == 'areasocial').first()
        if areasocial_m is None:
            areasocial_m = Modulo(title='Areas Social', route='/areasocial', name='areasocial', icon='account_balance')

        domicilio_m = session.query(Modulo).filter(Modulo.name == 'domicilio').first()
        if domicilio_m is None:
            domicilio_m = Modulo(title='Domicilios', route='/domicilio', name='domicilio', icon='home')

        gvehiculos_m = session.query(Modulo).filter(Modulo.name == 'gvehiculos').first()
        if gvehiculos_m is None:
            gvehiculos_m = Modulo(title='Gestion de Vehiculos', name='gvehiculos', icon='book')

        marca_m = session.query(Modulo).filter(Modulo.name == 'marca').first()
        if marca_m is None:
            marca_m = Modulo(title='Marcas', route='/marca', name='marca', icon='directions_car')

        modelo_m = session.query(Modulo).filter(Modulo.name == 'modelo').first()
        if modelo_m is None:
            modelo_m = Modulo(title='Modelos', route='/modelo', name='modelo', icon='directions_car')

        vehiculo_m = session.query(Modulo).filter(Modulo.name == 'vehiculo').first()
        if vehiculo_m is None:
            vehiculo_m = Modulo(title='Vehiculos', route='/vehiculo', name='vehiculo', icon='directions_car')

        provper_m = session.query(Modulo).filter(Modulo.name == 'provper').first()
        if provper_m is None:
            provper_m = Modulo(title='Prov. Permanentes', route='/provper', name='provper', icon='people')

        residente_m = session.query(Modulo).filter(Modulo.name == 'residente').first()
        if residente_m is None:
            residente_m = Modulo(title='Residentes', route='/residente', name='residente', icon='people_outline')

        evento_m = session.query(Modulo).filter(Modulo.name == 'evento').first()
        if evento_m is None:
            evento_m = Modulo(title='Eventos', route='/evento', name='evento', icon='event')

        invitado_m = session.query(Modulo).filter(Modulo.name == 'invitado').first()
        if invitado_m is None:
            invitado_m = Modulo(title='Invitados', route='/invitado', name='invitado', icon='person_add')

        movimiento_m = session.query(Modulo).filter(Modulo.name == 'movimiento').first()
        if movimiento_m is None:
            movimiento_m = Modulo(title='Control y Registro Vehicular', route='/movimiento', name='movimiento', icon='control_point')

        movimiento_p_m = session.query(Modulo).filter(Modulo.name == 'movimiento_p').first()
        if movimiento_p_m is None:
            movimiento_p_m = Modulo(title='Control y Registro Peatonal', route='/movimiento_p', name='movimiento_p', icon='control_point')

        portero_virtual_m = session.query(Modulo).filter(Modulo.name == 'portero_virtual').first()
        if portero_virtual_m is None:
            portero_virtual_m = Modulo(title='Portero Virtual', route='/portero_virtual', name='portero_virtual', icon='control_point')

        reporte_m = session.query(Modulo).filter(Modulo.name == 'reporte').first()
        if reporte_m is None:
            reporte_m = Modulo(title='Reportes', route='/reporte', name='reporte', icon='content_paste')

        registros_c_m = session.query(Modulo).filter(Modulo.name == 'registros_c').first()
        if registros_c_m is None:
            registros_c_m = Modulo(title='Registros', route='/registros_c', name='registros_c', icon='assignment')

        condominios_m.children.append(condominio_m)
        condominios_m.children.append(nropase_m)
        condominios_m.children.append(usuarioCondominio_m)
        condominios_m.children.append(areasocial_m)
        condominios_m.children.append(domicilio_m)
        condominios_m.children.append(gvehiculos_m)
        condominios_m.children.append(provper_m)
        condominios_m.children.append(residente_m)
        condominios_m.children.append(evento_m)
        condominios_m.children.append(invitado_m)
        condominios_m.children.append(movimiento_m)
        condominios_m.children.append(movimiento_p_m)
        condominios_m.children.append(portero_virtual_m)
        condominios_m.children.append(reporte_m)
        condominios_m.children.append(registros_c_m)

        gvehiculos_m.children.append(marca_m)
        gvehiculos_m.children.append(modelo_m)
        gvehiculos_m.children.append(vehiculo_m)


        query_condominio = session.query(Modulo).filter(Modulo.name == 'condominio_query').first()
        if query_condominio is None:
            query_condominio = Modulo(title='Consultar', route='',
                                   name='condominio_query',
                                   menu=False)

        insert_condominio = session.query(Modulo).filter(Modulo.name == 'condominio_insert').first()
        if insert_condominio is None:
            insert_condominio = Modulo(title='Adicionar', route='/condominio_insert',
                                    name='condominio_insert',
                                    menu=False)
        update_condominio = session.query(Modulo).filter(Modulo.name == 'condominio_update').first()
        if update_condominio is None:
            update_condominio = Modulo(title='Actualizar', route='/condominio_update',
                                    name='condominio_update',
                                    menu=False)
        delete_condominio = session.query(Modulo).filter(Modulo.name == 'condominio_delete').first()
        if delete_condominio is None:
            delete_condominio = Modulo(title='Dar de Baja', route='/condominio_delete',
                                    name='condominio_delete',
                                    menu=False)

        imprimir_condominio = session.query(Modulo).filter(Modulo.name == 'condominio_imprimir').first()
        if imprimir_condominio is None:
            imprimir_condominio = Modulo(title='Reportes', route='/condominio_imprimir',
                                      name='condominio_imprimir',
                                      menu=False)

        condominio_m.children.append(query_condominio)
        condominio_m.children.append(insert_condominio)
        condominio_m.children.append(update_condominio)
        condominio_m.children.append(delete_condominio)
        condominio_m.children.append(imprimir_condominio)

        query_nropase = session.query(Modulo).filter(Modulo.name == 'nropase_query').first()
        if query_nropase is None:
            query_nropase = Modulo(title='Consultar', route='',
                                   name='nropase_query',
                                   menu=False)

        insert_nropase = session.query(Modulo).filter(Modulo.name == 'nropase_insert').first()
        if insert_nropase is None:
            insert_nropase = Modulo(title='Adicionar', route='/nropase_insert',
                                    name='nropase_insert',
                                    menu=False)
        update_nropase = session.query(Modulo).filter(Modulo.name == 'nropase_update').first()
        if update_nropase is None:
            update_nropase = Modulo(title='Actualizar', route='/nropase_update',
                                    name='nropase_update',
                                    menu=False)
        delete_nropase = session.query(Modulo).filter(Modulo.name == 'nropase_delete').first()
        if delete_nropase is None:
            delete_nropase = Modulo(title='Dar de Baja', route='/nropase_delete',
                                    name='nropase_delete',
                                    menu=False)

        importar_nropase = session.query(Modulo).filter(Modulo.name == 'nropase_importar').first()
        if importar_nropase is None:
            importar_nropase = Modulo(title='Dar de Baja', route='/nropase_importar',
                                    name='nropase_importar',
                                    menu=False)

        imprimir_nropase = session.query(Modulo).filter(Modulo.name == 'nropase_imprimir').first()
        if imprimir_nropase is None:
            imprimir_nropase = Modulo(title='Reportes', route='/nropase_imprimir',
                                      name='nropase_imprimir',
                                      menu=False)

        nropase_m.children.append(query_nropase)
        nropase_m.children.append(insert_nropase)
        nropase_m.children.append(update_nropase)
        nropase_m.children.append(delete_nropase)
        nropase_m.children.append(importar_nropase)
        nropase_m.children.append(imprimir_nropase)

        query_usuarioCondominio = session.query(Modulo).filter(Modulo.name == 'usuarioCondominio_query').first()
        if query_usuarioCondominio is None:
            query_usuarioCondominio = Modulo(title='Consultar', route='',
                                   name='usuarioCondominio_query',
                                   menu=False)

        insert_usuarioCondominio = session.query(Modulo).filter(Modulo.name == 'usuarioCondominio_insert').first()
        if insert_usuarioCondominio is None:
            insert_usuarioCondominio = Modulo(title='Adicionar', route='/usuarioCondominio_insert',
                                    name='usuarioCondominio_insert',
                                    menu=False)
        update_usuarioCondominio = session.query(Modulo).filter(Modulo.name == 'usuarioCondominio_update').first()
        if update_usuarioCondominio is None:
            update_usuarioCondominio = Modulo(title='Actualizar', route='/usuarioCondominio_update',
                                    name='usuarioCondominio_update',
                                    menu=False)
        delete_usuarioCondominio = session.query(Modulo).filter(Modulo.name == 'usuarioCondominio_delete').first()
        if delete_usuarioCondominio is None:
            delete_usuarioCondominio = Modulo(title='Dar de Baja', route='/usuarioCondominio_delete',
                                    name='usuarioCondominio_delete',
                                    menu=False)

        imprimir_usuarioCondominio = session.query(Modulo).filter(Modulo.name == 'usuarioCondominio_imprimir').first()
        if imprimir_usuarioCondominio is None:
            imprimir_usuarioCondominio = Modulo(title='Reportes', route='/usuarioCondominio_imprimir',
                                      name='usuarioCondominio_imprimir',
                                      menu=False)

        usuarioCondominio_m.children.append(query_usuarioCondominio)
        usuarioCondominio_m.children.append(insert_usuarioCondominio)
        usuarioCondominio_m.children.append(update_usuarioCondominio)
        usuarioCondominio_m.children.append(delete_usuarioCondominio)
        usuarioCondominio_m.children.append(imprimir_usuarioCondominio)

        query_areasocial = session.query(Modulo).filter(Modulo.name == 'areasocial_query').first()
        if query_areasocial is None:
            query_areasocial = Modulo(title='Consultar', route='',
                                   name='areasocial_query',
                                   menu=False)

        insert_areasocial = session.query(Modulo).filter(Modulo.name == 'areasocial_insert').first()
        if insert_areasocial is None:
            insert_areasocial = Modulo(title='Adicionar', route='/areasocial_insert',
                                    name='areasocial_insert',
                                    menu=False)
        update_areasocial = session.query(Modulo).filter(Modulo.name == 'areasocial_update').first()
        if update_areasocial is None:
            update_areasocial = Modulo(title='Actualizar', route='/areasocial_update',
                                    name='areasocial_update',
                                    menu=False)
        delete_areasocial = session.query(Modulo).filter(Modulo.name == 'areasocial_delete').first()
        if delete_areasocial is None:
            delete_areasocial = Modulo(title='Dar de Baja', route='/areasocial_delete',
                                    name='areasocial_delete',
                                    menu=False)

        imprimir_areasocial = session.query(Modulo).filter(Modulo.name == 'areasocial_imprimir').first()
        if imprimir_areasocial is None:
            imprimir_areasocial = Modulo(title='Reportes', route='/areasocial_imprimir',
                                      name='areasocial_imprimir',
                                      menu=False)

        filtrar_areasocial = session.query(Modulo).filter(Modulo.name == 'areasocial_filtrar').first()
        if filtrar_areasocial is None:
            filtrar_areasocial = Modulo(title='Filtrar', route='/areasocial_filtrar',
                                      name='areasocial_filtrar',
                                      menu=False)

        areasocial_m.children.append(query_areasocial)
        areasocial_m.children.append(insert_areasocial)
        areasocial_m.children.append(update_areasocial)
        areasocial_m.children.append(delete_areasocial)
        areasocial_m.children.append(imprimir_areasocial)
        areasocial_m.children.append(filtrar_areasocial)

        query_domicilio = session.query(Modulo).filter(Modulo.name == 'domicilio_query').first()
        if query_domicilio is None:
            query_domicilio = Modulo(title='Consultar', route='',
                                   name='domicilio_query',
                                   menu=False)

        insert_domicilio = session.query(Modulo).filter(Modulo.name == 'domicilio_insert').first()
        if insert_domicilio is None:
            insert_domicilio = Modulo(title='Adicionar', route='/domicilio_insert',
                                    name='domicilio_insert',
                                    menu=False)
        update_domicilio = session.query(Modulo).filter(Modulo.name == 'domicilio_update').first()
        if update_domicilio is None:
            update_domicilio = Modulo(title='Actualizar', route='/domicilio_update',
                                    name='domicilio_update',
                                    menu=False)
        delete_domicilio = session.query(Modulo).filter(Modulo.name == 'domicilio_delete').first()
        if delete_domicilio is None:
            delete_domicilio = Modulo(title='Dar de Baja', route='/domicilio_delete',
                                    name='domicilio_delete',
                                    menu=False)

        imprimir_domicilio = session.query(Modulo).filter(Modulo.name == 'domicilio_imprimir').first()
        if imprimir_domicilio is None:
            imprimir_domicilio = Modulo(title='Reportes', route='/domicilio_imprimir',
                                      name='domicilio_imprimir',
                                      menu=False)

        filtrar_domicilio = session.query(Modulo).filter(Modulo.name == 'domicilio_filtrar').first()
        if filtrar_domicilio is None:
            filtrar_domicilio = Modulo(title='Filtrar', route='/domicilio_filtrar',
                                      name='domicilio_filtrar',
                                      menu=False)
        domicilio_m.children.append(query_domicilio)
        domicilio_m.children.append(insert_domicilio)
        domicilio_m.children.append(update_domicilio)
        domicilio_m.children.append(delete_domicilio)
        domicilio_m.children.append(imprimir_domicilio)
        domicilio_m.children.append(filtrar_domicilio)

        query_provper = session.query(Modulo).filter(Modulo.name == 'provper_query').first()
        if query_provper is None:
            query_provper = Modulo(title='Consultar', route='',
                                   name='provper_query',
                                   menu=False)

        insert_provper = session.query(Modulo).filter(Modulo.name == 'provper_insert').first()
        if insert_provper is None:
            insert_provper = Modulo(title='Adicionar', route='/provper_insert',
                                    name='provper_insert',
                                    menu=False)
        update_provper = session.query(Modulo).filter(Modulo.name == 'provper_update').first()
        if update_provper is None:
            update_provper = Modulo(title='Actualizar', route='/provper_update',
                                    name='provper_update',
                                    menu=False)
        delete_provper = session.query(Modulo).filter(Modulo.name == 'provper_delete').first()
        if delete_provper is None:
            delete_provper = Modulo(title='Dar de Baja', route='/provper_delete',
                                    name='provper_delete',
                                    menu=False)

        imprimir_provper = session.query(Modulo).filter(Modulo.name == 'provper_imprimir').first()
        if imprimir_provper is None:
            imprimir_provper = Modulo(title='Reportes', route='/provper_imprimir',
                                      name='provper_imprimir',
                                      menu=False)

        provper_m.children.append(query_provper)
        provper_m.children.append(insert_provper)
        provper_m.children.append(update_provper)
        provper_m.children.append(delete_provper)
        provper_m.children.append(imprimir_provper)

        query_residente = session.query(Modulo).filter(Modulo.name == 'residente_query').first()
        if query_residente is None:
            query_residente = Modulo(title='Consultar', route='',
                                   name='residente_query',
                                   menu=False)

        insert_residente = session.query(Modulo).filter(Modulo.name == 'residente_insert').first()
        if insert_residente is None:
            insert_residente = Modulo(title='Adicionar', route='/residente_insert',
                                    name='residente_insert',
                                    menu=False)
        update_residente = session.query(Modulo).filter(Modulo.name == 'residente_update').first()
        if update_residente is None:
            update_residente = Modulo(title='Actualizar', route='/residente_update',
                                    name='residente_update',
                                    menu=False)
        delete_residente = session.query(Modulo).filter(Modulo.name == 'residente_delete').first()
        if delete_residente is None:
            delete_residente = Modulo(title='Dar de Baja', route='/residente_delete',
                                    name='residente_delete',
                                    menu=False)

        imprimir_residente = session.query(Modulo).filter(Modulo.name == 'residente_imprimir').first()
        if imprimir_residente is None:
            imprimir_residente = Modulo(title='Reportes', route='/residente_imprimir',
                                      name='residente_imprimir',
                                      menu=False)

        residente_m.children.append(query_residente)
        residente_m.children.append(insert_residente)
        residente_m.children.append(update_residente)
        residente_m.children.append(delete_residente)
        residente_m.children.append(imprimir_residente)

        query_marca = session.query(Modulo).filter(Modulo.name == 'marca_query').first()
        if query_marca is None:
            query_marca = Modulo(title='Consultar', route='',
                                   name='marca_query',
                                   menu=False)

        insert_marca = session.query(Modulo).filter(Modulo.name == 'marca_insert').first()
        if insert_marca is None:
            insert_marca = Modulo(title='Adicionar', route='/marca_insert',
                                    name='marca_insert',
                                    menu=False)
        update_marca = session.query(Modulo).filter(Modulo.name == 'marca_update').first()
        if update_marca is None:
            update_marca = Modulo(title='Actualizar', route='/marca_update',
                                    name='marca_update',
                                    menu=False)
        delete_marca = session.query(Modulo).filter(Modulo.name == 'marca_delete').first()
        if delete_marca is None:
            delete_marca = Modulo(title='Dar de Baja', route='/marca_delete',
                                    name='marca_delete',
                                    menu=False)

        imprimir_marca = session.query(Modulo).filter(Modulo.name == 'marca_imprimir').first()
        if imprimir_marca is None:
            imprimir_marca = Modulo(title='Reportes', route='/marca_imprimir',
                                      name='marca_imprimir',
                                      menu=False)

        marca_m.children.append(query_marca)
        marca_m.children.append(insert_marca)
        marca_m.children.append(update_marca)
        marca_m.children.append(delete_marca)
        marca_m.children.append(imprimir_marca)

        query_modelo = session.query(Modulo).filter(Modulo.name == 'modelo_query').first()
        if query_modelo is None:
            query_modelo = Modulo(title='Consultar', route='',
                                   name='modelo_query',
                                   menu=False)

        insert_modelo = session.query(Modulo).filter(Modulo.name == 'modelo_insert').first()
        if insert_modelo is None:
            insert_modelo = Modulo(title='Adicionar', route='/modelo_insert',
                                    name='modelo_insert',
                                    menu=False)
        update_modelo = session.query(Modulo).filter(Modulo.name == 'modelo_update').first()
        if update_modelo is None:
            update_modelo = Modulo(title='Actualizar', route='/modelo_update',
                                    name='modelo_update',
                                    menu=False)
        delete_modelo = session.query(Modulo).filter(Modulo.name == 'modelo_delete').first()
        if delete_modelo is None:
            delete_modelo = Modulo(title='Dar de Baja', route='/modelo_delete',
                                    name='modelo_delete',
                                    menu=False)

        imprimir_modelo = session.query(Modulo).filter(Modulo.name == 'modelo_imprimir').first()
        if imprimir_modelo is None:
            imprimir_modelo = Modulo(title='Reportes', route='/modelo_imprimir',
                                      name='modelo_imprimir',
                                      menu=False)

        modelo_m.children.append(query_modelo)
        modelo_m.children.append(insert_modelo)
        modelo_m.children.append(update_modelo)
        modelo_m.children.append(delete_modelo)
        modelo_m.children.append(imprimir_modelo)

        query_vehiculo = session.query(Modulo).filter(Modulo.name == 'vehiculo_query').first()
        if query_vehiculo is None:
            query_vehiculo = Modulo(title='Consultar', route='',
                                   name='vehiculo_query',
                                   menu=False)

        insert_vehiculo = session.query(Modulo).filter(Modulo.name == 'vehiculo_insert').first()
        if insert_vehiculo is None:
            insert_vehiculo = Modulo(title='Adicionar', route='/vehiculo_insert',
                                    name='vehiculo_insert',
                                    menu=False)
        update_vehiculo = session.query(Modulo).filter(Modulo.name == 'vehiculo_update').first()
        if update_vehiculo is None:
            update_vehiculo = Modulo(title='Actualizar', route='/vehiculo_update',
                                    name='vehiculo_update',
                                    menu=False)
        delete_vehiculo = session.query(Modulo).filter(Modulo.name == 'vehiculo_delete').first()
        if delete_vehiculo is None:
            delete_vehiculo = Modulo(title='Dar de Baja', route='/vehiculo_delete',
                                    name='vehiculo_delete',
                                    menu=False)

        imprimir_vehiculo = session.query(Modulo).filter(Modulo.name == 'vehiculo_imprimir').first()
        if imprimir_vehiculo is None:
            imprimir_vehiculo = Modulo(title='Reportes', route='/vehiculo_imprimir',
                                      name='vehiculo_imprimir',
                                      menu=False)

        vehiculo_m.children.append(query_vehiculo)
        vehiculo_m.children.append(insert_vehiculo)
        vehiculo_m.children.append(update_vehiculo)
        vehiculo_m.children.append(delete_vehiculo)
        vehiculo_m.children.append(imprimir_vehiculo)

        query_evento = session.query(Modulo).filter(Modulo.name == 'evento_query').first()
        if query_evento is None:
            query_evento = Modulo(title='Consultar', route='',
                                  name='evento_query',
                                  menu=False)

        insert_evento = session.query(Modulo).filter(Modulo.name == 'evento_insert').first()
        if insert_evento is None:
            insert_evento = Modulo(title='Adicionar', route='/evento_insert',
                                   name='evento_insert',
                                   menu=False)
        update_evento = session.query(Modulo).filter(Modulo.name == 'evento_update').first()
        if update_evento is None:
            update_evento = Modulo(title='Actualizar', route='/evento_update',
                                   name='evento_update',
                                   menu=False)
        delete_evento = session.query(Modulo).filter(Modulo.name == 'evento_delete').first()
        if delete_evento is None:
            delete_evento = Modulo(title='Dar de Baja', route='/evento_delete',
                                   name='evento_delete',
                                   menu=False)

        imprimir_evento = session.query(Modulo).filter(Modulo.name == 'evento_imprimir').first()
        if imprimir_evento is None:
            imprimir_evento = Modulo(title='Reportes', route='/evento_imprimir',
                                     name='evento_imprimir',
                                     menu=False)

        evento_m.children.append(query_evento)
        evento_m.children.append(insert_evento)
        evento_m.children.append(update_evento)
        evento_m.children.append(delete_evento)
        evento_m.children.append(imprimir_evento)

        query_invitado = session.query(Modulo).filter(Modulo.name == 'invitado_query').first()
        if query_invitado is None:
            query_invitado = Modulo(title='Consultar', route='',
                                   name='invitado_query',
                                   menu=False)

        insert_invitado = session.query(Modulo).filter(Modulo.name == 'invitado_insert').first()
        if insert_invitado is None:
            insert_invitado = Modulo(title='Adicionar', route='/invitado_insert',
                                    name='invitado_insert',
                                    menu=False)
        update_invitado = session.query(Modulo).filter(Modulo.name == 'invitado_update').first()
        if update_invitado is None:
            update_invitado = Modulo(title='Actualizar', route='/invitado_update',
                                    name='invitado_update',
                                    menu=False)
        delete_invitado = session.query(Modulo).filter(Modulo.name == 'invitado_delete').first()
        if delete_invitado is None:
            delete_invitado = Modulo(title='Dar de Baja', route='/invitado_delete',
                                    name='invitado_delete',
                                    menu=False)

        imprimir_invitado = session.query(Modulo).filter(Modulo.name == 'invitado_imprimir').first()
        if imprimir_invitado is None:
            imprimir_invitado = Modulo(title='Reportes', route='/invitado_imprimir',
                                      name='invitado_imprimir',
                                      menu=False)

        invitado_m.children.append(query_invitado)
        invitado_m.children.append(insert_invitado)
        invitado_m.children.append(update_invitado)
        invitado_m.children.append(delete_invitado)
        invitado_m.children.append(imprimir_invitado)

        query_movimiento = session.query(Modulo).filter(Modulo.name == 'movimiento_query').first()
        if query_movimiento is None:
            query_movimiento = Modulo(title='Consultar', route='',
                                  name='movimiento_query',
                                  menu=False)

        insert_movimiento = session.query(Modulo).filter(Modulo.name == 'movimiento_insert').first()
        if insert_movimiento is None:
            insert_movimiento = Modulo(title='Adicionar', route='/movimiento_insert',
                                   name='movimiento_insert',
                                   menu=False)
        update_movimiento = session.query(Modulo).filter(Modulo.name == 'movimiento_update').first()
        if update_movimiento is None:
            update_movimiento = Modulo(title='Actualizar', route='/movimiento_update',
                                   name='movimiento_update',
                                   menu=False)
        delete_movimiento = session.query(Modulo).filter(Modulo.name == 'movimiento_delete').first()
        if delete_movimiento is None:
            delete_movimiento = Modulo(title='Dar de Baja', route='/movimiento_delete',
                                   name='movimiento_delete',
                                   menu=False)

        imprimir_movimiento = session.query(Modulo).filter(Modulo.name == 'movimiento_imprimir').first()
        if imprimir_movimiento is None:
            imprimir_movimiento = Modulo(title='Reportes', route='/movimiento_imprimir',
                                     name='movimiento_imprimir',
                                     menu=False)

        movimiento_m.children.append(query_movimiento)
        movimiento_m.children.append(insert_movimiento)
        movimiento_m.children.append(update_movimiento)
        movimiento_m.children.append(delete_movimiento)
        movimiento_m.children.append(imprimir_movimiento)

        query_movimiento_p = session.query(Modulo).filter(Modulo.name == 'movimiento_p_query').first()
        if query_movimiento_p is None:
            query_movimiento_p = Modulo(title='Consultar', route='',
                                  name='movimiento_p_query',
                                  menu=False)

        insert_movimiento_p = session.query(Modulo).filter(Modulo.name == 'movimiento_p_insert').first()
        if insert_movimiento_p is None:
            insert_movimiento_p = Modulo(title='Adicionar', route='/movimiento_p_insert',
                                   name='movimiento_p_insert',
                                   menu=False)
        update_movimiento_p = session.query(Modulo).filter(Modulo.name == 'movimiento_p_update').first()
        if update_movimiento_p is None:
            update_movimiento_p = Modulo(title='Actualizar', route='/movimiento_p_update',
                                   name='movimiento_p_update',
                                   menu=False)
        delete_movimiento_p = session.query(Modulo).filter(Modulo.name == 'movimiento_p_delete').first()
        if delete_movimiento_p is None:
            delete_movimiento_p = Modulo(title='Dar de Baja', route='/movimiento_p_delete',
                                   name='movimiento_p_delete',
                                   menu=False)

        imprimir_movimiento_p = session.query(Modulo).filter(Modulo.name == 'movimiento_p_imprimir').first()
        if imprimir_movimiento_p is None:
            imprimir_movimiento_p = Modulo(title='Reportes', route='/movimiento_p_imprimir',
                                     name='movimiento_p_imprimir',
                                     menu=False)

        movimiento_p_m.children.append(query_movimiento_p)
        movimiento_p_m.children.append(insert_movimiento_p)
        movimiento_p_m.children.append(update_movimiento_p)
        movimiento_p_m.children.append(delete_movimiento_p)
        movimiento_p_m.children.append(imprimir_movimiento_p)

        query_portero_virtual = session.query(Modulo).filter(Modulo.name == 'portero_virtual_query').first()
        if query_portero_virtual is None:
            query_portero_virtual = Modulo(title='Consultar', route='',
                                  name='portero_virtual_query',
                                  menu=False)

        insert_portero_virtual = session.query(Modulo).filter(Modulo.name == 'portero_virtual_insert').first()
        if insert_portero_virtual is None:
            insert_portero_virtual = Modulo(title='Adicionar', route='/portero_virtual_insert',
                                   name='portero_virtual_insert',
                                   menu=False)
        update_portero_virtual = session.query(Modulo).filter(Modulo.name == 'portero_virtual_update').first()
        if update_portero_virtual is None:
            update_portero_virtual = Modulo(title='Actualizar', route='/portero_virtual_update',
                                   name='portero_virtual_update',
                                   menu=False)
        delete_portero_virtual = session.query(Modulo).filter(Modulo.name == 'portero_virtual_delete').first()
        if delete_portero_virtual is None:
            delete_portero_virtual = Modulo(title='Dar de Baja', route='/portero_virtual_delete',
                                   name='portero_virtual_delete',
                                   menu=False)

        imprimir_portero_virtual = session.query(Modulo).filter(Modulo.name == 'portero_virtual_imprimir').first()
        if imprimir_portero_virtual is None:
            imprimir_portero_virtual = Modulo(title='Reportes', route='/portero_virtual_imprimir',
                                     name='portero_virtual_imprimir',
                                     menu=False)

        portero_virtual_m.children.append(query_portero_virtual)
        portero_virtual_m.children.append(insert_portero_virtual)
        portero_virtual_m.children.append(update_portero_virtual)
        portero_virtual_m.children.append(delete_portero_virtual)
        portero_virtual_m.children.append(imprimir_portero_virtual)

        query_reporte = session.query(Modulo).filter(Modulo.name == 'reporte_query').first()
        if query_reporte is None:
            query_reporte = Modulo(title='Consultar', route='',
                                    name='reporte_query',
                                    menu=False)

        imprimir_reporte = session.query(Modulo).filter(Modulo.name == 'reporte_imprimir').first()
        if imprimir_reporte is None:
            imprimir_reporte = Modulo(title='Imprimir', route='/reporte_imprimir',
                                       name='reporte_imprimir',
                                       menu=False)

        reporte_m.children.append(query_reporte)
        reporte_m.children.append(imprimir_reporte)

        query_registros_c = session.query(Modulo).filter(Modulo.name == 'registros_c_query').first()
        if query_registros_c is None:
            query_registros_c = Modulo(title='Consultar', route='',
                                     name='registros_c_query',
                                     menu=False)

        imprimir_registros_c = session.query(Modulo).filter(Modulo.name == 'registros_c_imprimir').first()
        if imprimir_registros_c is None:
            imprimir_registros_c = Modulo(title='Imprimir', route='/registros_c_imprimir',
                                        name='registros_c_imprimir',
                                        menu=False)

        registros_c_m.children.append(query_registros_c)
        registros_c_m.children.append(imprimir_registros_c)

        superadmin_role = session.query(Rol).filter(Rol.nombre == 'SUPER ADMINISTRADOR').first()
        admin_role = session.query(Rol).filter(Rol.nombre == 'ADMINISTRADOR').first()

        supervisor_role = session.query(Rol).filter(Rol.nombre == 'SUPERVISOR').first()
        operador_role = session.query(Rol).filter(Rol.nombre == 'OPERADOR').first()
        registrador_role = session.query(Rol).filter(Rol.nombre == 'REGISTRADOR').first()

        residente_role = session.query(Rol).filter(Rol.nombre == 'RESIDENTE').first()
        guardia_role = session.query(Rol).filter(Rol.nombre == 'GUARDIA').first()

        ###Modulos de Operaciones

        superadmin_role.modulos.append(condominios_m)
        superadmin_role.modulos.append(condominio_m)
        superadmin_role.modulos.append(nropase_m)
        superadmin_role.modulos.append(usuarioCondominio_m)
        superadmin_role.modulos.append(areasocial_m)
        superadmin_role.modulos.append(domicilio_m)
        superadmin_role.modulos.append(gvehiculos_m)
        superadmin_role.modulos.append(marca_m)
        superadmin_role.modulos.append(modelo_m)
        superadmin_role.modulos.append(vehiculo_m)
        superadmin_role.modulos.append(provper_m)
        superadmin_role.modulos.append(residente_m)
        superadmin_role.modulos.append(evento_m)
        superadmin_role.modulos.append(invitado_m)
        superadmin_role.modulos.append(movimiento_m)
        superadmin_role.modulos.append(movimiento_p_m)
        superadmin_role.modulos.append(portero_virtual_m)
        superadmin_role.modulos.append(reporte_m)
        superadmin_role.modulos.append(registros_c_m)

        admin_role.modulos.append(condominios_m)
        admin_role.modulos.append(condominio_m)
        admin_role.modulos.append(nropase_m)
        admin_role.modulos.append(usuarioCondominio_m)
        admin_role.modulos.append(areasocial_m)
        admin_role.modulos.append(domicilio_m)
        admin_role.modulos.append(gvehiculos_m)
        admin_role.modulos.append(marca_m)
        admin_role.modulos.append(modelo_m)
        admin_role.modulos.append(vehiculo_m)
        admin_role.modulos.append(provper_m)
        admin_role.modulos.append(residente_m)
        admin_role.modulos.append(evento_m)
        admin_role.modulos.append(invitado_m)
        admin_role.modulos.append(movimiento_m)
        admin_role.modulos.append(movimiento_p_m)
        admin_role.modulos.append(portero_virtual_m)
        admin_role.modulos.append(reporte_m)
        admin_role.modulos.append(registros_c_m)

        supervisor_role.modulos.append(condominios_m)
        supervisor_role.modulos.append(condominio_m)
        supervisor_role.modulos.append(nropase_m)
        supervisor_role.modulos.append(usuarioCondominio_m)
        supervisor_role.modulos.append(areasocial_m)
        supervisor_role.modulos.append(domicilio_m)
        supervisor_role.modulos.append(gvehiculos_m)
        supervisor_role.modulos.append(marca_m)
        supervisor_role.modulos.append(modelo_m)
        supervisor_role.modulos.append(vehiculo_m)
        supervisor_role.modulos.append(provper_m)
        supervisor_role.modulos.append(residente_m)
        supervisor_role.modulos.append(evento_m)
        supervisor_role.modulos.append(invitado_m)
        supervisor_role.modulos.append(movimiento_m)
        supervisor_role.modulos.append(movimiento_p_m)
        supervisor_role.modulos.append(portero_virtual_m)
        supervisor_role.modulos.append(reporte_m)
        supervisor_role.modulos.append(registros_c_m)

        operador_role.modulos.append(condominios_m)
        operador_role.modulos.append(condominio_m)
        operador_role.modulos.append(nropase_m)
        operador_role.modulos.append(usuarioCondominio_m)
        operador_role.modulos.append(areasocial_m)
        operador_role.modulos.append(domicilio_m)
        operador_role.modulos.append(gvehiculos_m)
        operador_role.modulos.append(marca_m)
        operador_role.modulos.append(modelo_m)
        operador_role.modulos.append(vehiculo_m)
        operador_role.modulos.append(provper_m)
        operador_role.modulos.append(residente_m)
        operador_role.modulos.append(evento_m)
        operador_role.modulos.append(invitado_m)
        operador_role.modulos.append(movimiento_m)
        operador_role.modulos.append(movimiento_p_m)
        operador_role.modulos.append(portero_virtual_m)
        operador_role.modulos.append(reporte_m)
        operador_role.modulos.append(registros_c_m)

        registrador_role.modulos.append(condominios_m)
        registrador_role.modulos.append(nropase_m)
        registrador_role.modulos.append(areasocial_m)
        registrador_role.modulos.append(domicilio_m)
        registrador_role.modulos.append(gvehiculos_m)
        registrador_role.modulos.append(marca_m)
        registrador_role.modulos.append(modelo_m)
        registrador_role.modulos.append(vehiculo_m)
        registrador_role.modulos.append(provper_m)
        registrador_role.modulos.append(residente_m)

        residente_role.modulos.append(evento_m)
        residente_role.modulos.append(invitado_m)

        guardia_role.modulos.append(movimiento_m)
        guardia_role.modulos.append(movimiento_p_m)
        guardia_role.modulos.append(registros_c_m)

        superadmin_role.modulos.append(query_condominio)
        superadmin_role.modulos.append(insert_condominio)
        superadmin_role.modulos.append(update_condominio)
        superadmin_role.modulos.append(delete_condominio)
        superadmin_role.modulos.append(imprimir_condominio)

        superadmin_role.modulos.append(query_nropase)
        superadmin_role.modulos.append(insert_nropase)
        superadmin_role.modulos.append(update_nropase)
        superadmin_role.modulos.append(delete_nropase)
        superadmin_role.modulos.append(imprimir_nropase)

        superadmin_role.modulos.append(query_usuarioCondominio)
        superadmin_role.modulos.append(insert_usuarioCondominio)
        superadmin_role.modulos.append(update_usuarioCondominio)
        superadmin_role.modulos.append(delete_usuarioCondominio)
        superadmin_role.modulos.append(imprimir_usuarioCondominio)

        superadmin_role.modulos.append(query_areasocial)
        superadmin_role.modulos.append(insert_areasocial)
        superadmin_role.modulos.append(update_areasocial)
        superadmin_role.modulos.append(delete_areasocial)
        superadmin_role.modulos.append(imprimir_areasocial)
        superadmin_role.modulos.append(filtrar_areasocial)

        superadmin_role.modulos.append(query_domicilio)
        superadmin_role.modulos.append(insert_domicilio)
        superadmin_role.modulos.append(update_domicilio)
        superadmin_role.modulos.append(delete_domicilio)
        superadmin_role.modulos.append(imprimir_domicilio)
        superadmin_role.modulos.append(filtrar_domicilio)

        superadmin_role.modulos.append(query_residente)
        superadmin_role.modulos.append(insert_residente)
        superadmin_role.modulos.append(update_residente)
        superadmin_role.modulos.append(delete_residente)
        superadmin_role.modulos.append(imprimir_residente)

        superadmin_role.modulos.append(query_provper)
        superadmin_role.modulos.append(insert_provper)
        superadmin_role.modulos.append(update_provper)
        superadmin_role.modulos.append(delete_provper)
        superadmin_role.modulos.append(imprimir_provper)

        superadmin_role.modulos.append(query_marca)
        superadmin_role.modulos.append(insert_marca)
        superadmin_role.modulos.append(update_marca)
        superadmin_role.modulos.append(delete_marca)
        superadmin_role.modulos.append(imprimir_marca)

        superadmin_role.modulos.append(query_modelo)
        superadmin_role.modulos.append(insert_modelo)
        superadmin_role.modulos.append(update_modelo)
        superadmin_role.modulos.append(delete_modelo)
        superadmin_role.modulos.append(imprimir_modelo)

        superadmin_role.modulos.append(query_vehiculo)
        superadmin_role.modulos.append(insert_vehiculo)
        superadmin_role.modulos.append(update_vehiculo)
        superadmin_role.modulos.append(delete_vehiculo)
        superadmin_role.modulos.append(imprimir_vehiculo)

        superadmin_role.modulos.append(query_evento)
        superadmin_role.modulos.append(insert_evento)
        superadmin_role.modulos.append(update_evento)
        superadmin_role.modulos.append(delete_evento)
        superadmin_role.modulos.append(imprimir_evento)

        superadmin_role.modulos.append(query_invitado)
        superadmin_role.modulos.append(insert_invitado)
        superadmin_role.modulos.append(update_invitado)
        superadmin_role.modulos.append(delete_invitado)
        superadmin_role.modulos.append(imprimir_invitado)

        superadmin_role.modulos.append(query_movimiento)
        superadmin_role.modulos.append(insert_movimiento)
        superadmin_role.modulos.append(update_movimiento)
        superadmin_role.modulos.append(delete_movimiento)
        superadmin_role.modulos.append(imprimir_movimiento)

        superadmin_role.modulos.append(query_movimiento_p)
        superadmin_role.modulos.append(insert_movimiento_p)
        superadmin_role.modulos.append(update_movimiento_p)
        superadmin_role.modulos.append(delete_movimiento_p)
        superadmin_role.modulos.append(imprimir_movimiento_p)

        superadmin_role.modulos.append(query_portero_virtual)
        superadmin_role.modulos.append(insert_portero_virtual)
        superadmin_role.modulos.append(update_portero_virtual)
        superadmin_role.modulos.append(delete_portero_virtual)
        superadmin_role.modulos.append(imprimir_portero_virtual)

        superadmin_role.modulos.append(query_reporte)
        superadmin_role.modulos.append(imprimir_reporte)

        superadmin_role.modulos.append(query_registros_c)
        superadmin_role.modulos.append(imprimir_registros_c)

        admin_role.modulos.append(query_condominio)
        admin_role.modulos.append(insert_condominio)
        admin_role.modulos.append(update_condominio)
        admin_role.modulos.append(delete_condominio)
        admin_role.modulos.append(imprimir_condominio)

        admin_role.modulos.append(query_nropase)
        admin_role.modulos.append(insert_nropase)
        admin_role.modulos.append(update_nropase)
        admin_role.modulos.append(delete_nropase)
        admin_role.modulos.append(imprimir_nropase)

        admin_role.modulos.append(query_usuarioCondominio)
        admin_role.modulos.append(insert_usuarioCondominio)
        admin_role.modulos.append(update_usuarioCondominio)
        admin_role.modulos.append(delete_usuarioCondominio)
        admin_role.modulos.append(imprimir_usuarioCondominio)

        admin_role.modulos.append(query_areasocial)
        admin_role.modulos.append(insert_areasocial)
        admin_role.modulos.append(update_areasocial)
        admin_role.modulos.append(delete_areasocial)
        admin_role.modulos.append(imprimir_areasocial)
        admin_role.modulos.append(filtrar_areasocial)

        admin_role.modulos.append(query_domicilio)
        admin_role.modulos.append(insert_domicilio)
        admin_role.modulos.append(update_domicilio)
        admin_role.modulos.append(delete_domicilio)
        admin_role.modulos.append(imprimir_domicilio)
        admin_role.modulos.append(filtrar_domicilio)

        admin_role.modulos.append(query_residente)
        admin_role.modulos.append(insert_residente)
        admin_role.modulos.append(update_residente)
        admin_role.modulos.append(delete_residente)
        admin_role.modulos.append(imprimir_residente)

        admin_role.modulos.append(query_provper)
        admin_role.modulos.append(insert_provper)
        admin_role.modulos.append(update_provper)
        admin_role.modulos.append(delete_provper)
        admin_role.modulos.append(imprimir_provper)

        admin_role.modulos.append(query_marca)
        admin_role.modulos.append(insert_marca)
        admin_role.modulos.append(update_marca)
        admin_role.modulos.append(delete_marca)
        admin_role.modulos.append(imprimir_marca)

        admin_role.modulos.append(query_modelo)
        admin_role.modulos.append(insert_modelo)
        admin_role.modulos.append(update_modelo)
        admin_role.modulos.append(delete_modelo)
        admin_role.modulos.append(imprimir_modelo)

        admin_role.modulos.append(query_vehiculo)
        admin_role.modulos.append(insert_vehiculo)
        admin_role.modulos.append(update_vehiculo)
        admin_role.modulos.append(delete_vehiculo)
        admin_role.modulos.append(imprimir_vehiculo)

        admin_role.modulos.append(query_evento)
        admin_role.modulos.append(insert_evento)
        admin_role.modulos.append(update_evento)
        admin_role.modulos.append(delete_evento)
        admin_role.modulos.append(imprimir_evento)

        admin_role.modulos.append(query_invitado)
        admin_role.modulos.append(insert_invitado)
        admin_role.modulos.append(update_invitado)
        admin_role.modulos.append(delete_invitado)
        admin_role.modulos.append(imprimir_invitado)

        admin_role.modulos.append(query_movimiento)
        admin_role.modulos.append(insert_movimiento)
        admin_role.modulos.append(update_movimiento)
        admin_role.modulos.append(delete_movimiento)
        admin_role.modulos.append(imprimir_movimiento)

        admin_role.modulos.append(query_movimiento_p)
        admin_role.modulos.append(insert_movimiento_p)
        admin_role.modulos.append(update_movimiento_p)
        admin_role.modulos.append(delete_movimiento_p)
        admin_role.modulos.append(imprimir_movimiento_p)

        admin_role.modulos.append(query_portero_virtual)
        admin_role.modulos.append(insert_portero_virtual)
        admin_role.modulos.append(update_portero_virtual)
        admin_role.modulos.append(delete_portero_virtual)
        admin_role.modulos.append(imprimir_portero_virtual)

        admin_role.modulos.append(query_reporte)
        admin_role.modulos.append(imprimir_reporte)

        admin_role.modulos.append(query_registros_c)
        admin_role.modulos.append(imprimir_registros_c)

        supervisor_role.modulos.append(query_condominio)
        supervisor_role.modulos.append(insert_condominio)
        supervisor_role.modulos.append(update_condominio)
        supervisor_role.modulos.append(delete_condominio)
        supervisor_role.modulos.append(imprimir_condominio)

        supervisor_role.modulos.append(query_nropase)
        supervisor_role.modulos.append(insert_nropase)
        supervisor_role.modulos.append(update_nropase)
        supervisor_role.modulos.append(delete_nropase)
        supervisor_role.modulos.append(imprimir_nropase)

        supervisor_role.modulos.append(query_usuarioCondominio)
        supervisor_role.modulos.append(insert_usuarioCondominio)
        supervisor_role.modulos.append(update_usuarioCondominio)
        supervisor_role.modulos.append(delete_usuarioCondominio)
        supervisor_role.modulos.append(imprimir_usuarioCondominio)

        supervisor_role.modulos.append(query_areasocial)
        supervisor_role.modulos.append(insert_areasocial)
        supervisor_role.modulos.append(update_areasocial)
        supervisor_role.modulos.append(delete_areasocial)
        supervisor_role.modulos.append(imprimir_areasocial)
        supervisor_role.modulos.append(filtrar_areasocial)

        supervisor_role.modulos.append(query_domicilio)
        supervisor_role.modulos.append(insert_domicilio)
        supervisor_role.modulos.append(update_domicilio)
        supervisor_role.modulos.append(delete_domicilio)
        supervisor_role.modulos.append(imprimir_domicilio)

        supervisor_role.modulos.append(query_residente)
        supervisor_role.modulos.append(insert_residente)
        supervisor_role.modulos.append(update_residente)
        supervisor_role.modulos.append(delete_residente)
        supervisor_role.modulos.append(imprimir_residente)

        supervisor_role.modulos.append(query_provper)
        supervisor_role.modulos.append(insert_provper)
        supervisor_role.modulos.append(update_provper)
        supervisor_role.modulos.append(delete_provper)
        supervisor_role.modulos.append(imprimir_provper)

        supervisor_role.modulos.append(query_marca)
        supervisor_role.modulos.append(insert_marca)
        supervisor_role.modulos.append(update_marca)
        supervisor_role.modulos.append(delete_marca)
        supervisor_role.modulos.append(imprimir_marca)

        supervisor_role.modulos.append(query_modelo)
        supervisor_role.modulos.append(insert_modelo)
        supervisor_role.modulos.append(update_modelo)
        supervisor_role.modulos.append(delete_modelo)
        supervisor_role.modulos.append(imprimir_modelo)

        supervisor_role.modulos.append(query_vehiculo)
        supervisor_role.modulos.append(insert_vehiculo)
        supervisor_role.modulos.append(update_vehiculo)
        supervisor_role.modulos.append(delete_vehiculo)
        supervisor_role.modulos.append(imprimir_vehiculo)

        supervisor_role.modulos.append(query_evento)
        supervisor_role.modulos.append(insert_evento)
        supervisor_role.modulos.append(update_evento)
        supervisor_role.modulos.append(delete_evento)
        supervisor_role.modulos.append(imprimir_evento)

        supervisor_role.modulos.append(query_invitado)
        supervisor_role.modulos.append(insert_invitado)
        supervisor_role.modulos.append(update_invitado)
        supervisor_role.modulos.append(delete_invitado)
        supervisor_role.modulos.append(imprimir_invitado)

        supervisor_role.modulos.append(query_movimiento)
        supervisor_role.modulos.append(insert_movimiento)
        supervisor_role.modulos.append(update_movimiento)
        supervisor_role.modulos.append(delete_movimiento)
        supervisor_role.modulos.append(imprimir_movimiento)

        supervisor_role.modulos.append(query_movimiento_p)
        supervisor_role.modulos.append(insert_movimiento_p)
        supervisor_role.modulos.append(update_movimiento_p)
        supervisor_role.modulos.append(delete_movimiento_p)
        supervisor_role.modulos.append(imprimir_movimiento_p)

        supervisor_role.modulos.append(query_portero_virtual)
        supervisor_role.modulos.append(insert_portero_virtual)
        supervisor_role.modulos.append(update_portero_virtual)
        supervisor_role.modulos.append(delete_portero_virtual)
        supervisor_role.modulos.append(imprimir_portero_virtual)

        supervisor_role.modulos.append(query_reporte)
        supervisor_role.modulos.append(imprimir_reporte)

        supervisor_role.modulos.append(query_registros_c)
        supervisor_role.modulos.append(imprimir_registros_c)

        operador_role.modulos.append(query_condominio)
        operador_role.modulos.append(insert_condominio)
        operador_role.modulos.append(update_condominio)
        operador_role.modulos.append(delete_condominio)
        operador_role.modulos.append(imprimir_condominio)

        operador_role.modulos.append(query_nropase)
        operador_role.modulos.append(insert_nropase)
        operador_role.modulos.append(update_nropase)
        operador_role.modulos.append(delete_nropase)
        operador_role.modulos.append(imprimir_nropase)

        operador_role.modulos.append(query_usuarioCondominio)
        operador_role.modulos.append(insert_usuarioCondominio)
        operador_role.modulos.append(update_usuarioCondominio)
        operador_role.modulos.append(delete_usuarioCondominio)
        operador_role.modulos.append(imprimir_usuarioCondominio)

        operador_role.modulos.append(query_areasocial)
        operador_role.modulos.append(insert_areasocial)
        operador_role.modulos.append(update_areasocial)
        operador_role.modulos.append(delete_areasocial)
        operador_role.modulos.append(imprimir_areasocial)
        operador_role.modulos.append(filtrar_areasocial)

        operador_role.modulos.append(query_domicilio)
        operador_role.modulos.append(insert_domicilio)
        operador_role.modulos.append(update_domicilio)
        operador_role.modulos.append(delete_domicilio)
        operador_role.modulos.append(imprimir_domicilio)

        operador_role.modulos.append(query_residente)
        operador_role.modulos.append(insert_residente)
        operador_role.modulos.append(update_residente)
        operador_role.modulos.append(delete_residente)
        operador_role.modulos.append(imprimir_residente)

        operador_role.modulos.append(query_provper)
        operador_role.modulos.append(insert_provper)
        operador_role.modulos.append(update_provper)
        operador_role.modulos.append(delete_provper)
        operador_role.modulos.append(imprimir_provper)

        operador_role.modulos.append(query_marca)
        operador_role.modulos.append(insert_marca)
        operador_role.modulos.append(update_marca)
        operador_role.modulos.append(delete_marca)
        operador_role.modulos.append(imprimir_marca)

        operador_role.modulos.append(query_modelo)
        operador_role.modulos.append(insert_modelo)
        operador_role.modulos.append(update_modelo)
        operador_role.modulos.append(delete_modelo)
        operador_role.modulos.append(imprimir_modelo)

        operador_role.modulos.append(query_vehiculo)
        operador_role.modulos.append(insert_vehiculo)
        operador_role.modulos.append(update_vehiculo)
        operador_role.modulos.append(delete_vehiculo)
        operador_role.modulos.append(imprimir_vehiculo)

        operador_role.modulos.append(query_evento)
        operador_role.modulos.append(insert_evento)
        operador_role.modulos.append(update_evento)
        operador_role.modulos.append(delete_evento)
        operador_role.modulos.append(imprimir_evento)

        operador_role.modulos.append(query_invitado)
        operador_role.modulos.append(insert_invitado)
        operador_role.modulos.append(update_invitado)
        operador_role.modulos.append(delete_invitado)
        operador_role.modulos.append(imprimir_invitado)

        operador_role.modulos.append(query_movimiento)
        operador_role.modulos.append(insert_movimiento)
        operador_role.modulos.append(update_movimiento)
        operador_role.modulos.append(delete_movimiento)
        operador_role.modulos.append(imprimir_movimiento)

        operador_role.modulos.append(query_movimiento_p)
        operador_role.modulos.append(insert_movimiento_p)
        operador_role.modulos.append(update_movimiento_p)
        operador_role.modulos.append(delete_movimiento_p)
        operador_role.modulos.append(imprimir_movimiento_p)

        operador_role.modulos.append(query_portero_virtual)
        operador_role.modulos.append(insert_portero_virtual)
        operador_role.modulos.append(update_portero_virtual)
        operador_role.modulos.append(delete_portero_virtual)
        operador_role.modulos.append(imprimir_portero_virtual)

        operador_role.modulos.append(query_reporte)
        operador_role.modulos.append(imprimir_reporte)

        operador_role.modulos.append(query_registros_c)
        operador_role.modulos.append(imprimir_registros_c)

        registrador_role.modulos.append(query_nropase)
        registrador_role.modulos.append(insert_nropase)
        registrador_role.modulos.append(update_nropase)
        registrador_role.modulos.append(delete_nropase)
        registrador_role.modulos.append(imprimir_nropase)

        registrador_role.modulos.append(query_areasocial)
        registrador_role.modulos.append(insert_areasocial)
        registrador_role.modulos.append(update_areasocial)
        registrador_role.modulos.append(delete_areasocial)
        registrador_role.modulos.append(imprimir_areasocial)
        registrador_role.modulos.append(filtrar_areasocial)

        registrador_role.modulos.append(query_domicilio)
        registrador_role.modulos.append(insert_domicilio)
        registrador_role.modulos.append(update_domicilio)
        registrador_role.modulos.append(delete_domicilio)
        registrador_role.modulos.append(imprimir_domicilio)
        registrador_role.modulos.append(filtrar_domicilio)

        registrador_role.modulos.append(query_residente)
        registrador_role.modulos.append(insert_residente)
        registrador_role.modulos.append(update_residente)
        registrador_role.modulos.append(delete_residente)
        registrador_role.modulos.append(imprimir_residente)

        registrador_role.modulos.append(query_provper)
        registrador_role.modulos.append(insert_provper)
        registrador_role.modulos.append(update_provper)
        registrador_role.modulos.append(delete_provper)
        registrador_role.modulos.append(imprimir_provper)

        registrador_role.modulos.append(query_marca)
        registrador_role.modulos.append(insert_marca)
        registrador_role.modulos.append(update_marca)
        registrador_role.modulos.append(delete_marca)
        registrador_role.modulos.append(imprimir_marca)

        registrador_role.modulos.append(query_modelo)
        registrador_role.modulos.append(insert_modelo)
        registrador_role.modulos.append(update_modelo)
        registrador_role.modulos.append(delete_modelo)
        registrador_role.modulos.append(imprimir_modelo)

        registrador_role.modulos.append(query_vehiculo)
        registrador_role.modulos.append(insert_vehiculo)
        registrador_role.modulos.append(update_vehiculo)
        registrador_role.modulos.append(delete_vehiculo)
        registrador_role.modulos.append(imprimir_vehiculo)


        residente_role.modulos.append(query_evento)
        residente_role.modulos.append(insert_evento)
        residente_role.modulos.append(update_evento)
        residente_role.modulos.append(delete_evento)
        residente_role.modulos.append(imprimir_evento)

        residente_role.modulos.append(query_invitado)
        residente_role.modulos.append(insert_invitado)
        residente_role.modulos.append(update_invitado)
        residente_role.modulos.append(delete_invitado)
        residente_role.modulos.append(imprimir_invitado)

        guardia_role.modulos.append(query_movimiento)
        guardia_role.modulos.append(insert_movimiento)
        guardia_role.modulos.append(update_movimiento)

        guardia_role.modulos.append(query_movimiento_p)
        guardia_role.modulos.append(insert_movimiento_p)
        guardia_role.modulos.append(update_movimiento_p)

        guardia_role.modulos.append(query_registros_c)
        guardia_role.modulos.append(imprimir_registros_c)


        session.add(Tipodocumento(id=1,nombre='Carnet de Identidad'))
        session.add(Tipodocumento(id=2,nombre='licencia Conducir'))
        session.add(Tipodocumento(id=3,nombre='Pasaporte'))
        session.add(Tipodocumento(id=4, nombre='Codigo QR'))
        session.add(Tipodocumento(id=5,nombre='Otros'))

        session.add(TipoEvento(id=1,nombre='Visita'))
        session.add(TipoEvento(id=2,nombre='Reunion'))
        session.add(TipoEvento(id=3,nombre='Matrimonio'))
        session.add(TipoEvento(id=4,nombre='Fiesta'))
        session.add(TipoEvento(id=5,nombre='Actividad Deportiva'))
        session.add(TipoEvento(id=6,nombre='Invitacion Rapida'))

        session.add(Tipopase(id=1,nombre='Visita'))
        session.add(Tipopase(id=2,nombre='Proveedor'))
        session.add(Tipopase(id=3,nombre='Taxi'))
        session.add(Tipopase(id=4,nombre='Otros'))

        session.add(Autorizacion(id=1,nombre='Residente'))
        session.add(Autorizacion(id=2,nombre='Administracion'))
        session.add(Autorizacion(id=3,nombre='Emergencia'))
        session.add(Autorizacion(id=4,nombre='Negativa de Ingreso'))
        session.add(Autorizacion(id=5, nombre='Otros'))

        session.add(Entrada(id=1,nombre='Entrada peatonal Visitas'))
        session.add(Entrada(id=2,nombre='Entrada vehicular Visitas'))
        session.add(Entrada(id=3,nombre='Entrada peatonal Residentes'))
        session.add(Entrada(id=4,nombre='Entrada vehicular Residentes'))
        session.add(Entrada(id=5,nombre='Salida peatonal Visitas'))
        session.add(Entrada(id=6,nombre='Salida vehicular Visitas'))
        session.add(Entrada(id=7,nombre='Salida peatonal Residentes'))
        session.add(Entrada(id=8,nombre='Salida vehicular Residentes'))
        session.add(Entrada(id=9, nombre='Entrada Porteria virtual'))

        session.add(Tipovehiculo(nombre='AUTO'))
        session.add(Tipovehiculo(nombre='CAMIONETA'))
        session.add(Tipovehiculo(nombre='VAGONETA'))
        session.add(Tipovehiculo(nombre='JEEP'))
        session.add(Tipovehiculo(nombre='CAMION'))
        session.add(Tipovehiculo( nombre='MOTOCICLETA'))
        session.add(Tipovehiculo(nombre='MOTO'))
        session.add(Tipovehiculo(nombre='MICRO'))
        session.add(Tipovehiculo(nombre='BICICLETA'))

        session.add(Color(nombre='AMARILLO'))
        session.add(Color(nombre='AZUL'))
        session.add(Color(nombre='BLANCO'))
        session.add(Color(nombre='CAFE'))
        session.add(Color(nombre='CELESTE'))
        session.add(Color(nombre='COBRE'))
        session.add(Color(nombre='GRIS'))
        session.add(Color(nombre='NARANJA'))
        session.add(Color(nombre='NEGRO'))
        session.add(Color(nombre='PLATEADO'))
        session.add(Color(nombre='PLOMO'))
        session.add(Color(nombre='ROJO'))
        session.add(Color(nombre='ROSADO'))
        session.add(Color(nombre='VERDE'))

        session.commit()

def condominio_schedule():

    def sincronizar_invitaciones():
        # print("sincronizacion")

        with transaction() as db:
            EventoManager(db).validar_eventos()
            EventoManager(db).expirar_eventos_pasados()
            EventoManager(db).expirar_eventos()

    schedule.every(1).minutes.do(sincronizar_invitaciones)