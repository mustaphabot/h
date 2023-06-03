# Generated by Django 4.1.6 on 2023-02-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0015_event_sponsor"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="category",
            field=models.CharField(
                choices=[("western", "Western"), ("other", "Other")],
                default="western",
                max_length=255,
            ),
        ),
    ]
