# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-09-24 19:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swivapp', '0003_auto_20180924_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='swiv',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
