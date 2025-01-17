# Generated by Django 5.1.1 on 2024-09-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="School",
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
                ("name", models.CharField(default="Unknown", max_length=255)),
                ("category", models.CharField(default="Public", max_length=255)),
                ("deviation", models.FloatField(default=0.0)),
                ("address", models.CharField(default="Public", max_length=255)),
                ("region", models.CharField(default="Public", max_length=255)),
                ("latitude", models.FloatField(default=35.68944)),
                ("longitude", models.FloatField(default=139.69167)),
                ("url", models.URLField(default="Unknown")),
            ],
        ),
    ]
