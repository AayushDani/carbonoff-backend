from django.urls import path

from .views import *


urlpatterns = [
    path('create-footprint', create_footprint, name="create-footprint"),
    path('get-footprints', get_footprints, name="get-footprints"),
    path('get-footprint/<int:footprint_id>',
         get_footprint, name="get-footprint"),
]
