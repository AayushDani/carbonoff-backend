from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import UserInformation

from .serializers import LoginSerializer, RegistrationSerializer