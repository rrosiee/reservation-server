from django.db import models

from base.models import BaseModel


# Main Section
class Reservation(BaseModel):
    # Main
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    applicant_count = models.IntegerField()
    is_confirmed = models.BooleanField(default=False, db_index=True)

    # FK
    reserver_user = models.ForeignKey(
        "user.User",
        verbose_name="예약자",
        on_delete=models.SET_NULL,
        null=True,
        related_name="reservations"
    )

    class Meta:
        db_table = "reservation"
        verbose_name = "예약"
        verbose_name_plural = "예약 목록"
