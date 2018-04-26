# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-04 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20180403_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='weekly_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('week1', models.FloatField(null=True)),
                ('week2', models.FloatField(null=True)),
                ('week3', models.FloatField(null=True)),
                ('week4', models.FloatField(null=True)),
                ('week5', models.FloatField(null=True)),
                ('week6', models.FloatField(null=True)),
                ('week7', models.FloatField(null=True)),
                ('week8', models.FloatField(null=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.item')),
            ],
        ),
        migrations.RemoveField(
            model_name='week1',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='week2',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='week3',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='week4',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='week5',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='week6',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='week7',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='week8',
            name='choice',
        ),
        migrations.AlterField(
            model_name='user_now',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_now',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.DeleteModel(
            name='week1',
        ),
        migrations.DeleteModel(
            name='week2',
        ),
        migrations.DeleteModel(
            name='week3',
        ),
        migrations.DeleteModel(
            name='week4',
        ),
        migrations.DeleteModel(
            name='week5',
        ),
        migrations.DeleteModel(
            name='week6',
        ),
        migrations.DeleteModel(
            name='week7',
        ),
        migrations.DeleteModel(
            name='week8',
        ),
    ]