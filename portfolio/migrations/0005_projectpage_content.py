# Generated by Django 3.2.9 on 2021-11-20 04:51

from django.db import migrations
import streamfieldblocks.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20211120_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='content',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.StructBlock([('richtext', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul']))])), ('carousel', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('flush_list', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock(help_text="List item's body text.")))])), ('responsive_image', streamfieldblocks.models.ResponsiveImageBlock())], blank=True, null=True),
        ),
    ]
