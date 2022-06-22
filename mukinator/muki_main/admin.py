from django.contrib import admin
from .models import Food

admin.site.register(Food)

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['meat', 'sea', 'spicy', 'country']
    