from django.db import models

class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=30, primary_key=True)
    pais = models.CharField(max_length=20)

class Cliente(models.Model):
    run_cliente = models.CharField(max_length=9, primary_key=True)
    nacionalidad_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    primer_nombre = models.CharField(max_length=40)
    segundo_nombre = models.CharField(max_length=40, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    idioma = models.CharField(max_length=20)
    telefono = models.IntegerField()
    correo_electronico = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField()

class Sucursal(models.Model):
    num_sucursal = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=50)

class Habitacion(models.Model):
    num_habitacion = models.AutoField(primary_key=True)
    sucursal_num_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    capacidad = models.IntegerField()
    categoria_habitacion = models.IntegerField()
    descripcion = models.CharField(max_length=2000)
    piso = models.IntegerField()
    precio_dia = models.DecimalField(max_digits=6, decimal_places=0)

class Reserva(models.Model):
    habitacion_num_habitacion = models.IntegerField()
    habitacion_sucursal_num_sucursal = models.IntegerField()
    cliente_run_cliente = models.CharField(max_length=9)
    fecha_inicio_reserva = models.DateTimeField()
    fecha_termino_reserva = models.DateTimeField()
    costo_total = models.DecimalField(max_digits=7, decimal_places=0)

class Rol(models.Model):
    cod_rol = models.CharField(max_length=10, primary_key=True)
    cargo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=1000)

class Trabajador(models.Model):
    run_trabajador = models.CharField(max_length=9, primary_key=True)
    rol_cod_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    sucursal_num_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    primer_nombre = models.CharField(max_length=40)
    segundo_nombre = models.CharField(max_length=40, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    correo_electronico = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=7, decimal_places=0)
    telefono = models.IntegerField()

    class Meta:
        unique_together = [('rol_cod_rol', 'sucursal_num_sucursal')]

