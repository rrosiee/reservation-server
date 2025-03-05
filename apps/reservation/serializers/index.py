from rest_framework.serializers import ModelSerializer

from apps.reservation.models import Reservation


# Main Section
class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "start_time", "end_time", "applicant_count", "is_confirmed")
