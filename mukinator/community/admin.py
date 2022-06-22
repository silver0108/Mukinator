from django.contrib import admin
from .models import Post, Comment, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
