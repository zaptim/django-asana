# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djasana', '0011_modifies_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djasana.Team', to_field='remote_id'),
        ),
    ]