# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tau', '0003_auto_20161207_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folder',
            old_name='full_path',
            new_name='path',
        ),
    ]