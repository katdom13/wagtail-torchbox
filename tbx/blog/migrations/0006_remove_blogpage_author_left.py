# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-21 12:10
from __future__ import unicode_literals

import json

from django.db import migrations


def migrate_author_left_into_author_snippet(apps, schema_editor):
    BlogPage = apps.get_model("blog.BlogPage")
    BlogPageAuthor = apps.get_model("blog.BlogPageAuthor")
    Author = apps.get_model("people.Author")

    # Update model
    for blog_page in BlogPage.objects.exclude(author_left=""):
        author, created = Author.objects.get_or_create(name=blog_page.author_left)
        blog_page.related_author.add(BlogPageAuthor(author=author))
        blog_page.related_author.commit()

    # Update revisions
    PageRevision = apps.get_model("wagtailcore.PageRevision")
    ContentType = apps.get_model("contenttypes.ContentType")
    blog_page_content_type = ContentType.objects.get(app_label="blog", model="blogpage")

    for revision in PageRevision.objects.filter(
        page__content_type=blog_page_content_type
    ):
        content = json.loads(revision.content_json)
        author_left = content.get("author_left", "")

        if author_left:
            author, created = Author.objects.get_or_create(name=author_left)

            if not "related_author" in content:
                content["related_author"] = []

            # Make sure this author isn't already attached to this blog post
            # (this is the case for blog post with id=1134)
            if content["related_author"]:
                current_author_ids = set(a["author"] for a in content["related_author"])
                if author.id in current_author_ids:
                    continue

            content["related_author"].append(
                {"pk": None, "page": revision.page_id, "author": author.id}
            )

            revision.content_json = json.dumps(content)
            revision.save()


def nooperation(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_remove_blogpageauthor_author_person_page"),
    ]

    operations = [
        migrations.RunPython(migrate_author_left_into_author_snippet, nooperation),
        migrations.RemoveField(model_name="blogpage", name="author_left",),
    ]
