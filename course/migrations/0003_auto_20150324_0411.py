# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.core.management import call_command

import os

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'initial_data.json'
fixture_file = os.path.join(fixture_dir, fixture_filename)


def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture_file) 



class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20150324_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='availablenextsemester',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='fallsemester',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='springsemester',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='summersemester',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.RunPython(load_fixture),
    ]
