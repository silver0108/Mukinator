from xmlrpc.client import boolean
from ast import keyword
from django.http import QueryDict
from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from django.db import reset_queries

from .models import Food
import random


qlist = {}
number = ['1', '2', '3']

def home(request):
    foods = Food.objects.all()
    print(number)
    print(reset_number)
    return render(request, 'muki_main/home.html', {'foods':foods})

def start(request):
    if 'start' in request.GET:
        integer = random.choice(number)
        number.remove(integer)
        test_str = 'test'+ integer + '.html'
        
        sort_foods = Food.objects.all()
        qlist['sort_foods'] = sort_foods
        
        return render(request, 'muki_main/' + test_str , qlist)
    
def sort_food(request):
    global number
    
    if "sort_foods" in qlist: #필터링 한 데이터 검사
        sort_foods = qlist['sort_foods'] #있으면 필터링 한 데이터 받아오기
    else:
        sort_foods = Food.objects.all() #없으면 Food 모델 다 가져오기
        
    if 'reset' in request.GET: #초기화
        sort_foods = Food.objects.all()
        qlist['sort_foods'] = sort_foods
        number.clear()
        for i in range(1,4):
            number.append(str(i))
        
        return redirect(home)    
    
    #고기
    if 'meat' in request.GET and len(number) > 0: #3번까지 질문하기
        meat = request.GET['meat']
        if meat:
            sort_foods = sort_foods.filter(Q(meat=meat))
            qlist['sort_foods'] = sort_foods
            
            integer = random.choice(number)
        
            if len(number) != 0:
                number.remove(integer)
            test_str = 'test'+ integer + '.html'
            
            return render(request, 'muki_main/' + test_str , qlist)
        
    elif 'meat' in request.GET and len(number) == 0:
        meat = request.GET['meat']
        if meat:
            sort_foods = sort_foods.filter(Q(meat=meat))
            qlist['sort_foods'] = sort_foods
        return render(request, 'muki_main/result.html', qlist)
    
    #맵기
    if 'hot' in request.GET and len(number) > 0:
        hot = request.GET['hot']
        if hot:
            sort_foods = sort_foods.filter(Q(spicy=hot))
            qlist['sort_foods'] = sort_foods
            
            integer = random.choice(number)
            
            if len(number) != 0:
                number.remove(integer)
            test_str = 'test'+ integer + '.html'
            
            return render(request, 'muki_main/' + test_str, qlist)
        
    elif 'hot' in request.GET and len(number) == 0:
        hot = request.GET['hot']
        if hot:
            sort_foods = sort_foods.filter(Q(spicy=hot))
            qlist['sort_foods'] = sort_foods
        return render(request, 'muki_main/result.html', qlist)
    
    #해산물
    if 'sea' in request.GET and len(number) > 0:
        sea = request.GET['sea']
        if sea:
            sort_foods = sort_foods.filter(Q(sea=sea))
            qlist['sort_foods'] = sort_foods
            
            integer = random.choice(number)
            
            if len(number) != 0:
                number.remove(integer)
            test_str = 'test'+ integer + '.html'
            
            return render(request, 'muki_main/' + test_str, qlist)
        
    elif 'sea' in request.GET and len(number) == 0:
        sea = request.GET['sea']
        if sea:
            sort_foods = sort_foods.filter(Q(sea=sea))
            qlist['sort_foods'] = sort_foods
        return render(request, 'muki_main/result.html', qlist)
    
    #국가별    
    if 'country' in request.GET and len(number) > 0:
        country = request.GET['country']
        if country:
            sort_foods = sort_foods.filter(Q(country=country))
            qlist['sort_foods'] = sort_foods
            
            integer = random.choice(number)
            
            if len(number) > 0:
                number.remove(integer)
            test_str = 'test'+ integer + '.html'
            
            return render(request, 'muki_main/' + test_str, qlist)
        
    elif 'country' in request.GET and len(number) == 0:
        country = request.GET['country']
        if country:
            sort_foods = sort_foods.filter(Q(country=country))
            qlist['sort_foods'] = sort_foods
        return render(request, 'muki_main/result.html', qlist)