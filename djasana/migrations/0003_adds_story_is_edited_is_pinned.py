# Generated by Django 2.0.5 on 2018-06-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djasana', '0002_adds_project_start_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='story',
            name='is_pinned',
            field=models.BooleanField(default=False),
        ),
    ]