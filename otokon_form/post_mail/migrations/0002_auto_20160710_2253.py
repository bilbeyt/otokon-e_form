# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post_mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='sender',
            field=models.ForeignKey(related_name='mail_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
