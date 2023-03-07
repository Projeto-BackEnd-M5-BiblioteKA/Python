import uuid
from django.db import models


class BookCopy(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    is_borrowed = models.BooleanField(default=False)
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )
