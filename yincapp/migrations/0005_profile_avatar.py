# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-01 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yincapp', '0004_auto_20170629_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
