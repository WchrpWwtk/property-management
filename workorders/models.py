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


class WorkOrder(models.Model):
    WORK_ORDER_TYPES = [
        ("Cleaning", "Cleaning"),
        ("Maid Request", "Maid Request"),
        ("Technician Request", "Technician Request"),
        ("Amenity Request", "Amenity Request"),
    ]

    STATUS_CHOICES = [
        ("Created", "Created"),
        ("Assigned", "Assigned"),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
        ("Cancel", "Cancel"),
    ]

    created_by = models.ForeignKey(
        PropertyUser, on_delete=models.CASCADE, related_name="created_workorders"
    )
    assigned_to = models.ForeignKey(
        PropertyUser, on_delete=models.CASCADE, related_name="assigned_workorders"
    )
    room = models.CharField(max_length=10)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    order_type = models.CharField(max_length=20, choices=WORK_ORDER_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # For Maid Request
    description = models.TextField(blank=True, null=True)

    # For Technician Request
    defect_type = models.CharField(max_length=50, blank=True, null=True)

    # For Amenity Request
    amenity_type = models.CharField(max_length=50, blank=True, null=True) 
    quantity = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return f"${self.id} {self.order_type} {self.room} {self.status}"