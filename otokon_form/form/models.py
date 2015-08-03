from django.db import models
from django.utils.translation import ugettext_lazy as _
from django import forms


class Form(models.Model):
    name = models.CharField(_("Full Name"), max_length=150)
    department = models.CharField(_("Department"), max_length=100)
    school_number = models.PositiveIntegerField(_("School Number"))
    birthday = models.DateField(_("Birthday"), auto_now_add=False,)
    reg_date = models.DateField(_("Registry Date"), auto_now_add=True)
    phone_number = models.CharField(_("Phone Number"), max_length=12)
    mail = models.EmailField(_("E-Mail"), unique=True)
    interests = models.TextField(_("Interests"))
    tech_info = models.TextField(_("Technical Information"))
    experience = models.TextField(_("Experiences"))
    is_projects = models.BooleanField(_("Join technical projects"), default=False)
    is_education = models.BooleanField(_("Join educations"), default=False)
    is_informatics = models.BooleanField(_("Join Informatics Team"), default=False)
    is_magazine = models.BooleanField(_("Join KONTROL Magazine"), default=False)
    is_robot = models.BooleanField(_("Join ITURO Team"), default=False)
    is_evaluated = models.BooleanField(_("Evaluated ?"), default=False)

    def __unicode__(self):
        return self.name
