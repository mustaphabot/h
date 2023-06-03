# Generated by Django 4.1.6 on 2023-02-12 02:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("magazine", "0019_archiveissue_magazine_ar_interne_78a924_idx"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="archivearticle",
            index=models.Index(
                fields=["drupal_node_id"], name="magazine_ar_drupal__fd3a5b_idx"
            ),
        ),
    ]
