# Generated by Django 2.2.5 on 2019-12-19 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20191218_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='amenity',
            new_name='amenities',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='facility',
            new_name='facilities',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='house_rule',
            new_name='house_rules',
        ),
    ]
