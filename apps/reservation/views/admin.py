from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins

from apps.reservation.models import Reservation
from apps.reservation.serializers import ReservationSerializer
from apps.reservation.views.filters import ReservationFilter
from apps.reservation.views.permissions import AdminReservationPermission


# Main Section
class AdminReservationsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [AdminReservationPermission]
    filterset_class = ReservationFilter

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="어드민 예약 리스트 조회",
        operation_description="",
        responses={200: ReservationSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
