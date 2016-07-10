from django.db import models
from form.models import Form
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User


class EmailMessage(models.Model):
    sender = models.ForeignKey(User, related_name="mail_sender")
    title = models.CharField(max_length=100)
    content = models.TextField()
    to = models.ManyToManyField(Form, related_name="mail_receiver")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=EmailMessage, dispatch_uid="emailmessage_identifier")
def EmailMessage_sender(sender, instance, *args, **kwargs):
    send_mail(
	    instance.title,
	    instance.content,
	    "otokon@itu.edu.tr",
        instance.to.all().values_list("mail", flat=True),
	    fail_silently=False,
    )
