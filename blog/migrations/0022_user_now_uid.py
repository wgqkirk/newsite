# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-02 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_remove_user_now_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_now',
            name='uid',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
