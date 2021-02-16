# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-16 12:41
from __future__ import unicode_literals

import json
from django.db import migrations


TAGS_TO_SERVICES = {
    "planet-drupal": [],
    "custom-web-apps": ["digital-products"],
    "drupal": [],
    "paid_search": ["digital-marketing", "ppc"],
    "news": [],
    "wagtail": ["wagtail"],
    "design": [],
    "tech": ["digital-products"],
    "digital_marketing": ["digital-marketing"],
    "analytics": ["digital-marketing", "data"],
    "web-development": ["digital-products"],
    "social-media": ["digital-marketing", "social-media"],
    "seo": ["digital-marketing", "seo"],
}


def map_tags_to_related_services(apps, schema_editor):
    WorkPage = apps.get_model("work.WorkPage")
    Tag = apps.get_model("torchbox.Tag")
    Service = apps.get_model("taxonomy.Service")

    TAG_ID_TO_SERVICES = {}
    for tag_slug, service_slugs in TAGS_TO_SERVICES.items():
        try:
            TAG_ID_TO_SERVICES[Tag.objects.get(slug=tag_slug).id]: [
                Service.objects.get(slug=service_slug) for service_slug in service_slugs
            ]
        except Tag.DoesNotExist:
            continue

    for case_study in WorkPage.objects.iterator():
        for tag_id in case_study.tags.values_list("tag_id", flat=True):
            for service in TAG_ID_TO_SERVICES[tag_id]:
                case_study.related_services.add(service)

        case_study.related_services.commit()

        if case_study.live and case_study.has_unpublished_changes:
            revision = case_study.revisions.order_by("created_at").last()
            content = json.loads(revision.content_json)
            services = []

            for tag in content["tags"]:
                services.extend(TAG_ID_TO_SERVICES[tag["tag"]])

            content["related_services"] = list(set(service.id for service in services))

            revision.content_json = json.dumps(content)
            revision.save()


def nooperation(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("work", "0013_workpage_related_services"),
        ("torchbox", "0110_rename_blogpagetaglist_to_tag"),
        ("taxonomy", "0002_initial_services"),
    ]

    operations = [
        migrations.RunPython(map_tags_to_related_services, nooperation),
    ]
