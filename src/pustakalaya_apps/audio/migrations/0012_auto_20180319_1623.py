# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-19 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0011_auto_20180313_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='audio.AudioSeries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='audio_types',
            field=models.ManyToManyField(blank=True, to='audio.AudioType', verbose_name='Audio types'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='collections',
            field=models.ManyToManyField(blank=True, to='collection.Collection', verbose_name='Add this audio to these collection'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='education_levels',
            field=models.ManyToManyField(blank=True, to='core.EducationLevel', verbose_name='Education Levels'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='core.Keyword', verbose_name='Select list of keywords'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='languages',
            field=models.ManyToManyField(blank=True, to='core.Language', verbose_name='Languages'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='sponsors',
            field=models.ManyToManyField(blank=True, to='core.Sponsor', verbose_name='Sponsor'),
        ),
    ]