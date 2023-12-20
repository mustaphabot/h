# Generated by Django 4.2.7 on 2023-12-20 18:38

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):
    dependencies = [
        ("facets", "0001_initial"),
        ("news", "0026_alter_newsitem_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsItemTopic",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="newstopicindexpage",
            name="page_ptr",
        ),
        migrations.RemoveField(
            model_name="newsitem",
            name="news_topic",
        ),
        migrations.DeleteModel(
            name="NewsTopic",
        ),
        migrations.DeleteModel(
            name="NewsTopicIndexPage",
        ),
        migrations.AddField(
            model_name="newsitemtopic",
            name="news_item",
            field=modelcluster.fields.ParentalKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="topics",
                to="news.newsitem",
            ),
        ),
        migrations.AddField(
            model_name="newsitemtopic",
            name="topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="related_news_items",
                to="facets.topic",
            ),
        ),
    ]