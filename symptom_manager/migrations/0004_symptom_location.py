# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-08 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom_manager', '0003_symptom'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='location',
            field=models.CharField(default='N/A', max_length=50),
            preserve_default=False,
        ),
    ]
