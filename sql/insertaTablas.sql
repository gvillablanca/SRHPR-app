-- SUCURSALES(ACTUALMENTE SOLO TIENEN 1)
INSERT INTO app_sucursal (direccion, ciudad, pais) VALUES ('Cabo Arestey 2464', 'Santiago', 'Chile');

-- NACIONALIDADES
INSERT INTO app_nacionalidad (nombre, pais) VALUES ('Chilena', 'Chile');
INSERT INTO app_nacionalidad (nombre, pais) VALUES ('Argentina', 'Argentina');
INSERT INTO app_nacionalidad (nombre, pais) VALUES ('Peruana', 'Peru');
INSERT INTO app_nacionalidad (nombre, pais) VALUES ('Colombiana', 'Colombia');
INSERT INTO app_nacionalidad (nombre, pais) VALUES ('Venezolana', 'Venezuela');
INSERT INTO app_nacionalidad (nombre, pais) VALUES ('Boliviana', 'Bolivia');
INSERT INTO app_nacionalidad (nombre, pais) VALUES ('Ecuatoriana', 'Ecuador');
INSERT INTO app_nacionalidad (nombre, pais) VALUES ('Uruguaya', 'Uruguay');

-- ROLES
INSERT INTO app_rol (codRol, titulo, cargoDetalle) VALUES ('ADMINISTRADOR','Administrador', 'Se encarga de la tomada de decisiones y de la administracion general de la empresa.');
INSERT INTO app_rol (codRol, titulo, cargoDetalle) VALUES ('DUENO', 'Dueño', 'Se encarga de la toma de decisiones y de la administracion general de la empresa, tiene la ultima palabra en las decisiones.');
INSERT INTO app_rol (codRol, titulo, cargoDetalle) VALUES ('SOPORTETI', 'Soporte TI', 'Se encarga de la mantencion de los equipos, de la red y de la infraestructura del sistema informatico.');
INSERT INTO app_rol (codRol, titulo, cargoDetalle) VALUES ('RECEPCION', 'Recepcion', 'Se encarga de la recepcion de los clientes y de la atencion de estos.');

-- TRABAJADORES
INSERT INTO app_trabajador (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, rol_cod_rol_id, sucursal_num_sucursal_id, salario, clave)
VALUES ('45678905', '9', 'Juan', 'Carlos', 'Caro', 'Arriagada', 'juancaro@hotmail.com', 456815358, '2023-09-14 16:41:36', 1, 'SOPORTETI', 1, 1400000, 'noteurchoe45684oeunretoru');

INSERT INTO app_trabajador (run, cv, primer_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, rol_cod_rol_id, sucursal_num_sucursal_id, salario, clave)
VALUES ('11980532', '0', 'Martina', 'Blaster', 'Blaster', 'martina@empresa.com', 987654321, '2023-09-14 16:41:36', 1, 'DUENO', 1, 2500000, 'lorem58masss5854chcuroeturc');

INSERT INTO app_trabajador (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, rol_cod_rol_id, sucursal_num_sucursal_id, salario, clave)
VALUES ('11111111', '1', 'Ana', 'María', 'Gómez', 'López', 'ana.gomez@email.com', 987654322, '2023-09-14 17:00:00', 1, 'RECEPCION', 1, 1200000, 'contraseña1');

INSERT INTO app_trabajador (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, rol_cod_rol_id, sucursal_num_sucursal_id, salario, clave)
VALUES ('22222222', '2', 'Luis', 'Miguel', 'Rodríguez', 'Martínez', 'luis.rodriguez@email.com', 987654323, '2023-09-14 17:05:00', 2, 'RECEPCION', 1, 1100000, 'contraseña2');

INSERT INTO app_trabajador (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, rol_cod_rol_id, sucursal_num_sucursal_id, salario, clave)
VALUES ('33333333', '3', 'María', 'Isabel', 'Pérez', 'González', 'maria.perez@email.com', 987654324, '2023-09-14 17:10:00', 3, 'RECEPCION', 1, 1150000, 'contraseña3');

INSERT INTO app_trabajador (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, rol_cod_rol_id, sucursal_num_sucursal_id, salario, clave)
VALUES ('44444444', 'k', 'Juan', 'Pablo', 'López', 'Sánchez', 'juan.lopez@email.com', 987654325, '2023-09-14 17:15:00', 4, 'RECEPCION', 1, 1250000, 'contraseña4');

-- CLIENTES
INSERT INTO app_cliente (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, idioma, clave)
VALUES ('12111111', '1', 'Pedro', 'José', 'Gómez', 'López', 'pedro.gomez@email.com', 987654326, '2023-09-14 18:00:00', 1, 'español', 'contraseñaCliente1');

INSERT INTO app_cliente (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, idioma, clave)
VALUES ('23222222', '2', 'Luisa', 'María', 'Rodríguez', 'Martínez', 'luisa.rod@email.com', 987654327, '2023-09-14 18:05:00', 1, 'español', 'contraseñaCliente2');

INSERT INTO app_cliente (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, idioma, clave)
VALUES ('34333333', '3', 'Carlos', 'Andrés', 'Pérez', 'González', 'carlos.perez@email.com', 987654328, '2023-09-14 18:10:00', 1, 'español', 'contraseñaCliente3');

INSERT INTO app_cliente (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, idioma, clave)
VALUES ('45444444', '4', 'María', 'Isabel', 'López', 'Sánchez', 'maria.lopez@email.com', 987654329, '2023-09-14 18:15:00', 1, 'español', 'contraseñaCliente4');

