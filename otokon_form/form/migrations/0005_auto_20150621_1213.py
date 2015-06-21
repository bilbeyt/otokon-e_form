# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20150621_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='birthday',
            field=models.DateField(help_text='Please enter birthday as YYYY-MM-DD', verbose_name='Birthday'),
        ),
    ]
