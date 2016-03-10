# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumen', '0002_auto_20160310_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumen',
            old_name='texto_resuemen',
            new_name='texto_resumen',
        ),
        migrations.RemoveField(
            model_name='resumen',
            name='url_resumen',
        ),
        migrations.AddField(
            model_name='resumen',
            name='url_resumen',
            field=models.ManyToManyField(blank=True, default=b'', to='resumen.UrlResumen'),
        ),
    ]