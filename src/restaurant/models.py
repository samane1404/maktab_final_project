from django.urls import reverse

from users.models import *


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
    manager = models.OneToOneField('users.Manager', primary_key=True, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_time']


class Food(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    category_food = models.ForeignKey('CategoryFood', on_delete=models.CASCADE, related_name='food_set')
    # category_meel = models.ManyToManyField('CategoryMeel')
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
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='menu_set')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='menu_sett')
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=1)
    image = models.ImageField(blank=True, null=True, upload_to='media', default='food.jpg')
    slug = models.SlugField(blank=True, null=True)
    category_meel = models.ManyToManyField(CategoryMeel, related_name='menu_settt')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.food)

    class Meta:
        ordering = ['created_time']

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("details_menu", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("remove_from_cart", kwargs={'slug': self.slug})
