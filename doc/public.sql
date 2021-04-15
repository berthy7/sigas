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

 Date: 10/12/2020 10:01:42
*/


-- ----------------------------
-- Sequence structure for acceso_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."acceso_id_seq";
CREATE SEQUENCE "public"."acceso_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for acceso_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."acceso_id_seq1";
CREATE SEQUENCE "public"."acceso_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for accesocerraduras_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."accesocerraduras_id_seq";
CREATE SEQUENCE "public"."accesocerraduras_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for accesocerraduras_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."accesocerraduras_id_seq1";
CREATE SEQUENCE "public"."accesocerraduras_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for accesotarjetas_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."accesotarjetas_id_seq";
CREATE SEQUENCE "public"."accesotarjetas_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for accesotarjetas_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."accesotarjetas_id_seq1";
CREATE SEQUENCE "public"."accesotarjetas_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for ajuste_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."ajuste_id_seq";
CREATE SEQUENCE "public"."ajuste_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for amistad_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."amistad_id_seq";
CREATE SEQUENCE "public"."amistad_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for amistad_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."amistad_id_seq1";
CREATE SEQUENCE "public"."amistad_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for areasocial_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."areasocial_id_seq";
CREATE SEQUENCE "public"."areasocial_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for areasocial_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."areasocial_id_seq1";
CREATE SEQUENCE "public"."areasocial_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for autorizacion_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."autorizacion_id_seq";
CREATE SEQUENCE "public"."autorizacion_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for autorizacion_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."autorizacion_id_seq1";
CREATE SEQUENCE "public"."autorizacion_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for bitacora_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."bitacora_id_seq";
CREATE SEQUENCE "public"."bitacora_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for bitacora_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."bitacora_id_seq1";
CREATE SEQUENCE "public"."bitacora_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for cerraduras_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."cerraduras_id_seq";
CREATE SEQUENCE "public"."cerraduras_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for cerraduras_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."cerraduras_id_seq1";
CREATE SEQUENCE "public"."cerraduras_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for codigoqr_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."codigoqr_id_seq";
CREATE SEQUENCE "public"."codigoqr_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for codigoqr_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."codigoqr_id_seq1";
CREATE SEQUENCE "public"."codigoqr_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for color_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."color_id_seq";
CREATE SEQUENCE "public"."color_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for color_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."color_id_seq1";
CREATE SEQUENCE "public"."color_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for condominio_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."condominio_id_seq";
CREATE SEQUENCE "public"."condominio_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for condominio_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."condominio_id_seq1";
CREATE SEQUENCE "public"."condominio_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for condominioentrada_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."condominioentrada_id_seq";
CREATE SEQUENCE "public"."condominioentrada_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for condominioentrada_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."condominioentrada_id_seq1";
CREATE SEQUENCE "public"."condominioentrada_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for condominiopases_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."condominiopases_id_seq";
CREATE SEQUENCE "public"."condominiopases_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for condominiopases_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."condominiopases_id_seq1";
CREATE SEQUENCE "public"."condominiopases_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for configuracionacceso_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."configuracionacceso_id_seq";
CREATE SEQUENCE "public"."configuracionacceso_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for configuracionacceso_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."configuracionacceso_id_seq1";
CREATE SEQUENCE "public"."configuracionacceso_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for configuraciondispositivo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."configuraciondispositivo_id_seq";
CREATE SEQUENCE "public"."configuraciondispositivo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for configuraciondispositivo_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."configuraciondispositivo_id_seq1";
CREATE SEQUENCE "public"."configuraciondispositivo_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for dispositivo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."dispositivo_id_seq";
CREATE SEQUENCE "public"."dispositivo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for dispositivo_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."dispositivo_id_seq1";
CREATE SEQUENCE "public"."dispositivo_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for dispositivoeventos_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."dispositivoeventos_id_seq";
CREATE SEQUENCE "public"."dispositivoeventos_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for dispositivoeventos_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."dispositivoeventos_id_seq1";
CREATE SEQUENCE "public"."dispositivoeventos_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for dispositivointerprete_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."dispositivointerprete_id_seq";
CREATE SEQUENCE "public"."dispositivointerprete_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for dispositivointerprete_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."dispositivointerprete_id_seq1";
CREATE SEQUENCE "public"."dispositivointerprete_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for domicilio_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."domicilio_id_seq";
CREATE SEQUENCE "public"."domicilio_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for domicilio_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."domicilio_id_seq1";
CREATE SEQUENCE "public"."domicilio_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for entrada_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."entrada_id_seq";
CREATE SEQUENCE "public"."entrada_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for entrada_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."entrada_id_seq1";
CREATE SEQUENCE "public"."entrada_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for evento_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."evento_id_seq";
CREATE SEQUENCE "public"."evento_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for evento_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."evento_id_seq1";
CREATE SEQUENCE "public"."evento_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for id
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."id";
CREATE SEQUENCE "public"."id" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for interprete_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."interprete_id_seq";
CREATE SEQUENCE "public"."interprete_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for interprete_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."interprete_id_seq1";
CREATE SEQUENCE "public"."interprete_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for invitacion_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."invitacion_id_seq";
CREATE SEQUENCE "public"."invitacion_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for invitacion_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."invitacion_id_seq1";
CREATE SEQUENCE "public"."invitacion_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for invitado_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."invitado_id_seq";
CREATE SEQUENCE "public"."invitado_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for invitado_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."invitado_id_seq1";
CREATE SEQUENCE "public"."invitado_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for marca_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."marca_id_seq";
CREATE SEQUENCE "public"."marca_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for marca_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."marca_id_seq1";
CREATE SEQUENCE "public"."marca_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for modelo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."modelo_id_seq";
CREATE SEQUENCE "public"."modelo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for modelo_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."modelo_id_seq1";
CREATE SEQUENCE "public"."modelo_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for modulo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."modulo_id_seq";
CREATE SEQUENCE "public"."modulo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for modulo_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."modulo_id_seq1";
CREATE SEQUENCE "public"."modulo_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for movimiento_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."movimiento_id_seq";
CREATE SEQUENCE "public"."movimiento_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for movimiento_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."movimiento_id_seq1";
CREATE SEQUENCE "public"."movimiento_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for nropase_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."nropase_id_seq";
CREATE SEQUENCE "public"."nropase_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for nropase_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."nropase_id_seq1";
CREATE SEQUENCE "public"."nropase_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for portero_virtual_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."portero_virtual_id_seq";
CREATE SEQUENCE "public"."portero_virtual_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for portero_virtual_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."portero_virtual_id_seq1";
CREATE SEQUENCE "public"."portero_virtual_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for principal_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."principal_id_seq";
CREATE SEQUENCE "public"."principal_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for principal_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."principal_id_seq1";
CREATE SEQUENCE "public"."principal_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for registroscontrolador_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."registroscontrolador_id_seq";
CREATE SEQUENCE "public"."registroscontrolador_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for registroscontrolador_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."registroscontrolador_id_seq1";
CREATE SEQUENCE "public"."registroscontrolador_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for residente_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."residente_id_seq";
CREATE SEQUENCE "public"."residente_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for residente_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."residente_id_seq1";
CREATE SEQUENCE "public"."residente_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for residenteacceso_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."residenteacceso_id_seq";
CREATE SEQUENCE "public"."residenteacceso_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for residenteacceso_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."residenteacceso_id_seq1";
CREATE SEQUENCE "public"."residenteacceso_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for residentedomicilio_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."residentedomicilio_id_seq";
CREATE SEQUENCE "public"."residentedomicilio_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for residentedomicilio_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."residentedomicilio_id_seq1";
CREATE SEQUENCE "public"."residentedomicilio_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for rol_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."rol_id_seq";
CREATE SEQUENCE "public"."rol_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for rol_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."rol_id_seq1";
CREATE SEQUENCE "public"."rol_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for servidorCorreo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."servidorCorreo_id_seq";
CREATE SEQUENCE "public"."servidorCorreo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for servidorCorreo_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."servidorCorreo_id_seq1";
CREATE SEQUENCE "public"."servidorCorreo_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipo_documento_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipo_documento_id_seq";
CREATE SEQUENCE "public"."tipo_documento_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipo_documento_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipo_documento_id_seq1";
CREATE SEQUENCE "public"."tipo_documento_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipo_evento_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipo_evento_id_seq";
CREATE SEQUENCE "public"."tipo_evento_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipo_evento_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipo_evento_id_seq1";
CREATE SEQUENCE "public"."tipo_evento_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipo_pase_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipo_pase_id_seq";
CREATE SEQUENCE "public"."tipo_pase_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipo_pase_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipo_pase_id_seq1";
CREATE SEQUENCE "public"."tipo_pase_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipo_vehiculo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipo_vehiculo_id_seq";
CREATE SEQUENCE "public"."tipo_vehiculo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipo_vehiculo_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipo_vehiculo_id_seq1";
CREATE SEQUENCE "public"."tipo_vehiculo_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipodispositivo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipodispositivo_id_seq";
CREATE SEQUENCE "public"."tipodispositivo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tipodispositivo_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tipodispositivo_id_seq1";
CREATE SEQUENCE "public"."tipodispositivo_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for usuario_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."usuario_id_seq";
CREATE SEQUENCE "public"."usuario_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for usuario_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."usuario_id_seq1";
CREATE SEQUENCE "public"."usuario_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for vehiculo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."vehiculo_id_seq";
CREATE SEQUENCE "public"."vehiculo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for vehiculo_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."vehiculo_id_seq1";
CREATE SEQUENCE "public"."vehiculo_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for versionmovil_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."versionmovil_id_seq";
CREATE SEQUENCE "public"."versionmovil_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Table structure for acceso
-- ----------------------------
DROP TABLE IF EXISTS "public"."acceso";
CREATE TABLE "public"."acceso" (
  "id" int4 NOT NULL DEFAULT nextval('acceso_id_seq1'::regclass),
  "fkrol" int4,
  "fkmodulo" int4
)
;

