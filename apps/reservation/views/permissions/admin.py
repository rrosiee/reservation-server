from rest_framework.permissions import BasePermission


# Main Section
class AdminReservationPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated or not user.is_admin:
            return False

        return True


class AdminReservationsPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated or not user.is_admin:
            return False

        return True
