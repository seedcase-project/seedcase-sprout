from django.conf import settings
from django.db import models

from app.date_type import TYPE_CHOICES


class TableMetadata(models.Model):
    name = models.CharField(max_length=128)
    original_file_name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   on_delete=models.PROTECT, related_name='creator')
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                    on_delete=models.PROTECT, related_name='modifier')


class ColumnMetadata(models.Model):
    table_metadata = models.ForeignKey(TableMetadata, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    data_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    allow_missing_value = models.BooleanField()
    allow_duplicate_value = models.BooleanField()
