# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20150727_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='is_education',
            field=models.BooleanField(default=False, verbose_name='Join educations'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_informatics',
            field=models.BooleanField(default=False, verbose_name='Join Informatics Team'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_magazine',
            field=models.BooleanField(default=False, verbose_name='Join KONTROL Magazine'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_projects',
            field=models.BooleanField(default=False, verbose_name='Join technical projects'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_robot',
            field=models.BooleanField(default=False, verbose_name='Join ITURO Team'),
        ),
    ]
