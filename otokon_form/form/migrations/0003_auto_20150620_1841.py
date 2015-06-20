# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20150620_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='birthday',
            field=models.DateField(help_text=b'Please enter birthday format YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='form',
            name='dorm_adress',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='home_adress',
            field=models.TextField(null=True, blank=True),
        ),
    ]
