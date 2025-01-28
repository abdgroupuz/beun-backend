from django.contrib import admin
from .models import Feedback, Comment

# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name']
    list_display_links = ['user']
    list_filter = ['user', 'created_at']
    search_fields = ['user__phone', 'text']
    readonly_fields = ['created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    list_display_links = ['user']
    list_filter = ['user', 'created_at']
    search_fields = ['user', 'text']
    readonly_fields = ['created_at', 'updated_at']
