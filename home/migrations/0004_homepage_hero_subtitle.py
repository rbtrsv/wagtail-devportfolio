# Generated by Django 3.2.9 on 2021-11-20 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_hero_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_subtitle',
            field=models.TextField(blank=True, help_text='Subtitle following the main title in the hero section.', max_length=200),
        ),
    ]
