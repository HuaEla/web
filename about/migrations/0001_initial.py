# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='superProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('aboutBlog', models.TextField(blank=True)),
                ('aboutAuthor', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('mail', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
