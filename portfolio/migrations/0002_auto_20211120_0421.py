# Generated by Django 3.2.9 on 2021-11-20 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='background_image',
            field=models.ForeignKey(help_text='Header background image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='headline_text',
            field=models.CharField(blank=True, help_text='Blog listing page header text.', max_length=70),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='date',
            field=models.DateField(verbose_name='Project Date'),
        ),
    ]