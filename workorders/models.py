from django.contrib.auth.models import AbstractUser, Group
from django.db import models


# Create your models here.
class PropertyUser(AbstractUser):
    USER_ROLES = [
        ("Guest", "Guest"),
        ("Maid Supervisor", "Maid Supervisor"),
        ("Technician Supervisor", "Technician Supervisor"),
    ]

    user_role = models.CharField(max_length=21, choices=USER_ROLES)
    user_permissions = models.ManyToManyField(
        "auth.Permission", blank=True, related_name="property_users"
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name="property_users_groups",
    )

    def __str__(self):
        return self.username
