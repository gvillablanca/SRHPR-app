# Custom migration to insert data into tables

from django.db import migrations
from django.conf import settings
import os

inserta_tablas_path = os.path.join(
    settings.BASE_DIR, 'sql', 'insertaTablas.sql')

with open(inserta_tablas_path, 'r') as f:
    inserta_tablas = f.read()

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(inserta_tablas),
    ]

