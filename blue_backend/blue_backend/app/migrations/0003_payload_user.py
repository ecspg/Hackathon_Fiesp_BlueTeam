# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 07:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_payload_neutral'),
    ]

    operations = [
        migrations.AddField(
            model_name='payload',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usu\xe1rio'),
        ),
    ]
