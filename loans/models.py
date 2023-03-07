from django.db import models
from .utils import default_devolution_date
import uuid


# Create your models here.
class Loan(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    devolution_date = models.DateField(default=default_devolution_date)
    is_returned = models.BooleanField(default=False)
    book_copy = models.ForeignKey(
        "books_copy.BookCopy", on_delete=models.CASCADE, related_name="loans"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="borrowed_books"
    )
