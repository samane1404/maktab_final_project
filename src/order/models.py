from django.db import models
from users.models import *
from restaurant.models import *


class OrderItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='order_item_order')
    quantity = models.IntegerField(blank=True, null=True, default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.food.name} for {self.user.username}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_final_price(self):
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem, related_name='order_set')
    ordered_date = models.DateTimeField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    address = models.ForeignKey('Address', related_name='address_1', on_delete=models.SET_NULL, blank=True, null=True)
    ref_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user} {self.address}"

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total



class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}: {self.zip} {self.city} {self.address}"
