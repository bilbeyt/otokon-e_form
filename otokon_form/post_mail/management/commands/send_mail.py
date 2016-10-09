from django.core.management.base import BaseCommand, CommandError
from post_mail.models import MailGroup
from django.conf import settings
from django.core.mail import send_mail


class Command(BaseCommand):
    args = '<files>'
    help = "Send message from text file to all members"

    def handle(self, *args, **options):
        try:
            group_slug = args[0]
        except:
            raise CommandError("Please enter group_slug")
        try:
            filename = args[1]
        except:
            raise CommandError("Please enter filename")
        try:
            subject = args[2]
        except:
            raise CommandError("Please enter subject")
        try:
            select = int(args[3])
        except:
            raise CommandError("Please specify for 1 OTOKON 2 ITURO")

        if select==1:
            sender = settings.MAIL_1
        elif select==2:
            sender = settings.MAIL_2

        with open(filename) as content:
            message_content = content.read()

        group = MailGroup.objects.get(slug=group_slug)

        for contact in group.contacts.all():
            try:
                send_mail(subject, message_content, sender, [contact.mail], fail_silently=False)
            except:
                self.stdout.write("Can not sent to {}".format(contact.name))

        self.stdout.write('All mails sent')
