import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                ("applicant_count", models.IntegerField()),
                ("is_confirmed", models.BooleanField(default=False)),
                (
                    "reserver_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="reservations",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="예약자",
                    ),
                ),
            ],
            options={
                "verbose_name": "예약",
                "verbose_name_plural": "예약 목록",
                "db_table": "reservation",
            },
        ),
    ]
