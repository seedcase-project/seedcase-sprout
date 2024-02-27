"""Metadata for a file."""
# Generated by Django 4.2.8 on 2024-02-27 13:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    """Metadata for a file."""

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sprout", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileMetaData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("original_file_name", models.TextField()),
                ("server_file_path", models.TextField()),
                ("file_extension", models.CharField(max_length=10)),
                ("file_size_bytes", models.BigIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "table_metadata",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sprout.tablemetadata",
                    ),
                ),
            ],
        ),
    ]
