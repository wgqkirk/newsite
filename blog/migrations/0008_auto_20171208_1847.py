# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171208_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.rank'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
