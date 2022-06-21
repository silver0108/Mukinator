from django.shortcuts import render,redirect, get_object_or_404
from .models import Food

def home(request):
    blogs = Food.objects.all()
    return render(request,'home.html',{'blogs':blogs})
