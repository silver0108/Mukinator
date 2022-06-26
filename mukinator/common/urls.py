from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('mypage/<int:pk>/', views.mypage, name='mypage'),
    path('update/', views.update, name='update'),
    path('mypost/<int:pk>/', views.mypost, name='mypost'),
    path('forget_id/', views.forget_id, name='forget_id'),
    path('password_reset/',
         views.UserPasswordResetView.as_view(template_name='common/password_reset_form.html'), name="password_reset"),
    path('password_reset_done/',
         views.UserPasswordResetDoneView.as_view(template_name='common/password_reset_done.html'),
         name="password_reset_done"),
    path('password_reset_complete/',
         views.UserPasswordResetCompleteView.as_view(template_name='common/password_reset_complete.html'),
         name="password_reset_complete"),
]
