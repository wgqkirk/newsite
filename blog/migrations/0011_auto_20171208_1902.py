# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171208_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='height',
            field=models.FloatField(default=0),
        ),
    ]
