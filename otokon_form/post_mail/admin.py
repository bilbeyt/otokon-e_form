from django.contrib import admin
from post_mail.models import EmailMessage
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
        for i in range(0,248):
            send("Hello", "Hello", "otokon@itu.edu.tr", "bilbeyt@gmail.com")


admin.site.register(EmailMessage, EmailMessageAdmin)
