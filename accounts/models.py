# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # By default, every new user is a customer
    is_customer = models.BooleanField(default=True)
    # You can also set up an explicit flag if necessary.
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
