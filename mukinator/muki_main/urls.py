from django.urls import path
from . import views

app_name = 'mukinator'

urlpatterns = [
    path('main', views.main, name="main"),
    path('start/<int:user_id>', views.start, name="start"),
    path('reset', views.reset, name="reset"),
    path('sort_food/<int:user_id>', views.sort_food, name="sort_food"),
    path('go_borad', views.go_board, name="go_board"),
    path('result/<int:user_id>', views.result, name="result"),

]