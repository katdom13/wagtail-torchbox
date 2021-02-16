# Generated by Django 2.2.17 on 2020-11-11 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0015_update_streamblock_templates"),
    ]

    operations = [
        migrations.RemoveField(model_name="personpage", name="address_1"),
        migrations.RemoveField(model_name="personpage", name="address_2"),
        migrations.RemoveField(model_name="personpage", name="alt_short_intro"),
        migrations.RemoveField(model_name="personpage", name="city"),
        migrations.RemoveField(model_name="personpage", name="country"),
        migrations.RemoveField(model_name="personpage", name="feed_image"),
        migrations.RemoveField(model_name="personpage", name="first_name"),
        migrations.RemoveField(model_name="personpage", name="last_name"),
        migrations.RemoveField(model_name="personpage", name="post_code"),
        migrations.RemoveField(model_name="personpage", name="short_biography"),
        migrations.RemoveField(model_name="personpage", name="short_intro"),
        migrations.RemoveField(model_name="personpage", name="email"),
        migrations.RemoveField(model_name="personpage", name="telephone"),
        migrations.DeleteModel(name="PersonPageRelatedLink"),
    ]
