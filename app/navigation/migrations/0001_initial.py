# Generated by Django 3.2.13 on 2022-04-20 13:22

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="NavigationMenuSetting",
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
                    "items",
                    wagtail.fields.StreamField(
                        [
                            (
                                "internal_page",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("title", wagtail.blocks.CharBlock()),
                                        (
                                            "page",
                                            wagtail.blocks.PageChooserBlock(),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "external_link",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("title", wagtail.blocks.CharBlock()),
                                        ("url", wagtail.blocks.URLBlock()),
                                    ]
                                ),
                            ),
                            (
                                "drop_down",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("title", wagtail.blocks.CharBlock()),
                                        (
                                            "items",
                                            wagtail.blocks.StreamBlock(
                                                [
                                                    (
                                                        "page",
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "title",
                                                                    wagtail.blocks.CharBlock(),
                                                                ),
                                                                (
                                                                    "page",
                                                                    wagtail.blocks.PageChooserBlock(),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    (
                                                        "external_link",
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "title",
                                                                    wagtail.blocks.CharBlock(),
                                                                ),
                                                                (
                                                                    "url",
                                                                    wagtail.blocks.URLBlock(),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
            ],
            options={
                "verbose_name": "Navigation menu (WF)",
            },
        ),
    ]
