# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-09-28 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import swivapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('swivapp', '0004_swiv_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swiv',
            name='content',
            field=models.CharField(max_length=140, validators=[swivapp.models.validate_content]),
        ),
    ]
