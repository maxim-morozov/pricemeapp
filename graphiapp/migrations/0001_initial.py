# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('WeddingBook', 'Wedding Book'), ('YoungBook', 'Young Book'), ('GoBook', 'GoBook'), ('DigitalMattedAlbum', 'The Digital Matted Album'), ('PrimoBook', 'Primo Book')], max_length=120)),
            ],
            options={
                'verbose_name': 'album_type',
                'verbose_name_plural': 'album_types',
            },
        ),
    ]