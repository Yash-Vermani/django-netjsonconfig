# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0011_template_config_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
