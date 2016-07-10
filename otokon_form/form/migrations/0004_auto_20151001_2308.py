# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20150930_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='department',
            field=models.CharField(max_length=100, verbose_name='Department', choices=[('Control and Automation Engineering', b'Kontrol ve Otomasyon M\xc3\xbchendisli\xc4\x9fi'), ('Computer Engineering', b'Bilgisayar M\xc3\xbchendisli\xc4\x9fi'), ('Electronics and Communication Engineering', b'Elektronik ve Haberle\xc5\x9fme M\xc3\xbchendisli\xc4\x9fi'), ('Electrical Engineering', b'Elektrik M\xc3\xbchendisli\xc4\x9fi'), ('Mechanical Engineering', b'Makina M\xc3\xbchendisli\xc4\x9fi'), ('Others', b'Di\xc4\x9fer')]),
        ),
    ]
