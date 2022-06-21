from django.urls import path

from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('post/create/', views.post_create, name='post_create'),
]
