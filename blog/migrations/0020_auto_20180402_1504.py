# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-02 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_admin_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='iden',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='rank',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='birth',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.item'),
            preserve_default=False,
        ),
    ]
