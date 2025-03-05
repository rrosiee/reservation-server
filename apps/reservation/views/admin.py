from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.reservation.models import Reservation
from apps.reservation.serializers import (
    ReservationUpdateAdminSerializer,
    ReservationListAdminSerializer,
    ReservationAdminSerializer,
)
from apps.reservation.views.filters import ReservationFilter
from apps.reservation.views.permissions import (
    AdminReservationsPermission,
    AdminReservationPermission,
)


# Main Section
class AdminReservationViewSet(
    viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin
):
    queryset = Reservation.objects.all().select_related("reserver_user")
    serializer_class = ReservationAdminSerializer
    permission_classes = [AdminReservationPermission]

    @swagger_auto_schema(
        tags=["Reservation - (어드민) 예약"],
        operation_id="예약 객체 조회",
        operation_description="",
        responses={200: ReservationAdminSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Reservation - (어드민) 예약"],
        operation_id="예약 객체 수정",
        operation_description="",
        request_body=ReservationUpdateAdminSerializer,
        responses={200: ReservationAdminSerializer()},
    )
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ReservationUpdateAdminSerializer(
            instance=instance, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(
            data=ReservationAdminSerializer(instance=instance).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        tags=["Reservation - (어드민) 예약"],
        operation_id="예약 객체 삭제",
        operation_description="",
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AdminReservationsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Reservation.objects.all().select_related("reserver_user")
    serializer_class = ReservationListAdminSerializer
    permission_classes = [AdminReservationsPermission]
    filterset_class = ReservationFilter
    pagination_class = PageNumberPagination
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ["start_time", "end_time", "created"]
    ordering = ["-created"]

    @swagger_auto_schema(
        tags=["Reservation - (어드민) 예약"],
        operation_id="어드민 예약 리스트 조회",
        operation_description="",
        responses={200: ReservationListAdminSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
