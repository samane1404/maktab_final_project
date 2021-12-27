from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Branch)
admin.site.register(Food)
admin.site.register(CategoryMeel)
admin.site.register(CategoryFood)
admin.site.register(Menu)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(OrderStatus)