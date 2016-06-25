from django.db import models
from django.utils.translation import ugettext_lazy as _


Department_Choices = (
    (_("Control and Automation Engineering"), ("KON")),
    (_("Computer Engineering"), ("BLG")),
    (_("Electronics and Communication Engineering"), ("EHB")),
    (_("Electrical Engineering"), ("ELE")),
    (_("Others"), ("OTH")),
)


class Form(models.Model):
    name = models.CharField(_("Full Name"), max_length=150)
    department = models.CharField(_("Department"), choices=Department_Choices, max_length=100)
    other_departments = models.CharField(_("Other Departments"), max_length=100, null=True, blank=True)
    school_number = models.PositiveIntegerField(_("School Number"))
    reg_date = models.DateField(_("Registry Date"), auto_now_add=True)
    phone_number = models.CharField(_("Phone Number"), max_length=15)
    mail = models.EmailField(_("E-Mail"), unique=True)
    interests = models.CharField(_("Interests"), max_length=150)
    tech_info = models.CharField(_("Technical Information"), max_length=150)
    experience = models.CharField(_("Experiences"), max_length=150)
    is_projects = models.BooleanField(_("Join technical projects"), default=False)
    is_education = models.BooleanField(_("Join educations"), default=False)
    is_informatics = models.BooleanField(_("Join Informatics Team"), default=False)
    is_magazine = models.BooleanField(_("Join KONTROL Magazine"), default=False)
    is_robot = models.BooleanField(_("Join ITURO Team"), default=False)
    is_evaluated = models.BooleanField(_("Evaluated ?"), default=False)

    def __unicode__(self):
        return self.name
