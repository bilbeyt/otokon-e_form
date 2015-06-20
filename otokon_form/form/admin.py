from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    exclude = ['slug',]
    list_display = ['name', 'is_organization', 'is_technical',
                    'is_informatics', 'is_social', 'is_publish', 'is_evaluated']
    search_fields = ['name', 'mail', 'department',]
    list_filter = ['is_organization', 'is_technical', 'is_informatics',
                    'is_social', "is_publish", 'is_evaluated',]


admin.site.register(Form, FormAdmin)
