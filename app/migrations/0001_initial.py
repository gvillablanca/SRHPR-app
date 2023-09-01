# Generated by Django 3.2 on 2023-09-01 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('num_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('sucursal_num_sucursal', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('categoria_habitacion', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('piso', models.IntegerField()),
                ('precio_dia', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('nacionalidad', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitacion_num_habitacion', models.IntegerField()),
                ('habitacion_sucursal_num_sucursal', models.IntegerField()),
                ('cliente_run_cliente', models.CharField(max_length=9)),
                ('fecha_inicio_reserva', models.DateTimeField()),
                ('fecha_termino_reserva', models.DateTimeField()),
                ('costo_total', models.DecimalField(decimal_places=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('cod_rol', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cargo', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('num_sucursal', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('run_trabajador', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('rol_cod_rol', models.CharField(max_length=10)),
                ('sucursal_num_sucursal', models.IntegerField()),
                ('primer_nombre', models.CharField(max_length=40)),
                ('segundo_nombre', models.CharField(blank=True, max_length=40, null=True)),
                ('apellido_paterno', models.CharField(max_length=40)),
                ('apellido_materno', models.CharField(max_length=40)),
                ('correo_electronico', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'unique_together': {('rol_cod_rol', 'sucursal_num_sucursal')},
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('run_cliente', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=40)),
                ('segundo_nombre', models.CharField(blank=True, max_length=40, null=True)),
                ('apellido_paterno', models.CharField(max_length=40)),
                ('apellido_materno', models.CharField(max_length=40)),
                ('idioma', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('correo_electronico', models.CharField(max_length=50)),
                ('fecha_registro', models.DateTimeField()),
                ('nacionalidad_nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nacionalidad')),
            ],
        ),
    ]