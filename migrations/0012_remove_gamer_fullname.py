# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 12:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamefy', '0011_auto_20171115_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamer',
            name='fullname',
        ),
    ]
