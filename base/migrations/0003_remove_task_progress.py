# Generated by Django 4.2.3 on 2023-08-01 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_date_task_duedate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='progress',
        ),
    ]
