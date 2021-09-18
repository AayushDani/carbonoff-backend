from django.urls import path

from .views import *

app_name = "user"

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),

    path('check-verification-status',
         user_verified_check, name="verification-check"),
    path('check-username/<str:username>',
         username_check, name="username-check"),

    path('get-user-profile', get_user_profile, name="get-profile"),
    path('edit-user-profile', edit_user_profile, name="edit-profile")
]

# verification email
