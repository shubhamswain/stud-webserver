# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 14:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tau.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_used', models.PositiveIntegerField(default=0, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=500)),
                ('file', models.FileField(upload_to=tau.models.upload_to)),
                ('drive', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tau.Drive')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('path', models.TextField(editable=False)),
                ('drive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tau.Drive')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tau.Folder')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tau.Folder'),
        ),
    ]
