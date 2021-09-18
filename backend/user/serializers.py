from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User


class LoginSerializer(serializers.ModelSerializer):

    identifier = serializers.CharField(required=True, max_length=128)
    password = serializers.CharField(
        required=True, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ['identifier', 'password']

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def save(self):

        data = {
            "identifier": self.validated_data['identifier'],
            "password": self.validated_data['password']
        }

        return data
