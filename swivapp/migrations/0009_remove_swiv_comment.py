# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-10-17 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swivapp', '0008_swiv_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swiv',
            name='comment',
        ),
    ]