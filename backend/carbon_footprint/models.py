from django.db import models

from django.contrib.auth.models import User


class CarbonFootprint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    footprint_id = models.AutoField(primary_key=True)

    carbon_footprint = models.IntegerField(blank=False, null=False)
    get_started_section_score = models.IntegerField(blank=False, null=False)
    travel_section_score = models.IntegerField(blank=False, null=False)
    home_section_score = models.IntegerField(blank=False, null=False)
    food_section_score = models.IntegerField(blank=False, null=False)
    shopping_section_score = models.IntegerField(blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Carbon Footprint"

    def __str__(self):
        return self.user.username + " -> " + self.created_at.date()
