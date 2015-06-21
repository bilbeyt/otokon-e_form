from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django import forms


class Form(models.Model):
    name = models.CharField(_("Full Name"), max_length=150)
    department = models.CharField(_("Department"), max_length=100)
    school_number = models.PositiveIntegerField(_("School Number"))
    term = models.PositiveSmallIntegerField(_("Term"))
    birthday = models.DateField(_("Birthday"), auto_now_add=False,
                help_text=(_("Please enter birthday as YYYY-MM-DD")))
    interests = models.TextField(_("Interests"))
    tech_info = models.TextField(_("Technical Information"),
                help_text=_("Your works about hardware or software"))
    phone_number = PhoneNumberField(_("Phone Number"), help_text=_("Please enter "
    "your country code too. For Turkey starts with +90"))
    mail = models.EmailField(_("E-Mail"), unique=True)
    dorm_adress = models.TextField(_("Dorm Adress"), null=True, blank=True)
    home_adress = models.TextField(_("Home Adress"), null=True, blank=True)
    reg_date = models.DateField(_("Registry Date"), auto_now_add=True)
    is_organization = models.BooleanField(_("Organization Team"), default=False,
                    help_text=(_("Organization team works actively in OTOKON's "
                    "related organizations such as ITURO and TOK. Advertising, "
                    "organization planning ,and communicating with sponsors are "
                    "the works for this team.")))
    is_technical = models.BooleanField(_("Technical Team"), default=False,
                 help_text=(_("This team works on the technical projects "
                 "which are suggested or already exist. Also, this team attends"
                 "local or international projects. Project managers and "
                 "the Education Team give necessary technical information.")))
    is_informatics = models.BooleanField(_("Informatics Team"), default=False,
                   help_text=(_("This team is responsible for club's computer and"
                   "forum. Also, this team works on online registry, database, "
                   "kiosk and RFID technologies.")))
    is_education = models.BooleanField(_("Education Team"), default=False,
                 help_text=(_("This team organizes seminars and educations to "
                 "sharing information. Also, this team provides a basis of "
                 "knowledge for OTOKON's technical projects.")))
    is_publish = models.BooleanField(_("Press and Publishment Team"), default=False,
               help_text=(_("This team works on archiving and sharing information"
               "which are provided from technical works and researches quickly. "
               "Also, this team publishes KONTROL magazine.")))
    is_social = models.BooleanField(_("Technical Trip and Social Activity Team"),
              default=False,
              help_text=(_("This team organize technical trip to give new points "
              "of view to members of club, also social activities are organized "
              "to motivate members")))
    is_evaluated = models.BooleanField(_("Evaluated ?"), default=False,
                 help_text=(_("Is form evaluated?")))

    def __unicode__(self):
        return self.name
