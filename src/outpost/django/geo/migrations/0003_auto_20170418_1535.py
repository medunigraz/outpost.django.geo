# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_floor_outline'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='origin',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='door',
            name='origin',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='floor',
            name='origin',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='origin',
            field=models.IntegerField(null=True),
        ),
    ]
