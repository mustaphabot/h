# Generated by Django 4.2 on 2023-05-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("magazine", "0023_magazineissue_drupal_node_id"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="magazineissue",
            index=models.Index(
                fields=["drupal_node_id"], name="magazine_ma_drupal__50c0bf_idx"
            ),
        ),
    ]
