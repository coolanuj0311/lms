# Generated by Django 4.0.8 on 2024-04-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_choice_id_alter_course_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecompletionstatusperuser',
            name='completion_status',
        ),
        migrations.RemoveField(
            model_name='coursecompletionstatusperuser',
            name='in_progress_status',
        ),
        migrations.AddField(
            model_name='coursecompletionstatusperuser',
            name='status',
            field=models.CharField(choices=[('started', 'Started'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='started', max_length=20),
        ),
    ]
