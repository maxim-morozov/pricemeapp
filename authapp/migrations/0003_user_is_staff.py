# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20171003_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='Staff'),
        ),
    ]