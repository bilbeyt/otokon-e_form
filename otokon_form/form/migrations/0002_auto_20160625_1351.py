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
            name='experience',
            field=models.CharField(max_length=150, verbose_name='Experiences'),
        ),
        migrations.AlterField(
            model_name='form',
            name='interests',
            field=models.CharField(max_length=150, verbose_name='Interests'),
        ),
        migrations.AlterField(
            model_name='form',
            name='tech_info',
            field=models.CharField(max_length=150, verbose_name='Technical Information'),
        ),
    ]
