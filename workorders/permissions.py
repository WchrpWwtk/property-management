from rest_framework import permissions


class IsMaidSupervisorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.user.is_authenticated
            and request.user.user_role == "Maid Supervisor"
        ):
            return True

        return False


class IsGuestOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_role == "Guest":
            return True

        return False
