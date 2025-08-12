from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Optional fields
    profession = models.CharField(max_length=100, blank=True, null=True)
    kids = models.PositiveIntegerField(blank=True, null=True)
    wife = models.BooleanField(default=False)  # True if married, False if not
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
