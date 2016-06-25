from django.contrib.auth.models import User, Group
from form.models import Form
from post_mail.models import EmailMessage
from rest_framework import viewsets
from form_api.serializers import UserSerializer, GroupSerializer, \
                                FormSerializer, EmailMessageSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FormViewSet(viewsets.ModelViewSet):

    queryset = Form.objects.all()
    serializer_class = FormSerializer


class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer
