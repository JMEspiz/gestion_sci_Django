# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 19:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumen', '0004_auto_20160310_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumen',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AddField(
            model_name='resumen',
            name='hora',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
