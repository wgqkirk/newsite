# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-03 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20180403_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='birth',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='registerdate',
            field=models.DateField(max_length=10),
        ),
    ]
