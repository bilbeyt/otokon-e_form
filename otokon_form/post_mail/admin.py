from django.contrib import admin
from post_mail.models import EmailMessage
from django.core.mail import send_mail
from form.models import Form


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
        send_mail(
            obj.title,
            obj.content,
            "otokon@itu.edu.tr",
            mails,
            fail_silently=False
    	)


admin.site.register(EmailMessage, EmailMessageAdmin)
