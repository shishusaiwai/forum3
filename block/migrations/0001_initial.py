# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-18 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='板块名称')),
                ('desc', models.CharField(max_length=100, verbose_name='板块描述')),
                ('manager_name', models.CharField(max_length=100, verbose_name='板块管理员名称')),
            ],
        ),
    ]
