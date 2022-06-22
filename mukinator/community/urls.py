from django.urls import path

from .views import base_views, post_views, comment_views

app_name = 'community'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:post_id>/',
         base_views.detail, name='detail'),

    # post_views.py
    path('post/create/',
         post_views.post_create, name='post_create'),
    path('post/modify/<int:post_id>/',
         post_views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>',
         post_views.post_delete, name='post_delete'),

    # comment_views.py
    path('comment/create/<int:post_id>/',
         comment_views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>',
         comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>',
         comment_views.comment_delete, name='comment_delete'),
]
