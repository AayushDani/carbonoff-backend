from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .models import UserInformation


class LoginSerializer(serializers.ModelSerializer):

    identifier = serializers.CharField(required=True, max_length=128)
    password = serializers.CharField(
        required=True, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ['identifier', 'password']

    def save(self):

        data = {
            "identifier": self.validated_data['identifier'],
            "password": self.validated_data['password']
        }

        return data


class RegistrationSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(required=True, max_length=128)
    last_name = serializers.CharField(required=True, max_length=128)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, max_length=128)
    country = serializers.CharField(required=True, max_length=128)
    state = serializers.CharField(required=True, max_length=128)
    city = serializers.CharField(required=True, max_length=128)

    password = serializers.CharField(
        required=True, write_only=True, max_length=128)
    confirm_password = serializers.CharField(
        required=True, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'country',
                  'state', 'city', 'password', 'confirm_password']

    def save(self):

        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        username = self.validated_data['username']
        country = self.validated_data['country']
        state = self.validated_data['state']
        city = self.validated_data['city']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(
                "The given passwords do not match. Kindly re-enter your password.")

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )

        user.set_password(password)
        user.save()

        user_information = UserInformation(user=user)
        user_information.country = country
        user_information.state = state
        user_information.city = city
        user_information.save()

        return user
