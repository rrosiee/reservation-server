from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.utils.timezone import now, timedelta
from rest_framework.serializers import ModelSerializer

from apps.reservation.models import Reservation


# Main Section
class ReservationCreateSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("title", "start_time", "end_time", "applicant_count")

    def validate(self, data):
        # Variables
        start_time = data.get("start_time")
        end_time = data.get("end_time")
        applicant_count = data.get("applicant_count")

        # 예약 시간 검증
        current_time = now()
        if (
                not start_time
                or not end_time
                or start_time >= end_time
                or start_time < current_time
        ):
            raise ValidationError("올바른 시작 및 종료 시간을 입력하세요.")
        elif start_time < current_time + timedelta(days=3):
            raise ValidationError("예약은 3일 전까지만 가능합니다.")

        # 해당 시간대에 겹치는 승인된 예약 조회
        already_applicant_count = (
                Reservation.objects.filter(
                    is_confirmed=True,
                    start_time__lt=end_time,  # 예약 종료 시간이 새 예약 시작 시간 이후인 경우
                    end_time__gt=start_time,  # 예약 시작 시간이 새 예약 종료 시간 이전인 경우
                ).aggregate(Sum("applicant_count"))["applicant_count__sum"]
                or 0
        )

        max_capacity = 50000
        if already_applicant_count + applicant_count > max_capacity:
            raise ValidationError(
                f"최대 {max_capacity - already_applicant_count:,}명 예약 가능합니다."
            )

        return data
