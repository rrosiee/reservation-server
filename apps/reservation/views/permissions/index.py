from rest_framework.permissions import BasePermission


# Main Section
class ReservationPermission(BasePermission):
    def has_object_permission(self, request, view, obj):

        user = request.user

        if view.action in ("retrieve",):
            if not (user.is_admin or obj.reserver_user == user):
                return False
        return True
