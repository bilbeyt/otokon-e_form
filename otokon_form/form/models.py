from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Form(models.Model):
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    school_number = models.PositiveIntegerField()
    term = models.PositiveSmallIntegerField()
    birthday = models.DateField(auto_now_add=False)
    interests = models.TextField()
    tech_info = models.TextField()
    phone_number = PhoneNumberField()
    mail = models.EmailField(unique=True)
    dorm_adress = models.TextField()
    home_adress = models.TextField()
    reg_date = models.DateField(auto_now_add=True)
    is_organization = models.BooleanField(default=False)
    is_technical = models.BooleanField(default=False)
    is_informatics = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    is_social = models.BooleanField(default=False)
    is_evaluated = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name


@receiver(pre_save, sender=Form)
def form_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
