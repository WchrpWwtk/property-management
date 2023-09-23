from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PropertyUser


class PropertyUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "user_role",
        "is_staff",
    )
    list_filter = ("user_role", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Custom Fields", {"fields": ("user_role",)}),  # Add any custom fields here
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "user_role",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(PropertyUser, PropertyUserAdmin)
