from django import views
from django.contrib import admin
from django.urls import path, include
from common import views
from community.views import base_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mukinator/', include('muki_main.urls')),
    path('community/', include('community.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),
    path('password_reset_confirm/<uidb64>/<token>/',
         views.UserPasswordResetConfirmView.as_view(template_name='common/password_reset_confirm.html'),
         name="password_reset_confirm"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
