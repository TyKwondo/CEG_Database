# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 22:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceg', '0009_auto_20170724_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userproject',
            old_name='projects',
            new_name='project',
        ),
    ]
