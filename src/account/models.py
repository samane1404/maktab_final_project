from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    SEX = (("male", "male"),("female", "famale"))
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    national_code = models.CharField(max_length=10)
    birthday_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    sex = models.CharField(max_length=10, choices=SEX)
    email = models.EmailField(unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    address = models.ManyToManyField('Address')
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    class Meta:
        ordering = ['created_time']


class Manager(models.Model):
    SEX = (("male", "male"),("female", "famale"))
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    national_code = models.CharField(max_length=10)
    birthday_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    sex = models.CharField(max_length=10, choices=SEX)
    email = models.EmailField(unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    address = models.ManyToManyField('Address')
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)   
    class Meta:
        ordering = ['created_time']

class Address(models.Model):
    city = models.CharField(max_length=30, blank=True, null=True)
    main_address = models.TextField(max_length=300)
    postal_code = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.city 
    class Meta:
        ordering = ['created_time']







# class Customer(Register):
#     class Meta:
#         abstract = True
#         ordering = ['created_tim']
#     def __str__(self):
#         return '{} {}'.format(self.first_name, self.last_name)

# class Manager(Register):
#     class Meta:
#         abstract = True
#         ordering = ['created_tim']
#     def __str__(self):
#         return '{} {}'.format(self.first_name, self.last_name)

