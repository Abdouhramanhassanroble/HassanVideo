# Generated by Django 4.2.2 on 2023-06-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0004_alter_task_options_remove_task_complete_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='terminer',
        ),
        migrations.RemoveField(
            model_name='task',
            name='titre',
        ),
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
