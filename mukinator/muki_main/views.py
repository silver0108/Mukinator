from xmlrpc.client import boolean
from ast import keyword
from django.http import QueryDict
from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from django.db import reset_queries

from .models import Food

global qlist
qlist = {}

def home(request):
    foods = Food.objects.all()
    return render(request, 'muki_main/test.html', {'foods':foods})

def sort_food(request):
    
    if 'reset' in request.GET:
        sort_foods = Food.objects.all()
        qlist['sort_foods'] = sort_foods
        return redirect(home)
        
    if "sort_foods" in qlist:
        sort_foods = qlist['sort_foods']
    else:
        sort_foods = Food.objects.all()
        
    if 'value' in request.GET:
        value = request.GET['value']
        if value:
            sort_foods = sort_foods.filter(Q(meat=value))
            qlist['sort_foods'] = sort_foods
            return render(request, 'muki_main/test2.html', qlist)

    if 'hot' in request.GET:
        hot = request.GET['hot']
        if hot:
            sort_foods = sort_foods.filter(Q(spicy=hot))
            qlist['sort_foods'] = sort_foods
            return render(request, 'muki_main/test2.html', qlist)

    if 'sea' in request.GET:
        sea = request.GET['sea']
        if sea:
            sort_foods = sort_foods.filter(Q(sea=sea))
            qlist['sort_foods'] = sort_foods
            return render(request, 'muki_main/test2.html', qlist)
        
    if 'country' in request.GET:
        country = request.GET['country']
        if country:
            sort_foods = sort_foods.filter(Q(country=country))
            qlist['sort_foods'] = sort_foods
            return render(request, 'muki_main/test2.html', qlist)