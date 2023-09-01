from django.contrib import admin
from .models import Nacionalidad, Cliente, Habitacion, Reserva, Rol, Sucursal, Trabajador

# Register your models here.

admin.site.register(Nacionalidad)
admin.site.register(Cliente)
admin.site.register(Habitacion)
admin.site.register(Reserva)
admin.site.register(Rol)
admin.site.register(Sucursal)
admin.site.register(Trabajador)
