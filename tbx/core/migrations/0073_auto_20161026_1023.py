# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-26 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0072_auto_20161026_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsettings',
            name='contact_email',
            field=models.EmailField(help_text='Email address', max_length=255),
        ),
    ]
