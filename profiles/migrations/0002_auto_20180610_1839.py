# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='subject',
        ),
    ]
