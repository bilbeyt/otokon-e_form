# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='is_education',
            field=models.BooleanField(default=False, help_text=b"This team organizes seminars and educations to sharing information. Also, this team provides a basis of knowledge for OTOKON's technical projects."),
        ),
        migrations.AlterField(
            model_name='form',
            name='dorm_adress',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='home_adress',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_evaluated',
            field=models.BooleanField(default=False, help_text=b'Is form evaluated?'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_informatics',
            field=models.BooleanField(default=False, help_text=b"This team is responsible for club's computer andforum. Also, this team works on online registry, database, kiosk and RFID technologies."),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_organization',
            field=models.BooleanField(default=False, help_text=b"Organization team works actively in OTOKON's related organizations such as ITURO and TOK. Advertising, organization planning ,and communicating with sponsors are the works for this team."),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_publish',
            field=models.BooleanField(default=False, help_text=b'This team works on archiving and sharing informationwhich are provided from technical works and researches quickly. Also, this team publishes OTOKON magazine.'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_social',
            field=models.BooleanField(default=False, help_text=b'This team organize technical trip to give new points of view to members of club, also social activities are organized to motivate members'),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_technical',
            field=models.BooleanField(default=False, help_text=b'This team works on the technical projects which are suggested or already exist. Also, this team attendslocal or international projects. Project managers and the Education Team give necessary technical information.'),
        ),
        migrations.AlterField(
            model_name='form',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text=b'Please enter your country code too. For Turkey starts with +90', max_length=128),
        ),
    ]
