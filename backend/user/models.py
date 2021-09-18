from django.db import models
from django.conf import settings
from django.db.models.query_utils import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.TextField(blank=False, null=False)
    state = models.TextField(blank=False, null=False)
    city = models.TextField(blank=False, null=False)

    verified_user_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "User Information"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
