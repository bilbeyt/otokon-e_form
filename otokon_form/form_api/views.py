from django.shortcuts import render
from django.contrib.auth.models import User, Group
from form.models import Form
from rest_framework import viewsets
from form_api.serializers import UserSerializer, GroupSerializer, FormSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FormViewSet(viewsets.ModelViewSet):

    queryset = Form.objects.all()
    serializer_class = FormSerializer
