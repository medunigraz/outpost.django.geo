# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("geo", "0014_auto_20170804_1711")]

    operations = [
        migrations.AlterModelOptions(
            name="edgecategory", options={"ordering": ("multiplicator", "addition")}
        ),
        migrations.RenameField(
            model_name="edgecategory", old_name="weight", new_name="multiplicator"
        ),
        migrations.AddField(
            model_name="edgecategory",
            name="addition",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]