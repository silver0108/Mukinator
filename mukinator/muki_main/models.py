from ssl import VerifyMode
from tabnanny import verbose
from django.db import models
from django.forms import CharField

class Food(models.Model):
    food_name = models.CharField(max_length=10, verbose_name="음식")
    meat = models.BooleanField(default=False, verbose_name="고기")
    sea = models.BooleanField(default=False, verbose_name="해산물")
    hot = models.BooleanField(default=False, verbose_name="매움")
    country = models.CharField(max_length=2, verbose_name="국가") 
    
    
    def __str__(self):
        return self.food_name
