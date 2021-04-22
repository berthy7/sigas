/*
 Navicat Premium Data Transfer

 Source Server         : Localhost
 Source Server Type    : PostgreSQL
 Source Server Version : 90600
 Source Host           : localhost:5432
 Source Catalog        : prueba_web
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 90600
 File Encoding         : 65001

 Date: 10/12/2020 10:01:08
*/


-- ----------------------------
-- Table structure for modulo
-- ----------------------------
DROP TABLE IF EXISTS "public"."modulo";
CREATE TABLE "public"."modulo" (
  "id" int4 NOT NULL DEFAULT nextval('modulo_id_seq1'::regclass),
  "route" varchar(100) COLLATE "pg_catalog"."default",
  "title" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "icon" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "menu" bool NOT NULL,
  "fkmodulo" int4
)
;

-- ----------------------------
-- Records of modulo
-- ----------------------------
INSERT INTO "public"."modulo" VALUES (1, NULL, 'Gestion de Usuarios Sigas', 'user_Modulo', 'person', 't', NULL);
INSERT INTO "public"."modulo" VALUES (2, '/rol', 'Perfiles', 'roles', 'dashboard', 't', 1);
INSERT INTO "public"."modulo" VALUES (3, '/usuario', 'Usuario', 'usuario', 'account_box', 't', 1);
INSERT INTO "public"."modulo" VALUES (4, '/usuario_profile', 'Perfil Usuario', 'perfil', 'dvr', 't', 1);
INSERT INTO "public"."modulo" VALUES (5, '/bitacora', 'Bitácora', 'bitacora', 'dvr', 't', 1);
INSERT INTO "public"."modulo" VALUES (6, '/ajuste', 'Ajustes', 'ajuste', 'settings', 't', 1);
INSERT INTO "public"."modulo" VALUES (7, '', 'Consultar', 'usuario_query', 'home', 'f', 3);
INSERT INTO "public"."modulo" VALUES (8, '/usuario_insert', 'Adicionar', 'usuario_insert', 'home', 'f', 3);
INSERT INTO "public"."modulo" VALUES (9, '/usuario_update', 'Actualizar', 'usuario_update', 'home', 'f', 3);
INSERT INTO "public"."modulo" VALUES (10, '/usuario_state', 'Habilitar', 'usuario_state', 'home', 'f', 3);
INSERT INTO "public"."modulo" VALUES (11, '/usuario_delete', 'Dar de Baja', 'usuario_delete', 'home', 'f', 3);
INSERT INTO "public"."modulo" VALUES (12, '/usuario_sesion', 'Session', 'usuario_sesion', 'home', 'f', 3);
INSERT INTO "public"."modulo" VALUES (13, '', 'Consultar', 'rol_query', 'home', 'f', 2);
INSERT INTO "public"."modulo" VALUES (14, '/rol_insert', 'Adicionar', 'rol_insert', 'home', 'f', 2);
INSERT INTO "public"."modulo" VALUES (15, '/rol_update', 'Actualizar', 'rol_update', 'home', 'f', 2);
INSERT INTO "public"."modulo" VALUES (16, '/rol_delete', 'Dar de Baja', 'rol_delete', 'home', 'f', 2);
INSERT INTO "public"."modulo" VALUES (17, '', 'Consultar', 'bitacora_query', 'home', 'f', 5);
INSERT INTO "public"."modulo" VALUES (18, '', 'Consultar', 'ajuste_query', 'home', 'f', 6);
INSERT INTO "public"."modulo" VALUES (19, '/ajuste_insert', 'Adicionar', 'ajuste_insert', 'home', 'f', 6);
INSERT INTO "public"."modulo" VALUES (20, '/ajuste_update', 'Actualizar', 'ajuste_update', 'home', 'f', 6);
INSERT INTO "public"."modulo" VALUES (21, '/ajuste_delete', 'Dar de Baja', 'ajuste_delete', 'home', 'f', 6);
INSERT INTO "public"."modulo" VALUES (22, NULL, 'Gestion de Condominio', 'condominios', 'domain', 't', NULL);
INSERT INTO "public"."modulo" VALUES (23, '/condominio', 'Condominios', 'condominio', 'location_city', 't', 22);
INSERT INTO "public"."modulo" VALUES (24, '/nropase', 'Cant. de Tarjetas', 'nropase', 'credit_card', 't', 22);
INSERT INTO "public"."modulo" VALUES (25, '/usuarioCondominio', 'Usuarios', 'usuarioCondominio', 'assignment_ind', 't', 22);
INSERT INTO "public"."modulo" VALUES (26, '/areasocial', 'Areas Social', 'areasocial', 'account_balance', 't', 22);
INSERT INTO "public"."modulo" VALUES (27, '/domicilio', 'Domicilios', 'domicilio', 'home', 't', 22);
INSERT INTO "public"."modulo" VALUES (28, NULL, 'Gestion de Vehiculos', 'gvehiculos', 'book', 't', 22);
INSERT INTO "public"."modulo" VALUES (29, '/provper', 'Prov. Permanentes', 'provper', 'people', 't', 22);
INSERT INTO "public"."modulo" VALUES (30, '/residente', 'Residentes', 'residente', 'people_outline', 't', 22);
INSERT INTO "public"."modulo" VALUES (31, '/evento', 'Eventos', 'evento', 'event', 't', 22);
INSERT INTO "public"."modulo" VALUES (32, '/invitado', 'Invitados', 'invitado', 'person_add', 't', 22);
INSERT INTO "public"."modulo" VALUES (33, '/movimiento', 'Control y Registro Vehicular', 'movimiento', 'control_point', 't', 22);
INSERT INTO "public"."modulo" VALUES (34, '/movimiento_p', 'Control y Registro Peatonal', 'movimiento_p', 'control_point', 't', 22);
INSERT INTO "public"."modulo" VALUES (35, '/portero_virtual', 'Portero Virtual', 'portero_virtual', 'control_point', 't', 22);
INSERT INTO "public"."modulo" VALUES (36, '/reporte', 'Reportes', 'reporte', 'content_paste', 't', 22);
INSERT INTO "public"."modulo" VALUES (37, '/registros_c', 'Registros', 'registros_c', 'assignment', 't', 22);
INSERT INTO "public"."modulo" VALUES (38, '', 'Consultar', 'condominio_query', 'home', 'f', 23);
INSERT INTO "public"."modulo" VALUES (39, '/condominio_insert', 'Adicionar', 'condominio_insert', 'home', 'f', 23);
INSERT INTO "public"."modulo" VALUES (40, '/condominio_update', 'Actualizar', 'condominio_update', 'home', 'f', 23);
INSERT INTO "public"."modulo" VALUES (41, '/condominio_delete', 'Dar de Baja', 'condominio_delete', 'home', 'f', 23);
INSERT INTO "public"."modulo" VALUES (42, '/condominio_imprimir', 'Reportes', 'condominio_imprimir', 'home', 'f', 23);
INSERT INTO "public"."modulo" VALUES (43, '', 'Consultar', 'nropase_query', 'home', 'f', 24);
INSERT INTO "public"."modulo" VALUES (44, '/nropase_insert', 'Adicionar', 'nropase_insert', 'home', 'f', 24);
INSERT INTO "public"."modulo" VALUES (45, '/nropase_update', 'Actualizar', 'nropase_update', 'home', 'f', 24);
INSERT INTO "public"."modulo" VALUES (46, '/nropase_delete', 'Dar de Baja', 'nropase_delete', 'home', 'f', 24);
INSERT INTO "public"."modulo" VALUES (47, '/nropase_importar', 'Importar', 'nropase_importar', 'home', 'f', 24);
INSERT INTO "public"."modulo" VALUES (48, '/nropase_imprimir', 'Reportes', 'nropase_imprimir', 'home', 'f', 24);
INSERT INTO "public"."modulo" VALUES (49, '', 'Consultar', 'usuarioCondominio_query', 'home', 'f', 25);
INSERT INTO "public"."modulo" VALUES (50, '/usuarioCondominio_insert', 'Adicionar', 'usuarioCondominio_insert', 'home', 'f', 25);
INSERT INTO "public"."modulo" VALUES (51, '/usuarioCondominio_update', 'Actualizar', 'usuarioCondominio_update', 'home', 'f', 25);
INSERT INTO "public"."modulo" VALUES (52, '/usuarioCondominio_state', 'Habilitar', 'usuarioCondominio_state', 'home', 'f', 25);
INSERT INTO "public"."modulo" VALUES (53, '/usuarioCondominio_delete', 'Dar de Baja', 'usuarioCondominio_delete', 'home', 'f', 25);
INSERT INTO "public"."modulo" VALUES (54, '/usuarioCondominio_sesion', 'Session', 'usuarioCondominio_sesion', 'home', 'f', 25);
INSERT INTO "public"."modulo" VALUES (55, '', 'Consultar', 'areasocial_query', 'home', 'f', 26);
INSERT INTO "public"."modulo" VALUES (56, '/areasocial_insert', 'Adicionar', 'areasocial_insert', 'home', 'f', 26);
INSERT INTO "public"."modulo" VALUES (57, '/areasocial_update', 'Actualizar', 'areasocial_update', 'home', 'f', 26);
INSERT INTO "public"."modulo" VALUES (58, '/areasocial_delete', 'Dar de Baja', 'areasocial_delete', 'home', 'f', 26);
INSERT INTO "public"."modulo" VALUES (59, '/areasocial_imprimir', 'Reportes', 'areasocial_imprimir', 'home', 'f', 26);
INSERT INTO "public"."modulo" VALUES (60, '/areasocial_filtrar', 'Filtrar', 'areasocial_filtrar', 'home', 'f', 26);
INSERT INTO "public"."modulo" VALUES (61, '', 'Consultar', 'domicilio_query', 'home', 'f', 27);
INSERT INTO "public"."modulo" VALUES (62, '/domicilio_insert', 'Adicionar', 'domicilio_insert', 'home', 'f', 27);
INSERT INTO "public"."modulo" VALUES (63, '/domicilio_update', 'Actualizar', 'domicilio_update', 'home', 'f', 27);
INSERT INTO "public"."modulo" VALUES (64, '/domicilio_delete', 'Dar de Baja', 'domicilio_delete', 'home', 'f', 27);
INSERT INTO "public"."modulo" VALUES (65, '/domicilio_imprimir', 'Reportes', 'domicilio_imprimir', 'home', 'f', 27);
INSERT INTO "public"."modulo" VALUES (66, '/domicilio_filtrar', 'Filtrar', 'domicilio_filtrar', 'home', 'f', 27);
INSERT INTO "public"."modulo" VALUES (67, '/marca', 'Marcas', 'marca', 'directions_car', 't', 28);
INSERT INTO "public"."modulo" VALUES (68, '/modelo', 'Modelos', 'modelo', 'directions_car', 't', 28);
INSERT INTO "public"."modulo" VALUES (69, '/vehiculo', 'Vehiculos', 'vehiculo', 'directions_car', 't', 28);
INSERT INTO "public"."modulo" VALUES (70, '', 'Consultar', 'provper_query', 'home', 'f', 29);
INSERT INTO "public"."modulo" VALUES (71, '/provper_insert', 'Adicionar', 'provper_insert', 'home', 'f', 29);
INSERT INTO "public"."modulo" VALUES (72, '/provper_update', 'Actualizar', 'provper_update', 'home', 'f', 29);
INSERT INTO "public"."modulo" VALUES (73, '/provper_delete', 'Dar de Baja', 'provper_delete', 'home', 'f', 29);
INSERT INTO "public"."modulo" VALUES (74, '/provper_imprimir', 'Reportes', 'provper_imprimir', 'home', 'f', 29);
INSERT INTO "public"."modulo" VALUES (75, '', 'Consultar', 'residente_query', 'home', 'f', 30);
INSERT INTO "public"."modulo" VALUES (76, '/residente_insert', 'Adicionar', 'residente_insert', 'home', 'f', 30);
INSERT INTO "public"."modulo" VALUES (77, '/residente_update', 'Actualizar', 'residente_update', 'home', 'f', 30);
INSERT INTO "public"."modulo" VALUES (78, '/residente_delete', 'Dar de Baja', 'residente_delete', 'home', 'f', 30);
INSERT INTO "public"."modulo" VALUES (79, '/residente_imprimir', 'Reportes', 'residente_imprimir', 'home', 'f', 30);
INSERT INTO "public"."modulo" VALUES (80, '', 'Consultar', 'evento_query', 'home', 'f', 31);
INSERT INTO "public"."modulo" VALUES (81, '/evento_insert', 'Adicionar', 'evento_insert', 'home', 'f', 31);
INSERT INTO "public"."modulo" VALUES (82, '/evento_update', 'Actualizar', 'evento_update', 'home', 'f', 31);
INSERT INTO "public"."modulo" VALUES (83, '/evento_delete', 'Dar de Baja', 'evento_delete', 'home', 'f', 31);
INSERT INTO "public"."modulo" VALUES (84, '/evento_imprimir', 'Reportes', 'evento_imprimir', 'home', 'f', 31);
INSERT INTO "public"."modulo" VALUES (85, '', 'Consultar', 'invitado_query', 'home', 'f', 32);
INSERT INTO "public"."modulo" VALUES (86, '/invitado_insert', 'Adicionar', 'invitado_insert', 'home', 'f', 32);
INSERT INTO "public"."modulo" VALUES (87, '/invitado_update', 'Actualizar', 'invitado_update', 'home', 'f', 32);
INSERT INTO "public"."modulo" VALUES (88, '/invitado_delete', 'Dar de Baja', 'invitado_delete', 'home', 'f', 32);
INSERT INTO "public"."modulo" VALUES (89, '/invitado_imprimir', 'Reportes', 'invitado_imprimir', 'home', 'f', 32);
INSERT INTO "public"."modulo" VALUES (90, '', 'Consultar', 'movimiento_query', 'home', 'f', 33);
INSERT INTO "public"."modulo" VALUES (91, '/movimiento_insert', 'Adicionar', 'movimiento_insert', 'home', 'f', 33);
INSERT INTO "public"."modulo" VALUES (92, '/movimiento_update', 'Actualizar', 'movimiento_update', 'home', 'f', 33);
INSERT INTO "public"."modulo" VALUES (93, '/movimiento_delete', 'Dar de Baja', 'movimiento_delete', 'home', 'f', 33);
INSERT INTO "public"."modulo" VALUES (94, '/movimiento_imprimir', 'Reportes', 'movimiento_imprimir', 'home', 'f', 33);
INSERT INTO "public"."modulo" VALUES (95, '', 'Consultar', 'movimiento_p_query', 'home', 'f', 34);
INSERT INTO "public"."modulo" VALUES (96, '/movimiento_p_insert', 'Adicionar', 'movimiento_p_insert', 'home', 'f', 34);
INSERT INTO "public"."modulo" VALUES (97, '/movimiento_p_update', 'Actualizar', 'movimiento_p_update', 'home', 'f', 34);
INSERT INTO "public"."modulo" VALUES (98, '/movimiento_p_delete', 'Dar de Baja', 'movimiento_p_delete', 'home', 'f', 34);
INSERT INTO "public"."modulo" VALUES (99, '/movimiento_p_imprimir', 'Reportes', 'movimiento_p_imprimir', 'home', 'f', 34);
INSERT INTO "public"."modulo" VALUES (100, '', 'Consultar', 'portero_virtual_query', 'home', 'f', 35);
INSERT INTO "public"."modulo" VALUES (101, '/portero_virtual_insert', 'Adicionar', 'portero_virtual_insert', 'home', 'f', 35);
INSERT INTO "public"."modulo" VALUES (102, '/portero_virtual_update', 'Actualizar', 'portero_virtual_update', 'home', 'f', 35);
INSERT INTO "public"."modulo" VALUES (103, '/portero_virtual_delete', 'Dar de Baja', 'portero_virtual_delete', 'home', 'f', 35);
INSERT INTO "public"."modulo" VALUES (104, '/portero_virtual_imprimir', 'Reportes', 'portero_virtual_imprimir', 'home', 'f', 35);
INSERT INTO "public"."modulo" VALUES (105, '', 'Consultar', 'reporte_query', 'home', 'f', 36);
INSERT INTO "public"."modulo" VALUES (106, '/reporte_imprimir', 'Imprimir', 'reporte_imprimir', 'home', 'f', 36);
INSERT INTO "public"."modulo" VALUES (107, '', 'Consultar', 'registros_c_query', 'home', 'f', 37);
INSERT INTO "public"."modulo" VALUES (108, '/registros_c_imprimir', 'Imprimir', 'registros_c_imprimir', 'home', 'f', 37);
INSERT INTO "public"."modulo" VALUES (109, '', 'Consultar', 'marca_query', 'home', 'f', 67);
INSERT INTO "public"."modulo" VALUES (110, '/marca_insert', 'Adicionar', 'marca_insert', 'home', 'f', 67);
INSERT INTO "public"."modulo" VALUES (111, '/marca_update', 'Actualizar', 'marca_update', 'home', 'f', 67);
INSERT INTO "public"."modulo" VALUES (112, '/marca_delete', 'Dar de Baja', 'marca_delete', 'home', 'f', 67);
INSERT INTO "public"."modulo" VALUES (113, '/marca_imprimir', 'Reportes', 'marca_imprimir', 'home', 'f', 67);
INSERT INTO "public"."modulo" VALUES (114, '', 'Consultar', 'modelo_query', 'home', 'f', 68);
INSERT INTO "public"."modulo" VALUES (115, '/modelo_insert', 'Adicionar', 'modelo_insert', 'home', 'f', 68);
INSERT INTO "public"."modulo" VALUES (116, '/modelo_update', 'Actualizar', 'modelo_update', 'home', 'f', 68);
INSERT INTO "public"."modulo" VALUES (117, '/modelo_delete', 'Dar de Baja', 'modelo_delete', 'home', 'f', 68);
INSERT INTO "public"."modulo" VALUES (118, '/modelo_imprimir', 'Reportes', 'modelo_imprimir', 'home', 'f', 68);
INSERT INTO "public"."modulo" VALUES (119, '', 'Consultar', 'vehiculo_query', 'home', 'f', 69);
INSERT INTO "public"."modulo" VALUES (120, '/vehiculo_insert', 'Adicionar', 'vehiculo_insert', 'home', 'f', 69);
INSERT INTO "public"."modulo" VALUES (121, '/vehiculo_update', 'Actualizar', 'vehiculo_update', 'home', 'f', 69);
INSERT INTO "public"."modulo" VALUES (122, '/vehiculo_delete', 'Dar de Baja', 'vehiculo_delete', 'home', 'f', 69);
INSERT INTO "public"."modulo" VALUES (123, '/vehiculo_imprimir', 'Reportes', 'vehiculo_imprimir', 'home', 'f', 69);
INSERT INTO "public"."modulo" VALUES (124, NULL, 'Gestion de Dispositivos', 'dispositivos', 'devices_other', 't', NULL);
INSERT INTO "public"."modulo" VALUES (125, '/dispositivo', 'Dispositivos', 'dispositivo', 'devices', 't', 124);
INSERT INTO "public"."modulo" VALUES (126, '/config_acceso', 'Configuracion de Acceso', 'config_acceso', 'settings_applications', 't', 124);
INSERT INTO "public"."modulo" VALUES (127, '/registros', 'Monitor de eventos', 'registros', 'assignment', 't', 124);
INSERT INTO "public"."modulo" VALUES (128, '', 'Consultar', 'dispositivo_query', 'home', 'f', 125);
INSERT INTO "public"."modulo" VALUES (129, '/dispositivo_insert', 'Adicionar', 'dispositivo_insert', 'home', 'f', 125);
INSERT INTO "public"."modulo" VALUES (130, '/dispositivo_update', 'Actualizar', 'dispositivo_update', 'home', 'f', 125);
INSERT INTO "public"."modulo" VALUES (131, '/dispositivo_delete', 'Dar de Baja', 'dispositivo_delete', 'home', 'f', 125);
INSERT INTO "public"."modulo" VALUES (132, '', 'Consultar', 'config_acceso_query', 'home', 'f', 126);
INSERT INTO "public"."modulo" VALUES (133, '/config_acceso_insert', 'Adicionar', 'config_acceso_insert', 'home', 'f', 126);
INSERT INTO "public"."modulo" VALUES (134, '/config_acceso_update', 'Actualizar', 'config_acceso_update', 'home', 'f', 126);
INSERT INTO "public"."modulo" VALUES (135, '/config_acceso_delete', 'Dar de Baja', 'config_acceso_delete', 'home', 'f', 126);
INSERT INTO "public"."modulo" VALUES (136, '', 'Consultar', 'registros_query', 'home', 'f', 127);
INSERT INTO "public"."modulo" VALUES (137, '/registros_imprimir', 'Imprimir', 'registros_imprimir', 'home', 'f', 127);

-- ----------------------------
-- Uniques structure for table modulo
-- ----------------------------
ALTER TABLE "public"."modulo" ADD CONSTRAINT "modulo_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table modulo
-- ----------------------------
ALTER TABLE "public"."modulo" ADD CONSTRAINT "modulo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table modulo
-- ----------------------------
ALTER TABLE "public"."modulo" ADD CONSTRAINT "modulo_fkmodulo_fkey" FOREIGN KEY ("fkmodulo") REFERENCES "public"."modulo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;