# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-09 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_auto_20180307_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoseries',
            options={'verbose_name_plural': 'Video series'},
        ),
        migrations.AlterField(
            model_name='videofileupload',
            name='file_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='File name'),
        ),
    ]
