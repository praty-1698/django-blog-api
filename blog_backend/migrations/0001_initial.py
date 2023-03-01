# Generated by Django 4.1.7 on 2023-03-01 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=50)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("world", "World"),
                            ("politics", "Politics"),
                            ("technology", "Technology"),
                            ("business", "Business"),
                            ("sports", "Sports"),
                        ],
                        default="world",
                        max_length=50,
                    ),
                ),
                ("excerpt", models.CharField(max_length=150)),
                ("month", models.CharField(max_length=3)),
                ("day", models.CharField(max_length=2)),
                ("content", models.TextField()),
                (
                    "date_created",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
            ],
        ),
    ]