-- ----------------------------
-- Records of acceso
-- ----------------------------
INSERT INTO "public"."acceso" VALUES (1, 1, 1);
INSERT INTO "public"."acceso" VALUES (2, 1, 2);
INSERT INTO "public"."acceso" VALUES (3, 1, 3);
INSERT INTO "public"."acceso" VALUES (4, 1, 4);
INSERT INTO "public"."acceso" VALUES (5, 1, 5);
INSERT INTO "public"."acceso" VALUES (6, 1, 6);
INSERT INTO "public"."acceso" VALUES (7, 1, 7);
INSERT INTO "public"."acceso" VALUES (8, 1, 8);
INSERT INTO "public"."acceso" VALUES (9, 1, 9);
INSERT INTO "public"."acceso" VALUES (10, 1, 10);
INSERT INTO "public"."acceso" VALUES (11, 1, 11);
INSERT INTO "public"."acceso" VALUES (12, 1, 12);
INSERT INTO "public"."acceso" VALUES (13, 1, 13);
INSERT INTO "public"."acceso" VALUES (14, 1, 14);
INSERT INTO "public"."acceso" VALUES (15, 1, 15);
INSERT INTO "public"."acceso" VALUES (16, 1, 16);
INSERT INTO "public"."acceso" VALUES (17, 1, 17);
INSERT INTO "public"."acceso" VALUES (18, 1, 18);
INSERT INTO "public"."acceso" VALUES (19, 1, 19);
INSERT INTO "public"."acceso" VALUES (20, 1, 20);
INSERT INTO "public"."acceso" VALUES (21, 1, 21);
INSERT INTO "public"."acceso" VALUES (22, 2, 1);
INSERT INTO "public"."acceso" VALUES (23, 2, 3);
INSERT INTO "public"."acceso" VALUES (24, 2, 4);
INSERT INTO "public"."acceso" VALUES (25, 2, 5);
INSERT INTO "public"."acceso" VALUES (26, 2, 7);
INSERT INTO "public"."acceso" VALUES (27, 2, 8);
INSERT INTO "public"."acceso" VALUES (28, 2, 9);
INSERT INTO "public"."acceso" VALUES (29, 2, 10);
INSERT INTO "public"."acceso" VALUES (30, 2, 11);
INSERT INTO "public"."acceso" VALUES (31, 2, 12);
INSERT INTO "public"."acceso" VALUES (32, 2, 17);
INSERT INTO "public"."acceso" VALUES (33, 4, 22);
INSERT INTO "public"."acceso" VALUES (34, 4, 24);
INSERT INTO "public"."acceso" VALUES (35, 4, 26);
INSERT INTO "public"."acceso" VALUES (36, 4, 27);
INSERT INTO "public"."acceso" VALUES (37, 4, 28);
INSERT INTO "public"."acceso" VALUES (38, 4, 67);
INSERT INTO "public"."acceso" VALUES (39, 4, 68);
INSERT INTO "public"."acceso" VALUES (40, 4, 69);
INSERT INTO "public"."acceso" VALUES (41, 4, 29);
INSERT INTO "public"."acceso" VALUES (42, 4, 30);
INSERT INTO "public"."acceso" VALUES (43, 4, 43);
INSERT INTO "public"."acceso" VALUES (44, 4, 44);
INSERT INTO "public"."acceso" VALUES (45, 4, 45);
INSERT INTO "public"."acceso" VALUES (46, 4, 46);
INSERT INTO "public"."acceso" VALUES (47, 4, 48);
INSERT INTO "public"."acceso" VALUES (48, 4, 55);
INSERT INTO "public"."acceso" VALUES (49, 4, 56);
INSERT INTO "public"."acceso" VALUES (50, 4, 57);
INSERT INTO "public"."acceso" VALUES (51, 4, 58);
INSERT INTO "public"."acceso" VALUES (52, 4, 59);
INSERT INTO "public"."acceso" VALUES (53, 4, 60);
INSERT INTO "public"."acceso" VALUES (54, 4, 61);
INSERT INTO "public"."acceso" VALUES (55, 4, 62);
INSERT INTO "public"."acceso" VALUES (56, 4, 63);
INSERT INTO "public"."acceso" VALUES (57, 4, 64);
INSERT INTO "public"."acceso" VALUES (58, 4, 65);
INSERT INTO "public"."acceso" VALUES (59, 4, 66);
INSERT INTO "public"."acceso" VALUES (60, 4, 75);
INSERT INTO "public"."acceso" VALUES (61, 4, 76);
INSERT INTO "public"."acceso" VALUES (62, 4, 77);
INSERT INTO "public"."acceso" VALUES (63, 4, 78);
INSERT INTO "public"."acceso" VALUES (64, 4, 79);
INSERT INTO "public"."acceso" VALUES (65, 4, 70);
INSERT INTO "public"."acceso" VALUES (66, 4, 71);
INSERT INTO "public"."acceso" VALUES (67, 4, 72);
INSERT INTO "public"."acceso" VALUES (68, 4, 73);
INSERT INTO "public"."acceso" VALUES (69, 4, 74);
INSERT INTO "public"."acceso" VALUES (70, 4, 109);
INSERT INTO "public"."acceso" VALUES (71, 4, 110);
INSERT INTO "public"."acceso" VALUES (72, 4, 111);
INSERT INTO "public"."acceso" VALUES (73, 4, 112);
INSERT INTO "public"."acceso" VALUES (74, 4, 113);
INSERT INTO "public"."acceso" VALUES (75, 4, 114);
INSERT INTO "public"."acceso" VALUES (76, 4, 115);
INSERT INTO "public"."acceso" VALUES (77, 4, 116);
INSERT INTO "public"."acceso" VALUES (78, 4, 117);
INSERT INTO "public"."acceso" VALUES (79, 4, 118);
INSERT INTO "public"."acceso" VALUES (80, 4, 119);
INSERT INTO "public"."acceso" VALUES (81, 4, 120);
INSERT INTO "public"."acceso" VALUES (82, 4, 121);
INSERT INTO "public"."acceso" VALUES (83, 4, 122);
INSERT INTO "public"."acceso" VALUES (84, 4, 123);
INSERT INTO "public"."acceso" VALUES (85, 1, 22);
INSERT INTO "public"."acceso" VALUES (86, 1, 23);
INSERT INTO "public"."acceso" VALUES (87, 1, 24);
INSERT INTO "public"."acceso" VALUES (88, 1, 25);
INSERT INTO "public"."acceso" VALUES (89, 1, 26);
INSERT INTO "public"."acceso" VALUES (90, 1, 27);
INSERT INTO "public"."acceso" VALUES (91, 1, 28);
INSERT INTO "public"."acceso" VALUES (92, 1, 67);
INSERT INTO "public"."acceso" VALUES (93, 1, 68);
INSERT INTO "public"."acceso" VALUES (94, 1, 69);
INSERT INTO "public"."acceso" VALUES (95, 1, 29);
INSERT INTO "public"."acceso" VALUES (96, 1, 30);
INSERT INTO "public"."acceso" VALUES (97, 1, 31);
INSERT INTO "public"."acceso" VALUES (98, 1, 32);
INSERT INTO "public"."acceso" VALUES (99, 1, 33);
INSERT INTO "public"."acceso" VALUES (100, 1, 34);
INSERT INTO "public"."acceso" VALUES (101, 1, 35);
INSERT INTO "public"."acceso" VALUES (102, 1, 36);
INSERT INTO "public"."acceso" VALUES (103, 1, 37);
INSERT INTO "public"."acceso" VALUES (104, 1, 38);
INSERT INTO "public"."acceso" VALUES (105, 1, 39);
INSERT INTO "public"."acceso" VALUES (106, 1, 40);
INSERT INTO "public"."acceso" VALUES (107, 1, 41);
INSERT INTO "public"."acceso" VALUES (108, 1, 42);
INSERT INTO "public"."acceso" VALUES (109, 1, 43);
INSERT INTO "public"."acceso" VALUES (110, 1, 44);
INSERT INTO "public"."acceso" VALUES (111, 1, 45);
INSERT INTO "public"."acceso" VALUES (112, 1, 46);
INSERT INTO "public"."acceso" VALUES (113, 1, 48);
INSERT INTO "public"."acceso" VALUES (114, 1, 49);
INSERT INTO "public"."acceso" VALUES (115, 1, 50);
INSERT INTO "public"."acceso" VALUES (116, 1, 51);
INSERT INTO "public"."acceso" VALUES (117, 1, 52);
INSERT INTO "public"."acceso" VALUES (118, 1, 53);
INSERT INTO "public"."acceso" VALUES (119, 1, 54);
INSERT INTO "public"."acceso" VALUES (120, 1, 55);
INSERT INTO "public"."acceso" VALUES (121, 1, 56);
INSERT INTO "public"."acceso" VALUES (122, 1, 57);
INSERT INTO "public"."acceso" VALUES (123, 1, 58);
INSERT INTO "public"."acceso" VALUES (124, 1, 59);
INSERT INTO "public"."acceso" VALUES (125, 1, 60);
INSERT INTO "public"."acceso" VALUES (126, 1, 61);
INSERT INTO "public"."acceso" VALUES (127, 1, 62);
INSERT INTO "public"."acceso" VALUES (128, 1, 63);
INSERT INTO "public"."acceso" VALUES (129, 1, 64);
INSERT INTO "public"."acceso" VALUES (130, 1, 65);
INSERT INTO "public"."acceso" VALUES (131, 1, 66);
INSERT INTO "public"."acceso" VALUES (132, 1, 75);
INSERT INTO "public"."acceso" VALUES (133, 1, 76);
INSERT INTO "public"."acceso" VALUES (134, 1, 77);
INSERT INTO "public"."acceso" VALUES (135, 1, 78);
INSERT INTO "public"."acceso" VALUES (136, 1, 79);
INSERT INTO "public"."acceso" VALUES (137, 1, 70);
INSERT INTO "public"."acceso" VALUES (138, 1, 71);
INSERT INTO "public"."acceso" VALUES (139, 1, 72);
INSERT INTO "public"."acceso" VALUES (140, 1, 73);
INSERT INTO "public"."acceso" VALUES (141, 1, 74);
INSERT INTO "public"."acceso" VALUES (142, 1, 109);
INSERT INTO "public"."acceso" VALUES (143, 1, 110);
INSERT INTO "public"."acceso" VALUES (144, 1, 111);
INSERT INTO "public"."acceso" VALUES (145, 1, 112);
INSERT INTO "public"."acceso" VALUES (146, 1, 113);
INSERT INTO "public"."acceso" VALUES (147, 1, 114);
INSERT INTO "public"."acceso" VALUES (148, 1, 115);
INSERT INTO "public"."acceso" VALUES (149, 1, 116);
INSERT INTO "public"."acceso" VALUES (150, 1, 117);
INSERT INTO "public"."acceso" VALUES (151, 1, 118);
INSERT INTO "public"."acceso" VALUES (152, 1, 119);
INSERT INTO "public"."acceso" VALUES (153, 1, 120);
INSERT INTO "public"."acceso" VALUES (154, 1, 121);
INSERT INTO "public"."acceso" VALUES (155, 1, 122);
INSERT INTO "public"."acceso" VALUES (156, 1, 123);
INSERT INTO "public"."acceso" VALUES (157, 1, 80);
INSERT INTO "public"."acceso" VALUES (158, 1, 81);
INSERT INTO "public"."acceso" VALUES (159, 1, 82);
INSERT INTO "public"."acceso" VALUES (160, 1, 83);
INSERT INTO "public"."acceso" VALUES (161, 1, 84);
INSERT INTO "public"."acceso" VALUES (162, 1, 85);
INSERT INTO "public"."acceso" VALUES (163, 1, 86);
INSERT INTO "public"."acceso" VALUES (164, 1, 87);
INSERT INTO "public"."acceso" VALUES (165, 1, 88);
INSERT INTO "public"."acceso" VALUES (166, 1, 89);
INSERT INTO "public"."acceso" VALUES (167, 1, 90);
INSERT INTO "public"."acceso" VALUES (168, 1, 91);
INSERT INTO "public"."acceso" VALUES (169, 1, 92);
INSERT INTO "public"."acceso" VALUES (170, 1, 93);
INSERT INTO "public"."acceso" VALUES (171, 1, 94);
INSERT INTO "public"."acceso" VALUES (172, 1, 95);
INSERT INTO "public"."acceso" VALUES (173, 1, 96);
INSERT INTO "public"."acceso" VALUES (174, 1, 97);
INSERT INTO "public"."acceso" VALUES (175, 1, 98);
INSERT INTO "public"."acceso" VALUES (176, 1, 99);
INSERT INTO "public"."acceso" VALUES (177, 1, 100);
INSERT INTO "public"."acceso" VALUES (178, 1, 101);
INSERT INTO "public"."acceso" VALUES (179, 1, 102);
INSERT INTO "public"."acceso" VALUES (180, 1, 103);
INSERT INTO "public"."acceso" VALUES (181, 1, 104);
INSERT INTO "public"."acceso" VALUES (182, 1, 105);
INSERT INTO "public"."acceso" VALUES (183, 1, 106);
INSERT INTO "public"."acceso" VALUES (184, 1, 107);
INSERT INTO "public"."acceso" VALUES (185, 1, 108);
INSERT INTO "public"."acceso" VALUES (186, 7, 31);
INSERT INTO "public"."acceso" VALUES (187, 7, 32);
INSERT INTO "public"."acceso" VALUES (188, 7, 80);
INSERT INTO "public"."acceso" VALUES (189, 7, 81);
INSERT INTO "public"."acceso" VALUES (190, 7, 82);
INSERT INTO "public"."acceso" VALUES (191, 7, 83);
INSERT INTO "public"."acceso" VALUES (192, 7, 84);
INSERT INTO "public"."acceso" VALUES (193, 7, 85);
INSERT INTO "public"."acceso" VALUES (194, 7, 86);
INSERT INTO "public"."acceso" VALUES (195, 7, 87);
INSERT INTO "public"."acceso" VALUES (196, 7, 88);
INSERT INTO "public"."acceso" VALUES (197, 7, 89);
INSERT INTO "public"."acceso" VALUES (198, 2, 22);
INSERT INTO "public"."acceso" VALUES (199, 2, 23);
INSERT INTO "public"."acceso" VALUES (200, 2, 24);
INSERT INTO "public"."acceso" VALUES (201, 2, 25);
INSERT INTO "public"."acceso" VALUES (202, 2, 26);
INSERT INTO "public"."acceso" VALUES (203, 2, 27);
INSERT INTO "public"."acceso" VALUES (204, 2, 28);
INSERT INTO "public"."acceso" VALUES (205, 2, 67);
INSERT INTO "public"."acceso" VALUES (206, 2, 68);
INSERT INTO "public"."acceso" VALUES (207, 2, 69);
INSERT INTO "public"."acceso" VALUES (208, 2, 29);
INSERT INTO "public"."acceso" VALUES (209, 2, 30);
INSERT INTO "public"."acceso" VALUES (210, 2, 31);
INSERT INTO "public"."acceso" VALUES (211, 2, 32);
INSERT INTO "public"."acceso" VALUES (212, 2, 33);
INSERT INTO "public"."acceso" VALUES (213, 2, 34);
INSERT INTO "public"."acceso" VALUES (214, 2, 35);
INSERT INTO "public"."acceso" VALUES (215, 2, 36);
INSERT INTO "public"."acceso" VALUES (216, 2, 37);
INSERT INTO "public"."acceso" VALUES (217, 2, 38);
INSERT INTO "public"."acceso" VALUES (218, 2, 39);
INSERT INTO "public"."acceso" VALUES (219, 2, 40);
INSERT INTO "public"."acceso" VALUES (220, 2, 41);
INSERT INTO "public"."acceso" VALUES (221, 2, 42);
INSERT INTO "public"."acceso" VALUES (222, 2, 43);
INSERT INTO "public"."acceso" VALUES (223, 2, 44);
INSERT INTO "public"."acceso" VALUES (224, 2, 45);
INSERT INTO "public"."acceso" VALUES (225, 2, 46);
INSERT INTO "public"."acceso" VALUES (226, 2, 48);
INSERT INTO "public"."acceso" VALUES (227, 2, 49);
INSERT INTO "public"."acceso" VALUES (228, 2, 50);
INSERT INTO "public"."acceso" VALUES (229, 2, 51);
INSERT INTO "public"."acceso" VALUES (230, 2, 52);
INSERT INTO "public"."acceso" VALUES (231, 2, 53);
INSERT INTO "public"."acceso" VALUES (232, 2, 54);
INSERT INTO "public"."acceso" VALUES (233, 2, 55);
INSERT INTO "public"."acceso" VALUES (234, 2, 56);
INSERT INTO "public"."acceso" VALUES (235, 2, 57);
INSERT INTO "public"."acceso" VALUES (236, 2, 58);
INSERT INTO "public"."acceso" VALUES (237, 2, 59);
INSERT INTO "public"."acceso" VALUES (238, 2, 60);
INSERT INTO "public"."acceso" VALUES (239, 2, 61);
INSERT INTO "public"."acceso" VALUES (240, 2, 62);
INSERT INTO "public"."acceso" VALUES (241, 2, 63);
INSERT INTO "public"."acceso" VALUES (242, 2, 64);
INSERT INTO "public"."acceso" VALUES (243, 2, 65);
INSERT INTO "public"."acceso" VALUES (244, 2, 66);
INSERT INTO "public"."acceso" VALUES (245, 2, 75);
INSERT INTO "public"."acceso" VALUES (246, 2, 76);
INSERT INTO "public"."acceso" VALUES (247, 2, 77);
INSERT INTO "public"."acceso" VALUES (248, 2, 78);
INSERT INTO "public"."acceso" VALUES (249, 2, 79);
INSERT INTO "public"."acceso" VALUES (250, 2, 70);
INSERT INTO "public"."acceso" VALUES (251, 2, 71);
INSERT INTO "public"."acceso" VALUES (252, 2, 72);
INSERT INTO "public"."acceso" VALUES (253, 2, 73);
INSERT INTO "public"."acceso" VALUES (254, 2, 74);
INSERT INTO "public"."acceso" VALUES (255, 2, 109);
INSERT INTO "public"."acceso" VALUES (256, 2, 110);
INSERT INTO "public"."acceso" VALUES (257, 2, 111);
INSERT INTO "public"."acceso" VALUES (258, 2, 112);
INSERT INTO "public"."acceso" VALUES (259, 2, 113);
INSERT INTO "public"."acceso" VALUES (260, 2, 114);
INSERT INTO "public"."acceso" VALUES (261, 2, 115);
INSERT INTO "public"."acceso" VALUES (262, 2, 116);
INSERT INTO "public"."acceso" VALUES (263, 2, 117);
INSERT INTO "public"."acceso" VALUES (264, 2, 118);
INSERT INTO "public"."acceso" VALUES (265, 2, 119);
INSERT INTO "public"."acceso" VALUES (266, 2, 120);
INSERT INTO "public"."acceso" VALUES (267, 2, 121);
INSERT INTO "public"."acceso" VALUES (268, 2, 122);
INSERT INTO "public"."acceso" VALUES (269, 2, 123);
INSERT INTO "public"."acceso" VALUES (270, 2, 80);
INSERT INTO "public"."acceso" VALUES (271, 2, 81);
INSERT INTO "public"."acceso" VALUES (272, 2, 82);
INSERT INTO "public"."acceso" VALUES (273, 2, 83);
INSERT INTO "public"."acceso" VALUES (274, 2, 84);
INSERT INTO "public"."acceso" VALUES (275, 2, 85);
INSERT INTO "public"."acceso" VALUES (276, 2, 86);
INSERT INTO "public"."acceso" VALUES (277, 2, 87);
INSERT INTO "public"."acceso" VALUES (278, 2, 88);
INSERT INTO "public"."acceso" VALUES (279, 2, 89);
INSERT INTO "public"."acceso" VALUES (280, 2, 90);
INSERT INTO "public"."acceso" VALUES (281, 2, 91);
INSERT INTO "public"."acceso" VALUES (282, 2, 92);
INSERT INTO "public"."acceso" VALUES (283, 2, 93);
INSERT INTO "public"."acceso" VALUES (284, 2, 94);
INSERT INTO "public"."acceso" VALUES (285, 2, 95);
INSERT INTO "public"."acceso" VALUES (286, 2, 96);
INSERT INTO "public"."acceso" VALUES (287, 2, 97);
INSERT INTO "public"."acceso" VALUES (288, 2, 98);
INSERT INTO "public"."acceso" VALUES (289, 2, 99);
INSERT INTO "public"."acceso" VALUES (290, 2, 100);
INSERT INTO "public"."acceso" VALUES (291, 2, 101);
INSERT INTO "public"."acceso" VALUES (292, 2, 102);
INSERT INTO "public"."acceso" VALUES (293, 2, 103);
INSERT INTO "public"."acceso" VALUES (294, 2, 104);
INSERT INTO "public"."acceso" VALUES (295, 2, 105);
INSERT INTO "public"."acceso" VALUES (296, 2, 106);
INSERT INTO "public"."acceso" VALUES (297, 2, 107);
INSERT INTO "public"."acceso" VALUES (298, 2, 108);
INSERT INTO "public"."acceso" VALUES (299, 3, 22);
INSERT INTO "public"."acceso" VALUES (300, 3, 23);
INSERT INTO "public"."acceso" VALUES (301, 3, 24);
INSERT INTO "public"."acceso" VALUES (302, 3, 25);
INSERT INTO "public"."acceso" VALUES (303, 3, 26);
INSERT INTO "public"."acceso" VALUES (304, 3, 27);
INSERT INTO "public"."acceso" VALUES (305, 3, 28);
INSERT INTO "public"."acceso" VALUES (306, 3, 67);
INSERT INTO "public"."acceso" VALUES (307, 3, 68);
INSERT INTO "public"."acceso" VALUES (308, 3, 69);
INSERT INTO "public"."acceso" VALUES (309, 3, 29);
INSERT INTO "public"."acceso" VALUES (310, 3, 30);
INSERT INTO "public"."acceso" VALUES (311, 3, 31);
INSERT INTO "public"."acceso" VALUES (312, 3, 32);
INSERT INTO "public"."acceso" VALUES (313, 3, 33);
INSERT INTO "public"."acceso" VALUES (314, 3, 34);
INSERT INTO "public"."acceso" VALUES (315, 3, 35);
INSERT INTO "public"."acceso" VALUES (316, 3, 36);
INSERT INTO "public"."acceso" VALUES (317, 3, 37);
INSERT INTO "public"."acceso" VALUES (318, 3, 38);
INSERT INTO "public"."acceso" VALUES (319, 3, 39);
INSERT INTO "public"."acceso" VALUES (320, 3, 40);
INSERT INTO "public"."acceso" VALUES (321, 3, 41);
INSERT INTO "public"."acceso" VALUES (322, 3, 42);
INSERT INTO "public"."acceso" VALUES (323, 3, 43);
INSERT INTO "public"."acceso" VALUES (324, 3, 44);
INSERT INTO "public"."acceso" VALUES (325, 3, 45);
INSERT INTO "public"."acceso" VALUES (326, 3, 46);
INSERT INTO "public"."acceso" VALUES (327, 3, 48);
INSERT INTO "public"."acceso" VALUES (328, 3, 49);
INSERT INTO "public"."acceso" VALUES (329, 3, 50);
INSERT INTO "public"."acceso" VALUES (330, 3, 51);
INSERT INTO "public"."acceso" VALUES (331, 3, 52);
INSERT INTO "public"."acceso" VALUES (332, 3, 53);
INSERT INTO "public"."acceso" VALUES (333, 3, 54);
INSERT INTO "public"."acceso" VALUES (334, 3, 55);
INSERT INTO "public"."acceso" VALUES (335, 3, 56);
INSERT INTO "public"."acceso" VALUES (336, 3, 57);
INSERT INTO "public"."acceso" VALUES (337, 3, 58);
INSERT INTO "public"."acceso" VALUES (338, 3, 59);
INSERT INTO "public"."acceso" VALUES (339, 3, 60);
INSERT INTO "public"."acceso" VALUES (340, 3, 61);
INSERT INTO "public"."acceso" VALUES (341, 3, 62);
INSERT INTO "public"."acceso" VALUES (342, 3, 63);
INSERT INTO "public"."acceso" VALUES (343, 3, 64);
INSERT INTO "public"."acceso" VALUES (344, 3, 65);
INSERT INTO "public"."acceso" VALUES (345, 3, 75);
INSERT INTO "public"."acceso" VALUES (346, 3, 76);
INSERT INTO "public"."acceso" VALUES (347, 3, 77);
INSERT INTO "public"."acceso" VALUES (348, 3, 78);
INSERT INTO "public"."acceso" VALUES (349, 3, 79);
INSERT INTO "public"."acceso" VALUES (350, 3, 70);
INSERT INTO "public"."acceso" VALUES (351, 3, 71);
INSERT INTO "public"."acceso" VALUES (352, 3, 72);
INSERT INTO "public"."acceso" VALUES (353, 3, 73);
INSERT INTO "public"."acceso" VALUES (354, 3, 74);
INSERT INTO "public"."acceso" VALUES (355, 3, 109);
INSERT INTO "public"."acceso" VALUES (356, 3, 110);
INSERT INTO "public"."acceso" VALUES (357, 3, 111);
INSERT INTO "public"."acceso" VALUES (358, 3, 112);
INSERT INTO "public"."acceso" VALUES (359, 3, 113);
INSERT INTO "public"."acceso" VALUES (360, 3, 114);
INSERT INTO "public"."acceso" VALUES (361, 3, 115);
INSERT INTO "public"."acceso" VALUES (362, 3, 116);
INSERT INTO "public"."acceso" VALUES (363, 3, 117);
INSERT INTO "public"."acceso" VALUES (364, 3, 118);
INSERT INTO "public"."acceso" VALUES (365, 3, 119);
INSERT INTO "public"."acceso" VALUES (366, 3, 120);
INSERT INTO "public"."acceso" VALUES (367, 3, 121);
INSERT INTO "public"."acceso" VALUES (368, 3, 122);
INSERT INTO "public"."acceso" VALUES (369, 3, 123);
INSERT INTO "public"."acceso" VALUES (370, 3, 80);
INSERT INTO "public"."acceso" VALUES (371, 3, 81);
INSERT INTO "public"."acceso" VALUES (372, 3, 82);
INSERT INTO "public"."acceso" VALUES (373, 3, 83);
INSERT INTO "public"."acceso" VALUES (374, 3, 84);
INSERT INTO "public"."acceso" VALUES (375, 3, 85);
INSERT INTO "public"."acceso" VALUES (376, 3, 86);
INSERT INTO "public"."acceso" VALUES (377, 3, 87);
INSERT INTO "public"."acceso" VALUES (378, 3, 88);
INSERT INTO "public"."acceso" VALUES (379, 3, 89);
INSERT INTO "public"."acceso" VALUES (380, 3, 90);
INSERT INTO "public"."acceso" VALUES (381, 3, 91);
INSERT INTO "public"."acceso" VALUES (382, 3, 92);
INSERT INTO "public"."acceso" VALUES (383, 3, 93);
INSERT INTO "public"."acceso" VALUES (384, 3, 94);
INSERT INTO "public"."acceso" VALUES (385, 3, 95);
INSERT INTO "public"."acceso" VALUES (386, 3, 96);
INSERT INTO "public"."acceso" VALUES (387, 3, 97);
INSERT INTO "public"."acceso" VALUES (388, 3, 98);
INSERT INTO "public"."acceso" VALUES (389, 3, 99);
INSERT INTO "public"."acceso" VALUES (390, 3, 100);
INSERT INTO "public"."acceso" VALUES (391, 3, 101);
INSERT INTO "public"."acceso" VALUES (392, 3, 102);
INSERT INTO "public"."acceso" VALUES (393, 3, 103);
INSERT INTO "public"."acceso" VALUES (394, 3, 104);
INSERT INTO "public"."acceso" VALUES (395, 3, 105);
INSERT INTO "public"."acceso" VALUES (396, 3, 106);
INSERT INTO "public"."acceso" VALUES (397, 3, 107);
INSERT INTO "public"."acceso" VALUES (398, 3, 108);
INSERT INTO "public"."acceso" VALUES (399, 6, 33);
INSERT INTO "public"."acceso" VALUES (400, 6, 34);
INSERT INTO "public"."acceso" VALUES (401, 6, 37);
INSERT INTO "public"."acceso" VALUES (402, 6, 90);
INSERT INTO "public"."acceso" VALUES (403, 6, 91);
INSERT INTO "public"."acceso" VALUES (404, 6, 92);
INSERT INTO "public"."acceso" VALUES (405, 6, 95);
INSERT INTO "public"."acceso" VALUES (406, 6, 96);
INSERT INTO "public"."acceso" VALUES (407, 6, 97);
INSERT INTO "public"."acceso" VALUES (408, 6, 107);
INSERT INTO "public"."acceso" VALUES (409, 6, 108);
INSERT INTO "public"."acceso" VALUES (410, 5, 22);
INSERT INTO "public"."acceso" VALUES (411, 5, 23);
INSERT INTO "public"."acceso" VALUES (412, 5, 24);
INSERT INTO "public"."acceso" VALUES (413, 5, 25);
INSERT INTO "public"."acceso" VALUES (414, 5, 26);
INSERT INTO "public"."acceso" VALUES (415, 5, 27);
INSERT INTO "public"."acceso" VALUES (416, 5, 28);
INSERT INTO "public"."acceso" VALUES (417, 5, 67);
INSERT INTO "public"."acceso" VALUES (418, 5, 68);
INSERT INTO "public"."acceso" VALUES (419, 5, 69);
INSERT INTO "public"."acceso" VALUES (420, 5, 29);
INSERT INTO "public"."acceso" VALUES (421, 5, 30);
INSERT INTO "public"."acceso" VALUES (422, 5, 31);
INSERT INTO "public"."acceso" VALUES (423, 5, 32);
INSERT INTO "public"."acceso" VALUES (424, 5, 33);
INSERT INTO "public"."acceso" VALUES (425, 5, 34);
INSERT INTO "public"."acceso" VALUES (426, 5, 35);
INSERT INTO "public"."acceso" VALUES (427, 5, 36);
INSERT INTO "public"."acceso" VALUES (428, 5, 37);
INSERT INTO "public"."acceso" VALUES (429, 5, 38);
INSERT INTO "public"."acceso" VALUES (430, 5, 39);
INSERT INTO "public"."acceso" VALUES (431, 5, 40);
INSERT INTO "public"."acceso" VALUES (432, 5, 41);
INSERT INTO "public"."acceso" VALUES (433, 5, 42);
INSERT INTO "public"."acceso" VALUES (434, 5, 43);
INSERT INTO "public"."acceso" VALUES (435, 5, 44);
INSERT INTO "public"."acceso" VALUES (436, 5, 45);
INSERT INTO "public"."acceso" VALUES (437, 5, 46);
INSERT INTO "public"."acceso" VALUES (438, 5, 48);
INSERT INTO "public"."acceso" VALUES (439, 5, 49);
INSERT INTO "public"."acceso" VALUES (440, 5, 50);
INSERT INTO "public"."acceso" VALUES (441, 5, 51);
INSERT INTO "public"."acceso" VALUES (442, 5, 52);
INSERT INTO "public"."acceso" VALUES (443, 5, 53);
INSERT INTO "public"."acceso" VALUES (444, 5, 54);
INSERT INTO "public"."acceso" VALUES (445, 5, 55);
INSERT INTO "public"."acceso" VALUES (446, 5, 56);
INSERT INTO "public"."acceso" VALUES (447, 5, 57);
INSERT INTO "public"."acceso" VALUES (448, 5, 58);
INSERT INTO "public"."acceso" VALUES (449, 5, 59);
INSERT INTO "public"."acceso" VALUES (450, 5, 60);
INSERT INTO "public"."acceso" VALUES (451, 5, 61);
INSERT INTO "public"."acceso" VALUES (452, 5, 62);
INSERT INTO "public"."acceso" VALUES (453, 5, 63);
INSERT INTO "public"."acceso" VALUES (454, 5, 64);
INSERT INTO "public"."acceso" VALUES (455, 5, 65);
INSERT INTO "public"."acceso" VALUES (456, 5, 75);
INSERT INTO "public"."acceso" VALUES (457, 5, 76);
INSERT INTO "public"."acceso" VALUES (458, 5, 77);
INSERT INTO "public"."acceso" VALUES (459, 5, 78);
INSERT INTO "public"."acceso" VALUES (460, 5, 79);
INSERT INTO "public"."acceso" VALUES (461, 5, 70);
INSERT INTO "public"."acceso" VALUES (462, 5, 71);
INSERT INTO "public"."acceso" VALUES (463, 5, 72);
INSERT INTO "public"."acceso" VALUES (464, 5, 73);
INSERT INTO "public"."acceso" VALUES (465, 5, 74);
INSERT INTO "public"."acceso" VALUES (466, 5, 109);
INSERT INTO "public"."acceso" VALUES (467, 5, 110);
INSERT INTO "public"."acceso" VALUES (468, 5, 111);
INSERT INTO "public"."acceso" VALUES (469, 5, 112);
INSERT INTO "public"."acceso" VALUES (470, 5, 113);
INSERT INTO "public"."acceso" VALUES (471, 5, 114);
INSERT INTO "public"."acceso" VALUES (472, 5, 115);
INSERT INTO "public"."acceso" VALUES (473, 5, 116);
INSERT INTO "public"."acceso" VALUES (474, 5, 117);
INSERT INTO "public"."acceso" VALUES (475, 5, 118);
INSERT INTO "public"."acceso" VALUES (476, 5, 119);
INSERT INTO "public"."acceso" VALUES (477, 5, 120);
INSERT INTO "public"."acceso" VALUES (478, 5, 121);
INSERT INTO "public"."acceso" VALUES (479, 5, 122);
INSERT INTO "public"."acceso" VALUES (480, 5, 123);
INSERT INTO "public"."acceso" VALUES (481, 5, 80);
INSERT INTO "public"."acceso" VALUES (482, 5, 81);
INSERT INTO "public"."acceso" VALUES (483, 5, 82);
INSERT INTO "public"."acceso" VALUES (484, 5, 83);
INSERT INTO "public"."acceso" VALUES (485, 5, 84);
INSERT INTO "public"."acceso" VALUES (486, 5, 85);
INSERT INTO "public"."acceso" VALUES (487, 5, 86);
INSERT INTO "public"."acceso" VALUES (488, 5, 87);
INSERT INTO "public"."acceso" VALUES (489, 5, 88);
INSERT INTO "public"."acceso" VALUES (490, 5, 89);
INSERT INTO "public"."acceso" VALUES (491, 5, 90);
INSERT INTO "public"."acceso" VALUES (492, 5, 91);
INSERT INTO "public"."acceso" VALUES (493, 5, 92);
INSERT INTO "public"."acceso" VALUES (494, 5, 93);
INSERT INTO "public"."acceso" VALUES (495, 5, 94);
INSERT INTO "public"."acceso" VALUES (496, 5, 95);
INSERT INTO "public"."acceso" VALUES (497, 5, 96);
INSERT INTO "public"."acceso" VALUES (498, 5, 97);
INSERT INTO "public"."acceso" VALUES (499, 5, 98);
INSERT INTO "public"."acceso" VALUES (500, 5, 99);
INSERT INTO "public"."acceso" VALUES (501, 5, 100);
INSERT INTO "public"."acceso" VALUES (502, 5, 101);
INSERT INTO "public"."acceso" VALUES (503, 5, 102);
INSERT INTO "public"."acceso" VALUES (504, 5, 103);
INSERT INTO "public"."acceso" VALUES (505, 5, 104);
INSERT INTO "public"."acceso" VALUES (506, 5, 105);
INSERT INTO "public"."acceso" VALUES (507, 5, 106);
INSERT INTO "public"."acceso" VALUES (508, 5, 107);
INSERT INTO "public"."acceso" VALUES (509, 5, 108);
INSERT INTO "public"."acceso" VALUES (510, 3, 124);
INSERT INTO "public"."acceso" VALUES (511, 3, 125);
INSERT INTO "public"."acceso" VALUES (512, 3, 126);
INSERT INTO "public"."acceso" VALUES (513, 3, 127);
INSERT INTO "public"."acceso" VALUES (514, 3, 128);
INSERT INTO "public"."acceso" VALUES (515, 3, 129);
INSERT INTO "public"."acceso" VALUES (516, 3, 130);
INSERT INTO "public"."acceso" VALUES (517, 3, 131);
INSERT INTO "public"."acceso" VALUES (518, 3, 132);
INSERT INTO "public"."acceso" VALUES (519, 3, 133);
INSERT INTO "public"."acceso" VALUES (520, 3, 134);
INSERT INTO "public"."acceso" VALUES (521, 3, 135);
INSERT INTO "public"."acceso" VALUES (522, 3, 136);
INSERT INTO "public"."acceso" VALUES (523, 3, 137);
INSERT INTO "public"."acceso" VALUES (524, 2, 124);
INSERT INTO "public"."acceso" VALUES (525, 2, 125);
INSERT INTO "public"."acceso" VALUES (526, 2, 126);
INSERT INTO "public"."acceso" VALUES (527, 2, 127);
INSERT INTO "public"."acceso" VALUES (528, 2, 128);
INSERT INTO "public"."acceso" VALUES (529, 2, 129);
INSERT INTO "public"."acceso" VALUES (530, 2, 130);
INSERT INTO "public"."acceso" VALUES (531, 2, 131);
INSERT INTO "public"."acceso" VALUES (532, 2, 132);
INSERT INTO "public"."acceso" VALUES (533, 2, 133);
INSERT INTO "public"."acceso" VALUES (534, 2, 134);
INSERT INTO "public"."acceso" VALUES (535, 2, 135);
INSERT INTO "public"."acceso" VALUES (536, 2, 136);
INSERT INTO "public"."acceso" VALUES (537, 2, 137);
INSERT INTO "public"."acceso" VALUES (538, 5, 124);
INSERT INTO "public"."acceso" VALUES (539, 5, 125);
INSERT INTO "public"."acceso" VALUES (540, 5, 126);
INSERT INTO "public"."acceso" VALUES (541, 5, 127);
INSERT INTO "public"."acceso" VALUES (542, 5, 128);
INSERT INTO "public"."acceso" VALUES (543, 5, 129);
INSERT INTO "public"."acceso" VALUES (544, 5, 130);
INSERT INTO "public"."acceso" VALUES (545, 5, 131);
INSERT INTO "public"."acceso" VALUES (546, 5, 132);
INSERT INTO "public"."acceso" VALUES (547, 5, 133);
INSERT INTO "public"."acceso" VALUES (548, 5, 134);
INSERT INTO "public"."acceso" VALUES (549, 5, 135);
INSERT INTO "public"."acceso" VALUES (550, 5, 136);
INSERT INTO "public"."acceso" VALUES (551, 5, 137);
INSERT INTO "public"."acceso" VALUES (552, 4, 124);
INSERT INTO "public"."acceso" VALUES (553, 4, 125);
INSERT INTO "public"."acceso" VALUES (554, 4, 126);
INSERT INTO "public"."acceso" VALUES (555, 4, 127);
INSERT INTO "public"."acceso" VALUES (556, 4, 128);
INSERT INTO "public"."acceso" VALUES (557, 4, 129);
INSERT INTO "public"."acceso" VALUES (558, 4, 130);
INSERT INTO "public"."acceso" VALUES (559, 4, 131);
INSERT INTO "public"."acceso" VALUES (560, 4, 132);
INSERT INTO "public"."acceso" VALUES (561, 4, 133);
INSERT INTO "public"."acceso" VALUES (562, 4, 134);
INSERT INTO "public"."acceso" VALUES (563, 4, 135);
INSERT INTO "public"."acceso" VALUES (564, 4, 136);
INSERT INTO "public"."acceso" VALUES (565, 4, 137);
INSERT INTO "public"."acceso" VALUES (566, 1, 124);
INSERT INTO "public"."acceso" VALUES (567, 1, 125);
INSERT INTO "public"."acceso" VALUES (568, 1, 126);
INSERT INTO "public"."acceso" VALUES (569, 1, 127);
INSERT INTO "public"."acceso" VALUES (570, 1, 128);
INSERT INTO "public"."acceso" VALUES (571, 1, 129);
INSERT INTO "public"."acceso" VALUES (572, 1, 130);
INSERT INTO "public"."acceso" VALUES (573, 1, 131);
INSERT INTO "public"."acceso" VALUES (574, 1, 132);
INSERT INTO "public"."acceso" VALUES (575, 1, 133);
INSERT INTO "public"."acceso" VALUES (576, 1, 134);
INSERT INTO "public"."acceso" VALUES (577, 1, 135);
INSERT INTO "public"."acceso" VALUES (578, 1, 136);
INSERT INTO "public"."acceso" VALUES (579, 1, 137);

