# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-19 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("geo", "0010_auto_20170428_0927")]

    operations = [
        migrations.RemoveField(model_name="beacon", name="level"),
        migrations.DeleteModel(name="Beacon"),
    ]
