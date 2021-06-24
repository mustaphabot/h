# Generated by Django 3.2.2 on 2021-06-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0004_memorial_memorial_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorial',
            name='display_name',
            field=models.CharField(blank=True, help_text="How to display the person's name, if different from combined given and family names.", max_length=255, null=True),
        ),
    ]
