from django.db import models

class Food(models.Model):
    food_name = models.CharField(max_length=10, verbose_name="음식")
    meat = models.BooleanField(default=False, verbose_name="고기")
    sea = models.BooleanField(default=False, verbose_name="해산물")
    ulken = models.BooleanField(default=False, verbose_name="얼큰")
    raw = models.BooleanField(default=False, verbose_name="날 것")
    spicy = models.BooleanField(default=False, verbose_name="매움")
    
    def __str__(self):
        return self.food_name