from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Food(models.Model):
    food_name = models.CharField(max_length=10)
    meat = models.BooleanField(default=False)
    seafood = models.BooleanField(default=False)
    hot = models.BooleanField(default=False)
    country = models.CharField(max_length=2) 
    meat_type = models.CharField(max_length=2, null=True)
    meal_type = models.CharField(max_length=2, null=True)
    seafood_type = models.CharField(max_length=2, null=True)
    
    def __str__(self):
        return self.food_name

class Result(models.Model):
    food_name = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='result', null=True)
    
    def __str__(self):
        return self.food_name