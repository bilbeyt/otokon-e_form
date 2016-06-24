from django.contrib import admin
from post_mail.models import EmailMessage


class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ["sender", "title", "time"]
    list_filter = ["time"]
    search_fields = ["sender", "title"]


admin.site.register(EmailMessage, EmailMessageAdmin)
