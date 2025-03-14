# Generated by Django 5.1.7 on 2025-03-10 06:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Scooter",
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
                ("model", models.CharField(max_length=100)),
                ("battery_capacity", models.IntegerField(default=100)),
                ("battery_level", models.IntegerField(default=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("available", "Доступен"),
                            ("rented", "Арендован"),
                            ("maintenance", "На обслуживании"),
                        ],
                        default="available",
                        max_length=20,
                    ),
                ),
                (
                    "last_maintenance_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
