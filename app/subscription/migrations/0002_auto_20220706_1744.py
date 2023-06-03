# Generated by Django 3.2.13 on 2022-07-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subscription", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="subscriber_address_country",
            field=models.CharField(
                blank=True,
                default="United States",
                help_text="Country for mailing",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="subscriber_address_locality",
            field=models.CharField(
                blank=True, help_text="City for the mailing address", max_length=255
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="subscriber_address_region",
            field=models.CharField(
                blank=True,
                default="",
                help_text="State for the mailing address",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="subscriber_postal_code",
            field=models.CharField(
                blank=True,
                help_text="Postal code for the mailing address",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="subscriber_street_address",
            field=models.CharField(
                blank=True,
                default="",
                help_text="The street address where a print subscription could be mailed",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="subscriber_street_address_line_2",
            field=models.CharField(
                blank=True,
                default="",
                help_text="If needed, second line for mailing address",
                max_length=255,
            ),
        ),
    ]
