# Generated by Django 3.2 on 2023-09-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230901_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='salario',
            field=models.DecimalField(decimal_places=0, max_digits=7),
        ),
    ]
