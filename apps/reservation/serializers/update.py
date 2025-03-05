from django.db.models import Sum
from django.utils.timezone import now, timedelta
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.reservation.models import Reservation
from utils.validate_date import validate_date


# Main Section
class ReservationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("start_time", "end_time", "applicant_count")

    def validate(self, data):
        # Variables
        instance = self.instance
        start_time = data.get("start_time", instance.start_time)
        end_time = data.get("end_time", instance.end_time)

        # 이미 확정된 예약 변경 불가
        if instance.is_confirmed:
            raise ValidationError("이미 확정된 예약은 수정이 불가합니다.")

        # 해당 예약이 0 ~ 2일 내로 시작되는 시험일 경우
        elif instance.end_time - now() <= timedelta(days=2):  # TODO : 날짜 기준으로 변경
            raise serializers.ValidationError("시험까지 2일 이내로 남은 예약은 수정할 수 없습니다.")

        # 예약 시간 검증
        if data.get("start_time") or data.get("end_time"):
            validate_date(start_time, end_time)

        # 해당 시간대에 겹치는 승인된 예약 조회
        if applicant_count := data.get("applicant_count"):
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


class ReservationUpdateAdminSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("start_time", "end_time", "applicant_count", "is_confirmed")
