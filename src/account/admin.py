from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', ]
    # fields = ['email', 'username', 'age']
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('age',)}),
    #     )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #      (None, {'fields': ('age',)}),
    #       )


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Customer)
class CustomerProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['id']
    list_editable = ['email']
    search_fields = ['username', 'email']

    def get_queryset(self, request):
        return Customer.objects.filter(is_staff=False)


@admin.register(Manager)
class ManagerProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['username']
    list_editable = ['email']
    search_fields = ['username', 'email']

    def get_queryset(self, request):
        return Manager.objects.filter(is_staff=True, is_superuser=False)


@admin.register(Admin)
class AdminProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['username']
    list_editable = ['email']
    search_fields = ['username', 'email']

    def get_queryset(self, request):
        return Admin.objects.filter(is_superuser=True)


@admin.register(Address)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['city', 'main', 'postal_code']
    list_display_links = ['postal_code']
    list_filter = ['main', 'city']
    list_per_page = 10
    search_fields = ('postal_code', 'city')
    # readonly_fields = ['postal_code']
