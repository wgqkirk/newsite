# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 06:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171204_1406'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='userstest',
        ),
    ]
