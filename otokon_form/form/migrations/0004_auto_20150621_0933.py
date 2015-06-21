# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20150620_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='slug',
        ),
        migrations.AlterField(
            model_name='form',
            name='birthday',
            field=models.DateField(help_text='Please enter your country code too.For Turkey starts with +90', verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='form',
            name='department',
            field=models.CharField(max_length=100, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='form',
            name='dorm_adress',
            field=models.TextField(null=True, verbose_name='Dorm Adress', blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='home_adress',
            field=models.TextField(null=True, verbose_name='Home Adress', blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='interests',
            field=models.TextField(verbose_name='Interests'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_education',
            field=models.BooleanField(default=False, help_text="This team organizes seminars and educations to sharing information. Also, this team provides a basis of knowledge for OTOKON's technical projects.", verbose_name='Education Team'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_evaluated',
            field=models.BooleanField(default=False, help_text=b'_(Is form evaluated?', verbose_name='Evaluated ?'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_informatics',
            field=models.BooleanField(default=False, help_text="This team is responsible for club's computer andforum. Also, this team works on online registry, database, kiosk and RFID technologies.", verbose_name='Informatics Team'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_organization',
            field=models.BooleanField(default=False, help_text="Organization team works actively in OTOKON's related organizations such as ITURO and TOK. Advertising, organization planning ,and communicating with sponsors are the works for this team.", verbose_name='Organization Team'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_publish',
            field=models.BooleanField(default=False, help_text='This team works on archiving and sharing informationwhich are provided from technical works and researches quickly. Also, this team publishes KONTROL magazine.', verbose_name='Press and Publishment Team'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_social',
            field=models.BooleanField(default=False, help_text='This team organize technical trip to give new points of view to members of club, also social activities are organized to motivate members', verbose_name='Technical Trip and Social Activity Team'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_technical',
            field=models.BooleanField(default=False, help_text='This team works on the technical projects which are suggested or already exist. Also, this team attendslocal or international projects. Project managers and the Education Team give necessary technical information.', verbose_name='Technical Team'),
        ),
        migrations.AlterField(
            model_name='form',
            name='mail',
            field=models.EmailField(unique=True, max_length=254, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='form',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='form',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Please enter your country code too. For Turkey starts with +90', max_length=128, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='form',
            name='reg_date',
            field=models.DateField(auto_now_add=True, verbose_name='Registry Date'),
        ),
        migrations.AlterField(
            model_name='form',
            name='school_number',
            field=models.PositiveIntegerField(verbose_name='School Number'),
        ),
        migrations.AlterField(
            model_name='form',
            name='tech_info',
            field=models.TextField(help_text='Your works about hardware or software', verbose_name='Technical Information'),
        ),
        migrations.AlterField(
            model_name='form',
            name='term',
            field=models.PositiveSmallIntegerField(verbose_name='Term'),
        ),
    ]
