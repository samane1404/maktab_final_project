from django.db import models
from account.models import *
from PIL import Image
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


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
    address = models.TextField(max_length=300, blank=True, null=True)
    main = models.BooleanField(blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='branch_set')
    category_food = models.ForeignKey('CategoryFood', on_delete=models.CASCADE, related_name='branch_set1')
    manager = models.OneToOneField('account.Manager', primary_key=True, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_time']


class Food(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    category_food = models.ForeignKey('CategoryFood', on_delete=models.CASCADE, related_name='food_set')
    category_meel = models.ManyToManyField('CategoryMeel')
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
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='menu_set')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='menu_sett')
    image = models.ImageField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.food)

    class Meta:
        ordering = ['created_time']


class Order(models.Model):
    STATUS = (("order", "order"), ("registration", "registration"), ("sent", "sent"), ("delivery", "delivery"))
    status = models.CharField(max_length=20, choices=STATUS, default='order')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.status)

    @property
    def get_cart_total(self):
        orderitems = self.order_set.all()
        total = sum([menu.get_total for menu in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.order_set.all()
        total = sum([menu.quantity for menu in orderitems])
        return total

    class Meta:
        ordering = ['created_time']


class OrderItem(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_set', blank=True, null=True)
    menu = models.ManyToManyField(Menu, related_name='orderitem_set')
    created_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        ordering = ['created_time']

    @property
    def get_total(self):
        total = self.menu.price * self.quantity
        return total


def save(self, *args, **kwargs):
    super().save()

    img = Image.open(self.avatar.path)

    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path)

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')