# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-08 10:27


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0044_aboutpage_heading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpageinvolvement',
            name='image',
        ),
        migrations.RemoveField(
            model_name='aboutpageoffice',
            name='image',
        ),
        migrations.RemoveField(
            model_name='aboutpageservice',
            name='image',
        ),
        migrations.AddField(
            model_name='aboutpageinvolvement',
            name='svg',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutpageoffice',
            name='svg',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutpageservice',
            name='svg',
            field=models.TextField(null=True),
        ),
    ]
