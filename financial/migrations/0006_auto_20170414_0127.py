# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-14 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0005_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.DeleteModel(
            name='transaction',
        ),
    ]
