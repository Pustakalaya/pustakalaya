# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/creator', verbose_name='Creator image'),
        ),
    ]