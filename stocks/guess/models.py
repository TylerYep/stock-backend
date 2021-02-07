import uuid

from django.db import models


class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    symbol = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=16)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Guess(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(default=uuid.uuid4)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    guessed_price = models.DecimalField(decimal_places=2, max_digits=16)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
