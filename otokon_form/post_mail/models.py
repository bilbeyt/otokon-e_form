from django.db import models
from form.models import Form
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class EmailMessage(models.Model):
    sender = models.ForeignKey(User, related_name="mail_sender")
    title = models.CharField(max_length=100)
    content = models.TextField()
    to = models.ManyToManyField(Form, related_name="mail_receiver")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MailGroup(models.Model):
    name = models.CharField(max_length=150, unique=True)
    contacts = models.ManyToManyField(Form)
    slug = models.SlugField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


@receiver(pre_save,sender=MailGroup)
def mail_group_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.name)
