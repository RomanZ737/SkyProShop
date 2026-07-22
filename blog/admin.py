from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (id, 'title', 'preview', 'created_at', 'is_active', 'views_number')
    list_filter = ('created_at', 'is_active', 'views_number')
    search_fields = ('title', 'content',)
