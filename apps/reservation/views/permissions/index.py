from rest_framework.permissions import BasePermission


# Main Section
class ReservationPermission(BasePermission):
    def has_object_permission(self, request, view, obj):

        user = request.user

        if view.action in ("retrieve", "partial_update", "destroy"):
            if not obj.reserver_user == user:
                return False
        return True
