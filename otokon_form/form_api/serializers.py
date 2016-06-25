from django.contrib.auth.models import User, Group
from rest_framework import serializers
from form.models import Form
from post_mail.models import EmailMessage


class FormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Form
        exclude = ("reg_date","is_evaluated",)



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class EmailMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailMessage
