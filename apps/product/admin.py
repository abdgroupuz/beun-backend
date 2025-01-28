from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Category, Image, Product, Tag

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "name_uz", "parent"]
    list_display_links = ["name_ru"]
    list_filter = ["name_ru", "name_uz", "parent__name_ru", "parent__name_uz"]
    readonly_fields = ["created_at", "updated_at"]

    search_fields = ["name_ru", "name_uz"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "image",
                    "parent",
                )
            },
        ),
        (
            _("Uzbek"),
            {
                "fields": ["name_uz"],
            },
        ),
        (
            _("Russian"),
            {
                "fields": ["name_ru"],
            },
        ),
        (
            "Date information",
            {
                "fields": ["created_at", "updated_at"],
                "classes": ["collapse"],
            },
        ),
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "name_uz"]
    list_display_links = ["name_ru"]
    list_filter = ["name_ru", "name_uz"]
    readonly_fields = ["created_at", "updated_at"]

    search_fields = ["name_ru", "name_uz"]

    fieldsets = (
        (
            _("Uzbek"),
            {
                "fields": ["name_uz"],
            },
        ),
        (
            _("Russian"),
            {
                "fields": ["name_ru"],
            },
        ),
        (
            "Date information",
            {
                "fields": ["created_at", "updated_at"],
                "classes": ["collapse"],
            },
        ),
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "name_uz"]
    list_display_links = ["name_ru"]
    list_filter = ["name_ru", "name_uz"]
    readonly_fields = ["created_at", "updated_at", "hit_count", "sold_count"]

    search_fields = ["name_ru", "name_uz"]

    fieldsets = (
        (
            _("Uzbek"),
            {
                "fields": ["name_uz", "short_description_uz", "description_uz"],
                "classes": ["collapse"],
            },
        ),
        (
            _("Russian"),
            {
                "fields": ["name_ru", "short_description_ru", "description_ru"],
                "classes": ["collapse"],
            },
        ),
        (
            None,
            {
                "fields": ["images", "category",("price", "discount", "discounted_price"), "count", "is_active", "spu", "tags"],
                "classes": ["wide", "extrapretty"],
            }
        ),
        (
            "Date information",
            {
                "fields": ["created_at", "updated_at", "hit_count", "sold_count",],
                "classes": ["collapse"],
            },
        ),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
