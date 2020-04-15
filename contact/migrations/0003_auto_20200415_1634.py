# Generated by Django 3.0.5 on 2020-04-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_organizationindexpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='drupal_full_name',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='drupal_full_name',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='drupal_full_name',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
