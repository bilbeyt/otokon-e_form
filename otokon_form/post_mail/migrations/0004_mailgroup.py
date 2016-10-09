# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_auto_20161009_2036'),
        ('post_mail', '0003_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('contacts', models.ManyToManyField(to='form.Form')),
            ],
        ),
    ]
