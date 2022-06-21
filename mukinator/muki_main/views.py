from re import template
from django.shortcuts import render,redirect, get_object_or_404
from .models import Food


def home(request):
    foods = Food.objects.all()
    return render(request, 'test.html', {'foods':foods})
