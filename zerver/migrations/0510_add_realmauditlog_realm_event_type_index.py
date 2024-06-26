# Generated by Django 4.2.12 on 2024-04-17 10:33

from django.contrib.postgres.operations import AddIndexConcurrently
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("zerver", "0509_fix_emoji_metadata"),
    ]

    operations = [
        AddIndexConcurrently(
            model_name="realmauditlog",
            index=models.Index(
                fields=["realm", "event_type", "event_time"],
                name="zerver_realmauditlog_realm__event_type__event_time",
            ),
        ),
    ]
