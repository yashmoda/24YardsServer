# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0002_auto_20170824_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertytable',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
