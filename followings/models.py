import uuid
from django.db import models


class Following(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="followings_books"
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="followers"
    )
