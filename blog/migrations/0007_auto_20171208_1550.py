# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 07:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171208_1543'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userifo',
            new_name='userinfo',
        ),
    ]