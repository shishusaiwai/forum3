# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-07-01 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160701_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='owner',
        ),
    ]
