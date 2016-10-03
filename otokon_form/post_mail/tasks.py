from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send(title, content, sender, to):
    send_mail(title, content, sender, (to,), fail_silently=False)
