from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins

from apps.reservation.models import Reservation
from apps.reservation.serializers import (
    ReservationSerializer,
    ReservationCreateSerializer,
    ReservationUpdateSerializer,
)


# Main Section
class ReservationViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Reservation.objects.all()
    serializers = {
        "default": ReservationSerializer,
        "create": ReservationCreateSerializer,
        "update": ReservationUpdateSerializer,
    }

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 객체 조회",
        operation_description="",
        responses={200: ReservationSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 객체 생성",
        operation_description="",
        request_body=ReservationCreateSerializer,
        responses={201: ReservationSerializer()},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 객체 수정",
        operation_description="",
        request_body=ReservationUpdateSerializer,
        responses={200: ReservationSerializer()},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 객체 삭제",
        operation_description="",
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ReservationsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Reservation.objects.all()
    serializers = {
        "default": ReservationSerializer,
    }

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 리스트 조회",
        operation_description="",
        responses={200: ReservationSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
