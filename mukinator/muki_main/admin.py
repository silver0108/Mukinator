from django.contrib import admin
from .models import Food, Result

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'meat', 'seafood', 'hot', 'country', 'meat_type', 'meal_type', 'seafood_type')

admin.site.register(Result)
