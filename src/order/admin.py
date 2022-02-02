from django.contrib import admin
from .models import *

# admin.site.register(Order)
@admin.register(Order)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered']
    list_display_links = ['user']
    list_filter = ['ordered_date']
    list_per_page = 10
    search_fields = ['ref_code']

# admin.site.register(OrderItem)
@admin.register(OrderItem)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']
    list_filter = ['user']
    list_per_page = 10
    search_fields = ['user']


admin.site.register(Address)