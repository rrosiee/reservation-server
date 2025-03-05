from datetime import datetime, timedelta

from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.reservation.models import Reservation
from apps.schedule.views.serializers import ScheduleSwaggerSerializer


# Main Section
class SchedulesViewSet(viewsets.ViewSet):
    time_unit = 30
    pagination_class = PageNumberPagination

    @classmethod
    def generate_time_slots(cls, target_date):
        """하루(00:00 ~ 23:59)의 `time_unit` 단위 시간 슬롯을 생성"""
        slot_list = []
        base_time = datetime.combine(target_date, datetime.min.time())
        num_slots = (24 * 60) // cls.time_unit

        for i in range(num_slots):
            start = base_time + timedelta(minutes=cls.time_unit * i)
            end = start + timedelta(minutes=cls.time_unit) - timedelta(microseconds=1)
            slot_list.append(
                {
                    "start_time": start,
                    "end_time": end,
                    "available_applicant_count": 50000,  # 기본 최대 인원 설정
                }
            )

        return slot_list

    @swagger_auto_schema(
        tags=["Reservation - 예약"],
        operation_id="예약 가능한 일정 리스트 조회",
        operation_description="운영/성능상 이유로 30분 단위로 예약이 가능합니다.",
        responses={200: ScheduleSwaggerSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                name="date",
                in_=openapi.IN_QUERY,
                description="조회할 날짜 (YYYY-MM-DD)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
                required=True,
            )
        ],
    )
    def list(self, request, *args, **kwargs):
        # 1. 날짜 검증
        date_str = request.GET.get("date")
        if not date_str:
            return Response({"error": "날짜를 입력하세요. (YYYY-MM-DD)"}, status=400)

        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "잘못된 날짜 형식입니다. (YYYY-MM-DD)"}, status=400)

        # 2. 해당 날짜의 모든 예약 데이터 조회
        reservations = list(
            Reservation.objects.filter(
                Q(start_time__date=target_date) | Q(end_time__date=target_date)
            )
            .exclude(is_confirmed=False)
            .values_list("start_time", "end_time", "applicant_count")
        )

        # 3. 30분 단위 슬롯 생성
        time_slots = self.generate_time_slots(target_date)

        # 4. 예약 반영
        for start_time, end_time, applicant_count in reservations:
            # 이진 탐색 느낌
            start_idx = (start_time.hour * 60 + start_time.minute) // self.time_unit
            end_idx = (end_time.hour * 60 + end_time.minute) // self.time_unit

            for i in range(start_idx, min(end_idx + 1, len(time_slots))):
                time_slots[i]["available_applicant_count"] = max(
                    time_slots[i]["available_applicant_count"] - applicant_count, 0
                )

        # 5. Pagination 적용
        paginator = self.pagination_class()
        paginated_slots = paginator.paginate_queryset(time_slots, request)

        return paginator.get_paginated_response(paginated_slots)