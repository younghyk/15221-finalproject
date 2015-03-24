# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.core.management import call_command


fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'initial_data.json'
fixture_file = os.path.join(fixture_dir, fixture_filename)


def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture_file) 
    

class Migration(migrations.Migration):
    
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.SmallIntegerField(unique=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('units', models.SmallIntegerField()),
                ('corequirements', models.CharField(max_length=200)),
                ('prerequirements', models.CharField(max_length=200)),
                ('fallsemester', models.BooleanField()),
                ('springsemester', models.BooleanField()),
                ('summersemester', models.BooleanField()),
                ('availablenextsemester', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.SmallIntegerField(unique=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(to='course.Department'),
            preserve_default=True,
        ),
        migrations.RunPython(load_fixture),
    ]
