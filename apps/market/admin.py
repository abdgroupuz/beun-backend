from django.contrib import admin
from .models import Cart, Item, Order

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']
    search_fields = ['user__phone']
    readonly_fields = ['user', 'products']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'created_at', 'updated_at']
    list_display_links = ['user']
    list_filter = ['user', 'products', 'status']
    search_fields = ['user__phone', 'products__product__name']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Item)
