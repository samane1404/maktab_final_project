from django.db import models
from account.models import *


class Restaurant(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_time']


class Branch(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(max_length=300)
    main = models.BooleanField()
    description = models.TextField(max_length=300)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category_food_id = models.ForeignKey('CategoryFood', on_delete=models.CASCADE)
    manager_id = models.OneToOneField('account.Manager', primary_key=True, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_time']


class Food(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(max_length=300)
    image = models.ImageField()
    category_food_id = models.ForeignKey('CategoryFood', on_delete=models.CASCADE)
    category_meel_id = models.ManyToManyField('CategoryMeel')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_time']


class CategoryMeel(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_time']


class CategoryFood(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_time']


class Menu(models.Model):
    price = models.IntegerField()
    quantity = models.IntegerField()
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.food_id)

    class Meta:
        ordering = ['created_time']


class OrderItem(models.Model):
    STATUS = (("order", "order"), ("registration", "registration"), ("sent", "sent"), ("delivery", "delivery"))
    quantity = models.IntegerField()
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='order')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['created_time']


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_id)

    class Meta:
        ordering = ['created_time']
