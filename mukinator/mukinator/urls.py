from django import views
from django.contrib import admin
from django.urls import path, include
from community.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('muki_main.urls')),
    path('community/', include('community.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),
]
