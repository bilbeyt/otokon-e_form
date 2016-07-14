from django.db import models
from form.models import Form
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings


class EmailMessage(models.Model):
    sender = models.ForeignKey(User, related_name="mail_sender")
    title = models.CharField(max_length=100)
    content = models.TextField()
    to = models.ManyToManyField(Form, related_name="mail_receiver")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

