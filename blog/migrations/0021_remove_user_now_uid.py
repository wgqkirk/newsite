# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-02 23:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20180402_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_now',
            name='uid',
        ),
    ]
