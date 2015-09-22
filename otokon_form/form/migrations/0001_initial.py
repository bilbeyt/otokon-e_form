# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('department', models.CharField(max_length=100, verbose_name='Department', choices=[('Control and Automation Engineering', b'KON'), ('Computer Engineering', b'BLG'), ('Electronics and Communication Engineering', b'EHB'), ('Electrical Engineering', b'ELE'), ('Others', b'OTH')])),
                ('other_departments', models.CharField(max_length=100, null=True, verbose_name='Other Departments', blank=True)),
                ('school_number', models.PositiveIntegerField(verbose_name='School Number')),
                ('reg_date', models.DateField(auto_now_add=True, verbose_name='Registry Date')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('mail', models.EmailField(unique=True, max_length=254, verbose_name='E-Mail')),
                ('interests', models.CharField(max_length=150, verbose_name='Interests', blank=True)),
                ('tech_info', models.CharField(max_length=150, verbose_name='Technical Information', blank=True)),
                ('experience', models.CharField(max_length=150, verbose_name='Experiences', blank=True)),
                ('is_projects', models.BooleanField(default=False, verbose_name='Join technical projects')),
                ('is_education', models.BooleanField(default=False, verbose_name='Join educations')),
                ('is_informatics', models.BooleanField(default=False, verbose_name='Join Informatics Team')),
                ('is_magazine', models.BooleanField(default=False, verbose_name='Join KONTROL Magazine')),
                ('is_robot', models.BooleanField(default=False, verbose_name='Join ITURO Team')),
                ('is_evaluated', models.BooleanField(default=False, verbose_name='Evaluated ?')),
            ],
        ),
    ]
