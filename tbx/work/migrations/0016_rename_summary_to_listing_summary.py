# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 17:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("work", "0015_workpage_body_word_count"),
    ]

    operations = [
        migrations.RenameField(
            model_name="workpage", old_name="summary", new_name="listing_summary",
        ),
    ]
