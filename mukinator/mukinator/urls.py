from django import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('muki_main.urls')),
    path('community/', include('community.urls')),
]
