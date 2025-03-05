from django.utils.timezone import now, timedelta
from rest_framework.exceptions import ValidationError


# Main Section
def validate_date(start_time, end_time, is_admin=False):
    current_time = now()

    if (
            not start_time
            or not end_time
            or start_time >= end_time
            or start_time < current_time
    ):
        raise ValidationError("올바른 시작 및 종료 시간을 입력하세요.")
    elif start_time < current_time + timedelta(days=3) and not is_admin:
        raise ValidationError("예약은 3일 전까지만 수정 및 생성 가능합니다.")
    elif start_time >= end_time:
        raise ValidationError("시작 시간이 종료 시간보다 늦을 수 없습니다.")
    elif start_time.minute not in [0, 30] or start_time.second != 0:
        raise ValidationError("시작 시간은 HH:00:00 또는 HH:30:00이어야 합니다.")
    elif end_time.minute not in [29, 59] or end_time.second != 59:
        raise ValidationError("종료 시간은 HH:29:59 또는 HH:59:59이어야 합니다.")

    return True
