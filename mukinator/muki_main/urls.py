from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sort_food', views.sort_food, name="sort_food"),
]