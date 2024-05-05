from django.contrib import admin
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from django.urls import path
from .yasg import urlpatterns as doc_url





urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('api/v1/', include('api.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_url




