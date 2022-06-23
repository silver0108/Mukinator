from xmlrpc.client import boolean
from ast import keyword
from django.http import QueryDict
from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from django.db import reset_queries

from .models import Food
from community.views.base_views import index
import random


qlist = {}
number = ['1', '2', '3']

def home(request):
    foods = Food.objects.all()
    return render(request, 'muki_main/home.html', {'foods':foods})

def start(request):
    
    if 'start' in request.POST:
        integer = random.choice(number)
        number.remove(integer)
        test_str = 'test'+ integer + '.html'
        
        sort_foods = Food.objects.all()
        qlist['sort_foods'] = sort_foods
        
        return render(request, 'muki_main/' + test_str , qlist)
    
def reset(request):
    
    if 'reset' in request.GET: #초기화
        sort_foods = Food.objects.all()
        qlist['sort_foods'] = sort_foods
        number.clear()
        for i in range(1,4):
            number.append(str(i))
        
        return redirect(home)  
        
def sort_food(request):
    global number
    
    
    if 'sort_foods' in qlist: #필터링 한 데이터 검사
        sort_foods = qlist['sort_foods'] #있으면 필터링 한 데이터 받아오기
    else:
        sort_foods = Food.objects.all() #없으면 Food 모델 다 가져오기
    
    if request.method == 'POST':
        keys = list(request.POST.keys())
        model_name = keys[1]
        
        if model_name in request.POST and len(number) > 0: #3번까지 질문하기
            value = request.POST[model_name]
           
            if value:
                sort_foods = sort_foods.filter(**{model_name: value})
                qlist['sort_foods'] = sort_foods
                
                integer = random.choice(number)
            
                if len(number) != 0:
                    number.remove(integer)
                test_str = 'test'+ integer + '.html'
                
                return render(request, 'muki_main/' + test_str , qlist)
            
        elif model_name in request.POST and len(number) == 0:
            value = request.POST[model_name]
            if value:
                sort_foods = sort_foods.filter(**{model_name: value})
                qlist['sort_foods'] = sort_foods
            return render(request, 'muki_main/result.html', qlist)
        
    
def go_board(request):
    if 'go_board' in request.GET:
        return redirect(index)