from rest_framework.permissions import BasePermission


# Main Section
class AdminReservationPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        if view.action in ("list",):
            if not user.is_admin:
                return False
        return True
