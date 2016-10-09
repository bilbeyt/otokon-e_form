# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='department',
            field=models.CharField(max_length=100, verbose_name='Department', choices=[('KON', 'Control and Automation Engineering'), ('BLG', 'Computer Engineering'), ('EHB', 'Electronics and Communication Engineering'), ('ELE', 'Electrical Engineering'), ('OTH', 'Others')]),
        ),
    ]
