from django.shortcuts import get_object_or_404, render,redirect
from .models import Food, Result
from community.views.base_views import index
import random
from django.contrib.auth import get_user_model
User = get_user_model()

qlist = {}
number = ['1', '2', '3']
specific_number = ['4', '5', '6']
qnum = 1
check = False

def main(request):
    global qnum, check

    qnum = 1
    check = False
    
    number.clear()
    for i in range(1,4):
        number.append(str(i))
        
    specific_number.clear()
    for i in range(4,7):
        specific_number.append(str(i))
        
    foods = Food.objects.all()
    sort_foods = Food.objects.none()
    
    context = {
        'foods':foods,
        'sort_foods':sort_foods,
        'qnum':qnum,
        'check':check
    }
    return render(request, 'muki_main/front.html', context)

def start(request):
    global qnum, check
    qnum += 1
    check = False
    if 'start' in request.POST:
        number.clear()
        for i in range(1,4):
            number.append(str(i))
        
        specific_number.clear()
        for i in range(4,7):
            specific_number.append(str(i))
            
        integer = random.choice(number)
        number.remove(integer)
        
        sort_foods = Food.objects.all()
        qlist['sort_foods'] = sort_foods
        
        context = {
            'sort_foods':qlist,
            'integer':integer,
            'qnum':qnum,
            'check':check
        }
        return render(request, 'muki_main/front.html', context)
        
def reset(request):
    global qnum, check
    check = False
    if 'reset' in request.GET: #초기화
        sort_foods = Food.objects.all()
        qlist['sort_foods'] = sort_foods
        
        number.clear()
        for i in range(1,4):
            number.append(str(i))
            
        specific_number.clear()
        for i in range(4,7):
            specific_number.append(str(i))
        
        qnum = 1
        return redirect('mukinator:main')  
        
def sort_food(request):    
    global qnum, check
    qnum += 1
    
    check = False
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
                specific_number.remove('5')
                specific_number.remove('6')
            else:
                specific_number.remove('4')
                specific_number.remove('6')
              
        elif model_name == "seafood":
            specific_number.remove('4')
            specific_number.remove('5')
            
        if value:
            sort_foods = sort_foods.filter(**{model_name: value})
            qlist['sort_foods'] = sort_foods
            
            if len(number) != 0: #리스트가 0이 아니면
                integer = random.choice(number) #리스트에서 하나 고르고
                number.remove(integer) #고른 숫자 삭제
                
            elif len(number) == 0 and len(specific_number) != 1: #리스트가 0이고 세부 질문 리스트가 1이 아니면
                integer = random.choice(specific_number) #위와 같은 동작
                specific_number.remove(integer)
                
            elif len(specific_number) == 1: #세부 질문 리스트가 1이면
                integer = random.choice(specific_number) #랜덤으로 숫자 고르기
            
            if len(sort_foods) == 1 or len(sort_foods) == 0:#음식이 1개 남거나 없다면
                value = request.POST[model_name]
                if value:
                    sort_foods = sort_foods.filter(**{model_name: value}) #필터링
                    qlist['sort_foods'] = sort_foods
                    
                    #최근 추천 음식 저장
                    if request.user.is_authenticated: #로그인 되어 있으면 user 저장
                        if len(sort_foods) > 0:
                            Result(
                                food_name = list(sort_foods)[0],
                                user = request.user
                            ).save()
                    else: #로그인 안되어 있으면 food_name 만 저장
                        if len(sort_foods) > 0:
                            Result(
                                food_name = list(sort_foods)[0],
                            ).save()
                            
                    if request.user.is_authenticated: #로그인 되어 있으면 user.id 가져오기
                        person = get_object_or_404(User, pk = request.user.id)
                    else: #아니면 None으로 넘기기
                        person = None
                        
                    #pk순으로 정렬 후 food_name 중복 제거
                    results = Result.objects.filter(user=request.user.id).order_by("-pk").values("food_name").distinct()
                    results = results[:5]
                    
                    check = True
                    context = {
                        'sort_foods':qlist,
                        'person':person,
                        'results':results,
                        'check':check,
                        'qnum':qnum
                    }                   
                return render(request, 'muki_main/front.html', context) #결과창으로
            
            context = {
                'sort_foods':qlist,
                'integer':integer,
                'qnum':qnum,
                'check':check
            }       
            return render(request, 'muki_main/front.html' , context)
    
def go_board(request):
    
    number.clear()
    for i in range(1,4):
        number.append(str(i))
            
    specific_number.clear()
    for i in range(4,7):
        specific_number.append(str(i))
    
    if 'go_board' in request.GET:
        return redirect(index)