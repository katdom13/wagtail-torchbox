# Generated by Django 2.1.5 on 2019-03-25 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0027_create_subservice_page"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="servicepageclientlogo", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="servicepagefeaturedblogpost", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="servicepagefeaturedcasestudy", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="servicepagekeypoint", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="servicepageprocess", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="servicepagetestimonial", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="servicepageusaclientlogo", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="subservicepageclientlogo", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="subservicepagefeaturedblogpost", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="subservicepagefeaturedcasestudy",
            options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="subservicepagekeypoint", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="subservicepageprocess", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="subservicepagetestimonial", options={"ordering": ["sort_order"]},
        ),
        migrations.AlterModelOptions(
            name="subservicepageusaclientlogo", options={"ordering": ["sort_order"]},
        ),
    ]
