# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171208_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='height',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weight',
            field=models.FloatField(max_length=10),
        ),
    ]