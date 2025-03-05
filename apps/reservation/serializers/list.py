from rest_framework.serializers import ModelSerializer

from apps.reservation.models import Reservation
from apps.user.serializers import UserSerializer


# Main Section
class ReservationListSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "id",
            "title",
            "start_time",
            "end_time",
            "applicant_count",
            "is_confirmed",
        )


class ReservationListAdminSerializer(ModelSerializer):
    reserver_user = UserSerializer()

    class Meta:
        model = Reservation
        fields = (
            "id",
            "title",
            "start_time",
            "end_time",
            "applicant_count",
            "is_confirmed",
            "reserver_user",
        )
