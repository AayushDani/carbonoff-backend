from django.utils.translation import get_supported_language_variant
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .models import CarbonFootprint


class CarbonFootprintSerializer(serializers.ModelSerializer):

    token = serializers.CharField()
    carbon_footprint = serializers.IntegerField()
    get_started_section_score = serializers.IntegerField()
    travel_section_score = serializers.IntegerField()
    home_section_score = serializers.IntegerField()
    food_section_score = serializers.IntegerField()
    shopping_section_score = serializers.IntegerField()

    class Meta:
        model = CarbonFootprint

        fields = ['token', 'carbon_footprint', 'get_started_section_score', 'travel_section_score',
                  'home_section_score', 'food_section_score', 'shopping_section_score']

    def save(self):

        token = self.validated_data['token']
        user = Token.objects.get(key=token).user

        carbon_footprint = self.validated_data['carbon_footprint']
        get_started_section_score = self.validated_data['get_started_section_score']
        travel_section_score = self.validated_data['travel_section_score']
        home_section_score = self.validated_data['home_section_score']
        food_section_score = self.validated_data['food_section_score']
        shopping_section_score = self.validated_data['shopping_section_score']

        carbon_footprint = CarbonFootprint(
            user=user,
            carbon_footprint=carbon_footprint,
            get_started_section_score=get_started_section_score,
            travel_section_score=travel_section_score,
            home_section_score=home_section_score,
            food_section_score=food_section_score,
            shopping_section_score=shopping_section_score,
        )

        carbon_footprint.save()

        return carbon_footprint
