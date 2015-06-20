# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('department', models.CharField(max_length=100)),
                ('school_number', models.PositiveIntegerField()),
                ('term', models.PositiveSmallIntegerField()),
                ('birthday', models.DateField()),
                ('interests', models.TextField()),
                ('tech_info', models.TextField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('mail', models.EmailField(unique=True, max_length=254)),
                ('dorm_adress', models.TextField()),
                ('home_adress', models.TextField()),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('is_organization', models.BooleanField(default=False)),
                ('is_technical', models.BooleanField(default=False)),
                ('is_informatics', models.BooleanField(default=False)),
                ('is_publish', models.BooleanField(default=False)),
                ('is_social', models.BooleanField(default=False)),
                ('is_evaluated', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]
