import uuid
from django.db import models


class Book(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    summary = models.TextField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    copies_quantity = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)
