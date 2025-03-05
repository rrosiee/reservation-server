from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status, filters
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.reservation.models import Reservation
from apps.reservation.serializers import (
    ReservationSerializer,
    ReservationCreateSerializer,
    ReservationUpdateSerializer,
    ReservationListSerializer,
)
from apps.reservation.views.filters import ReservationFilter
from apps.reservation.views.permissions import ReservationPermission


# Main Section
class ReservationViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [ReservationPermission]

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 객체 조회",
        operation_description="`제약 조건` : 본인의 예약만 조회 가능",
        responses={200: ReservationSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 객체 생성",
        operation_description="""
        `제약 조건` : 동시간대에 50000명 - 확정 인원만큼만 인원 선정 가능, 시험 시작일 3일 전까지만 생성 가능, 30분 단위로 시험 등록 가능
        """,
        request_body=ReservationCreateSerializer,
        responses={201: ReservationSerializer()},
    )
    def create(self, request, *args, **kwargs):
        serializer = ReservationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reservation = serializer.save(reserver_user=request.user)
        return Response(
            data=ReservationSerializer(instance=reservation).data, status=200
        )

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 객체 수정",
        operation_description="""
        `제약 조건` : 본인의 예약만 수정 가능, 동시간대에 50000명 - 확정 인원만큼만 인원 선정 가능, 시험 시작일 3일 전까지만 수정 가능, 30분 단위로 시험 등록 가능
        """,
        request_body=ReservationUpdateSerializer,
        responses={200: ReservationSerializer()},
    )
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ReservationUpdateSerializer(
            instance, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 객체 삭제",
        operation_description="""
        `제약 조건` : 확정 되기 전의 본인의 예약만 삭제 가능
        """,
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        if self.get_object().is_confirmed:
            raise ValidationError("예약이 확정된 경우, 예약을 삭제할 수 없습니다.")
        return super().destroy(request, *args, **kwargs)


class ReservationsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer
    filterset_class = ReservationFilter
    pagination_class = PageNumberPagination
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ["start_time", "end_time", "created"]
    ordering = ["-created"]

    def get_queryset(self):
        return Reservation.objects.filter(reserver_user=self.request.user)

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 리스트 조회",
        operation_description="""
        `제약 조건` : 본인의 예약 리스트만 조회 가능
        """,
        responses={200: ReservationListSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
