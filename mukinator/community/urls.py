from django.urls import path

from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('comment/modify/<int:comment_id>', views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
