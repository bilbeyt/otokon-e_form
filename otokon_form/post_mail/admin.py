from django.contrib import admin
from post_mail.models import EmailMessage, MailGroup
from form.models import Form
from post_mail.tasks import send


class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ["sender", "title", "time"]
    list_filter = ["time"]
    search_fields = ["sender", "title"]
    exclude = ["sender"]

    def save_model(self, request, obj, form, change):
        obj.sender = request.user
        ids = request.POST.getlist("to")
        mails = Form.objects.filter(id__in=ids).values_list("mail", flat=True)
        super(EmailMessageAdmin, self).save_model(request, obj, form, change)
        for mail in mails:
                send(obj.title, obj.content, "otokon@itu.edu.tr", mail)


class MailGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "created_date", "slug"]
    list_filter = ["created_date"]
    search_fields = ["name"]
    exclude = ["slug"]


admin.site.register(EmailMessage, EmailMessageAdmin)
admin.site.register(MailGroup, MailGroupAdmin)
