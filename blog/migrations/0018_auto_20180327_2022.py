# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20180314_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='coach',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('birth', models.DateTimeField(max_length=10)),
                ('tel', models.CharField(max_length=11)),
                ('registerdate', models.DateField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=20)),
                ('itemcost', models.CharField(max_length=20)),
                ('itemtime', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user_now',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('weight', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='registerdata',
            new_name='registerdate',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='registerdata',
            new_name='registerdate',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='id',
        ),
        migrations.AddField(
            model_name='admin',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='coach',
            name='charge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.item'),
        ),
    ]