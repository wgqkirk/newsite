# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20171208_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='height',
            field=models.FloatField(),
        ),
    ]