import os
from django.db import migrations
from django.conf import settings


def create_initial_objects(apps, schema_editor):
    """Create initial database objects from settings"""
    print(os.getcwd())
    for obj in settings.INITIAL_OBJECTS:
        Model = apps.get_model(obj["app"], obj["model"])
        for kwargs in obj['kwargs']:
            o = Model(**kwargs)
            o.save()

        # obj_list = [Model(**kwargs) for kwargs in obj["kwargs"]]
        # Model.objects.bulk_create(obj_list)


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_objects)
    ]
