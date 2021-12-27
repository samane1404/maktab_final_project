from django.db import models
from account.models import *
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
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
    description = models.TextField(max_length=300)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE,)
    category_food_id = models.ForeignKey('CategoryFood', on_delete=models.CASCADE,)
    manager_id = models.OneToOneField('account.Manager', primary_key=True, on_delete=models.CASCADE,)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['created_time']

class Food(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(max_length=300)
    image = models.ImageField()
    category_food_id = models.ForeignKey('CategoryFood', on_delete=models.CASCADE,)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['created_time']

class CategoryMeel(models.Model):
    name = models.ManyToManyField(Food)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['created_time']

class CategoryFood(models.Model):
    name = models.ManyToManyField(Food)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['created_time']

class Menu(models.Model):
    price = models.IntegerField()
    quantity = models.IntegerField()
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE,)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE,)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['created_time']

class OrderItem(models.Model):
    quantity = models.IntegerField()
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE,)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['created_time']

class Order(models.Model):
    customer_id = models.ForeignKey(Customer,  on_delete=models.CASCADE,)
    order_status_id = models.ForeignKey('OrderStatus',  on_delete=models.CASCADE,)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['created_time']

class OrderStatus(models.Model):
    status = models.CharField(max_length=10)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['created_time']