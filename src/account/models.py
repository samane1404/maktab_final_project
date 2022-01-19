from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username


class Customer(CustomUser):
    # device = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        proxy = True
    def save(self, *arg, **kwarg):
        if not self.id:
            self.is_superuser = False
            self.is_staff = False
        return super(Customer, self).save(*arg, **kwarg)
    # def __str__(self):
    #     if self.username:
    #         name = self.username
    #     else:
    #         name = self.device
    #     return(name)


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
    address = models.TextField(max_length=300, blank=True, null=True)
    main = models.BooleanField(blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    customer = models.ManyToManyField(Customer, blank=True, null=True, related_name='x')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)

    class Meta:
        ordering = ['created_time']

    def save(self, *args, **kwargs):
        super().save()



class Profile(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

