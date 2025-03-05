from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from apps.reservation.models import Reservation
from apps.reservation.serializers import (
    ReservationSerializer,
)


# Main Section
class SchedulesViewSet(
    viewsets.GenericViewSet,
):
    queryset = Reservation.objects.all()
    serializers = {
        "default": ReservationSerializer,
    }

    @swagger_auto_schema(
        tags=["Schedule - 일정"],
        operation_id="예약 가능한 일정 리스트 조회",
        operation_description="",
        responses={200: ReservationSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(
            data=ReservationSerializer(instance=queryset, many=True), status=200
        )
