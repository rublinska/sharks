# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20180322_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(null=True, upload_to=b'events_gallery/posters'),
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='image',
            field=models.ImageField(upload_to=b'events_gallery/gallery'),
        ),
    ]
