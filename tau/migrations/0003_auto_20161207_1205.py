# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tau', '0002_auto_20161207_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tau.Folder'),
        ),
    ]