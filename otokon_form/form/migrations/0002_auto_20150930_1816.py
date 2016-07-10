# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='department',
            field=models.CharField(max_length=100, verbose_name='Department', choices=[('Control and Automation Engineering', b'Control and Automation Engineering'), ('Computer Engineering', b'BLG'), ('Electronics and Communication Engineering', b'EHB'), ('Electrical Engineering', b'ELE'), ('Others', b'OTH')]),
        ),
    ]
