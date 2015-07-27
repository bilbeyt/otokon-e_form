from django.contrib import admin
from .models import Form
from django.db import models


class FormAdmin(admin.ModelAdmin):

    exclude = ['reg_date',]
    list_display = ['name', 'is_projects', 'is_education', 'is_informatics',
                    'is_magazine', 'is_robot', 'reg_date']
    search_fields = ['name', 'mail', 'department',]
    list_filter = ['is_projects', 'is_education', 'is_informatics',
                    'is_magazine', "is_robot", 'is_evaluated',]


admin.site.register(Form, FormAdmin)

a
