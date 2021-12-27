from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Customer)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_display_links = ['email']
    list_filter = ['first_name', 'last_name']
    list_per_page = 10
    search_fields = ('national_code', 'email')
    readonly_fields = ['national_code', 'email']

@admin.register(Manager)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_display_links = ['email']
    list_filter = ['first_name', 'last_name']
    list_per_page = 10
    search_fields = ('national_code', 'email')
    readonly_fields = ['national_code', 'email']