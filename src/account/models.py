from profile import Profile

from django.db import models

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    def __str__(self):
        return self.email


class Customer(CustomUser):
    # address = models.ManyToManyField('Address')
    class Meta:
        proxy = True
    def save(self, *arg, **kwarg):
        if not self.id:
            self.is_superuser = False
            self.is_staff = False
        return super(Customer, self).save(*arg, **kwarg)



class Manager(CustomUser):
    class Meta:
        proxy = True
    def save(self, *arg, **kwarg):
        if not self.id:
            self.is_superuser = False
            self.is_staff = True
        return super(Manager, self).save(*arg, **kwarg)


class Admin(CustomUser):
    class Meta:
        proxy = True
    def save(self, *arg, **kwarg):
        if not self.id:
            self.is_superuser = True
        return super(Admin, self).save(*arg, **kwarg)


class Address(models.Model):
    city = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(max_length=300)
    main = models.BooleanField()
    postal_code = models.IntegerField()
    customer = models.ManyToManyField(Customer)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city

    class Meta:
        ordering = ['created_time']
