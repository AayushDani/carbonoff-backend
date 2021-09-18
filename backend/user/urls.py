from django.urls import path

from .views import *

app_name = "user"

urlpatterns = [
    path('login/', login, name="login"),
]

# check verified email or not
# registration
