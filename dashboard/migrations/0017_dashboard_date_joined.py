# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-14 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_dashboard_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
