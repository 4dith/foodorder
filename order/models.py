from django.db import models
from restaurants.models import Item, Restaurant
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name='orders')
    placed_at = models.DateTimeField()
    accepted = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} on {self.placed_at}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='orders')
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.item.name} (x{self.quantity})"