# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-11-14 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('swivapp', '0012_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='swiv',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='swiv',
            name='document',
            field=models.FileField(default=django.utils.timezone.now, upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='swiv',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]