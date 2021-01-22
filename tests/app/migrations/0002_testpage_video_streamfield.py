# Generated by Django 3.1.5 on 2021-01-21 22:54

from django.db import migrations
import wagtail.core.fields
import wagtailvideos.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpage',
            name='video_streamfield',
            field=wagtail.core.fields.StreamField([('video', wagtailvideos.blocks.VideoChooserBlock())], blank=True),
        ),
    ]