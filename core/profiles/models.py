from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _ 

from core.common.models import TimeStampedUUIDModel


User = get_user_model()

class Profile(TimeStampedUUIDModel):
    class Gender(models.TextChoices):
        MALE = "male", _("male")
        FEMALE = "female", _("female")


    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=50,
        choices=Gender.choices,
        default=Gender.MALE
        )
    about_me = models.TextField(blank=True, null=True)

    def __str__(self) :
        return str(self.user.username)

