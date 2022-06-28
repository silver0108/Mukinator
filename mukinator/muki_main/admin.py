from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import Food, Result

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'meat', 'seafood', 'hot', 'country', 'meat_type', 'meal_type', 'seafood_type')

admin.site.register(Result)


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
    
admin.site.register(Session, SessionAdmin)
