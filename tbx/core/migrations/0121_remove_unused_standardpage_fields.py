# Generated by Django 2.1.5 on 2019-01-24 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("torchbox", "0120_remove_contactpage"),
    ]

    operations = [
        migrations.RemoveField(model_name="standardpageclient", name="image",),
        migrations.RemoveField(model_name="standardpageclient", name="link_document",),
        migrations.RemoveField(model_name="standardpageclient", name="link_page",),
        migrations.RemoveField(model_name="standardpageclient", name="page",),
        migrations.RemoveField(model_name="standardpagecontentblock", name="page",),
        migrations.RemoveField(
            model_name="standardpagerelatedlink", name="link_document",
        ),
        migrations.RemoveField(model_name="standardpagerelatedlink", name="link_page",),
        migrations.RemoveField(model_name="standardpagerelatedlink", name="page",),
        migrations.RemoveField(model_name="standardpage", name="credit",),
        migrations.RemoveField(model_name="standardpage", name="email",),
        migrations.RemoveField(model_name="standardpage", name="feed_image",),
        migrations.RemoveField(model_name="standardpage", name="heading",),
        migrations.RemoveField(model_name="standardpage", name="main_image",),
        migrations.RemoveField(model_name="standardpage", name="quote",),
        migrations.DeleteModel(name="StandardPageClient",),
        migrations.DeleteModel(name="StandardPageContentBlock",),
        migrations.DeleteModel(name="StandardPageRelatedLink",),
    ]
