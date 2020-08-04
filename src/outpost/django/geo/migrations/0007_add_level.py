# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-26 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("geo", "0006_background")]

    operations = [
        migrations.AddField(
            model_name="beacon",
            name="level",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="geo.Level"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="node",
            name="level",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="geo.Level"
            ),
            preserve_default=False,
        ),
    ]