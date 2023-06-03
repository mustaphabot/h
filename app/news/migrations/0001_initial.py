# Generated by Django 3.2.12 on 2022-03-21 08:46

import datetime

import django.db.models.deletion
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models

import blocks.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsTopic",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsTopicIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsType",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsTypeIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsItem",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "teaser",
                    models.TextField(
                        help_text="Briefly summarize the news item for display in news lists",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(),
                            ),
                            (
                                "heading",
                                wagtail.blocks.CharBlock(form_classname="full title"),
                            ),
                            (
                                "image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        (
                                            "width",
                                            wagtail.blocks.IntegerBlock(
                                                help_text="Enter the desired image width value in pixels up to 800 max.",
                                                max_value=800,
                                                min_value=0,
                                            ),
                                        ),
                                    ],
                                    classname="full title",
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.blocks.RichTextBlock(
                                    features=[
                                        "h2",
                                        "h3",
                                        "h4",
                                        "bold",
                                        "italic",
                                        "ol",
                                        "ul",
                                        "hr",
                                        "link",
                                        "document-link",
                                        "image",
                                        "superscript",
                                        "superscript",
                                        "strikethrough",
                                        "blockquote",
                                    ]
                                ),
                            ),
                            ("pullquote", blocks.blocks.PullQuoteBlock()),
                        ]
                    ),
                ),
                ("publication_date", models.DateField(default=datetime.date.today)),
                (
                    "news_topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="news_items",
                        to="news.newstopic",
                    ),
                ),
                (
                    "news_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="news_items",
                        to="news.newstype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
