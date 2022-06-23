from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('start', views.start, name="start"),
    path('reset', views.reset, name="reset"),
    path('sort_food', views.sort_food, name="sort_food"),
    path('go_borad', views.go_board, name="go_board"),
]