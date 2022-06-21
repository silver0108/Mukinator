from django.db import models

class Food(models.Model):
    food_name = models.CharField(max_length=10)
    main = models.CharField(max_length=5)
    soup = models.CharField(max_length=5)
    meat = models.CharField(max_length=5)
    spicy = models.CharField(max_length=5)
    oily = models.CharField(max_length=5)