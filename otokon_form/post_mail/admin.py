from django.contrib import admin
from post_mail.models import EmailMessage


class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ["sender", "title", "time"]
    list_filter = ["time"]
    search_fields = ["sender", "title"]
    exclude = ["sender"]
   
    def save_model(self, request, obj, form, change):
	obj.sender = request.user
	super(EmailMessageAdmin, self).save_model(request, obj, form, change)


admin.site.register(EmailMessage, EmailMessageAdmin)
