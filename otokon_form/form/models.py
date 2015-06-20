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
    birthday = models.DateField(auto_now_add=False, help_text="Please enter "
    "birthday format YYYY-MM-DD")
    interests = models.TextField()
    tech_info = models.TextField()
    phone_number = PhoneNumberField(help_text="Please enter your country code "
    "too. For Turkey starts with +90")
    mail = models.EmailField(unique=True)
    dorm_adress = models.TextField(null=True, blank=True)
    home_adress = models.TextField(null=True, blank=True)
    reg_date = models.DateField(auto_now_add=True)
    is_organization = models.BooleanField(default=False,
                    help_text=("Organization team works actively in OTOKON's "
                    "related organizations such as ITURO and TOK. Advertising, "
                    "organization planning ,and communicating with sponsors are "
                    "the works for this team."))
    is_technical = models.BooleanField(default=False,
                 help_text=("This team works on the technical projects "
                 "which are suggested or already exist. Also, this team attends"
                 "local or international projects. Project managers and "
                 "the Education Team give necessary technical information."))
    is_informatics = models.BooleanField(default=False,
                   help_text=("This team is responsible for club's computer and"
                   "forum. Also, this team works on online registry, database, "
                   "kiosk and RFID technologies."))
    is_education = models.BooleanField(default=False,
                 help_text=("This team organizes seminars and educations to "
                 "sharing information. Also, this team provides a basis of "
                 "knowledge for OTOKON's technical projects."))
    is_publish = models.BooleanField(default=False,
               help_text=("This team works on archiving and sharing information"
               "which are provided from technical works and researches quickly. "
               "Also, this team publishes OTOKON magazine."))
    is_social = models.BooleanField(default=False,
              help_text=("This team organize technical trip to give new points "
              "of view to members of club, also social activities are organized "
              "to motivate members"))
    is_evaluated = models.BooleanField(default=False,
                 help_text="Is form evaluated?")
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name


@receiver(pre_save, sender=Form)
def form_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
