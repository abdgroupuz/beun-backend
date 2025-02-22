from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Category, Image, Product, Tag

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "name_uz", "name_en", "parent"]
    list_display_links = ["name_ru"]
    list_filter = [
        "name_ru",
        "name_uz",
        "name_en",
        "parent__name_ru",
        "parent__name_uz",
        "parent__name_en",
    ]
    readonly_fields = ["created_at", "updated_at"]

    search_fields = ["name_ru", "name_uz", "name_en"]

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
            _("English"),
            {
                "fields": ["name_en"],
            },
        ),
        (
            _("Date information"),
            {
                "fields": ["created_at", "updated_at"],
                "classes": ["collapse"],
            },
        ),
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "name_uz", "name_en"]
    list_display_links = ["name_ru"]
    list_filter = ["name_ru", "name_uz", "name_en"]
    readonly_fields = ["created_at", "updated_at"]

    search_fields = ["name_ru", "name_uz", "name_en"]

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
            _("English"),
            {
                "fields": ["name_en"],
            },
        ),
        (
            _("Date information"),
            {
                "fields": ["created_at", "updated_at"],
                "classes": ["collapse"],
            },
        ),
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name_ru",
        "name_uz",
        "name_en",
        "category",
        "price",
        "discount",
        "discounted_price",
        "count",
        "is_active",
    ]
    list_display_links = ["name_ru"]
    list_filter = [
        "name_ru",
        "name_uz",
        "name_en",
        "category__name_ru",
        "category__name_uz",
        "category__name_en",
        "price",
        "discount",
        "discounted_price",
        "count",
        "is_active",
    ]
    readonly_fields = ["created_at", "updated_at", "hit_count", "sold_count"]

    search_fields = [
        "name_ru",
        "name_uz",
        "name_en",
        "short_description_ru",
        "short_description_uz",
        "short_description_en",
        "description_ru",
        "description_uz",
        "description_en",
    ]

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
            _("English"),
            {
                "fields": ["name_en", "short_description_en", "description_en"],
                "classes": ["collapse"],
            },
        ),
        (
            None,
            {
                "fields": [
                    "images",
                    "category",
                    "price",
                    ("discount", "discounted_price"),
                    "count",
                    "is_active",
                    "spu",
                    "tags",
                ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Date information"),
            {
                "fields": [
                    "created_at",
                    "updated_at",
                    "hit_count",
                    "sold_count",
                ],
                "classes": ["collapse"],
            },
        ),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
