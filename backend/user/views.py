import re
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import UserInformation

from .serializers import LoginSerializer, RegistrationSerialize, ProfileSerializer


@api_view(['POST', ])
@permission_classes((AllowAny,))
def login(request):

    if request.method == "POST":
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save()
            identifier = data['identifier']
            password = data['password']

            user = None

            if '@' in identifier:
                try:
                    user = User.objects.get(email=identifier)
                except:
                    data = {
                        "response": "There exists no user with the given email address."
                    }

                    return Response(data=data, status=status.HTTP_403_FORBIDDEN)

            else:
                try:
                    user = User.objects.get(username=identifier)
                except:
                    data = {
                        "response": "There exists no user with the given username."
                    }

                    return Response(data=data, status=status.HTTP_403_FORBIDDEN)

            if not user.check_password(password):
                data = {
                    "response": "The given password was incorrect."
                }

                return Response(data=data, status=status.HTTP_403_FORBIDDEN)

            user_information = UserInformation.objects.get(user=user)
            verified_user_status = user_information.verified_user_status

            data = {
                "response": "The user was successfully authenticated.",
                "token": Token.objects.get(user=user).key,
                "verified_user_status": verified_user_status
            }
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes((AllowAny,))
def register(request):

    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            data = {
                "response": "The given user was successfully created."
            }
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes((AllowAny,))
def username_check(request, username):

    users = User.objects.all()

    for user in users:
        if user.username == username:
            data = {
                "response": "The given username has already been taken by another user."
            }

            return Response(data=data, status=status.HTTP_403_FORBIDDEN)

    data = {
        "response": "The given username is available."
    }

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def user_verified_check(request):

    user = request.user
    user_information = UserInformation.objects.get(user=user)

    if user_information.verified_user_status:
        data = {
            "response": "The given user has verified their profile."
        }

        response_status = status.HTTP_200_OK
    else:
        data = {
            "response": "The given user is yet to verify their profile."
        }

        response_status = status.HTTP_403_FORBIDDEN

    return Response(data=data, status=response_status)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def get_user_profile(request):

    user = request.user
    user_information = UserInformation.objects.get(user=user)

    data = {
        "response": {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "username": user.username,
            "country": user_information.country,
            "state": user_information.state,
            "city": user_information.city
        }
    }

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def edit_user_profile(request):

    if request.method == "PUT":
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            data = {
                "response": "The user's profile was successfully updated."
            }
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=data, status=status.HTTP_200_OK)
