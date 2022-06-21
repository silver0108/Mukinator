from django.contrib import admin
from django.urls import path, include
from muki_main.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
]
