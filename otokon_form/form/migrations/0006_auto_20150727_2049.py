# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20150621_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='dorm_adress',
        ),
        migrations.RemoveField(
            model_name='form',
            name='home_adress',
        ),
        migrations.RemoveField(
            model_name='form',
            name='is_organization',
        ),
        migrations.RemoveField(
            model_name='form',
            name='is_publish',
        ),
        migrations.RemoveField(
            model_name='form',
            name='is_social',
        ),
        migrations.RemoveField(
            model_name='form',
            name='is_technical',
        ),
        migrations.RemoveField(
            model_name='form',
            name='term',
        ),
        migrations.AddField(
            model_name='form',
            name='experience',
            field=models.TextField(default=1, verbose_name='Experiences'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='is_magazine',
            field=models.BooleanField(default=False, verbose_name='Join KONTROL Magazine ?'),
        ),
        migrations.AddField(
            model_name='form',
            name='is_projects',
            field=models.BooleanField(default=False, verbose_name='Join texhnical projects ?'),
        ),
        migrations.AddField(
            model_name='form',
            name='is_robot',
            field=models.BooleanField(default=False, verbose_name='Join ITURO Team ?'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_education',
            field=models.BooleanField(default=False, verbose_name='Join educations ?'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_evaluated',
            field=models.BooleanField(default=False, verbose_name='Evaluated ?'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_informatics',
            field=models.BooleanField(default=False, verbose_name='Join Informatics Team ?'),
        ),
        migrations.AlterField(
            model_name='form',
            name='tech_info',
            field=models.TextField(verbose_name='Technical Information'),
        ),
    ]
