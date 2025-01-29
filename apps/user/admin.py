from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy

from .models import User, SMS, Address

# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(TokenProxy)


class SMSAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_module_permission(self, request):
        return request.user.is_superuser


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address']
    list_display_links = ['user']
    list_filter = ['user']
    search_fields = ['user__phone', 'address']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone','get_full_name', 'is_active', 'is_staff', 'is_superuser']
    list_display_links = ['phone']
    list_filter = ['is_active', 'is_superuser']
    search_fields = ['phone',]

admin.site.register(SMS, SMSAdmin)
