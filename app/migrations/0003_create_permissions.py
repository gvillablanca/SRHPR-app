from django.db import migrations
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


def create_permission(apps, schema_editor):
    # Get the content type for the user model
    content_type = ContentType.objects.get_for_model(User)
    # Create the permission
    permissionUser = Permission.objects.create(
        codename='rol_cliente',
        name='Tiene acceso a la vista de cliente',
        content_type=content_type,
    )

    permissionSupervisor = Permission.objects.create(
        codename='rol_admin',
        name='Tiene acceso a la pagina de administrador',
        content_type=content_type,
    )


    permissionSupervisor = Permission.objects.create(
        codename='rol_soporteti',
        name='Tiene acceso a la vista de soporte tecnico',
        content_type=content_type,
    )

    permissionSupervisor = Permission.objects.create(
        codename='rol_recepcion',
        name='Tiene acceso a la vista de recepcion',
        content_type=content_type,
    )

class Migration(migrations.Migration):

    dependencies = [('app', '0002_insert_data'),
                    ]

    operations = [
        migrations.RunPython(create_permission),
    ]
