# Generated by Django 4.2.3 on 2023-07-31 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='dueDate',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='priority',
        ),
    ]