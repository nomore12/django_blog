from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")


admin.site.register(Post, PostAdmin)