# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 17:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blackBelt_app', '0002_friend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]