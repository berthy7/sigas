from .usuarios.usuario.controllers import *
from .usuarios.rol.controllers import *
from .usuarios.login.controllers import *

from server.operaciones.bitacora.controllers import *

from server.condominios.condominio.controllers import *
from server.condominios.nropase.controllers import *
from server.condominios.usuario.controllers import *
from server.condominios.areasocial.controllers import *
from server.condominios.domicilio.controllers import *
from server.condominios.residente.controllers import *
from server.condominios.provper.controllers import *
from server.condominios.vehiculo.controllers import *
from server.condominios.marca.controllers import *
from server.condominios.modelo.controllers import *
from server.condominios.reporte.controllers import *
from server.condominios.reporte.controllers import *
from server.condominios.registros_c.controllers import *

from server.condominios.evento.controllers import *
from server.condominios.invitado.controllers import *
from server.condominios.movimiento.controllers import *
from server.condominios.movimiento_p.controllers import *
from server.servicios.controllers import *

from server.dispositivos.dispositivo.controllers import *
from server.dispositivos.config_acceso.controllers import *
from server.dispositivos.registros.controllers import *

from .main.controllers import Index
from tornado.web import StaticFileHandler


def get_handlers():
    """Retorna una lista con las rutas, sus manejadores y datos extras."""
    handlers = list()
    # Login
    handlers.append((r'/login', LoginController))
    handlers.append((r'/logout', LogoutController))
    handlers.append((r'/manual', ManualController))

    # Principal
    handlers.append((r'/', Index))

    # Usuario
    handlers.extend(get_routes(UsuarioController))
    handlers.extend(get_routes(RolController))


    # Operaciones
    handlers.extend(get_routes(BitacoraController))


    # Condominio
    handlers.extend(get_routes(CondominioController))
    handlers.extend(get_routes(NropaseController))
    handlers.extend(get_routes(UsuarioCondominioController))
    handlers.extend(get_routes(AreasocialController))
    handlers.extend(get_routes(DomicilioController))
    handlers.extend(get_routes(ResidenteController))
    handlers.extend(get_routes(ProvperController))
    handlers.extend(get_routes(VehiculoController))
    handlers.extend(get_routes(MarcaController))
    handlers.extend(get_routes(ModeloController))
    handlers.extend(get_routes(EventoController))
    handlers.extend(get_routes(InvitadoController))
    handlers.extend(get_routes(MovimientoController))
    handlers.extend(get_routes(Movimiento_pController))
    handlers.extend(get_routes(ReporteController))
    handlers.extend(get_routes(Registros_cController))

    # Dispositivos
    handlers.extend(get_routes(DispositivoController))
    handlers.extend(get_routes(ConfigaccesoController))
    handlers.extend(get_routes(RegistrosController))

    # Recursos por submodulo
    handlers.append((r'/resources/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'common', 'resources')}))

    handlers.append((r'/common/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'common', 'assets')}))
    handlers.append((r'/main/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'main', 'assets')}))
    handlers.append((r'/operaciones/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'operaciones')}))
    handlers.append((r'/condominios/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'condominios')}))
    handlers.append((r'/usuarios/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'usuarios')}))
    handlers.append((r'/dispositivos/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'dispositivos')}))
    handlers.append((r'/servicios/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'servicios')}))

    #Servicios Movil

    handlers.extend(get_routes(ApiCondominioController))


    return handlers


def get_routes(handler):
    routes = list()
    for route in handler.routes:
        routes.append((route, handler))
    return routes
