from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_superuser', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)


class CustomerAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_superuser', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(Customer, CustomerAdmin)


class ManagerAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_superuser', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(Manager, ManagerAdmin)


class AdminAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_superuser', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(Admin, AdminAdmin)


@admin.register(Profile)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['city', 'bio', 'address']
    list_display_links = ['city', 'bio']
    list_filter = ['city']
    list_per_page = 10
    search_fields = ['city']
