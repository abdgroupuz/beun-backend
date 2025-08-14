from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Post, Certificate, Star, Result, Faq, Banner, SpecialOffer

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "get_short_body",
        "url",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "created_at"]
    search_fields = [
        "short_body_uz",
        "short_body_ru",
        "short_body_en",
        "body_uz",
        "body_ru",
        "body_en",
        "url",
    ]
    list_editable = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]

    def get_short_body(self, obj):
        return obj.short_body_ru[:20]

    get_short_body.short_description = _("Short Body")

    fieldsets = (
        (None, {"fields": ("image", "url", "is_active")}),
        (_("Uzbek"), {"fields": ("short_body_uz", "body_uz")}),
        (_("Russian"), {"fields": ("short_body_ru", "body_ru")}),
        (_("English"), {"fields": ("short_body_en", "body_en")}),
        (
            _("Date Information"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ["id", "get_body", "created_at", "updated_at"]
    search_fields = ["body_uz", "body_ru", "body_en"]
    readonly_fields = ["created_at", "updated_at"]

    def get_body(self, obj):
        return obj.body_ru[:20]

    get_body.short_description = _("Description")

    fieldsets = (
        (None, {"fields": ("image",)}),
        (_("Uzbek"), {"fields": ("body_uz",)}),
        (_("Russian"), {"fields": ("body_ru",)}),
        (_("English"), {"fields": ("body_en",)}),
        (
            _("Date Information"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name_ru", "is_active", "created_at", "updated_at"]
    search_fields = ["full_name_uz", "full_name_ru", "full_name_en"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (None, {"fields": ("image",)}),
        (_("Uzbek"), {"fields": ("full_name_uz",)}),
        (_("Russian"), {"fields": ("full_name_ru",)}),
        (_("English"), {"fields": ("full_name_en",)}),
        (
            _("Date Information"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (None, {"fields": ("image",)}),
        (
            _("Date Information"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ["id", "question_ru", "created_at", "updated_at"]
    search_fields = [
        "question_uz",
        "question_ru",
        "question_en",
        "answer_uz",
        "answer_ru",
        "answer_en",
    ]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (_("Uzbek"), {"fields": ("question_uz", "answer_uz")}),
        (_("Russian"), {"fields": ("question_ru", "answer_ru")}),
        (_("English"), {"fields": ("question_en", "answer_en")}),
        (
            _("Date Information"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["id", "url", "source", "is_active"]
    list_editable = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (None, {"fields": ("source", "source_md", "source_sm", "url", "is_active")}),
        (
            _("Date Information"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )

@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "photo", "end_date"]
    list_editable = ["end_date"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (None, {"fields": ("product", "photo", "end_date")}),
        (
            _("Date Information"),
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )