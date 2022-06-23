from pyexpat import model
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
specific_number = ['4', '5', '6']

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
            
        specific_number.clear()
        for i in range(4,7):
            specific_number.append(str(i))
        
        return redirect(home)  
        
def sort_food(request):
    
    print(number, specific_number)

    if 'sort_foods' in qlist: #필터링 한 데이터 검사
        sort_foods = qlist['sort_foods'] #있으면 필터링 한 데이터 받아오기
    else:
        sort_foods = Food.objects.all() #없으면 Food 모델 다 가져오기
    
    keys = list(request.POST.keys())
    model_name = keys[1]
        
    if model_name in request.POST: #3번까지 질문하기
        value = request.POST[model_name]
        
        if model_name == "meat" :
            if value == "True":
                print("meat")
                specific_number.remove('5')
                specific_number.remove('6')
                print(specific_number)
            else:
                print("meal")
                specific_number.remove('4')
                specific_number.remove('6')
              
        elif model_name == "seafood":
            print("seafood")
            specific_number.remove('4')
            specific_number.remove('5')
            print(specific_number)
            
        if value:
            sort_foods = sort_foods.filter(**{model_name: value})
            qlist['sort_foods'] = sort_foods
            
            if len(number) != 0:
                integer = random.choice(number)
                number.remove(integer)
                test_str = 'test'+ integer + '.html'
            elif len(number) == 0 and len(specific_number) != 1:
                integer = random.choice(specific_number)
                specific_number.remove(integer)
                test_str = 'test'+ integer + '.html'
            elif len(specific_number) == 1:
                integer = random.choice(specific_number)
                test_str = 'test'+ integer + '.html'
            
            if len(sort_foods) == 1 or len(sort_foods) == 0:
                value = request.POST[model_name]
                if value:
                    sort_foods = sort_foods.filter(**{model_name: value})
                    qlist['sort_foods'] = sort_foods
                return render(request, 'muki_main/result.html', qlist)
            
            return render(request, 'muki_main/' + test_str , qlist)
    
def go_board(request):
    if 'go_board' in request.GET:
        return redirect(index)