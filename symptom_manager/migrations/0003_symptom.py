# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-07 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('symptom_manager', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidentid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('commonality', models.IntegerField()),
            ],
        ),
    ]