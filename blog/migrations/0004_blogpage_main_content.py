# Generated by Django 3.2.9 on 2021-11-20 03:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='main_content',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True),
        ),
    ]