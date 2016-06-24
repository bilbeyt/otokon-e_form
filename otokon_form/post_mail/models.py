from django.db import models
from form.models import Form
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail


class EmailMessage(models.Model):
    sender = models.ForeignKey(Form, related_name="mail_sender")
    title = models.CharField(max_length=100)
    content = models.TextField()
    to = models.ManyToManyField(Form, related_name="mail_receiver")
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
	return self.title


@receiver(pre_save, sender=EmailMessage)
def EmailMessage_sender(sender, instance, *args, **kwargs):
    send_mail(
	instance.title,
	instance.content,
	instance.sender.mail,
        instance.to.all().values_list("mail", flat=True),
	fail_silently=False,
    ) 
