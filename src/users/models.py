from PIL import Image
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username


class Customer(CustomUser):
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


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    city = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
