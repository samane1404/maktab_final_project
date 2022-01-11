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
    list_display = ['food', 'price', 'quantity']
    list_display_links = ['food']
    list_filter = ['food']
    list_per_page = 10
    search_fields = ['food']

@admin.register(OrderItem)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['order']
    list_display_links = ['order']
    list_filter = ['order']
    list_per_page = 10
    search_fields = ['order']

@admin.register(Order)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status']
    list_display_links = ['status']
    list_filter = ['status']
    list_per_page = 10
    search_fields = ['status']