-- ----------------------------
-- Table structure for accesocerraduras
-- ----------------------------
DROP TABLE IF EXISTS "public"."accesocerraduras";
CREATE TABLE "public"."accesocerraduras" (
  "id" int4 NOT NULL DEFAULT nextval('accesocerraduras_id_seq1'::regclass),
  "fkconfigacceso" int4,
  "fkcerraduras" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of accesocerraduras
-- ----------------------------

-- ----------------------------
-- Table structure for accesotarjetas
-- ----------------------------
DROP TABLE IF EXISTS "public"."accesotarjetas";
CREATE TABLE "public"."accesotarjetas" (
  "id" int4 NOT NULL DEFAULT nextval('accesotarjetas_id_seq1'::regclass),
  "fkconfigacceso" int4,
  "fknropase" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of accesotarjetas
-- ----------------------------

-- ----------------------------
-- Table structure for ajuste
-- ----------------------------
DROP TABLE IF EXISTS "public"."ajuste";
CREATE TABLE "public"."ajuste" (
  "id" int4 NOT NULL DEFAULT nextval('ajuste_id_seq'::regclass),
  "claveSecreta" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "enabled" bool
)
;

-- ----------------------------
-- Records of ajuste
-- ----------------------------

-- ----------------------------
-- Table structure for amistad
-- ----------------------------
DROP TABLE IF EXISTS "public"."amistad";
CREATE TABLE "public"."amistad" (
  "id" int4 NOT NULL DEFAULT nextval('amistad_id_seq1'::regclass),
  "fkresidente" int4,
  "fkinvitado" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of amistad
-- ----------------------------

-- ----------------------------
-- Table structure for areasocial
-- ----------------------------
DROP TABLE IF EXISTS "public"."areasocial";
CREATE TABLE "public"."areasocial" (
  "id" int4 NOT NULL DEFAULT nextval('areasocial_id_seq1'::regclass),
  "codigo" int4,
  "nombre" varchar(100) COLLATE "pg_catalog"."default",
  "ubicacion" varchar(100) COLLATE "pg_catalog"."default",
  "fkcondominio" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of areasocial
-- ----------------------------

-- ----------------------------
-- Table structure for autorizacion
-- ----------------------------
DROP TABLE IF EXISTS "public"."autorizacion";
CREATE TABLE "public"."autorizacion" (
  "id" int4 NOT NULL DEFAULT nextval('autorizacion_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "estado" bool
)
;

-- ----------------------------
-- Records of autorizacion
-- ----------------------------
INSERT INTO "public"."autorizacion" VALUES (1, 'Residente', 't');
INSERT INTO "public"."autorizacion" VALUES (2, 'Administracion', 't');
INSERT INTO "public"."autorizacion" VALUES (3, 'Emergencia', 't');
INSERT INTO "public"."autorizacion" VALUES (4, 'Negativa de Ingreso', 't');
INSERT INTO "public"."autorizacion" VALUES (5, 'Otros', 't');

-- ----------------------------
-- Table structure for bitacora
-- ----------------------------
DROP TABLE IF EXISTS "public"."bitacora";
CREATE TABLE "public"."bitacora" (
  "id" int8 NOT NULL DEFAULT nextval('bitacora_id_seq1'::regclass),
  "fkusuario" int4,
  "ip" varchar(100) COLLATE "pg_catalog"."default",
  "accion" varchar(200) COLLATE "pg_catalog"."default",
  "fecha" timestamp(6) NOT NULL,
  "tabla" varchar(200) COLLATE "pg_catalog"."default",
  "identificador" int4
)
;

-- ----------------------------
-- Records of bitacora
-- ----------------------------

-- ----------------------------
-- Table structure for cerraduras
-- ----------------------------
DROP TABLE IF EXISTS "public"."cerraduras";
CREATE TABLE "public"."cerraduras" (
  "id" int4 NOT NULL DEFAULT nextval('cerraduras_id_seq1'::regclass),
  "numero" int4 NOT NULL,
  "nombre" varchar(100) COLLATE "pg_catalog"."default",
  "fkdispositivo" int4,
  "fkentrada" int4,
  "estado" bool,
  "linea" bool
)
;

-- ----------------------------
-- Records of cerraduras
-- ----------------------------

-- ----------------------------
-- Table structure for codigoqr
-- ----------------------------
DROP TABLE IF EXISTS "public"."codigoqr";
CREATE TABLE "public"."codigoqr" (
  "id" int4 NOT NULL DEFAULT nextval('codigoqr_id_seq1'::regclass),
  "codigo" text COLLATE "pg_catalog"."default" NOT NULL,
  "tarjeta" text COLLATE "pg_catalog"."default" NOT NULL,
  "situacion" varchar(100) COLLATE "pg_catalog"."default",
  "dispositivo" varchar(100) COLLATE "pg_catalog"."default",
  "estado" bool
)
;

-- ----------------------------
-- Records of codigoqr
-- ----------------------------

-- ----------------------------
-- Table structure for color
-- ----------------------------
DROP TABLE IF EXISTS "public"."color";
CREATE TABLE "public"."color" (
  "id" int4 NOT NULL DEFAULT nextval('color_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "estado" bool
)
;

-- ----------------------------
-- Records of color
-- ----------------------------
INSERT INTO "public"."color" VALUES (1, 'AMARILLO', 't');
INSERT INTO "public"."color" VALUES (2, 'AZUL', 't');
INSERT INTO "public"."color" VALUES (3, 'BLANCO', 't');
INSERT INTO "public"."color" VALUES (4, 'CAFE', 't');
INSERT INTO "public"."color" VALUES (5, 'CELESTE', 't');
INSERT INTO "public"."color" VALUES (6, 'COBRE', 't');
INSERT INTO "public"."color" VALUES (7, 'GRIS', 't');
INSERT INTO "public"."color" VALUES (8, 'NARANJA', 't');
INSERT INTO "public"."color" VALUES (9, 'NEGRO', 't');
INSERT INTO "public"."color" VALUES (10, 'PLATEADO', 't');
INSERT INTO "public"."color" VALUES (11, 'PLOMO', 't');
INSERT INTO "public"."color" VALUES (12, 'ROJO', 't');
INSERT INTO "public"."color" VALUES (13, 'ROSADO', 't');
INSERT INTO "public"."color" VALUES (14, 'VERDE', 't');
INSERT INTO "public"."color" VALUES (15, 'PLATA', 't');

-- ----------------------------
-- Table structure for condominio
-- ----------------------------
DROP TABLE IF EXISTS "public"."condominio";
CREATE TABLE "public"."condominio" (
  "id" int4 NOT NULL DEFAULT nextval('condominio_id_seq1'::regclass),
  "codigo" varchar(100) COLLATE "pg_catalog"."default",
  "nombre" varchar(100) COLLATE "pg_catalog"."default",
  "cant_casas" int4,
  "cant_departamentos" int4,
  "cant_vehiculos" int4,
  "cant_residentes" int4,
  "cant_tarjetas" int4,
  "contrato" int4,
  "fechai" date,
  "fechaf" date,
  "singuardia" bool,
  "estado" bool,
  "ip_publica" varchar(100) COLLATE "pg_catalog"."default",
  "ip_privada" varchar(100) COLLATE "pg_catalog"."default",
  "puerto" varchar(100) COLLATE "pg_catalog"."default",
  "invitacionpaselibre" bool,
  "invitacionmultiple" bool
)
;

-- ----------------------------
-- Records of condominio
-- ----------------------------

-- ----------------------------
-- Table structure for condominioentrada
-- ----------------------------
DROP TABLE IF EXISTS "public"."condominioentrada";
CREATE TABLE "public"."condominioentrada" (
  "id" int4 NOT NULL DEFAULT nextval('condominioentrada_id_seq1'::regclass),
  "fkcondominio" int4,
  "fkentrada" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of condominioentrada
-- ----------------------------

-- ----------------------------
-- Table structure for condominiopases
-- ----------------------------
DROP TABLE IF EXISTS "public"."condominiopases";
CREATE TABLE "public"."condominiopases" (
  "id" int4 NOT NULL DEFAULT nextval('condominiopases_id_seq1'::regclass),
  "fkcondominio" int4,
  "fknropase" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of condominiopases
-- ----------------------------

-- ----------------------------
-- Table structure for configuracionacceso
-- ----------------------------
DROP TABLE IF EXISTS "public"."configuracionacceso";
CREATE TABLE "public"."configuracionacceso" (
  "id" int4 NOT NULL DEFAULT nextval('configuracionacceso_id_seq1'::regclass),
  "nombre" varchar(250) COLLATE "pg_catalog"."default",
  "codigoacceso" varchar(100) COLLATE "pg_catalog"."default",
  "fkcondominio" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of configuracionacceso
-- ----------------------------

-- ----------------------------
-- Table structure for configuraciondispositivo
-- ----------------------------
DROP TABLE IF EXISTS "public"."configuraciondispositivo";
CREATE TABLE "public"."configuraciondispositivo" (
  "id" int4 NOT NULL DEFAULT nextval('configuraciondispositivo_id_seq1'::regclass),
  "codigo" text COLLATE "pg_catalog"."default" NOT NULL,
  "tarjeta" text COLLATE "pg_catalog"."default" NOT NULL,
  "situacion" varchar(100) COLLATE "pg_catalog"."default",
  "fkdispositivo" int4,
  "estado" bool,
  "codigoacceso" varchar(100) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of configuraciondispositivo
-- ----------------------------

-- ----------------------------
-- Table structure for dispositivo
-- ----------------------------
DROP TABLE IF EXISTS "public"."dispositivo";
CREATE TABLE "public"."dispositivo" (
  "id" int4 NOT NULL DEFAULT nextval('dispositivo_id_seq1'::regclass),
  "codigo" int4,
  "ip" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "puerto" int4 NOT NULL,
  "descripcion" varchar(100) COLLATE "pg_catalog"."default",
  "modelo" varchar(100) COLLATE "pg_catalog"."default",
  "fkcondominio" int4,
  "fktipodispositivo" int4,
  "situacion" bool,
  "estado" bool
)
;

-- ----------------------------
-- Records of dispositivo
-- ----------------------------

-- ----------------------------
-- Table structure for dispositivoeventos
-- ----------------------------
DROP TABLE IF EXISTS "public"."dispositivoeventos";
CREATE TABLE "public"."dispositivoeventos" (
  "id" int4 NOT NULL DEFAULT nextval('dispositivoeventos_id_seq1'::regclass),
  "codigo" int4 NOT NULL,
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "descripcion" text COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of dispositivoeventos
-- ----------------------------
INSERT INTO "public"."dispositivoeventos" VALUES (1, 0, 'Apertura', 'In [Card Only] verification mode, the person has open door permission punch the card and triggers this normal event of open the door.');
INSERT INTO "public"."dispositivoeventos" VALUES (2, 1, 'Apertura normal dentro de la zona horaria', 'At the normally open period (set to normally open period of a single door or the door open period after the first card normally open), or through the remote normal open operation, the person has open door permission punch the effective card at the opened door to trigger this normal events.');
INSERT INTO "public"."dispositivoeventos" VALUES (3, 2, '1ra apertura nomarl(tarjeta accion)', 'In [Card Only] verification mode, the person has first card normally open permission, punch card at the setting first card normally open period but the door is not opened, and trigger the normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (4, 3, 'Multitarjeta abierta (tarjeta accionada)', 'In [Card Only] verification mode, multi-card combination can be used to open the door. After the last piece of card verified, the system trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (5, 4, 'Contraseña de emergencia abierta', 'The password (also known as the super password) set for the current door can be used for door open. It will trigger this normal event after the emergency password verified.');
INSERT INTO "public"."dispositivoeventos" VALUES (6, 5, 'Apertura normal durante la zona horaria abierto', 'If the current door is set a normally open period, the door will open automatically after the setting start time, and trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (7, 6, 'Evento de vinculación activado', 'When the linkage setting the system takes effect, trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (8, 7, 'Alarma Cancelada', 'When the user cancel the alarm of the corresponding door, and the operation is success, trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (9, 8, 'Apertura remota', 'When the user opens a door from remote and the operation is successful, it will trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (10, 9, 'Cierre remoto', 'When the user close a door from remote and the operation is successful, it will trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (11, 10, 'Deshabilitar la zona horaria de apertura normal intradía', 'When the door is in Normally Open (NO) state, swipe your valid card five times through the reader or call ControlDevice to disable the NO period on that day. In this case, trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (12, 11, 'Habilitar zona horaria de apertura normal intradía', 'When the door’s NO period is disabled, swipe your valid card (held by the same user) five times through the reader or call ControlDevice to enable the NO period on that day. In this case, trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (13, 12, 'Salida auxiliar abierta', 'If the output point address is set to a specific auxiliary output point and the action type is set enabled in a linkage setting record, then this normal event will be triggered as long as this linkage setting takes effect.');
INSERT INTO "public"."dispositivoeventos" VALUES (14, 13, 'Cerrar salida auxiliar', 'Events that are triggered when you disable the auxiliary input through linkage operations or by calling ControlDevice.');
INSERT INTO "public"."dispositivoeventos" VALUES (15, 14, 'Apertura huella presionada', 'Normal events that are triggered after any person authorized to open the door presses his fingerprint and passes the verification in “Fingerprint only” or “Card/Fingerprint” verification modes.');
INSERT INTO "public"."dispositivoeventos" VALUES (16, 15, 'Multitarjeta abierta (presione la huella digital)', 'Multi-card open(Fingerprint required): normal events that are triggered when the last person opens the door with his fingerprint in “Finger print” verification mode.');
INSERT INTO "public"."dispositivoeventos" VALUES (17, 16, 'Apertura huella presionada durante la zona horaria', 'Normal events that are triggered after any person authorized to open the door presses his valid fingerprint during the NO duration (including the NO durations set for single doors and the first-card NO duration) and through remote operations.');
INSERT INTO "public"."dispositivoeventos" VALUES (18, 17, 'Apertura tarjejta mas huella', 'Normal events that are triggered after any person authorized to open the door swipes his card and presses his fingerprint to pass the verification in the “Card + Fingerprint” verification mode.');
INSERT INTO "public"."dispositivoeventos" VALUES (19, 18, '1ra Apertura (Presione huella)', 'Normal events that are triggered after any person authorized to open the door becomes the first one to press his fingerprint and pass the verification during the preset first-card NO duration and in either the “Fingerprint only” or the “Card/Fingerprint” verification mode.');
INSERT INTO "public"."dispositivoeventos" VALUES (20, 19, '1ra Apertura (Tarjeta mas huella)', 'Normal events that are triggered after any person authorized to open the door becomes the first one to swipe his card and press his fingerprint to pass the verification during the preset first-card NO duration and in the “Card + Fingerprint” verification mode.');
INSERT INTO "public"."dispositivoeventos" VALUES (21, 20, 'Intervalo de accion demasiado corto', 'When the interval between two card punching is less than the interval preset for the door, trigger this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (22, 21, 'Puerta Inactiva por Zona horaria (Tarjeta Accion)', 'In [Card Only] verification mode, the user has the door open permission, punch card but not at the door effective period of time, and trigger this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (23, 22, 'Zona horaria ilegal', 'The user with the permission of opening the current door, punches the card during the invalid time zone, and triggers this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (24, 23, 'Acceso denegado', 'The registered card without the access permission of the current door, punch to open the door, triggers this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (25, 24, 'Anti Passback', 'When the anti-pass back setting of the system takes effect, triggers this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (26, 25, 'Interlock', 'When the interlocking rules of the system take effect, trigger this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (27, 26, 'Autenticación de múltiples tarjetas (tarjeta Accionada)', 'Use multi-card combination to open the door, the card verification before the last one (whether verified or not), trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (28, 27, 'Tarjeta no registrada', 'Refers to the current card is not registered in the system, trigger this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (29, 28, 'Apertura tiempo agotado', 'The door sensor detect that it is expired the delay time after opened, if not close the door, trigger this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (30, 29, 'Tarjeta Expirada', 'The person with the door access permission, punch card to open the door after the effective time of the access control, can not be verified and will trigger this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (31, 30, 'Error de contraseña', 'Use card plus password, duress password or emergency password to open the door, trigger this event if the password is wrong.');
INSERT INTO "public"."dispositivoeventos" VALUES (32, 31, 'Intervalo de presión de huellas dactilares demasiado corto', 'When the interval between two consecutive fingerprints is less than the interval preset for the door, trigger this abnormal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (33, 32, 'Autenticación de múltiples tarjetas (presione con huella)', 'In either the “Fingerprint only” or the “Card/Fingerprint” verification mode, when any person presses his fingerprint to open the door through the multi-card access mode and before the last verification, trigger this event regardless of whether the verification attempt succeeds.');
INSERT INTO "public"."dispositivoeventos" VALUES (34, 33, 'Huella expirada', 'When any person fails to pass the verification with his fingerprint at the end of the access control duration preset by himself, trigger this event.');
INSERT INTO "public"."dispositivoeventos" VALUES (35, 34, 'Huella no registrada', 'Events that are triggered when any fingerprints are not registered in the system or registered but not synchronized to the device.');
INSERT INTO "public"."dispositivoeventos" VALUES (36, 35, 'Puerta inactiva por Zona horaria (Presione con huella)', 'Abnormal events that are triggered when any person authorized to open the door presses his fingerprint during the preset valid duration.');
INSERT INTO "public"."dispositivoeventos" VALUES (37, 36, 'Puerta inactiva por Zona horaria (Botón de salida)', 'Abnormal events that are triggered when any person fails to open the door by pressing the Unlock button during the preset valid duration.');
INSERT INTO "public"."dispositivoeventos" VALUES (38, 37, 'Error al cerrar durante la zona horaria de apertura normal', 'Abnormal events that are triggered when any person fails to close the door in NO state by calling ControlDevice.');
INSERT INTO "public"."dispositivoeventos" VALUES (39, 101, 'Coacción apertura contraseña', 'Use the duress password of current door verified and triggered');
INSERT INTO "public"."dispositivoeventos" VALUES (40, 102, 'Abierto accidentalmente', 'Except all the normal events (normal events such as user with door open permission to punch card and open the door, password open door, open the door at normally open period, remote door open, the linkage triggered door open), the door sensor detect the door is opened, that is the door is unexpectedly opened.');
INSERT INTO "public"."dispositivoeventos" VALUES (41, 103, 'Coacción apertura huella', 'Use the duress fingerprint of current door verified and triggered alarm event.');
INSERT INTO "public"."dispositivoeventos" VALUES (42, 200, 'Puerta abierta correctamente', 'When the door sensor detects that the door has been properly opened, triggering this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (43, 201, 'Puerta cerrada correctamente', 'When the door sensor detects that the door has been properly closed, triggering this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (44, 202, 'Botón de salida abierta', 'User press the exit button to open the door within the door valid time zone, and trigger this normal event.');
INSERT INTO "public"."dispositivoeventos" VALUES (45, 203, 'Apertura multitarjeta (tarjeta más huella digital)', 'Normal events that are triggered when any person passes the verification with his card and fingerprint in multi-card access mode.');
INSERT INTO "public"."dispositivoeventos" VALUES (46, 204, 'Apertura normal sobre Zona horaria', 'After the setting normal open time zone, the door will close automatically. The normal open time zone include the normal open time zone in door setting and the selected normal open time zone in first card setting.');
INSERT INTO "public"."dispositivoeventos" VALUES (47, 205, 'Apertura normal remota', 'Normal events that are triggered when the door is set to the NO state for remote opening operations.');
INSERT INTO "public"."dispositivoeventos" VALUES (48, 206, 'Inicio del dispositivo', 'When the device is being activated, this normal event is triggered.');
INSERT INTO "public"."dispositivoeventos" VALUES (49, 220, 'Entrada auxiliar desconectada', 'When any auxiliary input point breaks down, this normal event is triggered.');
INSERT INTO "public"."dispositivoeventos" VALUES (50, 221, 'Entrada auxiliar en corto', 'When any auxiliary input point has short circuited, this normal event is triggered.');
INSERT INTO "public"."dispositivoeventos" VALUES (51, 255, 'Esta obteniendo el estado de la puerta y alarma', 'Ver documentacion adjunto 7.');

-- ----------------------------
-- Table structure for dispositivointerprete
-- ----------------------------
DROP TABLE IF EXISTS "public"."dispositivointerprete";
CREATE TABLE "public"."dispositivointerprete" (
  "id" int4 NOT NULL DEFAULT nextval('dispositivointerprete_id_seq1'::regclass),
  "fkdispositivo" int4,
  "fkinterprete" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of dispositivointerprete
-- ----------------------------

-- ----------------------------
-- Table structure for domicilio
-- ----------------------------
DROP TABLE IF EXISTS "public"."domicilio";
CREATE TABLE "public"."domicilio" (
  "id" int4 NOT NULL DEFAULT nextval('domicilio_id_seq1'::regclass),
  "codigo" varchar(100) COLLATE "pg_catalog"."default",
  "numero" varchar(100) COLLATE "pg_catalog"."default",
  "ubicacion" varchar(100) COLLATE "pg_catalog"."default",
  "fkcondominio" int4,
  "tipo" varchar(100) COLLATE "pg_catalog"."default",
  "interno" varchar(100) COLLATE "pg_catalog"."default",
  "estado" bool
)
;

-- ----------------------------
-- Records of domicilio
-- ----------------------------

-- ----------------------------
-- Table structure for entrada
-- ----------------------------
DROP TABLE IF EXISTS "public"."entrada";
CREATE TABLE "public"."entrada" (
  "id" int4 NOT NULL DEFAULT nextval('entrada_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default",
  "estado" bool
)
;

-- ----------------------------
-- Records of entrada
-- ----------------------------
INSERT INTO "public"."entrada" VALUES (1, 'Entrada peatonal Visitas', 't');
INSERT INTO "public"."entrada" VALUES (2, 'Entrada vehicular Visitas', 't');
INSERT INTO "public"."entrada" VALUES (3, 'Entrada peatonal Residentes', 't');
INSERT INTO "public"."entrada" VALUES (4, 'Entrada vehicular Residentes', 't');
INSERT INTO "public"."entrada" VALUES (5, 'Salida peatonal Visitas', 't');
INSERT INTO "public"."entrada" VALUES (6, 'Salida vehicular Visitas', 't');
INSERT INTO "public"."entrada" VALUES (7, 'Salida peatonal Residentes', 't');
INSERT INTO "public"."entrada" VALUES (8, 'Salida vehicular Residentes', 't');
INSERT INTO "public"."entrada" VALUES (9, 'Entrada Porteria virtual', 't');

-- ----------------------------
-- Table structure for evento
-- ----------------------------
DROP TABLE IF EXISTS "public"."evento";
CREATE TABLE "public"."evento" (
  "id" int4 NOT NULL DEFAULT nextval('evento_id_seq1'::regclass),
  "codigo" int4,
  "descripcion" varchar(255) COLLATE "pg_catalog"."default",
  "fktipoevento" int4,
  "fkresidente" int4,
  "fechai" date,
  "fechaf" date,
  "horai" time(6),
  "horaf" time(6),
  "fkdomicilio" int4,
  "fkareasocial" int4,
  "situacion" varchar(100) COLLATE "pg_catalog"."default",
  "multiacceso" bool,
  "paselibre" bool,
  "multiple" bool,
  "estado" bool
)
;

-- ----------------------------
-- Records of evento
-- ----------------------------

-- ----------------------------
-- Table structure for interprete
-- ----------------------------
DROP TABLE IF EXISTS "public"."interprete";
CREATE TABLE "public"."interprete" (
  "id" int4 NOT NULL DEFAULT nextval('interprete_id_seq1'::regclass),
  "nombre" varchar(200) COLLATE "pg_catalog"."default",
  "estado" bool
)
;

-- ----------------------------
-- Records of interprete
-- ----------------------------
INSERT INTO "public"."interprete" VALUES (1, 'Servidor Ciudad Jardin', 't');
INSERT INTO "public"."interprete" VALUES (2, 'Servidor Demo', 't');

-- ----------------------------
-- Table structure for invitacion
-- ----------------------------
DROP TABLE IF EXISTS "public"."invitacion";
CREATE TABLE "public"."invitacion" (
  "id" int4 NOT NULL DEFAULT nextval('invitacion_id_seq1'::regclass),
  "fkevento" int4,
  "fkinvitado" int4,
  "fktipopase" int4,
  "codigoautorizacion" text COLLATE "pg_catalog"."default",
  "estado" bool
)
;

-- ----------------------------
-- Records of invitacion
-- ----------------------------

-- ----------------------------
-- Table structure for invitado
-- ----------------------------
DROP TABLE IF EXISTS "public"."invitado";
CREATE TABLE "public"."invitado" (
  "id" int4 NOT NULL DEFAULT nextval('invitado_id_seq1'::regclass),
  "codigo" int4,
  "nombre" varchar(100) COLLATE "pg_catalog"."default",
  "apellidop" varchar(100) COLLATE "pg_catalog"."default",
  "apellidom" varchar(100) COLLATE "pg_catalog"."default",
  "sexo" varchar(10) COLLATE "pg_catalog"."default",
  "ci" varchar(50) COLLATE "pg_catalog"."default",
  "expendido" varchar(20) COLLATE "pg_catalog"."default",
  "telefono" varchar(100) COLLATE "pg_catalog"."default",
  "foto" text COLLATE "pg_catalog"."default",
  "descripcion" text COLLATE "pg_catalog"."default",
  "permanente" bool,
  "fknropase" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of invitado
-- ----------------------------

-- ----------------------------
-- Table structure for marca
-- ----------------------------
DROP TABLE IF EXISTS "public"."marca";
CREATE TABLE "public"."marca" (
  "id" int4 NOT NULL DEFAULT nextval('marca_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "estado" bool
)
;

-- ----------------------------
-- Records of marca
-- ----------------------------

-- ----------------------------
-- Table structure for modelo
-- ----------------------------
DROP TABLE IF EXISTS "public"."modelo";
CREATE TABLE "public"."modelo" (
  "id" int4 NOT NULL DEFAULT nextval('modelo_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "fkmarca" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of modelo
-- ----------------------------

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
-- Table structure for movimiento
-- ----------------------------
DROP TABLE IF EXISTS "public"."movimiento";
CREATE TABLE "public"."movimiento" (
  "id" int4 NOT NULL DEFAULT nextval('movimiento_id_seq1'::regclass),
  "codigo" int4,
  "fkinvitacion" int4,
  "fktipodocumento" int4,
  "fkinvitado" int4,
  "fkvehiculo" int4,
  "fechai" timestamp(6),
  "fechaf" timestamp(6),
  "fechar" timestamp(6),
  "fkresidente" int4,
  "fkautorizacion" int4,
  "fkdomicilio" int4,
  "fkareasocial" int4,
  "fktipopase" int4,
  "codigoautorizacion" text COLLATE "pg_catalog"."default",
  "fknropase" int4,
  "observacion" text COLLATE "pg_catalog"."default",
  "tipo" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "cantpasajeros" int4,
  "fktipodocumento_conductor" int4,
  "fkconductor" int4,
  "visita" bool,
  "estado" bool
)
;

-- ----------------------------
-- Records of movimiento
-- ----------------------------

-- ----------------------------
-- Table structure for nropase
-- ----------------------------
DROP TABLE IF EXISTS "public"."nropase";
CREATE TABLE "public"."nropase" (
  "id" int4 NOT NULL DEFAULT nextval('nropase_id_seq1'::regclass),
  "codigo" int4,
  "numero" text COLLATE "pg_catalog"."default",
  "tarjeta" text COLLATE "pg_catalog"."default",
  "tipo" varchar(200) COLLATE "pg_catalog"."default",
  "situacion" varchar(200) COLLATE "pg_catalog"."default",
  "estado" bool
)
;

-- ----------------------------
-- Records of nropase
-- ----------------------------

-- ----------------------------
-- Table structure for portero_virtual
-- ----------------------------
DROP TABLE IF EXISTS "public"."portero_virtual";
CREATE TABLE "public"."portero_virtual" (
  "id" int4 NOT NULL DEFAULT nextval('portero_virtual_id_seq1'::regclass),
  "codigo" int4,
  "fkinvitacion" int4,
  "fkcerradura" int4,
  "fktipodocumento" int4,
  "fkinvitado" int4,
  "fechai" timestamp(6),
  "fechaf" timestamp(6),
  "fechar" timestamp(6),
  "fkresidente" int4,
  "fkautorizacion" int4,
  "fktipopase" int4,
  "codigoautorizacion" text COLLATE "pg_catalog"."default",
  "observacion" text COLLATE "pg_catalog"."default",
  "tipo" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "sincronizacion" bool,
  "estado" bool
)
;

-- ----------------------------
-- Records of portero_virtual
-- ----------------------------

-- ----------------------------
-- Table structure for principal
-- ----------------------------
DROP TABLE IF EXISTS "public"."principal";
CREATE TABLE "public"."principal" (
  "id" int4 NOT NULL DEFAULT nextval('principal_id_seq1'::regclass),
  "estado" bool
)
;

-- ----------------------------
-- Records of principal
-- ----------------------------
INSERT INTO "public"."principal" VALUES (1, 'f');

-- ----------------------------
-- Table structure for registroscontrolador
-- ----------------------------
DROP TABLE IF EXISTS "public"."registroscontrolador";
CREATE TABLE "public"."registroscontrolador" (
  "id" int4 NOT NULL DEFAULT nextval('registroscontrolador_id_seq1'::regclass),
  "tarjeta" text COLLATE "pg_catalog"."default" NOT NULL,
  "codigo" text COLLATE "pg_catalog"."default" NOT NULL,
  "verificado" int4 NOT NULL,
  "puerta" int4 NOT NULL,
  "evento" int4 NOT NULL,
  "estado" int4 NOT NULL,
  "time" timestamp(6),
  "fkdispositivo" int4,
  "sincronizado" bool,
  "alertado" bool
)
;

-- ----------------------------
-- Records of registroscontrolador
-- ----------------------------

-- ----------------------------
-- Table structure for residente
-- ----------------------------
DROP TABLE IF EXISTS "public"."residente";
CREATE TABLE "public"."residente" (
  "id" int4 NOT NULL DEFAULT nextval('residente_id_seq1'::regclass),
  "codigo" int4,
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "apellidop" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "apellidom" varchar(100) COLLATE "pg_catalog"."default",
  "sexo" varchar(10) COLLATE "pg_catalog"."default",
  "ci" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "expendido" varchar(20) COLLATE "pg_catalog"."default",
  "fechanacimiento" date,
  "telefono" varchar(100) COLLATE "pg_catalog"."default",
  "foto" text COLLATE "pg_catalog"."default",
  "codigoqr" text COLLATE "pg_catalog"."default",
  "tipo" varchar(20) COLLATE "pg_catalog"."default",
  "correo" varchar(255) COLLATE "pg_catalog"."default",
  "fknropase" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of residente
-- ----------------------------

-- ----------------------------
-- Table structure for residenteacceso
-- ----------------------------
DROP TABLE IF EXISTS "public"."residenteacceso";
CREATE TABLE "public"."residenteacceso" (
  "id" int4 NOT NULL DEFAULT nextval('residenteacceso_id_seq1'::regclass),
  "fkresidente" int4,
  "fechai" date,
  "fechaf" date,
  "estado" bool
)
;

-- ----------------------------
-- Records of residenteacceso
-- ----------------------------

-- ----------------------------
-- Table structure for residentedomicilio
-- ----------------------------
DROP TABLE IF EXISTS "public"."residentedomicilio";
CREATE TABLE "public"."residentedomicilio" (
  "id" int4 NOT NULL DEFAULT nextval('residentedomicilio_id_seq1'::regclass),
  "fkresidente" int4,
  "fkdomicilio" int4,
  "vivienda" bool,
  "estado" bool
)
;

-- ----------------------------
-- Records of residentedomicilio
-- ----------------------------

-- ----------------------------
-- Table structure for rol
-- ----------------------------
DROP TABLE IF EXISTS "public"."rol";
CREATE TABLE "public"."rol" (
  "id" int4 NOT NULL DEFAULT nextval('rol_id_seq1'::regclass),
  "nombre" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "descripcion" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "enabled" bool
)
;

-- ----------------------------
-- Records of rol
-- ----------------------------
INSERT INTO "public"."rol" VALUES (1, 'SUPER ADMINISTRADOR', 'Todos los permisos', 't');
INSERT INTO "public"."rol" VALUES (2, 'ADMINISTRADOR', 'Permisos de Administrador', 't');
INSERT INTO "public"."rol" VALUES (3, 'SUPERVISOR', '', 't');
INSERT INTO "public"."rol" VALUES (4, 'REGISTRADOR', '', 't');
INSERT INTO "public"."rol" VALUES (5, 'OPERADOR', '', 't');
INSERT INTO "public"."rol" VALUES (6, 'GUARDIA', '', 't');
INSERT INTO "public"."rol" VALUES (7, 'RESIDENTE', '', 't');

-- ----------------------------
-- Table structure for servidorCorreo
-- ----------------------------
DROP TABLE IF EXISTS "public"."servidorCorreo";
CREATE TABLE "public"."servidorCorreo" (
  "id" int4 NOT NULL DEFAULT nextval('"servidorCorreo_id_seq1"'::regclass),
  "servidor" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "puerto" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "correo" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "password" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "estado" bool
)
;

-- ----------------------------
-- Records of servidorCorreo
-- ----------------------------
INSERT INTO "public"."servidorCorreo" VALUES (1, 'smtp.gmail.com', '587', 'NotificacionSigas@gmail.com', 'Sigas2020', 't');

-- ----------------------------
-- Table structure for tipo_documento
-- ----------------------------
DROP TABLE IF EXISTS "public"."tipo_documento";
CREATE TABLE "public"."tipo_documento" (
  "id" int4 NOT NULL DEFAULT nextval('tipo_documento_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "estado" bool
)
;

-- ----------------------------
-- Records of tipo_documento
-- ----------------------------
INSERT INTO "public"."tipo_documento" VALUES (1, 'Carnet de Identidad', 't');
INSERT INTO "public"."tipo_documento" VALUES (2, 'licencia Conducir', 't');
INSERT INTO "public"."tipo_documento" VALUES (3, 'Pasaporte', 't');
INSERT INTO "public"."tipo_documento" VALUES (4, 'Codigo QR', 't');
INSERT INTO "public"."tipo_documento" VALUES (5, 'Otros', 't');

-- ----------------------------
-- Table structure for tipo_evento
-- ----------------------------
DROP TABLE IF EXISTS "public"."tipo_evento";
CREATE TABLE "public"."tipo_evento" (
  "id" int4 NOT NULL DEFAULT nextval('tipo_evento_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "estado" bool
)
;

-- ----------------------------
-- Records of tipo_evento
-- ----------------------------
INSERT INTO "public"."tipo_evento" VALUES (1, 'Visita', 't');
INSERT INTO "public"."tipo_evento" VALUES (2, 'Reunion', 't');
INSERT INTO "public"."tipo_evento" VALUES (3, 'Matrimonio', 't');
INSERT INTO "public"."tipo_evento" VALUES (4, 'Fiesta', 't');
INSERT INTO "public"."tipo_evento" VALUES (5, 'Actividad Deportiva', 't');
INSERT INTO "public"."tipo_evento" VALUES (6, 'Invitacion Rapida', 't');

-- ----------------------------
-- Table structure for tipo_pase
-- ----------------------------
DROP TABLE IF EXISTS "public"."tipo_pase";
CREATE TABLE "public"."tipo_pase" (
  "id" int4 NOT NULL DEFAULT nextval('tipo_pase_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "estado" bool
)
;

-- ----------------------------
-- Records of tipo_pase
-- ----------------------------

-- ----------------------------
-- Table structure for tipo_vehiculo
-- ----------------------------
DROP TABLE IF EXISTS "public"."tipo_vehiculo";
CREATE TABLE "public"."tipo_vehiculo" (
  "id" int4 NOT NULL DEFAULT nextval('tipo_vehiculo_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "estado" bool
)
;

-- ----------------------------
-- Records of tipo_vehiculo
-- ----------------------------
INSERT INTO "public"."tipo_vehiculo" VALUES (1, 'AUTO', 't');
INSERT INTO "public"."tipo_vehiculo" VALUES (2, 'CAMIONETA', 't');
INSERT INTO "public"."tipo_vehiculo" VALUES (3, 'VAGONETA', 't');
INSERT INTO "public"."tipo_vehiculo" VALUES (4, 'JEEP', 't');
INSERT INTO "public"."tipo_vehiculo" VALUES (5, 'CAMION', 't');
INSERT INTO "public"."tipo_vehiculo" VALUES (6, 'MOTOCICLETA', 't');
INSERT INTO "public"."tipo_vehiculo" VALUES (7, 'MOTO', 't');
INSERT INTO "public"."tipo_vehiculo" VALUES (8, 'MICRO', 't');
INSERT INTO "public"."tipo_vehiculo" VALUES (9, 'BICICLETA', 't');

-- ----------------------------
-- Table structure for tipodispositivo
-- ----------------------------
DROP TABLE IF EXISTS "public"."tipodispositivo";
CREATE TABLE "public"."tipodispositivo" (
  "id" int4 NOT NULL DEFAULT nextval('tipodispositivo_id_seq1'::regclass),
  "nombre" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "estado" bool
)
;

-- ----------------------------
-- Records of tipodispositivo
-- ----------------------------
INSERT INTO "public"."tipodispositivo" VALUES (1, 'Controlador de 1 Cerradura', 't');
INSERT INTO "public"."tipodispositivo" VALUES (2, 'Controlador de 2 Cerraduras', 't');
INSERT INTO "public"."tipodispositivo" VALUES (3, 'Controlador de 4 Cerraduras', 't');
INSERT INTO "public"."tipodispositivo" VALUES (4, 'Terminal Biometrico', 't');

-- ----------------------------
-- Table structure for usuario
-- ----------------------------
DROP TABLE IF EXISTS "public"."usuario";
CREATE TABLE "public"."usuario" (
  "id" int4 NOT NULL DEFAULT nextval('usuario_id_seq1'::regclass),
  "codigo" int4,
  "nombre" varchar(100) COLLATE "pg_catalog"."default",
  "apellidop" varchar(100) COLLATE "pg_catalog"."default",
  "apellidom" varchar(100) COLLATE "pg_catalog"."default",
  "telefono" varchar(100) COLLATE "pg_catalog"."default",
  "correo" varchar(255) COLLATE "pg_catalog"."default",
  "ci" varchar(50) COLLATE "pg_catalog"."default",
  "expendido" varchar(20) COLLATE "pg_catalog"."default",
  "username" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "password" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "token" varchar(2000) COLLATE "pg_catalog"."default",
  "fkrol" int4 NOT NULL,
  "fkcondominio" int4,
  "fkresidente" int4,
  "sigas" bool,
  "estado" bool,
  "enabled" bool,
  "login" bool
)
;

-- ----------------------------
-- Records of usuario
-- ----------------------------
INSERT INTO "public"."usuario" VALUES (1, NULL, '', '', '', '', NULL, NULL, NULL, 'admin', '6b5ca57ddd0d069ff19d117dba24ecc4d12be3d4f361e61167a11f54ee09f91d153bc7900d4f27c8e921f601c7c1ac0acd2fa3b45b7879b9c785b03fcf0313c2', 'Sin Token', 1, NULL, NULL, 't', 't', 't', 'f');

-- ----------------------------
-- Table structure for vehiculo
-- ----------------------------
DROP TABLE IF EXISTS "public"."vehiculo";
CREATE TABLE "public"."vehiculo" (
  "id" int4 NOT NULL DEFAULT nextval('vehiculo_id_seq1'::regclass),
  "codigo" int4,
  "placa" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "fktipo" int4,
  "fkcolor" int4,
  "fkmarca" int4,
  "fkmodelo" int4,
  "fkresidente" int4,
  "fkinvitado" int4,
  "fknropase" int4,
  "estado" bool
)
;

-- ----------------------------
-- Records of vehiculo
-- ----------------------------

-- ----------------------------
-- Table structure for versionmovil
-- ----------------------------
DROP TABLE IF EXISTS "public"."versionmovil";
CREATE TABLE "public"."versionmovil" (
  "id" int4 NOT NULL DEFAULT nextval('versionmovil_id_seq'::regclass),
  "version" varchar(50) COLLATE "pg_catalog"."default",
  "estado" bool
)
;

-- ----------------------------
-- Records of versionmovil
-- ----------------------------
INSERT INTO "public"."versionmovil" VALUES (1, '1.0.0', 't');

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."acceso_id_seq"', 568, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."acceso_id_seq1"
OWNED BY "public"."acceso"."id";
SELECT setval('"public"."acceso_id_seq1"', 580, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."accesocerraduras_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."accesocerraduras_id_seq1"
OWNED BY "public"."accesocerraduras"."id";
SELECT setval('"public"."accesocerraduras_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."accesotarjetas_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."accesotarjetas_id_seq1"
OWNED BY "public"."accesotarjetas"."id";
SELECT setval('"public"."accesotarjetas_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."ajuste_id_seq"
OWNED BY "public"."ajuste"."id";
SELECT setval('"public"."ajuste_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."amistad_id_seq"', 26, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."amistad_id_seq1"
OWNED BY "public"."amistad"."id";
SELECT setval('"public"."amistad_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."areasocial_id_seq"', 3, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."areasocial_id_seq1"
OWNED BY "public"."areasocial"."id";
SELECT setval('"public"."areasocial_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."autorizacion_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."autorizacion_id_seq1"
OWNED BY "public"."autorizacion"."id";
SELECT setval('"public"."autorizacion_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."bitacora_id_seq"', 631, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."bitacora_id_seq1"
OWNED BY "public"."bitacora"."id";
SELECT setval('"public"."bitacora_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."cerraduras_id_seq"', 10, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."cerraduras_id_seq1"
OWNED BY "public"."cerraduras"."id";
SELECT setval('"public"."cerraduras_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."codigoqr_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."codigoqr_id_seq1"
OWNED BY "public"."codigoqr"."id";
SELECT setval('"public"."codigoqr_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."color_id_seq"', 17, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."color_id_seq1"
OWNED BY "public"."color"."id";
SELECT setval('"public"."color_id_seq1"', 16, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."condominio_id_seq"', 4, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."condominio_id_seq1"
OWNED BY "public"."condominio"."id";
SELECT setval('"public"."condominio_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."condominioentrada_id_seq"', 20, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."condominioentrada_id_seq1"
OWNED BY "public"."condominioentrada"."id";
SELECT setval('"public"."condominioentrada_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."condominiopases_id_seq"', 20, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."condominiopases_id_seq1"
OWNED BY "public"."condominiopases"."id";
SELECT setval('"public"."condominiopases_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."configuracionacceso_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."configuracionacceso_id_seq1"
OWNED BY "public"."configuracionacceso"."id";
SELECT setval('"public"."configuracionacceso_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."configuraciondispositivo_id_seq"', 225, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."configuraciondispositivo_id_seq1"
OWNED BY "public"."configuraciondispositivo"."id";
SELECT setval('"public"."configuraciondispositivo_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."dispositivo_id_seq"', 4, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."dispositivo_id_seq1"
OWNED BY "public"."dispositivo"."id";
SELECT setval('"public"."dispositivo_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."dispositivoeventos_id_seq"', 4, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."dispositivoeventos_id_seq1"
OWNED BY "public"."dispositivoeventos"."id";
SELECT setval('"public"."dispositivoeventos_id_seq1"', 52, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."dispositivointerprete_id_seq"', 6, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."dispositivointerprete_id_seq1"
OWNED BY "public"."dispositivointerprete"."id";
SELECT setval('"public"."dispositivointerprete_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."domicilio_id_seq"', 281, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."domicilio_id_seq1"
OWNED BY "public"."domicilio"."id";
SELECT setval('"public"."domicilio_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."entrada_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."entrada_id_seq1"
OWNED BY "public"."entrada"."id";
SELECT setval('"public"."entrada_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."evento_id_seq"', 118, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."evento_id_seq1"
OWNED BY "public"."evento"."id";
SELECT setval('"public"."evento_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."id"', 541, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."interprete_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."interprete_id_seq1"
OWNED BY "public"."interprete"."id";
SELECT setval('"public"."interprete_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."invitacion_id_seq"', 137, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."invitacion_id_seq1"
OWNED BY "public"."invitacion"."id";
SELECT setval('"public"."invitacion_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."invitado_id_seq"', 26, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."invitado_id_seq1"
OWNED BY "public"."invitado"."id";
SELECT setval('"public"."invitado_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."marca_id_seq"', 10, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."marca_id_seq1"
OWNED BY "public"."marca"."id";
SELECT setval('"public"."marca_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."modelo_id_seq"', 6, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."modelo_id_seq1"
OWNED BY "public"."modelo"."id";
SELECT setval('"public"."modelo_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."modulo_id_seq"', 131, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."modulo_id_seq1"
OWNED BY "public"."modulo"."id";
SELECT setval('"public"."modulo_id_seq1"', 138, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."movimiento_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."movimiento_id_seq1"
OWNED BY "public"."movimiento"."id";
SELECT setval('"public"."movimiento_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."nropase_id_seq"', 20, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."nropase_id_seq1"
OWNED BY "public"."nropase"."id";
SELECT setval('"public"."nropase_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."portero_virtual_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."portero_virtual_id_seq1"
OWNED BY "public"."portero_virtual"."id";
SELECT setval('"public"."portero_virtual_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."principal_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."principal_id_seq1"
OWNED BY "public"."principal"."id";
SELECT setval('"public"."principal_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."registroscontrolador_id_seq"', 2696, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."registroscontrolador_id_seq1"
OWNED BY "public"."registroscontrolador"."id";
SELECT setval('"public"."registroscontrolador_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."residente_id_seq"', 19, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."residente_id_seq1"
OWNED BY "public"."residente"."id";
SELECT setval('"public"."residente_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."residenteacceso_id_seq"', 21, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."residenteacceso_id_seq1"
OWNED BY "public"."residenteacceso"."id";
SELECT setval('"public"."residenteacceso_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."residentedomicilio_id_seq"', 19, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."residentedomicilio_id_seq1"
OWNED BY "public"."residentedomicilio"."id";
SELECT setval('"public"."residentedomicilio_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."rol_id_seq"', 9, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."rol_id_seq1"
OWNED BY "public"."rol"."id";
SELECT setval('"public"."rol_id_seq1"', 8, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."servidorCorreo_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."servidorCorreo_id_seq1"
OWNED BY "public"."servidorCorreo"."id";
SELECT setval('"public"."servidorCorreo_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."tipo_documento_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tipo_documento_id_seq1"
OWNED BY "public"."tipo_documento"."id";
SELECT setval('"public"."tipo_documento_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."tipo_evento_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tipo_evento_id_seq1"
OWNED BY "public"."tipo_evento"."id";
SELECT setval('"public"."tipo_evento_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."tipo_pase_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tipo_pase_id_seq1"
OWNED BY "public"."tipo_pase"."id";
SELECT setval('"public"."tipo_pase_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."tipo_vehiculo_id_seq"', 11, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tipo_vehiculo_id_seq1"
OWNED BY "public"."tipo_vehiculo"."id";
SELECT setval('"public"."tipo_vehiculo_id_seq1"', 10, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."tipodispositivo_id_seq"', 3, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."tipodispositivo_id_seq1"
OWNED BY "public"."tipodispositivo"."id";
SELECT setval('"public"."tipodispositivo_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."usuario_id_seq"', 25, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."usuario_id_seq1"
OWNED BY "public"."usuario"."id";
SELECT setval('"public"."usuario_id_seq1"', 2, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."vehiculo_id_seq"', 14, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."vehiculo_id_seq1"
OWNED BY "public"."vehiculo"."id";
SELECT setval('"public"."vehiculo_id_seq1"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."versionmovil_id_seq"
OWNED BY "public"."versionmovil"."id";
SELECT setval('"public"."versionmovil_id_seq"', 2, false);

-- ----------------------------
-- Primary Key structure for table acceso
-- ----------------------------
ALTER TABLE "public"."acceso" ADD CONSTRAINT "acceso_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table accesocerraduras
-- ----------------------------
ALTER TABLE "public"."accesocerraduras" ADD CONSTRAINT "accesocerraduras_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table accesotarjetas
-- ----------------------------
ALTER TABLE "public"."accesotarjetas" ADD CONSTRAINT "accesotarjetas_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table ajuste
-- ----------------------------
ALTER TABLE "public"."ajuste" ADD CONSTRAINT "ajuste_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table amistad
-- ----------------------------
ALTER TABLE "public"."amistad" ADD CONSTRAINT "amistad_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table areasocial
-- ----------------------------
ALTER TABLE "public"."areasocial" ADD CONSTRAINT "areasocial_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table autorizacion
-- ----------------------------
ALTER TABLE "public"."autorizacion" ADD CONSTRAINT "autorizacion_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table bitacora
-- ----------------------------
ALTER TABLE "public"."bitacora" ADD CONSTRAINT "bitacora_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table cerraduras
-- ----------------------------
ALTER TABLE "public"."cerraduras" ADD CONSTRAINT "cerraduras_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table codigoqr
-- ----------------------------
ALTER TABLE "public"."codigoqr" ADD CONSTRAINT "codigoqr_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table color
-- ----------------------------
ALTER TABLE "public"."color" ADD CONSTRAINT "color_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table condominio
-- ----------------------------
ALTER TABLE "public"."condominio" ADD CONSTRAINT "condominio_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table condominioentrada
-- ----------------------------
ALTER TABLE "public"."condominioentrada" ADD CONSTRAINT "condominioentrada_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table condominiopases
-- ----------------------------
ALTER TABLE "public"."condominiopases" ADD CONSTRAINT "condominiopases_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table configuracionacceso
-- ----------------------------
ALTER TABLE "public"."configuracionacceso" ADD CONSTRAINT "configuracionacceso_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table configuraciondispositivo
-- ----------------------------
ALTER TABLE "public"."configuraciondispositivo" ADD CONSTRAINT "configuraciondispositivo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table dispositivo
-- ----------------------------
ALTER TABLE "public"."dispositivo" ADD CONSTRAINT "dispositivo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table dispositivoeventos
-- ----------------------------
ALTER TABLE "public"."dispositivoeventos" ADD CONSTRAINT "dispositivoeventos_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table dispositivointerprete
-- ----------------------------
ALTER TABLE "public"."dispositivointerprete" ADD CONSTRAINT "dispositivointerprete_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table domicilio
-- ----------------------------
ALTER TABLE "public"."domicilio" ADD CONSTRAINT "domicilio_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table entrada
-- ----------------------------
ALTER TABLE "public"."entrada" ADD CONSTRAINT "entrada_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table evento
-- ----------------------------
ALTER TABLE "public"."evento" ADD CONSTRAINT "evento_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table interprete
-- ----------------------------
ALTER TABLE "public"."interprete" ADD CONSTRAINT "interprete_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table invitacion
-- ----------------------------
ALTER TABLE "public"."invitacion" ADD CONSTRAINT "invitacion_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table invitado
-- ----------------------------
ALTER TABLE "public"."invitado" ADD CONSTRAINT "invitado_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table marca
-- ----------------------------
ALTER TABLE "public"."marca" ADD CONSTRAINT "marca_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table modelo
-- ----------------------------
ALTER TABLE "public"."modelo" ADD CONSTRAINT "modelo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table modulo
-- ----------------------------
ALTER TABLE "public"."modulo" ADD CONSTRAINT "modulo_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table modulo
-- ----------------------------
ALTER TABLE "public"."modulo" ADD CONSTRAINT "modulo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table movimiento
-- ----------------------------
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table nropase
-- ----------------------------
ALTER TABLE "public"."nropase" ADD CONSTRAINT "nropase_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table portero_virtual
-- ----------------------------
ALTER TABLE "public"."portero_virtual" ADD CONSTRAINT "portero_virtual_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table principal
-- ----------------------------
ALTER TABLE "public"."principal" ADD CONSTRAINT "principal_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table registroscontrolador
-- ----------------------------
ALTER TABLE "public"."registroscontrolador" ADD CONSTRAINT "registroscontrolador_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table residente
-- ----------------------------
ALTER TABLE "public"."residente" ADD CONSTRAINT "residente_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table residenteacceso
-- ----------------------------
ALTER TABLE "public"."residenteacceso" ADD CONSTRAINT "residenteacceso_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table residentedomicilio
-- ----------------------------
ALTER TABLE "public"."residentedomicilio" ADD CONSTRAINT "residentedomicilio_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table rol
-- ----------------------------
ALTER TABLE "public"."rol" ADD CONSTRAINT "rol_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table servidorCorreo
-- ----------------------------
ALTER TABLE "public"."servidorCorreo" ADD CONSTRAINT "servidorCorreo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tipo_documento
-- ----------------------------
ALTER TABLE "public"."tipo_documento" ADD CONSTRAINT "tipo_documento_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tipo_evento
-- ----------------------------
ALTER TABLE "public"."tipo_evento" ADD CONSTRAINT "tipo_evento_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tipo_pase
-- ----------------------------
ALTER TABLE "public"."tipo_pase" ADD CONSTRAINT "tipo_pase_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tipo_vehiculo
-- ----------------------------
ALTER TABLE "public"."tipo_vehiculo" ADD CONSTRAINT "tipo_vehiculo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tipodispositivo
-- ----------------------------
ALTER TABLE "public"."tipodispositivo" ADD CONSTRAINT "tipodispositivo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table usuario
-- ----------------------------
ALTER TABLE "public"."usuario" ADD CONSTRAINT "usuario_username_key" UNIQUE ("username");

-- ----------------------------
-- Primary Key structure for table usuario
-- ----------------------------
ALTER TABLE "public"."usuario" ADD CONSTRAINT "usuario_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table vehiculo
-- ----------------------------
ALTER TABLE "public"."vehiculo" ADD CONSTRAINT "vehiculo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table versionmovil
-- ----------------------------
ALTER TABLE "public"."versionmovil" ADD CONSTRAINT "versionmovil_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table acceso
-- ----------------------------
ALTER TABLE "public"."acceso" ADD CONSTRAINT "acceso_fkmodulo_fkey" FOREIGN KEY ("fkmodulo") REFERENCES "public"."modulo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."acceso" ADD CONSTRAINT "acceso_fkrol_fkey" FOREIGN KEY ("fkrol") REFERENCES "public"."rol" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table accesocerraduras
-- ----------------------------
ALTER TABLE "public"."accesocerraduras" ADD CONSTRAINT "accesocerraduras_fkcerraduras_fkey" FOREIGN KEY ("fkcerraduras") REFERENCES "public"."cerraduras" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."accesocerraduras" ADD CONSTRAINT "accesocerraduras_fkconfigacceso_fkey" FOREIGN KEY ("fkconfigacceso") REFERENCES "public"."configuracionacceso" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table accesotarjetas
-- ----------------------------
ALTER TABLE "public"."accesotarjetas" ADD CONSTRAINT "accesotarjetas_fkconfigacceso_fkey" FOREIGN KEY ("fkconfigacceso") REFERENCES "public"."configuracionacceso" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."accesotarjetas" ADD CONSTRAINT "accesotarjetas_fknropase_fkey" FOREIGN KEY ("fknropase") REFERENCES "public"."nropase" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table amistad
-- ----------------------------
ALTER TABLE "public"."amistad" ADD CONSTRAINT "amistad_fkinvitado_fkey" FOREIGN KEY ("fkinvitado") REFERENCES "public"."invitado" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."amistad" ADD CONSTRAINT "amistad_fkresidente_fkey" FOREIGN KEY ("fkresidente") REFERENCES "public"."residente" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table areasocial
-- ----------------------------
ALTER TABLE "public"."areasocial" ADD CONSTRAINT "areasocial_fkcondominio_fkey" FOREIGN KEY ("fkcondominio") REFERENCES "public"."condominio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table bitacora
-- ----------------------------
ALTER TABLE "public"."bitacora" ADD CONSTRAINT "bitacora_fkusuario_fkey" FOREIGN KEY ("fkusuario") REFERENCES "public"."usuario" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table cerraduras
-- ----------------------------
ALTER TABLE "public"."cerraduras" ADD CONSTRAINT "cerraduras_fkdispositivo_fkey" FOREIGN KEY ("fkdispositivo") REFERENCES "public"."dispositivo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."cerraduras" ADD CONSTRAINT "cerraduras_fkentrada_fkey" FOREIGN KEY ("fkentrada") REFERENCES "public"."entrada" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table condominioentrada
-- ----------------------------
ALTER TABLE "public"."condominioentrada" ADD CONSTRAINT "condominioentrada_fkcondominio_fkey" FOREIGN KEY ("fkcondominio") REFERENCES "public"."condominio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."condominioentrada" ADD CONSTRAINT "condominioentrada_fkentrada_fkey" FOREIGN KEY ("fkentrada") REFERENCES "public"."entrada" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table condominiopases
-- ----------------------------
ALTER TABLE "public"."condominiopases" ADD CONSTRAINT "condominiopases_fkcondominio_fkey" FOREIGN KEY ("fkcondominio") REFERENCES "public"."condominio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."condominiopases" ADD CONSTRAINT "condominiopases_fknropase_fkey" FOREIGN KEY ("fknropase") REFERENCES "public"."nropase" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table configuracionacceso
-- ----------------------------
ALTER TABLE "public"."configuracionacceso" ADD CONSTRAINT "configuracionacceso_fkcondominio_fkey" FOREIGN KEY ("fkcondominio") REFERENCES "public"."condominio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table configuraciondispositivo
-- ----------------------------
ALTER TABLE "public"."configuraciondispositivo" ADD CONSTRAINT "configuraciondispositivo_fkdispositivo_fkey" FOREIGN KEY ("fkdispositivo") REFERENCES "public"."dispositivo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table dispositivo
-- ----------------------------
ALTER TABLE "public"."dispositivo" ADD CONSTRAINT "dispositivo_fkcondominio_fkey" FOREIGN KEY ("fkcondominio") REFERENCES "public"."condominio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."dispositivo" ADD CONSTRAINT "dispositivo_fktipodispositivo_fkey" FOREIGN KEY ("fktipodispositivo") REFERENCES "public"."tipodispositivo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table dispositivointerprete
-- ----------------------------
ALTER TABLE "public"."dispositivointerprete" ADD CONSTRAINT "dispositivointerprete_fkdispositivo_fkey" FOREIGN KEY ("fkdispositivo") REFERENCES "public"."dispositivo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."dispositivointerprete" ADD CONSTRAINT "dispositivointerprete_fkinterprete_fkey" FOREIGN KEY ("fkinterprete") REFERENCES "public"."interprete" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table domicilio
-- ----------------------------
ALTER TABLE "public"."domicilio" ADD CONSTRAINT "domicilio_fkcondominio_fkey" FOREIGN KEY ("fkcondominio") REFERENCES "public"."condominio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table evento
-- ----------------------------
ALTER TABLE "public"."evento" ADD CONSTRAINT "evento_fkareasocial_fkey" FOREIGN KEY ("fkareasocial") REFERENCES "public"."areasocial" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."evento" ADD CONSTRAINT "evento_fkdomicilio_fkey" FOREIGN KEY ("fkdomicilio") REFERENCES "public"."domicilio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."evento" ADD CONSTRAINT "evento_fkresidente_fkey" FOREIGN KEY ("fkresidente") REFERENCES "public"."residente" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."evento" ADD CONSTRAINT "evento_fktipoevento_fkey" FOREIGN KEY ("fktipoevento") REFERENCES "public"."tipo_evento" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table invitacion
-- ----------------------------
ALTER TABLE "public"."invitacion" ADD CONSTRAINT "invitacion_fkevento_fkey" FOREIGN KEY ("fkevento") REFERENCES "public"."evento" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."invitacion" ADD CONSTRAINT "invitacion_fkinvitado_fkey" FOREIGN KEY ("fkinvitado") REFERENCES "public"."invitado" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."invitacion" ADD CONSTRAINT "invitacion_fktipopase_fkey" FOREIGN KEY ("fktipopase") REFERENCES "public"."tipo_pase" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table invitado
-- ----------------------------
ALTER TABLE "public"."invitado" ADD CONSTRAINT "invitado_fknropase_fkey" FOREIGN KEY ("fknropase") REFERENCES "public"."nropase" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table modelo
-- ----------------------------
ALTER TABLE "public"."modelo" ADD CONSTRAINT "modelo_fkmarca_fkey" FOREIGN KEY ("fkmarca") REFERENCES "public"."marca" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table modulo
-- ----------------------------
ALTER TABLE "public"."modulo" ADD CONSTRAINT "modulo_fkmodulo_fkey" FOREIGN KEY ("fkmodulo") REFERENCES "public"."modulo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table movimiento
-- ----------------------------
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fkareasocial_fkey" FOREIGN KEY ("fkareasocial") REFERENCES "public"."areasocial" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fkautorizacion_fkey" FOREIGN KEY ("fkautorizacion") REFERENCES "public"."autorizacion" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fkconductor_fkey" FOREIGN KEY ("fkconductor") REFERENCES "public"."invitado" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fkdomicilio_fkey" FOREIGN KEY ("fkdomicilio") REFERENCES "public"."domicilio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fkinvitacion_fkey" FOREIGN KEY ("fkinvitacion") REFERENCES "public"."invitacion" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fkinvitado_fkey" FOREIGN KEY ("fkinvitado") REFERENCES "public"."invitado" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fknropase_fkey" FOREIGN KEY ("fknropase") REFERENCES "public"."nropase" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fkresidente_fkey" FOREIGN KEY ("fkresidente") REFERENCES "public"."residente" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fktipodocumento_conductor_fkey" FOREIGN KEY ("fktipodocumento_conductor") REFERENCES "public"."tipo_documento" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fktipodocumento_fkey" FOREIGN KEY ("fktipodocumento") REFERENCES "public"."tipo_documento" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fktipopase_fkey" FOREIGN KEY ("fktipopase") REFERENCES "public"."tipo_pase" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."movimiento" ADD CONSTRAINT "movimiento_fkvehiculo_fkey" FOREIGN KEY ("fkvehiculo") REFERENCES "public"."vehiculo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table portero_virtual
-- ----------------------------
ALTER TABLE "public"."portero_virtual" ADD CONSTRAINT "portero_virtual_fkautorizacion_fkey" FOREIGN KEY ("fkautorizacion") REFERENCES "public"."autorizacion" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."portero_virtual" ADD CONSTRAINT "portero_virtual_fkcerradura_fkey" FOREIGN KEY ("fkcerradura") REFERENCES "public"."cerraduras" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."portero_virtual" ADD CONSTRAINT "portero_virtual_fkinvitacion_fkey" FOREIGN KEY ("fkinvitacion") REFERENCES "public"."invitacion" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."portero_virtual" ADD CONSTRAINT "portero_virtual_fkinvitado_fkey" FOREIGN KEY ("fkinvitado") REFERENCES "public"."invitado" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."portero_virtual" ADD CONSTRAINT "portero_virtual_fkresidente_fkey" FOREIGN KEY ("fkresidente") REFERENCES "public"."residente" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."portero_virtual" ADD CONSTRAINT "portero_virtual_fktipodocumento_fkey" FOREIGN KEY ("fktipodocumento") REFERENCES "public"."tipo_documento" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."portero_virtual" ADD CONSTRAINT "portero_virtual_fktipopase_fkey" FOREIGN KEY ("fktipopase") REFERENCES "public"."tipo_pase" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table registroscontrolador
-- ----------------------------
ALTER TABLE "public"."registroscontrolador" ADD CONSTRAINT "registroscontrolador_fkdispositivo_fkey" FOREIGN KEY ("fkdispositivo") REFERENCES "public"."dispositivo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table residente
-- ----------------------------
ALTER TABLE "public"."residente" ADD CONSTRAINT "residente_fknropase_fkey" FOREIGN KEY ("fknropase") REFERENCES "public"."nropase" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table residenteacceso
-- ----------------------------
ALTER TABLE "public"."residenteacceso" ADD CONSTRAINT "residenteacceso_fkresidente_fkey" FOREIGN KEY ("fkresidente") REFERENCES "public"."residente" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table residentedomicilio
-- ----------------------------
ALTER TABLE "public"."residentedomicilio" ADD CONSTRAINT "residentedomicilio_fkdomicilio_fkey" FOREIGN KEY ("fkdomicilio") REFERENCES "public"."domicilio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."residentedomicilio" ADD CONSTRAINT "residentedomicilio_fkresidente_fkey" FOREIGN KEY ("fkresidente") REFERENCES "public"."residente" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table usuario
-- ----------------------------
ALTER TABLE "public"."usuario" ADD CONSTRAINT "usuario_fkcondominio_fkey" FOREIGN KEY ("fkcondominio") REFERENCES "public"."condominio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."usuario" ADD CONSTRAINT "usuario_fkresidente_fkey" FOREIGN KEY ("fkresidente") REFERENCES "public"."residente" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."usuario" ADD CONSTRAINT "usuario_fkrol_fkey" FOREIGN KEY ("fkrol") REFERENCES "public"."rol" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table vehiculo
-- ----------------------------
ALTER TABLE "public"."vehiculo" ADD CONSTRAINT "vehiculo_fkcolor_fkey" FOREIGN KEY ("fkcolor") REFERENCES "public"."color" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."vehiculo" ADD CONSTRAINT "vehiculo_fkinvitado_fkey" FOREIGN KEY ("fkinvitado") REFERENCES "public"."invitado" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."vehiculo" ADD CONSTRAINT "vehiculo_fkmarca_fkey" FOREIGN KEY ("fkmarca") REFERENCES "public"."marca" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."vehiculo" ADD CONSTRAINT "vehiculo_fkmodelo_fkey" FOREIGN KEY ("fkmodelo") REFERENCES "public"."modelo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."vehiculo" ADD CONSTRAINT "vehiculo_fknropase_fkey" FOREIGN KEY ("fknropase") REFERENCES "public"."nropase" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."vehiculo" ADD CONSTRAINT "vehiculo_fkresidente_fkey" FOREIGN KEY ("fkresidente") REFERENCES "public"."residente" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."vehiculo" ADD CONSTRAINT "vehiculo_fktipo_fkey" FOREIGN KEY ("fktipo") REFERENCES "public"."tipo_vehiculo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
