# Generated by Django 3.2.13 on 2022-06-08 12:19

import re

import django.core.validators
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0006_alter_communitypage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="communitypage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading_level",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("h2", "Level 2 (child of level 1)"),
                                            ("h3", "Level 3 (child of level 2)"),
                                            ("h4", "Level 4 (child of level 3)"),
                                            ("h5", "Level 5 (child of level 4)"),
                                            ("h6", "Level 6 (child of level 5)"),
                                        ],
                                        help_text="These different heading levels help to communicate the organization and hierarchy of the content on a page.",
                                    ),
                                ),
                                (
                                    "heading_text",
                                    wagtail.blocks.CharBlock(
                                        help_text="The text to appear in the heading."
                                    ),
                                ),
                                (
                                    "target_slug",
                                    wagtail.blocks.CharBlock(
                                        help_text="Used to link to a specific location within this page. A slug should only contain letters, numbers, underscore (_), or hyphen (-).",
                                        required=False,
                                        validators=(
                                            django.core.validators.RegexValidator(
                                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                                "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                                                "invalid",
                                            ),
                                        ),
                                    ),
                                ),
                                (
                                    "color",
                                    wagtail_color_panel.blocks.NativeColorBlock(
                                        required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("rich_text", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "card",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Add a title", required=True
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "image_align",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[("left", "Left"), ("right", "Right")],
                                        help_text="Whether to align the image left or right on the block.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "button",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "button_text",
                                                wagtail.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "page_link",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                        ],
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "card_row",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    (
                                        "page",
                                        wagtail.blocks.PageChooserBlock(required=True),
                                    ),
                                    (
                                        "text",
                                        wagtail.blocks.CharBlock(required=False),
                                    ),
                                ],
                                label="Page",
                            ),
                            template="streams/blocks/card_row.html",
                        ),
                    ),
                    (
                        "spacer",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "height",
                                    wagtail.blocks.IntegerBlock(
                                        help_text="The height of this spacer in 'em' values where 1 em is one uppercase M."
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                null=True,
            ),
        ),
    ]
