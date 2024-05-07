# Generated by Django 4.0.8 on 2024-05-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_coursecompletionstatusperuser_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadvideo',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='uploadvideo',
            name='video_duration',
            field=models.DurationField(help_text='Duration of the video', null=True),
        ),
    ]