INSERT INTO app_cliente (run, cv, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, correo_electronico, telefono, fecha_registro, nacionalidad_nacionalidad_id, idioma, clave)
VALUES ('56555555', '5', 'Javier', 'Miguel', 'Martínez', 'Rodríguez', 'javier.martinez@email.com', 987654330, '2023-09-14 18:20:00', 2, 'español', 'contraseñaCliente5');

-- HABITACIONES
-- Piso 1 (5 habitaciones estándar)
INSERT INTO app_habitacion (sucursal_num_sucursal_id, capacidad, categoria_habitacion, descripcion, piso, precio_dia)
VALUES (1, 2, 1, 'Habitación doble estándar con vista a la ciudad en el piso 1', 1, 80000),
       (1, 2, 1, 'Habitación doble estándar con balcón en el piso 1', 1, 80000),
       (1, 2, 1, 'Habitación doble estándar con desayuno incluido en el piso 1', 1, 80000),
       (1, 2, 1, 'Habitación doble estándar con acceso a la piscina en el piso 1', 1, 80000),
       (1, 2, 1, 'Habitación doble estándar estándar en el piso 1', 1, 80000);

-- Piso 2 (5 habitaciones estándar)
INSERT INTO app_habitacion (sucursal_num_sucursal_id, capacidad, categoria_habitacion, descripcion, piso, precio_dia)
VALUES (1, 2, 1, 'Habitación doble estándar con vista al jardín en el piso 2', 2, 80000),
       (1, 2, 1, 'Habitación doble estándar con terraza privada en el piso 2', 2, 80000),
       (1, 2, 1, 'Habitación doble estándar con jacuzzi en el piso 2', 2, 80000),
       (1, 2, 1, 'Habitación doble estándar con baño compartido en el piso 2', 2, 80000),
       (1, 2, 1, 'Habitación doble estándar estándar en el piso 2', 2, 80000);

-- Piso 3 (5 habitaciones estándar)
INSERT INTO app_habitacion (sucursal_num_sucursal_id, capacidad, categoria_habitacion, descripcion, piso, precio_dia)
VALUES (1, 2, 1, 'Habitación doble estándar con vista al mar en el piso 3', 3, 80000),
       (1, 2, 1, 'Habitación doble estándar con acceso directo a la playa en el piso 3', 3, 80000),
       (1, 2, 1, 'Habitación doble estándar con minibar en el piso 3', 3, 80000),
       (1, 2, 1, 'Habitación doble estándar con escritorio en el piso 3', 3, 80000),
       (1, 2, 1, 'Habitación doble estándar estándar en el piso 3', 3, 80000);

-- Piso 4 (5 habitaciones premium)
INSERT INTO app_habitacion (sucursal_num_sucursal_id, capacidad, categoria_habitacion, descripcion, piso, precio_dia)
VALUES (1, 2, 2, 'Suite premium con vista panorámica en el piso 4', 4, 120000),
       (1, 4, 2, 'Suite premium con cama king size en el piso 4', 4, 120000),
       (1, 3, 2, 'Suite premium con sala de estar en el piso 4', 4, 120000),
       (1, 3, 2, 'Suite premium con bañera de hidromasaje en el piso 4', 4, 120000),
       (1, 4, 2, 'Suite premium con servicio de habitaciones las 24 horas en el piso 4', 4, 120000);

-- RESERVAS
-- Reserva 1: Cliente Pedro Gómez (1 noche)
INSERT INTO app_reserva (habitacion_sucursal_num_sucursal_id, habitacion_num_habitacion_id, idCliente_id, fecha_inicio_reserva, fecha_termino_reserva, costo_total)
VALUES (1, 1, 1, '2023-09-14 18:30:00', '2023-09-15 18:30:00', 80000);

-- Reserva 2: Cliente Luisa Rodríguez (2 noches)
INSERT INTO app_reserva (habitacion_sucursal_num_sucursal_id, habitacion_num_habitacion_id, idCliente_id, fecha_inicio_reserva, fecha_termino_reserva, costo_total)
VALUES (1, 2, 2, '2023-09-14 18:35:00', '2023-09-16 18:35:00', 160000);

-- Reserva 3: Cliente Carlos Pérez (3 noches)
INSERT INTO app_reserva (habitacion_sucursal_num_sucursal_id, habitacion_num_habitacion_id, idCliente_id, fecha_inicio_reserva, fecha_termino_reserva, costo_total)
VALUES (1, 3, 3, '2023-09-14 18:40:00', '2023-09-17 18:40:00', 240000);

-- Reserva 4: Cliente María López (4 noches)
INSERT INTO app_reserva (habitacion_sucursal_num_sucursal_id, habitacion_num_habitacion_id, idCliente_id, fecha_inicio_reserva, fecha_termino_reserva, costo_total)
VALUES (1, 4, 4, '2023-09-14 18:45:00', '2023-09-18 18:45:00', 320000);

-- Reserva 5: Cliente Javier Martínez (5 noches)
INSERT INTO app_reserva (habitacion_sucursal_num_sucursal_id, habitacion_num_habitacion_id, idCliente_id, fecha_inicio_reserva, fecha_termino_reserva, costo_total)
VALUES (1, 5, 5, '2023-09-14 18:50:00', '2023-09-19 18:50:00', 400000);
