from django.db import models
from django.utils import timezone

class Order(models.Model):
    book_id = models.IntegerField()
    total_price = models.FloatField()
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} - Book {self.book_id}"
