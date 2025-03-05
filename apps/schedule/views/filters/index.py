from datetime import datetime

import django_filters
from django.utils.timezone import make_aware
from django_filters import BooleanFilter, CharFilter

from apps.reservation.models import Reservation


# Main Section
class ReservationFilter(django_filters.FilterSet):
    start_date = CharFilter(method="start_date_filter")
    end_date = CharFilter(method="end_date_filter")
    is_confirmed = BooleanFilter(field_name="is_confirmed")

    class Meta:
        model = Reservation
        fields = (
            "start_date",
            "end_date",
            "is_confirmed",
        )

    def start_date_filter(self, queryset, name, value):
        try:
            start_date = make_aware(datetime.strptime(value, "%Y-%m-%d"))
            return queryset.filter(start_time__gte=start_date)
        except ValueError:
            raise ValueError("날짜 형식은 YYYY-MM-DD이어야 합니다.")

    def end_date_filter(self, queryset, name, value):
        try:
            end_date = make_aware(datetime.strptime(value, "%Y-%m-%d"))
            return queryset.filter(end_time__lte=end_date)
        except ValueError:
            raise ValueError("날짜 형식은 YYYY-MM-DD이어야 합니다.")
