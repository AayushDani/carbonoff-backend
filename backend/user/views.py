from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import UserInformation

from .serializers import LoginSerializer


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
