from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

User = settings.AUTH_USER_MODEL


class CustomUser(AbstractUser):
    # id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username


class Customer(CustomUser):
    class Meta:
        proxy = True


class Manager(CustomUser):
    class Meta:
        proxy = True


class Admin(CustomUser):
    class Meta:
        proxy = True

    # def save(self, *arg, **kwarg):
    #     if self.id:
    #         pass
    #     else:
    #         self.is_superuser = False
    #         self.is_staff = False
    #     return super(Customer, self).save(*arg, **kwarg)

    # def save(self, *arg, **kwarg):
    #     if self.id:
    #         pass
    #     else:
    #         self.is_superuser = False
    #         self.is_staff = True
    #     return super(Manager, self).save(*arg, **kwarg)

    # def save(self, *arg, **kwarg):
    #     if self.id:
    #         pass
    #     else:
    #         self.is_superuser = True
    #     return super(Admin, self).save(*arg, **kwarg)


class Address(models.Model):
    city = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(max_length=300)
    main = models.BooleanField()
    postal_code = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    class Meta:
        ordering = ['created_time']
