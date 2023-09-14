from django.db import models

class Nacionalidad(models.Model):
    idNacionalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=20)

class Sucursal(models.Model):
    num_sucursal = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)

class Habitacion(models.Model):
    num_habitacion = models.AutoField(primary_key=True)
    sucursal_num_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    capacidad = models.IntegerField()
    categoria_habitacion = models.IntegerField()
    descripcion = models.CharField(max_length=2000)
    piso = models.IntegerField()
    precio_dia = models.DecimalField(max_digits=6, decimal_places=0)

class Rol(models.Model):
    cod_rol = models.CharField(max_length=20, primary_key=True)
    titulo = models.CharField(max_length=80)
    cargoDetalle = models.CharField(max_length=2000)

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    run = models.CharField(max_length=8)
    cv = models.CharField(max_length=1)
    primer_nombre = models.CharField(max_length=40)
    segundo_nombre = models.CharField(max_length=40, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    correo_electronico = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_registro = models.DateTimeField()

    class Meta:
        abstract = True

class Trabajador(Persona):
    rol_cod_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    sucursal_num_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=7, decimal_places=0)
    clave = models.CharField(max_length=100)

    class Meta:
        unique_together = [('rol_cod_rol', 'sucursal_num_sucursal')]

class Cliente(Persona):
    nacionalidad_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    idioma = models.CharField(max_length=20)
    clave = models.CharField(max_length=100)

class Reserva(models.Model):
    habitacion_num_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    habitacion_sucursal_num_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio_reserva = models.DateTimeField()
    fecha_termino_reserva = models.DateTimeField()
    costo_total = models.DecimalField(max_digits=7, decimal_places=0)

