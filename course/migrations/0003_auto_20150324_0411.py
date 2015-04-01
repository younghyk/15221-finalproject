# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django.core.management import call_command

import os


''' This commented code allows for fixture loading
fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'initial_data.json'
fixture_file = os.path.join(fixture_dir, fixture_filename)

def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture_file) 
'''
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data2sql'))
dept_filename = 'departmentdata.json'
dept_file = os.path.join(data_dir, dept_filename)
cour_filename = 'outdesc.json'
cour_file = os.path.join(data_dir, cour_filename)


def load_departments(apps, schema_editor):
    Department = apps.get_model("course","Department")
    with open(dept_file) as data_fileD: 
        datad = json.load(data_fileD)
        for dd in datad:
            dept_temp = Department(id=dd["dept_id"], title=dd['dept_name'])
            dept_temp.save()
    
def load_courses(apps, schema_editor):
    Course = apps.get_model("course","Course")
    with open(filename) as data_file:
        data = json.load(data_file)
        for cd in data:
            cour_temp = Course(id=cd['num'], department=cd['num']/1000, 
                title=cd['name'], description=cd['desc'], units=cd['units'],
                corequirements=cd['coreqs'], prerequirements=cd['prereqs'],
                fallsemester='F' in coursedata['semester'], 
                springsemester='S' in coursedata['semester'], 
                summersemester='U' in coursedata['semester'])
            cour_temp.save()

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
        # migrations.RunPython(load_fixture),
        migrations.RunPython(load_departments),
        migrations.RunPython(load_courses),
    ]
