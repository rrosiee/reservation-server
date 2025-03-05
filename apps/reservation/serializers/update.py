from rest_framework.serializers import ModelSerializer

from apps.reservation.models import Reservation


# Main Section
class ReservationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("start_time", "end_time", "applicant_count")


class ReservationUpdateAdminSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("start_time", "end_time", "applicant_count", "is_confirmed")
