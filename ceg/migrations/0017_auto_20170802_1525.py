# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceg', '0016_auto_20170802_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userproject',
            name='project',
        ),
        migrations.RemoveField(
            model_name='userproject',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='UserProject',
        ),
    ]
