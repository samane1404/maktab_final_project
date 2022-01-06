from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Restaurant)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']

@admin.register(Branch)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name', 'main']
    list_display_links = ['name']
    list_filter = ['name', 'main', 'city']
    list_per_page = 10
    search_fields = ['name', 'city']

@admin.register(Food)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']

@admin.register(CategoryMeel)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']

@admin.register(CategoryFood)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_linmeks = ['name']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']

@admin.register(Menu)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['food_id', 'price', 'quantity']
    list_display_links = ['food_id']
    list_filter = ['food_id']
    list_per_page = 10
    search_fields = ['food_id']

@admin.register(OrderItem)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'status']
    list_display_links = ['status']
    list_filter = ['status']
    list_per_page = 10
    search_fields = ['status']

admin.site.register(Order)

from .models import Bar, BarTime
from django.contrib import admin

from django_jalali.admin.filters import JDateFieldListFilter

# you need import this for adding jalali calander widget
import django_jalali.admin as jadmin


class BarAdmin(admin.ModelAdmin):
    list_filter = (
        ('date', JDateFieldListFilter),
    )


admin.site.register(Bar, BarAdmin)


class BarTimeAdmin(admin.ModelAdmin):
    list_filter = (
        ('datetime', JDateFieldListFilter),
    )


admin.site.register(BarTime, BarTimeAdmin)